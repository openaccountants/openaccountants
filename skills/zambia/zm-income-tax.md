---
name: zm-income-tax
description: "Use this skill for Zambia personal income tax in 2026: PAYE bands 0% to 37%, self-employed income tax, turnover tax with the K30,000 nil band, rental income tax, presumptive tax, provisional tax and annual return. Trigger on how much PAYE do I pay, Zambia income tax, net pay Zambia, turnover tax, presumptive tax, rental tax, ITF/1A. For employees, sole traders and landlords. Companies use the corporate skill; payroll remittance uses the payroll skill."
jurisdiction: ZM
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zambia Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Charge year 2026 (1 January to 31 December). Authority: ZRA. Law: Income Tax Act, Cap. 323.

## Who this applies to

Employees (PAYE), sole traders, partners and landlords. Turnover K5,000,000 or less: turnover tax is required, except excluded groups below. Above that, or for partnerships, management and consultancy, and standard mining: income tax on any turnover. Partners each file, plus one joint partnership return.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Monthly bands | Held in [Payroll](zm-payroll-social.md) | 2026 | https://www.zra.org.zm/tax-information/ |
| Annual band 1 | First K61,200, 0% | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Taxation-on-partnerships.pdf |
| Annual band 2 | K61,200 to K85,200, 20% | 2026 | same |
| Annual band 3 | K85,200 to K110,400, 30% | 2026 | same |
| Annual band 4 | Above K110,400, 37% | 2026 | same |
| Turnover tax | K30,000 a year or K2,500 a month or less 0%; above, up to K5,000,000, 5% | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf |
| Excluded from turnover tax | Consultancy, mining other than artisanal, partnerships, public service vehicles under 50 seats | 2026 | same |
| Rental income tax | Up to K30,000 0%; K30,000 to K800,000 4%; above K800,000 16% | 2026 | same |
| Presumptive tax per vehicle a year | 36 to 49 seats K10,368; 22 to 35 K7,776; 18 to 21 K5,184; 12 to 17 K2,592; under 12 K1,296; 50 seats and above leave the regime | 2026 | same |
| Betting and gaming monthly | Casino K5,000 per table; lottery 15% net proceeds; betting 15% gross takings; machines K500 each | 2026 | same |
| Artisanal mining | 4% of income after mineral royalty, monthly by the 14th | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Guide-to-Filing-Tax-Returns.pdf |
| Minimum alternative tax | 1% of turnover for income tax payers, creditable | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf |


## The base

### Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. Amounts are in ZMW (K). Mobile-money references (MTN MoMo, Airtel Money, Zamtel Kwacha) are common in Zambian statements.

#### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Line | Treatment | Notes |
| --- | --- | --- | --- |
| SALARY, STIPENDJU, NET PAY, EMPLOYER [name] | Employment income | PAYE income (employer-side) | Employee tax handled via PAYE, not self-employed return |
| Client name + PAYMENT, DEPOSIT, INVOICE, TRANSFER IN | Business turnover | Self-employed income | If turnover-tax taxpayer, this is turnover base |
| FEES, CONSULTANCY, PROFESSIONAL FEES | Business turnover | Self-employed income | NB: consultancy is EXCLUDED from turnover tax : taxed under income tax |
| MTN MOMO, AIRTEL MONEY, ZAMTEL KWACHA (received) | Business turnover | Self-employed income | Mobile-money receipt : match to invoices |
| STRIPE PAYOUT, PAYPAL PAYOUT, WISE PAYOUT, FLUTTERWAVE | Business turnover | Self-employed income | Platform payout : match to underlying invoices |
| RENT RECEIVED, RENTAL | Rental income | Rental income tax (own regime) | See Section 5.5 : not turnover tax |
| INTEREST, INTERESSI | Investment income | Excluded from turnover tax | Interest is excluded; may be subject to WHT |
| DIVIDEND | Investment income | Excluded from turnover tax | Dividends excluded; usually WHT |
| ZRA REFUND, TAX REFUND | EXCLUDE | Not income | Prior-year tax refund |
| GRANT, GOVERNMENT GRANT | Check nature | Capital grants EXCLUDE; revenue grants = turnover | Flag for reviewer |

#### 3.2 Expense Patterns (Debits): Allowable (income-tax taxpayers only)

**3.2 Expense Patterns (Debits): Allowable (income-tax taxpayers only)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, RENT [commercial] | Office rent | Deductible | Dedicated business premises |
| INSURANCE (business) | Business insurance | Deductible | Must be business-related |
| ACCOUNTANT, AUDITOR, ZICA, BOOKKEEP | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, ADVOCATE (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising | Deductible |  |
| TRAINING, CPD, COURSE, SEMINAR | Training | Deductible | Must relate to current business |
| BANK CHARGE, MAINTENANCE FEE, LEDGER FEE | Bank charges | Deductible | Business account only |
| MOMO CHARGE, MOBILE MONEY FEE, AIRTEL MONEY FEE | Transaction fees | Deductible | Business transactions |
| DOMAIN, HOSTING, AWS, DIGITALOCEAN | IT infrastructure | Deductible |  |

- **Turnover-tax note** : Note: a turnover-tax taxpayer pays 5% on turnover and does NOT deduct expenses. The deduction patterns below apply only to self-employed individuals taxed under the standard income-tax regime.

#### 3.3 Expense Patterns (Debits): Software / SaaS

**3.3 Expense Patterns (Debits): Software / SaaS**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, DROPBOX | Software subscription | Deductible |  |

#### 3.4 Expense Patterns (Debits): Utilities (apportion if mixed-use)

**3.4 Expense Patterns (Debits): Utilities (apportion if mixed-use)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ZESCO | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| LWSC, WATER UTILITY, NWSC | Water | T2 if home office | Proportional if home |
| MTN, AIRTEL, ZAMTEL (airtime/data) | Telecoms | T2 | Business-use portion only; default 0% if mixed |

#### 3.5 Expense Patterns (Debits): Travel

**3.5 Expense Patterns (Debits): Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| PROFLIGHT, EMIRATES, KENYA AIRWAYS, ETHIOPIAN | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, LODGE | Accommodation | Deductible if business travel |  |
| YANGO, BOLT, ULENDO, TAXI | Local transport | Deductible if business purpose |  |
| FUEL, PETROL, DIESEL, PUMA, TOTAL ENERGIES | Vehicle fuel | T2: business % only | Requires mileage log |

#### 3.6 Expense Patterns (Debits): NOT Deductible

**3.6 Expense Patterns (Debits): NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, BAR, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private/entertainment in nature |
| GROCERIES, SHOPRITE, PICK N PAY, SPAR, PERSONAL | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, ZRA PENALTY | Fines/penalties | NOT deductible | Public policy |
| ZRA PAYMENT, INCOME TAX, PAYE PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

#### 3.7 Statutory Deductions / Liability Movements

**3.7 Statutory Deductions / Liability Movements**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NAPSA, PENSION CONTRIBUTION | Statutory deduction (payroll) | 5% employee / 5% employer; not a trading expense for the individual |
| NHIMA, HEALTH INSURANCE | Statutory deduction (payroll) | 0.5% employee / 0.5% employer |
| VAT PAYMENT, ZRA VAT | EXCLUDE | VAT liability payment, not expense |
| PROVISIONAL TAX, ZRA PROVISIONAL | Credit against liability | Not an expense |

#### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, LOAN PRINCIPAL | EXCLUDE | Loan principal movement |

#### 3.9 Zambian Banks / Mobile Money: Statement Format Reference

**3.9 Zambian Banks / Mobile Money: Statement Format Reference**

| Provider | Common Patterns | Notes |
| --- | --- | --- |
| Zanaco | TRANSFER, DD, STANDING ORDER, CHARGES | PDF/CSV; date DD/MM/YYYY |
| Stanbic Bank Zambia | PAYMENT, TRF, FEE | PDF/CSV; counterparty in description |
| FNB Zambia | PAYMENT, DEBIT ORDER, FEE | PDF/CSV |
| Absa Zambia | TRANSFER, DEBIT ORDER, CHARGE | PDF |
| MTN MoMo | RECEIVED FROM, SENT TO, WITHDRAWAL, CHARGE | Mobile-money statement; very common |
| Airtel Money | RECEIVED, PAYMENT, CASH OUT, FEE | Mobile-money statement |

### Tier 1 Rules (When Data Is Clear)

#### 5.1 The Wholly and Exclusively Test (income-tax taxpayers)

- **Wholly and exclusively test** : An expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned on a reasonable, documented basis. (General Zambian income-tax principle; verify exact section against the Income Tax Act before publishing : unconfirmed.)

#### 5.2 PAYE Computation (employees)

- **PAYE monthly band application** : Apply the progressive monthly bands (Section 1) to gross monthly taxable earnings: - 0 - K5,100: 0% - K5,101 - K7,100: 20% (cumulative K400 at top) - K7,101 - K9,200: 30% (cumulative K1,030 at top) - Over K9,200: 37% Employer deducts PAYE monthly and remits to ZRA by the 10th of the following month.

#### 5.3 NAPSA (social security)

- **NAPSA contribution rule** : 10% total = 5% employee + 5% employer, on gross monthly earnings, capped at the NAPSA ceiling (see payroll skill, unverified) monthly insurable-earnings ceiling (max the ceiling amount per party). The earnings base includes basic salary, bonuses, commissions, severance, overtime, leave allowance, and acting allowance.

#### 5.4 NHIMA (health insurance)

- **NHIMA contribution rule** : 1% total = 0.5% employee + 0.5% employer, on gross earnings (basic plus all allowances/overtime/bonuses). Compulsory for all workers including casual, temporary, and contract. Monthly returns due by the 10th.

#### 5.5 Self-Employed Regimes

**Self-Employed Regimes**

| Regime | Scope | Rate | Source |
| --- | --- | --- | --- |
| Turnover tax | Annual turnover ≤ K5,000,000 (excludes interest, dividends, royalties, consultancy, standard mining) | 0% up to K30,000; 5% above | unconfirmed |
| Rental income tax | Rental turnover | 0% ≤ K30,000; 4% K30,000-800,000; 16% > K800,000 | unconfirmed |
| Presumptive (passenger transport) | Per vehicle, annual | See table below | unconfirmed |
| Standard income tax | Turnover > K5,000,000 or excluded income | PAYE bands applied to taxable profit | unconfirmed |

- **Turnover tax filing** : Turnover tax taxpayers pay 5% above K30,000 a year and do NOT deduct expenses. Returns and payment due by the 14th of the following month.

**Presumptive tax : passenger transport (annual, per vehicle)**

| Vehicle seating | Annual presumptive tax (ZMW) |
| --- | --- |
| 36-49 seater | 10,368 |
| 22-35 seater | 7,776 |
| 18-21 seater | 5,184 |
| 12-17 seater | 2,592 |
| Below 12 seater (incl. taxis) | 1,296 |

#### 5.6 Provisional (Advance) Income Tax : non-employment income

- **Provisional tax filing rule** : Individuals earning over K61,200/year from non-employment sources file quarterly provisional returns. Quarter deadlines: 31 Mar, 30 Jun, 30 Sep, 31 Dec (manual Q1 submission 5 Mar). New registrants after 31 Mar: within 90 days of registration.

#### 5.7 VAT Interaction (self-employed crossing the threshold)

**VAT Interaction**

| Item | Detail | Source |
| --- | --- | --- |
| Standard VAT rate | 16% | unconfirmed |
| Registration threshold | Annual turnover > K800,000 (or > K200,000 in any consecutive 3-month period) | unconfirmed |
| VAT returns | Monthly, due by the 18th (e-filing) | ZRA tax information |

- **K800,000 threshold note** : Note: the K800,000 threshold no longer governs turnover-tax eligibility (now K5m) but still governs VAT registration.

#### 5.8 Non-Deductible Expenses (income-tax taxpayers)

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Not wholly and exclusively for production of income |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax / PAYE itself | Tax on income |
| Capital expenditure | Relieved via capital allowances, not as expense unconfirmed |
| Drawings / personal withdrawals | Not an expense |

### Tier 2 Catalogue (Reviewer Judgement Required)

#### 6.1 Home Office Deduction (income-tax traders)

- **Home office deduction rule** : - Calculate the proportion of the home used for business (dedicated room as a percentage of total rooms or floor area) - Apply that percentage to: rent, ZESCO electricity, water, internet, maintenance - Must be a dedicated workspace; a dual-use room does NOT qualify **Conservative default:** 0% deduction until reviewer confirms the arrangement. **Flag for reviewer:** confirm room count / floor-area basis and that the workspace is genuinely dedicated.

#### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use rule** : - Only the business-use percentage of fuel, insurance, maintenance, and capital allowances is deductible - Client must maintain a mileage log (business trips vs total) **Conservative default:** 0% business use until a mileage log is provided. **Flag for reviewer:** confirm the business percentage is documented and reasonable, and the applicable wear-and-tear rate. unconfirmed

#### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rule** : - Business-use portion only (MTN/Airtel/Zamtel airtime and data) **Conservative default:** 0% deduction until the business percentage is confirmed.

#### 6.4 Turnover-Tax vs Income-Tax Election

- **Election rule** : - Turnover tax (5%, no deductions) suits low-expense businesses; the standard income-tax regime suits high-expense businesses - The election interacts with the K5,000,000 turnover ceiling and excluded-income rules **Flag for reviewer:** confirm which regime minimises tax and is correctly registered with ZRA.

#### 6.5 Rental Income Banding

- **Rental income banding rule** : - Rental turnover is taxed on its own scale (0% / 4% / 16%); confirm gross rental turnover and that no expenses are netted off before applying the rate **Flag for reviewer:** confirm the rental turnover figure and band.

#### 6.6 Bad Debt Write-Off (income-tax traders)

- **Bad debt write-off rule** : - Deductible only if the income was previously declared, all reasonable recovery steps were taken, and the debt is genuinely irrecoverable **Flag for reviewer** to confirm all three conditions.

### Excel Working Paper Template

```
ZAMBIA INCOME TAX: WORKING PAPER
Charge Year: 2025
Client: ___________________________
Status: Employee (PAYE) / Sole trader (turnover tax) / Sole trader (income tax)

PART A: EMPLOYEE (PAYE), MONTHLY
  A1. Gross monthly earnings (basic + allowances)   ___________
  A2. PAYE (apply monthly bands)                     ___________
  A3. NAPSA employee 5% (cap the ceiling amount)              ___________
  A4. NHIMA employee 0.5%                            ___________
  A5. NET PAY (A1 - A2 - A3 - A4)                    ___________
  Memo: NAPSA employer 5% (cap the ceiling amount)            ___________
  Memo: NHIMA employer 0.5%                          ___________

PART B: SOLE TRADER, TURNOVER TAX
  B1. Annual turnover (excl. interest/dividends/
      royalties/consultancy/mining)                  ___________
  B2. Less exempt first K30,000                       ___________
  B3. Taxable turnover (B1 - B2, not below 0)        ___________
  B4. Turnover tax (B3 x 5%)                          ___________

PART C: SOLE TRADER, STANDARD INCOME TAX
  C1. Gross business income                           ___________
  C2. Less allowable expenses                         ___________
  C3. Less capital allowances [GAP : rates TBC]       ___________
  C4. Taxable profit (C1 - C2 - C3)                   ___________
  C5. Income tax (apply annual bands)                 ___________
  C6. Less provisional tax paid                       ___________
  C7. Tax due / refund (C5 - C6)                      ___________

REVIEWER FLAGS:
  [ ] Employment status confirmed (PAYE vs self-employed)?
  [ ] Turnover-tax vs income-tax regime confirmed?
  [ ] Turnover below K5,000,000 ceiling confirmed?
  [ ] NAPSA ceiling applied correctly?
  [ ] NHIMA 0.5%/0.5% split confirmed (RESEARCH GAP)?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] Entertainment and personal expenses excluded?
  [ ] VAT registration status confirmed (> K800,000)?
```

### Bank Statement Reading Guide

### Zambian Statement Formats

**Zambian Statement Formats**

| Provider | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Zanaco | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description holds counterparty + reference |
| Stanbic Zambia | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant |
| FNB Zambia | PDF, CSV | Date, Description, Amount, Balance | Debit orders for recurring expenses |
| Absa Zambia | PDF | Date, Particulars, Debit, Credit | Shorter descriptions |
| MTN MoMo | PDF/SMS export | Date, Type, Counterparty, Amount, Charge | "Received from" = income; "Sent to" = expense |
| Airtel Money | PDF/SMS export | Date, Type, Counterparty, Amount, Fee | "Cash out" = withdrawal |

### Key Terms

**Key Terms**

| Term | Meaning | Classification Hint |
| --- | --- | --- |
| MoMo / Mobile Money | Mobile-money transfer | Check direction for income/expense |
| Cash out / Withdrawal | Cash taken out | Ask what the cash was for |
| Standing order / Debit order | Recurring debit | Regular expense (rent, subscription) |
| Charge / Fee / Ledger fee | Bank or MoMo charge | Deductible (business account) |
| ZESCO | National electricity utility | Utility (T2 if home office) |
| NAPSA / NHIMA | Statutory payroll deductions | Not a trading expense for the individual |
| ZRA | Revenue authority | Tax payment : exclude / credit |


## Deadlines and filing

Turnover tax and rental income tax: return and payment by the 14th of the next month. Provisional return 31 March; instalments payable 10 April, 10 July, 10 October, 10 January. Annual return and balance 21 June. Moving between turnover tax and income tax happens only at the start of a charge year. Move at the following year if turnover will pass K5,000,000, and notify ZRA on TaxOnline.

**How to file turnover tax.** Log in at the ZRA portal (www.zra.org.zm, tax portal) with TPIN, password and captcha, enter the one-time password sent to email and phone, then choose Returns, File a return. Enter tax type Turnover Tax, account name and period. Answer "Do you want to file a nil return?": YES then Submit, or NO, Next. Select the income code and enter the taxable amount, one line per source, Next. Confirm the summary, Submit. A reference number is generated. Pay through TaxOnline, TaxOnApp or *858#.

Annual return steps: [Corporate income tax](zm-corporate-income-tax.md); ITF 56 certificate applies. PAYE refunds use ITF/1A.

## Penalties and interest

Late return: individual 1,000 penalty units (K400), company 2,000 (K800) per month or part month; turnover tax 250 units (K100). Late turnover tax payment: 0.5% per month or part month plus Bank of Zambia discount rate plus 2%. Other late payment: 5% plus the same interest. Underpaying by a third on estimate: 25%.

## Cross-border points

Non-residents pay on Zambian source income; most is by final withholding. Remittances above USD 2,000 need tax clearance.

## Two worked examples that recompute

**Simple.** Employee: see K15,000 in the payroll skill. Annual trader profit K200,000:

```oa-check
name: Trader K200,000
inputs:
  profit: 200000
steps:
  - tax: 4800 + 7560 + (profit - 110400) * 0.37
expected:
  tax: 45512.00
```

**Decision: stay on turnover tax or move up.** Same trader, K1,200,000 turnover: ZRA's monthly example gives (K100,000 less K2,500) at 5% for 12 months, K58,500. Income tax would be K45,512, but below K5,000,000 turnover tax is required, so the comparison shows the cost of the regime, not a free choice. If the trade is consultancy, income tax applies.

```oa-check
name: Turnover tax against income tax
inputs:
  monthly: 100000
steps:
  - tot: (monthly - 2500) * 0.05 * 12
  - it: 45512
  - diff: tot - it
expected:
  tot: 58500.00
  diff: 12988.00
```

### Example 5: Non-deductible entertainment (income-tax trader)

**Input line:**
`22/04/2025 ; ABSA CARD ; CHRISMA RESTAURANT ; CLIENT DINNER ; -850.00 ; ZMW`

**Reasoning:**
Client entertainment is private/entertainment in nature and not wholly and exclusively for the production of income. Not deductible. No apportionment.

**Classification:** NOT deductible. Exclude from expenses.

### Example 6: Internal transfer (exclude)

**Input line:**
`15/05/2025 ; ZANACO ; OWN ACCOUNT - SAVINGS ; ; -5,000.00 ; ZMW`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.


## Ask the client first

### Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable (employee/PAYE):** gross monthly earnings (basic + allowances), and confirmation the person is an employee. Optionally: confirmation of NAPSA/NHIMA applicability.

**Minimum viable (self-employed):** bank statement for the charge year in CSV, PDF, or pasted text, plus the nature of the business and approximate annual turnover (to decide turnover tax vs income tax).

**Recommended:** payslips, NAPSA/NHIMA contribution records, sales invoices, purchase invoices/receipts, prior-year ZRA assessment, VAT registration status.

**Ideal:** complete income and expenditure account, asset register, provisional-tax payment confirmations, employment contract / minimum-wage order applicable to the sector.

**Refusal if minimum is missing: SOFT WARN.** No earnings figure (employee) or no bank statement (self-employed) = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported and that the wholly-and-exclusively test is met."

### Refusal Catalogue

- **R-ZM-1** : Employment status unknown. "PAYE (employee) and turnover/income tax (self-employed) are entirely different regimes. This skill cannot compute tax without knowing the person's status. Please confirm before proceeding."
- **R-ZM-2** : Turnover near or above K5,000,000. "Turnover tax applies only to annual turnover up to ZMW 5,000,000 (PwC, ZM other taxes). Above this the business files under the standard income-tax regime, and VAT registration may be required. Escalate to a ZICA-qualified accountant."
- **R-ZM-3** : Companies, partnerships, group structures. "This skill covers individuals: employees and sole traders only. Companies and partnerships file separate returns under different rules. Escalate to a ZICA-qualified accountant."
- **R-ZM-4** : Mining, farming, or special-sector income. "Mining and certain sector incomes are excluded from turnover tax and have bespoke regimes. Out of scope. Escalate to a ZICA-qualified accountant."
- **R-ZM-5** : Non-resident / withholding-tax matters. "Most non-resident income is taxed via withholding tax, not the PAYE/income-tax bands. Out of scope. Escalate to a ZICA-qualified accountant."
- **R-ZM-6** : Arrears / ZRA enforcement. "Client has outstanding tax arrears or is subject to ZRA enforcement. Late-payment penalties (5% plus BoZ discount rate + 2% interest) compound. Do not advise. Escalate immediately."
- **R-ZM-7** : VAT return requested. "This skill covers income tax / PAYE / turnover tax only. For Zambia VAT, use the zambia-vat skill (if available) or escalate."

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether earner is employee or self-employed | STOP: do not compute without status |
| Unknown gross vs net of allowances | Treat the figure as gross monthly earnings |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category (self-employed) | Not deductible |
| Unknown whether NAPSA ceiling applies | Apply the NAPSA ceiling (see payroll skill, unverified) ceiling |
| Unknown turnover-tax vs income-tax election | Turnover tax if turnover ≤ K5,000,000 (see R-ZM-2) |
| Unknown VAT registration | Not VAT-registered (use gross amounts) |
| Charge year not stated | Current charge year (2025/2026 bands are identical) |

### Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING: reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS: ZAMBIA INCOME TAX
1. Are you an employee (paid a salary) or self-employed (run your own business)?
2. If self-employed: what is your approximate annual turnover? (decides turnover tax vs income tax)
3. Does your income include interest, dividends, royalties, consultancy, or mining? (excluded from turnover tax)
4. Are you VAT-registered, or above K800,000 annual turnover?
5. Do you let property? If so, what is the gross annual rent?
6. Home office: dedicated room or shared space? If dedicated, what % of floor area?
7. Vehicle: used for business? If yes, what % business use, and do you keep a mileage log?
8. Phone/internet: what % is business use?
9. Are NAPSA and NHIMA deducted from your pay (employee) or do you pay them yourself?
10. Have you paid any provisional tax this charge year?
```


## PROHIBITIONS

- NEVER compute tax without confirming employee (PAYE) vs self-employed status
- NEVER apply turnover tax to interest, dividends, royalties, consultancy, or standard mining income
- NEVER allow expense deductions for a turnover-tax taxpayer (5% is on turnover)
- NEVER exceed the NAPSA insurable-earnings ceiling (the NAPSA ceiling (see payroll skill, unverified)/month → max the ceiling amount per party)
- NEVER treat NAPSA or NHIMA as a trading expense of the individual
- NEVER allow entertainment, personal, or fine/penalty expenses as deductions
- NEVER allow income tax / PAYE itself as a deduction
- NEVER assume the 2025 NAPSA ceiling, NHIMA split, or minimum wage carries into 2026 without confirmation
- NEVER treat a unconfirmed figure as confirmed : flag it for the reviewer
- NEVER present tax calculations as definitive: always label as estimated and pending professional review


### Authority and Source References

**Authority and Source References**

| Topic | Reference |
| --- | --- |
| PAYE rates / tax-free threshold | unconfirmed |
| Filing deadline / provisional tax | unconfirmed |
| Turnover / rental / presumptive tax / VAT | unconfirmed |
| NAPSA ceiling / rate / NAE | unconfirmed |
| NHIMA rate | unconfirmed |
| Penalties / due dates | ZRA penalties (zra.org.zm/penalties); ZRA payment due dates (zra.org.zm/payment-due-dates) |
| Minimum wage | Ministry of Labour & Social Security (mlss.gov.zm); SI No. 3 of 2025 |

### Filing, Forms & Employer Obligations

**Filing, Forms & Employer Obligations**

| Item | Detail | Source |
| --- | --- | --- |
| Annual individual return deadline | 21 June following the charge year | unconfirmed |
| Statute of limitations | 6 years from end of charge year (except fraud/wilful default) | unconfirmed |
| Monthly PAYE remittance | by the 10th of the following month | ZRA payment due dates |
| Monthly PAYE return form | ITF P16 (annual reconciliation: P18) | ZRA PAYE leaflet : unconfirmed |
| Turnover-tax return / payment | by the 14th of the following month | unconfirmed |
| VAT returns | monthly, by the 18th | ZRA tax information |

### Penalties & Interest

**Penalties & Interest**

| Breach | Charge | Source |
| --- | --- | --- |
| Late submission of return | 250 penalty units (K100) per month or part month | ZRA penalties page / penalties leaflet : unconfirmed |
| Late payment of tax | 5% of the amount due, plus interest at Bank of Zambia discount rate + 2% | ZRA penalties page |

### Minimum Wage (2025)

No single national minimum wage; set by sector via Statutory Instruments under the Minimum Wages and Conditions of Employment Act (Cap 276).

**Minimum Wage (2025)**

| Order | Monthly (ZMW) | Source |
| --- | --- | --- |
| General Workers Order | 2,313.10 | unconfirmed |
| Domestic Workers Order | 1,300.00 (incl. housing/transport/lunch allowances) | unconfirmed |
| Shop Workers Order | graded by job level | unconfirmed |
| Transport (SI No. 3 of 2025) | bus drivers 3,000; truck drivers 4,000 | MLSS SI No. 3 of 2025 |

### Test Suite

Input: Employee, gross K4,500/month.
Expected: PAYE K0 NAPSA and NHIMA not computed: rates unverified.

Input: Employee, gross K8,000/month.
Expected: PAYE K670 (K400 + K900×30%) NAPSA and NHIMA not computed: rates unverified.

Input: Employee, gross K40,000/month.
Expected: PAYE K12,426 (K1,030 + K30,800×37%) NAPSA and NHIMA not computed: rates unverified.

Input: Employee, gross the NAPSA ceiling (see payroll skill, unverified)/month.
Expected: NAPSA not computed: ceiling unverified.

Input: Self-employed (standard regime), taxable profit K150,000/year.
Expected: Income tax = K12,360 + (150,000 − 110,400)×37% = K12,360 + K14,652 = K27,012.

Input: Sole trader, annual turnover K200,000 (no excluded income), under K5m ceiling.
Expected: Turnover tax = (200,000 − 12,000) × 5% = K188,000 × 5% = K9,400/year.

Input: Gross annual rent K500,000.
Expected: Rental income tax at 4% (band K30,000-800,000) = K500,000 × 4% = K20,000. [Confirm whether the first K30,000 is 0% before applying : PwC bands as stated; reviewer to confirm marginal vs flat application.]

Input: K850 client dinner claimed as expense (income-tax trader).
Expected: Remove : not deductible.


## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) (No. 2) Act No. 17 of 2025, whole Act; read for the figures cited | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf | 2026-11-01 |
| Income Tax (Amendment) Act No. 10 of 2025, whole Act; read for the figures cited | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf | 2026-11-01 |
| VAT (Amendment) Act No. 19 of 2025, whole Act; read for the figures cited | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2019%20of%202025%20The%20Value%20Added%20Tax%20%28Amendment%29%20Act.pdf | 2026-11-01 |
| ZRA Tax Information page, Turnover Tax and PAYE sections; read for the figures cited | https://www.zra.org.zm/tax-information/ | 2026-11-01 |
| ZRA Payment Due Dates page; read for the figures cited | https://www.zra.org.zm/payment-due-dates/ | 2026-11-01 |
| ZRA leaflet Turnover Tax (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Turnover-Tax.pdf | 2026-11-01 |
| ZRA Guide to Filing Tax Returns (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Guide-to-Filing-Tax-Returns.pdf | 2026-11-01 |
| ZRA leaflet Introduction to Income Tax (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-Income-Tax.pdf | 2026-11-01 |
| ZRA leaflet Rental Income Tax (2026), OCR read; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/06/Rental-Income-Tax.pdf | 2026-11-01 |
| ZRA Advance Income Tax on remittances leaflet (2026), first page; read for the figures cited | https://www.zra.org.zm/wp-content/uploads/2026/08/Refunds-of-Advance-Income-Tax-on-Remittance.pdf | 2026-11-01 |

Not yet confirmed: NAPSA and NHIMA (payroll skill), including the old 2025 figures of ceiling K34,164, national average earnings K8,541 and NHIMA 1%; whether turnover tax above K30,000 falls on total turnover or on the excess (ZRA example taxes the excess, its note says total); table cells marked unconfirmed carried from the old file; minimum wage orders; old source labels removed where they named commercial firms.

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
