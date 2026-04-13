---
name: ca-fed-t2125
description: >
  Use this skill whenever asked about Canadian self-employment business income reported on Form T2125 (Statement of Business or Professional Activities). Trigger on phrases like "T2125", "business income Canada", "self-employed expenses", "CCA", "capital cost allowance", "home office Canada", "motor vehicle expenses CRA", "business-use-of-home", "sole proprietor Canada", "net business income", "business number BN", "fiscal year end", "GST ITC", or any question about computing, classifying, or reporting business income and expenses for a Canadian sole proprietor. Covers Parts 1-8 of T2125, allowable expenses, CCA classes and rates, AccII, business-use-of-home, motor vehicle expenses, GST/HST interaction, and net income computation. ALWAYS read this skill before touching any T2125 work.
version: 2.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Canada Self-Employment (T2125) -- Sole Proprietor Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Canada -- Federal |
| Tax | Federal income tax on business income + CPP self-employed contributions |
| Currency | CAD only |
| Tax year | Calendar year (sole proprietors must use December 31 fiscal year-end) |
| Primary legislation | Income Tax Act (ITA), R.S.C. 1985, c. 1 (5th Supp.) |
| Supporting legislation | Income Tax Regulations (ITR); Excise Tax Act (ETA) for GST/HST; CRA Guide T4002 |
| Tax authority | Canada Revenue Agency (CRA) |
| Filing portal | CRA My Account / NETFILE / EFILE |
| Filing deadline | 15 June (self-employed), but tax owing due 30 April |
| Form | T2125 -- Statement of Business or Professional Activities |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Canadian CPA sign-off required |
| Skill version | 2.0 |

### Federal Tax Brackets (2025) [T1]

| Taxable Income (CAD) | Rate |
|---|---|
| 0 -- 57,375 | 15% |
| 57,376 -- 114,750 | 20.5% |
| 114,751 -- 158,468 | 26% |
| 158,469 -- 220,000 | 29% |
| 220,001+ | 33% |

**Provincial tax is additional.** Each province has its own brackets. This skill covers federal only. Combined marginal rates range from ~20% to ~54% depending on province.

### Basic Personal Amount (2025) [T1]

| Item | Amount (CAD) |
|---|---|
| Basic personal amount (income under ~$177,882) | $16,129 |
| Basic personal amount (income over ~$253,414) | $14,538 |
| BPA clawback zone | Linear reduction between thresholds |

### CPP Self-Employed Contributions (2025) [T1]

| Item | Value |
|---|---|
| CPP rate (self-employed pay both portions) | 11.9% (2 x 5.95%) |
| CPP2 rate | 8% (2 x 4%) on earnings between first and second ceilings |
| First earnings ceiling | $71,300 |
| Second earnings ceiling | $81,200 |
| Basic exemption | $3,500 |
| Maximum CPP contribution | $8,068.20 |
| Maximum CPP2 contribution | $792.00 |

Half of CPP self-employed contributions is deductible on Line 22200.

### Key T2125 Thresholds [T1]

| Item | Value |
|---|---|
| GST/HST registration required | Over $30,000 in 4 consecutive quarters |
| CCA deduction | Optional -- can claim any amount up to the maximum |
| Instant asset write-off (CEBA) | See AccII rules -- enhanced first-year deduction |
| Business-use-of-home | Only if principal place of business OR used exclusively for income-earning and meeting clients |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Unknown business-use % (vehicle, home, phone) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown CCA class | Do not depreciate -- ask |
| Unknown GST/HST status | Not registered (gross amounts are the cost) |
| Unknown whether expense is business or personal | Personal (not deductible) |
| Unknown vehicle km split | 0% business |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full calendar year (January-December), confirmation of business activity and NAICS code.

**Recommended** -- all invoices issued, purchase receipts, vehicle km log, home office measurements, GST/HST returns filed, prior year T2125.

**Ideal** -- complete bookkeeping records, CCA schedule from prior year, motor vehicle log, T4 slips (if also employed), prior year Notice of Assessment.

### Refusal Catalogue

**R-CA-1 -- Corporations.** "Corporations file T2 corporate tax returns. This skill covers sole proprietors filing T2125 only."

**R-CA-2 -- Partnerships.** "Partnerships file T2125 at the partnership level with allocation to partners. Partnership-specific rules are out of scope."

**R-CA-3 -- Non-residents.** "Non-resident business income has different rules. Out of scope."

**R-CA-4 -- SR&ED claims.** "Scientific Research and Experimental Development tax credits require specialised review. Escalate."

**R-CA-5 -- Farming/fishing income.** "Farming (T2042) and fishing (T2121) have their own forms and special rules. Out of scope."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | T2125 Line | Treatment | Notes |
|---|---|---|---|
| CLIENT DEPOSIT, CLIENT PAYMENT, [client name] | Line 8299 (Gross revenue) | Business income | Core revenue |
| STRIPE PAYOUT, STRIPE TRANSFER | Line 8299 | Business income | Match to underlying invoices. Report gross (before Stripe fees). |
| PAYPAL TRANSFER, PAYPAL PAYOUT | Line 8299 | Business income | Same -- report gross before fees |
| ETRANSFER [client name], INTERAC | Line 8299 | Business income | Common Canadian payment method |
| GST/HST REFUND, CRA GST REFUND | Check | May be income | GST/HST refund of ITCs: NOT income. Net income adjustment if previously expensed. |
| INTEREST, SAVINGS INTEREST | NOT T2125 | Interest income | Report on Line 12100, not T2125 |
| DIVIDEND | NOT T2125 | Dividend income | Report on Line 12000/12010 |
| EMPLOYMENT INCOME, SALARY | NOT T2125 | Employment income | T4 slip income |
| CRA REFUND, TAX REFUND | EXCLUDE | Not income | Tax refund |
| RENTAL INCOME | NOT T2125 | Rental | Report on T776 |
| OWN TRANSFER, SAVINGS TRANSFER | EXCLUDE | Internal | Between own accounts |

### 3.2 Expense Patterns (Debits on Bank Statement)

| Pattern | T2125 Line | Tier | Treatment |
|---|---|---|---|
| RENT, OFFICE RENT, COMMERCIAL LEASE | Line 8910 (Rent) | T1 | Fully deductible if business premises |
| PROPERTY TAX (business premises) | Line 8810 (Property taxes) | T1 | Fully deductible for business property |
| HYDRO, ELECTRICITY, GAS, ENBRIDGE, HYDRO ONE | Line 8945 (Utilities) | T2 | If home: business-use % only. If office: fully deductible. |
| BELL, ROGERS, TELUS, SHAW | Line 8220 (Telephone/utilities) | T2 | Business portion only |
| INTERNET, WIFI | Line 8220 | T2 | Business portion only |
| INSURANCE, BUSINESS INSURANCE, LIABILITY | Line 8690 (Insurance) | T1 | Fully deductible if business insurance |
| ACCOUNTING, BOOKKEEPER, CPA | Line 8860 (Professional fees) | T1 | Fully deductible |
| LAWYER, LEGAL FEE | Line 8860 | T1 | Deductible if business-related |
| OFFICE SUPPLIES, STAPLES, GRAND & TOY | Line 8810 (Office expenses) | T1 | Fully deductible |
| BANK FEE, MONTHLY FEE, NSF | Line 8710 (Interest and bank charges) | T1 | Fully deductible for business account |
| STRIPE FEE, PAYPAL FEE, SQUARE FEE | Line 8710 | T1 | Payment processing fees: fully deductible |
| INTEREST (business loan) | Line 8710 | T1 | Fully deductible |
| ADVERTISING, GOOGLE ADS, META ADS, FACEBOOK | Line 8520 (Advertising) | T1 | Fully deductible |
| MEALS (client entertainment) | Line 8523 (Meals and entertainment) | T1 | 50% deductible only. The other 50% is permanently disallowed. |
| MEALS (business travel, alone) | Line 8523 | T1 | 50% deductible |
| SOFTWARE, SUBSCRIPTION, SAAS | Line 8810 or 8860 | T1 | Fully deductible |
| TRAINING, COURSE, CONFERENCE | Line 9270 (Other expenses) | T1 | Fully deductible if business-related |
| GAS, FUEL, PETRO-CANADA, SHELL, ESSO | Motor vehicle expenses | T2 | Business km / total km. Keep a log. |
| CAR INSURANCE, AUTO INSURANCE | Motor vehicle expenses | T2 | Business km proportion only |
| CAR REPAIR, SERVICE, OIL CHANGE | Motor vehicle expenses | T2 | Business km proportion only |
| PARKING (business) | Motor vehicle or travel | T1 | Fully deductible if business purpose |
| CRA INCOME TAX, TAX INSTALMENT | EXCLUDE | Not deductible | Income tax is not a business expense |
| CRA GST PAYMENT, GST REMITTANCE | EXCLUDE from T2125 | T1 | GST is separate system. Net of GST on T2125 if registered. |
| CPP CONTRIBUTION | EXCLUDE from T2125 | T1 | CPP is not a T2125 expense. Half deductible on Line 22200. |
| PERSONAL, GROCERY, AMAZON (personal) | EXCLUDE | Not deductible | Personal expenses |
| COMPUTER, LAPTOP, EQUIPMENT (over $500) | CCA (not current expense) | T1 | Capital -- claim CCA. See Section 5.4. |
| MEMBERSHIP, DUES, PROFESSIONAL BODY | Line 8760 (Management fees) or 9270 | T1 | Fully deductible if business-related |
| SUBCONTRACTOR, CONTRACTOR PAYMENT | Line 8340 (Subcontracts) | T1 | Fully deductible. Issue T4A if over $500. |

### 3.3 SaaS Subscriptions

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Line 8810/8860 -- fully deductible | Operating expense |
| SLACK, ZOOM, NOTION, FIGMA, GITHUB | Line 8810/8860 -- fully deductible | Same |
| AWS, HEROKU, DIGITAL OCEAN | Line 8810 -- fully deductible | Hosting costs |
| QUICKBOOKS, XERO, FRESHBOOKS, WAVE | Line 8860 -- fully deductible | Accounting software |

### 3.4 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, SAVINGS, TFSA, RRSP | EXCLUDE | Not business transaction |
| MORTGAGE, RENT (personal) | EXCLUDE (or home office %) | Personal. Home office portion in business-use-of-home. |
| ATM, CASH WITHDRAWAL | T2 -- ask | Default exclude |
| DONATION, CHARITY | EXCLUDE from T2125 | Personal tax credit, not business expense |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Proprietor (Web Developer)

**Input:** Gross revenue CAD 95,000. Not GST registered (under $30K threshold last year, now over -- must register). Expenses: home office (see below), software CAD 2,400, accounting CAD 1,500, subcontractor CAD 8,000, travel CAD 3,000, meals (50%) CAD 1,200 (deductible: CAD 600).

**Home office:** 1,200 sq ft house, 150 sq ft office (12.5%). Mortgage interest CAD 8,000, property tax CAD 4,000, utilities CAD 3,600, insurance CAD 1,800. Total: CAD 17,400 x 12.5% = CAD 2,175.

**Computation:**
- Revenue: CAD 95,000
- Expenses: 2,400 + 1,500 + 8,000 + 3,000 + 600 + 2,175 = CAD 17,675
- Net business income: CAD 77,325
- CPP: (77,325 - 3,500) x 11.9% = CAD 8,068.20 (hits maximum)
- Half CPP deductible: CAD 4,034.10

### Example 2 -- Vehicle (Km-Based Apportionment)

**Input:** Total km driven: 25,000. Business km: 15,000 (60%). Vehicle costs: gas CAD 3,600, insurance CAD 2,400, repairs CAD 800, licence CAD 120. Car cost CAD 36,000 (Class 10).

**Computation:**
- Operating costs: (3,600 + 2,400 + 800 + 120) x 60% = CAD 4,152
- CCA: CAD 36,000 x 30% (Class 10 rate) x 60% = CAD 6,480 (first year: AccII provides 1.5x = CAD 9,720 if eligible)
- Total vehicle deduction: CAD 4,152 + CCA amount

### Example 3 -- Meals (50% Rule)

**Input:** CAD 2,500 in restaurant receipts for client meetings.

**Classification:** Only 50% deductible = CAD 1,250. This is a permanent restriction under ITA s67.1. The full CAD 2,500 is reported on Line 8523, then 50% is added back.

### Example 4 -- CCA on Computer Equipment

**Input:** Laptop purchased for CAD 2,800. Class 50 (55% rate). First year.

**Classification:** CCA Class 50 at 55%. With AccII (Accelerated Investment Incentive), first-year deduction enhanced: 1.5 x 55% x CAD 2,800 = CAD 2,310 (but cannot exceed cost, so CAD 2,310). UCC year-end: CAD 490.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income [T1]

**Legislation:** ITA s9

All revenue from business activities. Report gross on Line 8299. If GST/HST registered, report net of GST/HST.

### 5.2 Deductible Expenses [T1]

**Legislation:** ITA s18

Must be incurred to earn business income. Must be reasonable (s67). Personal or living expenses are not deductible (s18(1)(h)).

### 5.3 Meals and Entertainment [T1]

**Legislation:** ITA s67.1

50% limitation on meals and entertainment. Applies to all business meals, client entertainment, and food/drink. Long-haul truck drivers: 80%.

### 5.4 Capital Cost Allowance (CCA) [T1]

**Legislation:** ITA s20(1)(a); ITR Schedule II

| Class | Rate | Assets |
|---|---|---|
| 1 | 4% | Buildings (non-residential after March 2007) |
| 8 | 20% | Furniture, fixtures, equipment, photocopiers |
| 10 | 30% | Motor vehicles (passenger, cost < $37,000 limit) |
| 10.1 | 30% | Passenger vehicles over $37,000 (cost capped at limit) |
| 12 | 100% | Small tools, computer software, cutlery |
| 43 | 30% | Manufacturing equipment |
| 50 | 55% | Computer hardware, data network equipment |
| 54 | 30% | Zero-emission passenger vehicles (cost cap $61,000) |
| 55 | 40% | Zero-emission vehicles not in class 54 |

**Passenger vehicle cost limit (2025):** CAD 37,000 (excluding GST/HST). Luxury vehicles capped at this amount for CCA purposes (Class 10.1).

**AccII (Accelerated Investment Incentive):** For eligible property acquired after November 20, 2018, the first-year CCA is enhanced by a 1.5x multiplier on the half-year rule. Effectively, you get 1.5 times the normal first-year CCA.

### 5.5 Business-Use-of-Home [T1/T2]

**Legislation:** ITA s18(12)

| Condition | Eligibility |
|---|---|
| Principal place of business | YES -- deduction allowed |
| Exclusive use for business + regular meetings | YES -- deduction allowed |
| Neither condition met | NO deduction |

Deductible expenses: proportion of rent/mortgage interest, property tax, utilities, insurance, maintenance. Proportion = business area / total area.

**Cannot create or increase a business loss.** Excess carried forward to the next year.

### 5.6 Filing Deadlines [T1]

| Item | Deadline |
|---|---|
| T1 filing (self-employed) | 15 June |
| Tax payment due | 30 April (even though filing deadline is 15 June) |
| Quarterly instalments | 15 March, 15 June, 15 September, 15 December |
| T4A issuance (subcontractors) | Last day of February |
| GST/HST annual return | 15 June (if annual filer) |

### 5.7 Penalties [T1]

| Offence | Penalty |
|---|---|
| Late filing | 5% of balance owing + 1% per month late (max 12 months) |
| Repeated late filing (2nd+ time in 3 years) | 10% + 2% per month (max 20 months) |
| Late instalment | Instalment interest at prescribed rate |
| Gross negligence | 50% of understated tax or overstated credits |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

Confirm: (1) principal place of business OR exclusive use + client meetings, (2) area measurements, (3) expense amounts. Cannot create or increase a loss. Excess carried forward.

**Flag for reviewer:** Confirm eligibility conditions and area calculation.

### 6.2 Motor Vehicle [T2]

Must keep a contemporaneous km log. CRA audits vehicle claims frequently. If no log exists, default to 0% business use.

**Flag for reviewer:** Confirm km log exists and business percentage is reasonable.

### 6.3 Reasonableness (s67) [T2]

All expenses must be "reasonable in the circumstances." CRA can deny excessive expenses even if legitimately incurred. Flag any single expense that appears disproportionate.

### 6.4 CCA vs Expense [T2]

Items with lasting value beyond one year: CCA. Items consumed in the year: current expense. Software subscriptions: current expense. Software perpetual licences: CCA Class 12 (100%). Hardware: CCA Class 50.

---

## Section 7 -- Excel Working Paper Template

```
T2125 WORKING PAPER -- Tax Year 2025

A. GROSS INCOME
  A1. Gross sales/revenue (Line 8299)              ___________
  A2. GST/HST collected (if registered)            ___________
  A3. Net sales (A1 - A2 if applicable)            ___________

B. EXPENSES
  B1. Advertising (8520)                           ___________
  B2. Meals and entertainment (8523) -- 50%        ___________
  B3. Subcontracts (8340)                          ___________
  B4. Insurance (8690)                             ___________
  B5. Interest and bank charges (8710)             ___________
  B6. Management and admin (8760)                  ___________
  B7. Office expenses (8810)                       ___________
  B8. Professional fees (8860)                     ___________
  B9. Rent (8910)                                  ___________
  B10. Telephone and utilities (8220)              ___________
  B11. Travel (8520)                               ___________
  B12. Other expenses (9270)                       ___________
  B13. Total expenses                              ___________

C. NET INCOME BEFORE CCA AND HOME OFFICE
  C1. A3 - B13                                     ___________

D. CCA
  D1. Class 8 (20%)                                ___________
  D2. Class 10/10.1 (30%)                          ___________
  D3. Class 50 (55%)                               ___________
  D4. Other classes                                ___________
  D5. Total CCA                                    ___________

E. BUSINESS-USE-OF-HOME
  E1. Business area %                              ___________
  E2. Total home costs                             ___________
  E3. Deductible portion (E1 x E2)                 ___________

F. NET BUSINESS INCOME (C1 - D5 - E3)              ___________

REVIEWER FLAGS:
  [ ] Vehicle km log available?
  [ ] Home office eligibility confirmed?
  [ ] CCA schedule reconciled from prior year?
  [ ] Meals at 50% applied?
  [ ] All T2 items flagged?
```

---

## Section 8 -- Bank Statement Reading Guide

### Canadian Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| RBC, TD, BMO, Scotiabank, CIBC | CSV, PDF | Date, Description, Debit, Credit, Balance |
| Desjardins | CSV | Date, Description, Withdrawal, Deposit |
| Tangerine, Simplii, EQ Bank | CSV | Date, Transaction, Amount |
| Wise, Revolut | CSV | Date, Description, Amount, Currency |

### Key Canadian Banking Terms

| Term | Classification Hint |
|---|---|
| e-Transfer / Interac | Very common -- check direction and counterparty |
| PAD (Pre-Authorized Debit) | Regular expense |
| POS | Point-of-sale purchase |
| Direct Deposit | Could be income or employment |
| NSF | Non-sufficient funds fee -- bank charge |
| Service Charge | Monthly bank fee |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- CANADA T2125
1. What is your business name and NAICS code?
2. Do you have a Business Number (BN)?
3. Are you GST/HST registered?
4. Do you work from home? Is it your principal place of business?
5. Do you use a vehicle for business? Do you have a km log?
6. Any capital purchases this year? (computers, equipment, vehicles)
7. Do you have subcontractors you paid over $500?
8. Are you also employed (T4 income)?
9. Province of residence?
10. Prior year T2125 / CCA schedule available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Business income | ITA s9 |
| Deductible expenses | ITA s18 |
| Reasonableness | ITA s67 |
| Meals 50% limit | ITA s67.1 |
| CCA | ITA s20(1)(a); ITR Schedule II |
| Motor vehicle limits | ITA s67.2, s67.3; ITR 7307 |
| Business-use-of-home | ITA s18(12) |
| CPP self-employed | CPP Act s10, s12 |
| Filing deadlines | ITA s150(1) |
| Penalties | ITA s162, s163 |
| GST/HST | ETA Part IX |

### Interaction with GST/HST [T1]

| Scenario | Income Tax Treatment |
|---|---|
| GST/HST collected on sales (registrant) | NOT income. Report net of GST/HST on T2125. |
| ITC (Input Tax Credit) recovered | NOT an expense. Report net of recoverable GST/HST. |
| Non-registrant (under $30K threshold) | GST/HST paid on purchases IS part of the cost. Report gross. |
| ITCs denied (personal use portion) | Non-recoverable GST/HST is part of the expense cost. |

---

## PROHIBITIONS

- NEVER allow personal or living expenses as business deductions
- NEVER allow more than 50% of meals and entertainment
- NEVER claim CCA without a prior-year UCC reconciliation
- NEVER claim home office if neither principal-place-of-business nor exclusive-use test is met
- NEVER allow home office to create or increase a business loss
- NEVER claim vehicle expenses without a km log
- NEVER exceed the passenger vehicle cost limit for CCA
- NEVER include income tax payments as business expenses
- NEVER include CPP contributions as T2125 expenses (half goes to Line 22200)
- NEVER report GST/HST-inclusive amounts on T2125 if the business is a registrant
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
