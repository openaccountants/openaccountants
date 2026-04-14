---
name: ng-income-tax
description: >
  Use this skill whenever asked about Nigerian personal income tax for self-employed individuals (sole proprietors / freelancers). Trigger on phrases like "Nigeria income tax", "PITA", "FIRS", "self-assessment Nigeria", "progressive tax Nigeria", "minimum tax Nigeria", "consolidated relief", "CRA Nigeria", "TIN Nigeria", "WHT Nigeria", "income tax Lagos", "income tax Abuja", "state IRS", or any question about computing or filing income tax for a self-employed person in Nigeria. This skill covers progressive rates (7-24%), minimum tax (1% of gross income), consolidated relief allowance, capital allowances, withholding tax credits, self-assessment filing, and FIRS/state IRS requirements. ALWAYS read this skill before touching any Nigerian income tax work.
version: 2.0
---

# Nigerian Personal Income Tax — Self-Employed / Sole Proprietor (PITA) v2.0

## Section 1 — Quick Reference

### Progressive Tax Rates (PITA, Sixth Schedule)

| Taxable Income (NGN) | Rate |
|---|---|
| First 300,000 | 7% |
| Next 300,000 (300,001 -- 600,000) | 11% |
| Next 500,000 (600,001 -- 1,100,000) | 15% |
| Next 500,000 (1,100,001 -- 1,600,000) | 19% |
| Next 1,600,000 (1,600,001 -- 3,200,000) | 21% |
| Above 3,200,000 | 24% |

### Consolidated Relief Allowance (CRA)

CRA = max(NGN 200,000, 1% x Gross Income) + 20% x Gross Income

The CRA replaced the previous personal allowance / children's allowance system from 2020.

### Minimum Tax

| Rule | Detail |
|---|---|
| Rate | 1% of gross income |
| When it applies | When computed tax (per progressive rates) is LESS than minimum tax |
| Effect | Taxpayer pays the HIGHER of computed tax or minimum tax |

### Capital Allowances (PITA, Fifth Schedule)

| Asset | Initial Allowance | Annual Allowance |
|---|---|---|
| Building (industrial) | 15% | 10% |
| Motor vehicles | 50% | 25% |
| Plant and machinery | 50% | 25% |
| Furniture and fittings | 25% | 20% |
| Computer equipment | 50% | 25% |

### Computation Structure

| Step | Description |
|---|---|
| A | Gross income from business |
| B | Less: Allowable business deductions |
| C | Assessable income (A minus B) |
| D | Add: Other income (investment, rental, etc.) |
| E | Gross total income (C plus D) |
| F | Less: Consolidated Relief Allowance |
| G | Less: Other reliefs (pension, NHF, life insurance) |
| H | Taxable income (E minus F minus G) |
| I | Tax per progressive rate table |
| J | Compare with minimum tax (1% of gross) |
| K | Tax payable (higher of I and J) |
| L | Less: WHT credits |
| M | Tax due / (refund) |

### Other Reliefs (PITA, s 33)

| Relief | Amount / Rule |
|---|---|
| Pension contribution | Actual contribution to approved scheme (min 8% of basic + housing + transport) |
| National Housing Fund | 2.5% of basic salary (voluntary for self-employed) |
| Life insurance premium | Actual premium paid |
| National Health Insurance | Actual premium paid |

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Residency unknown | STOP — non-residents taxed differently |
| State of residence unknown | STOP — determines filing authority |
| CRA computed on net income | WRONG — CRA is on GROSS income |
| Capital expenditure directly deducted | WRONG — use capital allowances |
| WHT certificate missing | Do NOT credit without certificate |
| Minimum tax not checked | ALWAYS compare computed tax vs 1% of gross |
| Filing authority unclear | FIRS for FCT (Abuja); state IRS for all others |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Computed tax = 0 but minimum tax > 0 | Minimum tax applies |
| No WHT certificates from clients | Cannot credit without certificates |
| Expenses close to income (high ratio) | Minimum tax likely applies |
| Multiple state operations | Verify correct filing authority |
| Capital expenditure directly expensed | Must use capital allowance schedule |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

1. **Residency status** — resident vs non-resident
2. **State of residence** — determines FIRS (FCT) or state IRS
3. **Gross income from self-employment** — total business receipts
4. **Business expenses** — nature, amount, and documentation
5. **Other income** — employment, investment, rental
6. **Life insurance and pension contributions** — for relief computation
7. **National Housing Fund contributions** — if applicable
8. **TIN** — Tax Identification Number
9. **WHT certificates** — from clients who withheld tax
10. **Bank statements** — 12 months (calendar year)
11. **Capital assets purchased** — for capital allowance computation

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-NG-1 | Non-resident earning Nigeria-source income | Stop — WHT as final tax (10% on professional services); different rules |
| R-NG-2 | Residency unknown | Stop — different treatment |
| R-NG-3 | State of residence unknown | Stop — determines filing authority |
| R-NG-4 | Capital expenditure claimed as expense | Reject — must use capital allowance schedule |
| R-NG-5 | Old personal allowance / children's allowance system | Stop — replaced by CRA from 2020 |
| R-NG-6 | Petroleum profits tax | Escalate — separate regime |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSFER FROM [client]` / `NIP CR [client]` | Gross income — PITA taxable | Standard NIP (NIBSS Instant Payment) transfer from client |
| I-02 | `USSD CREDIT` / `*737 CREDIT` | Gross income — PITA taxable | USSD banking credit from client |
| I-03 | `POS SETTLEMENT` / `CARD COLLECTION` | Gross income — gross-up | POS terminal settlement |
| I-04 | `PAYSTACK PAYOUT` / `PAYSTACK SETTLEMENT` | Gross income — gross-up | Paystack (Nigerian payment processor) payout |
| I-05 | `FLUTTERWAVE PAYOUT` / `FLUTTERWAVE SETTLEMENT` | Gross income — gross-up | Flutterwave settlement |
| I-06 | `STRIPE PAYOUT NGN` | Gross income — gross-up or foreign | Stripe payout; classify by payer country |
| I-07 | `PAYPAL TRANSFER` / `PAYPAL WITHDRAWAL` | Gross income — foreign source likely | PayPal; flag for FX conversion |
| I-08 | `PAYONEER DEPOSIT` | Gross income — foreign source | Payoneer settlement |
| I-09 | `OPAY RECEIVED` / `PALMPAY RECEIVED` | Gross income — PITA taxable | Mobile money / fintech receipt |
| I-10 | `TAX REFUND FIRS` / `REFUND SIRS` | NOT income — tax refund | Refund from tax authority |
| I-11 | `INTEREST EARNED` / `SAVINGS INTEREST` | Investment income | Add to gross total income |
| I-12 | `RENTAL INCOME` / `RENT RECEIVED` | Rental income | Add to gross total income |
| I-13 | `WHT DEDUCTED` (annotation on payment) | WHT credit — not income reduction | Credit against final tax; require certificate |

### 3.2 Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `OFFICE RENT` / `RENT PAYMENT [landlord]` | Rent — fully deductible | Require receipt/invoice |
| E-02 | `EKEDC` / `IKEDC` / `AEDC` / `BEDC` / `PHED` / `KAEDCO` | Electricity — deductible (business proportion) | Distribution company payment |
| E-03 | `MTN` / `AIRTEL` / `GLO` / `9MOBILE` | Phone/internet — deductible (business %) | Telecom provider |
| E-04 | `SPECTRANET` / `SMILE` / `IPNX` / `SWIFT NETWORK` | Internet — deductible (business %) | ISP provider |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — fully deductible | Professional tools |
| E-06 | `ACCOUNTANT` / `AUDIT FEE` / `TAX CONSULTANT` | Professional fees — fully deductible | |
| E-07 | `ARIK AIR` / `AIR PEACE` / `DANA AIR` / `IBOM AIR` | Air travel — deductible (business purpose) | Document purpose |
| E-08 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — deductible (business travel) | Business purpose |
| E-09 | `PENSION CONTRIBUTION` / `RSA [fund name]` | Pension — relief deduction | Approved pension scheme contribution |
| E-10 | `NHF` / `NATIONAL HOUSING FUND` | NHF — relief deduction | If applicable |
| E-11 | `LIFE INSURANCE` / `PREMIUM PAYMENT` | Life insurance — relief deduction | Own life insurance |
| E-12 | `NHIS` / `HEALTH INSURANCE` | Health insurance — relief deduction | National/private health |
| E-13 | `TAX PAYMENT FIRS` / `SIRS PAYMENT` | Tax payment — NOT deductible | Payment of tax liability |
| E-14 | `FUEL` / `PETROL` / `DIESEL` / `TOTAL` / `OANDO` / `CONOIL` | Fuel — deductible (business proportion) | Document business use |
| E-15 | `OFFICE SUPPLIES` / `STATIONERY` | Supplies — fully deductible | |
| E-16 | `MARKETING` / `GOOGLE ADS` / `META ADS` / `ADVERTISING` | Marketing — fully deductible | |
| E-17 | `STAFF SALARY` / `PAYROLL` | Staff costs — fully deductible | Include PAYE obligations for staff |
| E-18 | `TRAINING` / `COURSE` / `CERTIFICATION` | Training — fully deductible | Professional development |
| E-19 | `GENERATOR FUEL` / `DIESEL GEN` | Generator fuel — deductible (business %) | Common in Nigeria due to power supply |

### 3.3 Nigerian Bank Fees (Deductible)

| Pattern | Treatment | Notes |
|---|---|---|
| GTBANK, GUARANTY TRUST | Deductible for business account fees | Now GTCo |
| ACCESS BANK | Deductible for business account fees | Merged with Diamond Bank |
| ZENITH BANK | Deductible for business account fees | |
| UBA, UNITED BANK FOR AFRICA | Deductible for business account fees | |
| FIRST BANK, FBN | Deductible for business account fees | |
| STANBIC IBTC | Deductible for business account fees | |
| FCMB, FIRST CITY MONUMENT | Deductible for business account fees | |
| FIDELITY BANK | Deductible for business account fees | |
| STERLING BANK | Deductible for business account fees | |
| WEMA BANK / ALAT | Deductible for business account fees | |
| KUDA BANK, OPAY, PALMPAY, MONIEPOINT | Deductible for business account fees | Fintech/digital banks |
| ACCOUNT MAINTENANCE FEE, COT | Deductible | Commission on turnover / maintenance |
| SMS ALERT FEE, NOTIFICATION FEE | Deductible | Banking notification charges |
| TRANSFER FEE, NIP FEE | Deductible | Inter-bank transfer fees |
| STAMP DUTY | EXCLUDE | Government levy on transactions |

### 3.4 Government and Statutory (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FIRS, FEDERAL INLAND REVENUE | EXCLUDE | Federal tax authority payment |
| LIRS, LAGOS STATE IRS | EXCLUDE | State tax authority |
| CAC, CORPORATE AFFAIRS COMMISSION | Deductible | Business registration fee |
| STAMP DUTY CHARGE | EXCLUDE | Government levy |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN ACCOUNT TRANSFER, SELF TRANSFER | EXCLUDE | Internal movement |
| ATM WITHDRAWAL | TIER 2 — ask | Default exclude; determine purpose |
| LOAN DISBURSEMENT | EXCLUDE | Loan proceeds, not income |
| LOAN REPAYMENT | EXCLUDE | Loan principal, out of scope |

---

## Section 4 — Worked Examples

### Example 1 — GTBank (Lagos, IT Consultant)

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

**Step 1 — Income**

Annualised gross: NGN 8,000,000. WHT deducted by PJ clients: NGN 500,000.

**Step 2 — Expenses**

Accounting: NGN 150,000; travel: NGN 85,000; telecom: NGN 300,000; software: NGN 240,000; marketing: NGN 180,000; office rent: NGN 1,200,000; generator fuel: NGN 360,000; other: NGN 485,000. Total: NGN 3,000,000.

**Step 3 — Computation**

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

### Example 2 — Access Bank (Abuja, Consultant — WHT Heavy)

**Bank:** Access Bank
**Client:** Amina Bello, management consultant, Abuja (FCT — file with FIRS)

Gross: NGN 12,000,000. All from corporate clients with 10% WHT.
WHT suffered: NGN 1,200,000.
After CRA and expenses: tax per rates = NGN 950,000.
Less WHT: NGN 1,200,000.
Result: **refund of NGN 250,000** (WHT > tax). File with FIRS for refund.

### Example 3 — Zenith Bank (Port Harcourt, Physician)

**Bank:** Zenith Bank
**Client:** Dr. Emeka Nwosu, physician, Port Harcourt, Rivers State

Gross: NGN 20,000,000 (hospital fees + private patients).
Expenses: NGN 5,000,000.
CRA: 200,000 + 4,000,000 = NGN 4,200,000.
Pension: NGN 800,000.
Taxable: 20,000,000 - 5,000,000 - 4,200,000 - 800,000 = NGN 10,000,000.

Tax: 21,000 + 33,000 + 75,000 + 95,000 + 336,000 + (10,000,000 - 3,200,000) x 24% = 560,000 + 1,632,000 = **NGN 2,192,000**

File with Rivers State IRS (not FIRS).

### Example 4 — Kuda Bank (Lagos, Freelance Designer — Low Income)

**Bank:** Kuda Bank (digital)
**Client:** Ngozi Eze, freelance designer, Lagos

Gross: NGN 600,000. Expenses: NGN 100,000.
CRA: 200,000 + 120,000 = NGN 320,000.
Taxable: 600,000 - 100,000 - 320,000 = NGN 180,000.
Tax: 7% x 180,000 = NGN 12,600.
Minimum tax: 1% x 600,000 = NGN 6,000.
Pay NGN 12,600 (higher).

### Example 5 — UBA (Lagos, Minimum Tax Scenario)

**Bank:** UBA
**Client:** Tunde Adeyemi, consultant, Lagos

Gross: NGN 10,000,000. Expenses: NGN 9,000,000.
CRA: 200,000 + 2,000,000 = NGN 2,200,000. Pension: NGN 500,000.
Taxable: 10,000,000 - 9,000,000 - 2,200,000 - 500,000 = max(0, -1,700,000) = NGN 0.
Computed tax: NGN 0.
Minimum tax: 1% x 10,000,000 = **NGN 100,000**.
Tax payable: NGN 100,000 (minimum tax applies).

### Example 6 — First Bank (Kano, Multiple Income Sources)

**Bank:** First Bank
**Client:** Ibrahim Musa, accountant, Kano, also earns rental income

Self-employment: NGN 6,000,000. Rental income: NGN 2,400,000.
Total gross: NGN 8,400,000.
CRA on total gross: 200,000 + 1,680,000 = NGN 1,880,000.
All income aggregates. Apply expenses per source. Progressive rates on combined taxable income.
File with Kano State IRS.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-NG-1 — CRA is computed on GROSS income, not net**
The Consolidated Relief Allowance formula uses gross total income (before expenses), not assessable or taxable income. This is a common error. Always apply CRA to gross.

**T1-NG-2 — Minimum tax is a floor**
Always compare computed tax per progressive rates with 1% of gross income. The taxpayer pays whichever is HIGHER. Minimum tax cannot be avoided by high expenses.

**T1-NG-3 — Capital expenditure must use capital allowances**
Never deduct capital expenditure directly as a business expense. Use the Fifth Schedule rates (initial allowance in year of first use, annual allowance thereafter).

**T1-NG-4 — WHT is a credit, not income reduction**
Withholding tax (10% on professional fees, 5% on contracts) deducted by clients is a credit against final tax. It does not reduce gross income. Must have WHT certificate to claim credit.

**T1-NG-5 — Filing authority depends on state of residence**
FCT (Abuja) residents file with FIRS. All other states file with the State Internal Revenue Service (SIRS). This is not optional.

**T1-NG-6 — Old personal allowance system is abolished**
The pre-2020 system of personal allowance + children's allowance + dependent relative allowance was replaced by CRA. Never apply the old deductions.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-NG-1 | Mixed-use vehicle | Business proportion must be documented | Flag — reviewer determines reasonable business-use % |
| T2-NG-2 | Home office expenses | Proportional deduction for dedicated space | Flag — document proportion and exclusivity |
| T2-NG-3 | Capital allowance computation for complex assets | Initial vs annual allowance; residual value tracking | Flag — verify asset register and allowance schedule |
| T2-NG-4 | Multiple state operations | Dual filing obligation possible | Flag — verify correct filing authority for each income source |
| T2-NG-5 | Foreign income for Nigerian resident | Worldwide income taxable; treaty credits may apply | Escalate — treaty analysis required |
| T2-NG-6 | Voluntary NHF / NHIS contributions | Relief amounts depend on actual contribution vs statutory basis | Verify contribution receipts and applicable relief limits |

---

## Section 7 — Excel Working Paper Template

```
NIGERIAN PITA WORKING PAPER (SELF-EMPLOYED / SOLE PROPRIETOR)
Taxpayer: _______________  TIN: _______________  FY: 2025 (Calendar Year)
State: _______________  Filing Authority: [ ] FIRS (FCT)  [ ] State IRS

SECTION A — GROSS INCOME
                                        NGN
Business receipts:                     ___________
Platform payouts (grossed up):         ___________
Other business income:                 ___________
TOTAL BUSINESS GROSS                   ___________

SECTION B — ALLOWABLE BUSINESS DEDUCTIONS
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

SECTION C — ASSESSABLE INCOME
Gross business - deductions            ___________

SECTION D — OTHER INCOME
Investment income:                     ___________
Rental income:                         ___________
Employment income:                     ___________
GROSS TOTAL INCOME                     ___________

SECTION E — RELIEFS
CRA: max(200,000, 1% x Gross) + 20% x Gross  ___________
Pension contribution:                  ___________
NHF:                                   ___________
Life insurance:                        ___________
NHIS:                                  ___________
TOTAL RELIEFS                          ___________

SECTION F — TAXABLE INCOME
Gross total - deductions - reliefs     ___________

SECTION G — TAX COMPUTATION
Tax per progressive rates:             ___________
Minimum tax (1% x gross):             ___________
TAX PAYABLE (higher):                 ___________

SECTION H — CREDITS
WHT suffered (with certificates):      (___________)
TAX DUE / (REFUND)                    ___________

SECTION I — REVIEWER FLAGS
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

---

## Section 8 — Bank Statement Reading Guide

### GTBank (Guaranty Trust / GTCo)
- Export: CSV/PDF from GTBank Internet Banking / GTWorld app
- Columns: `Date;Description;Debit;Credit;Balance`
- Amount format: comma thousands, period decimal (e.g., `2,500,000.00`)
- Date: DD/MM/YYYY or DD-MMM-YYYY
- Credits: `NIP CR FROM [sender]`, `MOBILE TRANSFER FROM [sender]`

### Access Bank
- Export: CSV/Excel from Access More app / Internet Banking
- Columns: `Date;Narration;Debit;Credit;Balance`
- Credits: `NIP CREDIT FROM [sender]`, `TRANSFER FROM [sender]`

### Zenith Bank
- Export: CSV from Zenith Internet Banking / ZMobile
- Columns: `Trans Date;Value Date;Description;Debit;Credit;Balance`
- Credits: `NIP CR [sender]`, `INWARD TRF FROM [sender]`

### UBA (United Bank for Africa)
- Export: CSV/PDF from UBA Internet Banking / UBA Mobile
- Standard Nigerian bank format

### First Bank of Nigeria (FBN)
- Export: CSV from FirstBank Online / FirstMobile
- Columns: `Date;Description;Debit;Credit;Balance`

### Stanbic IBTC
- Export: CSV from Stanbic IBTC Internet Banking
- Standard format

### Kuda Bank / OPay / PalmPay / Moniepoint (Digital)
- Export: CSV/PDF from app
- Simple format; credit/debit columns or single column
- Narrations: `Transfer from [name]`, `Received from [name]`
- OPay: `OPay Transfer from [name]`
- PalmPay: `PalmPay Transfer from [name]`
- Moniepoint: `Moniepoint Transfer from [name]`

### Paystack / Flutterwave Settlements
- Appear in primary bank statement as `PAYSTACK SETTLEMENT` or `FLUTTERWAVE PAYOUT`
- Gross-up required — platform deducts fees before settlement
- Cross-reference with Paystack/Flutterwave merchant dashboard for gross amounts

### Key Nigerian Banking Notes
- All amounts in NGN (Nigerian naira); comma thousands, period decimal
- NIP (NIBSS Instant Payment) is the standard inter-bank transfer system
- USSD banking (*737 for GTBank, *901 for Access, *966 for Zenith, etc.) common for mobile transfers
- POS (Point of Sale) settlements may be delayed 1-3 days
- Stamp duty charges (NGN 50 on transactions above NGN 10,000) are not deductible business expenses
- Multiple accounts across banks is common — consolidate all statements

---

## Section 9 — Onboarding Fallback

**Filing authority:**
> "Nigerian personal income tax is administered by the Federal Inland Revenue Service (FIRS) for residents of the Federal Capital Territory (Abuja) and by the State Internal Revenue Service (SIRS) for residents of all other states. Where do you reside? This determines where you file your self-assessment return."

**WHT certificates:**
> "If your clients deducted withholding tax (10% on professional fees, 5% on contracts) from your payments, you need the WHT certificates (credit notes) to claim these as credits against your annual tax. Contact each client to obtain their WHT certificates. Without them, the credit cannot be claimed."

**CRA explanation:**
> "Under the Consolidated Relief Allowance (introduced by Finance Act 2020), you receive an automatic deduction of the higher of NGN 200,000 or 1% of your gross income, plus an additional 20% of your gross income. This replaces the old personal allowance, children's allowance, and dependent relative allowance. No documentation is needed for CRA — it is computed automatically."

**Minimum tax:**
> "Even if your computed tax per the progressive rates is very low or zero (due to high expenses), you are still required to pay a minimum tax of 1% of your gross income. The minimum tax acts as a floor — you pay whichever is higher between computed tax and minimum tax."

---

## Section 10 — Reference Material

### Key Legislation
- **Personal Income Tax Act (PITA)** — Cap P8 LFN 2004, as amended by Finance Act 2020, 2021, 2023
- **FIRS Establishment Act** — Federal Inland Revenue Service
- **Pension Reform Act 2014** — pension contribution requirements
- **Finance Act 2020** — introduced CRA and simplified minimum tax

### Filing Calendar

| Deadline | Event |
|---|---|
| 31 March | Self-assessment return (PITA s 41-44) |
| 31 March | Payment of tax due |
| Monthly | WHT remittance (if agente de retención) |

### Penalties

| Offence | Penalty |
|---|---|
| Late filing | NGN 50,000 first month + NGN 25,000/subsequent month |
| Late payment | 10% of tax due + interest at CBN MPR + spread |
| Failure to keep records | NGN 50,000 fine |
| Incorrect return (without fraud) | Twice the difference |
| Tax evasion | NGN 20,000 fine or 3 years imprisonment or both |

### Record Keeping
- Minimum retention: 6 years
- Business records, invoices, receipts, bank statements, contracts
- WHT certificates: retain permanently for audit

### Useful References
- FIRS: www.firs.gov.ng
- TaxPro Max: taxpromax.firs.gov.ng
- State IRS portals: vary by state (LIRS: lirs.gov.ng, etc.)
- Joint Tax Board (JTB): www.jtb.gov.ng


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
