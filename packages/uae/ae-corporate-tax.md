---
name: ae-corporate-tax
description: >
  Use this skill whenever asked about UAE Corporate Tax for freelancers, sole establishments, or small businesses. Trigger on phrases like "how much tax do I pay in UAE", "corporate tax UAE", "CT return", "FTA", "small business relief", "free zone tax", "qualifying free zone person", "AED 375,000", "9% tax", "taxable income UAE", "corporate tax registration", "UAE tax return", "self-employed tax UAE", "freelancer tax Dubai", "EmaraTax", or any question about computing or filing UAE corporate tax. This skill covers the 0%/9% rate structure, small business relief (revenue under AED 3M), qualifying free zone person rules, deductible and non-deductible expenses, transfer pricing, registration requirements, and filing deadlines. Note: the UAE has NO personal income tax — self-employed individuals and sole establishments are subject to corporate tax. ALWAYS read this skill before touching any UAE corporate tax work.
version: 2.0
---

# UAE Corporate Tax — Freelancers and Sole Establishments v2.0

## Section 1 — Quick Reference

### Corporate Tax Rates

| Taxable Income (AED) | Rate |
|---|---|
| 0 -- 375,000 | 0% |
| 375,001+ | 9% |

Qualifying Free Zone Person: 0% on qualifying income; 9% on non-qualifying income.

No personal income tax in the UAE. Self-employed individuals and sole establishments are subject to corporate tax if turnover exceeds AED 1,000,000.

### Small Business Relief (SBR)

| Condition | Requirement |
|---|---|
| Revenue threshold | <= AED 3,000,000 |
| Must be Resident Person | Yes |
| Not a QFZP | Cannot claim both |
| Election required | YES — must actively elect on CT return |
| Effect | Taxable income deemed nil; tax = AED 0 |
| Loss carry-forward | NOT available in SBR year |
| Valid period | Tax periods starting on or before 31 December 2026 |

### Natural Person Threshold

| Rule | Detail |
|---|---|
| Turnover threshold | AED 1,000,000 in a calendar year |
| Below threshold | Not subject to corporate tax; no registration required |
| Above threshold | Must register, file, and pay corporate tax |

### Computation Structure

| Step | Description |
|---|---|
| A | Accounting income per financial statements (IFRS) |
| B | +/- Adjustments required by CT Law |
| C | Less: Exempt income (qualifying dividends, participations) |
| D | Plus: Non-deductible expenditure |
| E | Less: Carry-forward tax losses (up to 75% of taxable income) |
| F | Taxable income |
| G | Less: AED 375,000 nil rate band |
| H | Amount subject to 9% |
| I | Corporate tax payable |

### Non-Deductible Expenses

| Expense | Treatment |
|---|---|
| Fines and penalties (government) | Fully non-deductible |
| Bribes / corrupt payments | Fully non-deductible |
| Non-qualifying donations | Non-deductible |
| Entertainment | 50% non-deductible (only 50% allowed) |
| Personal expenses of owner | Fully non-deductible |
| Income tax / CT payments | Non-deductible |
| Dividends / profit distributions | Not an expense |
| General provisions for doubtful debts | Non-deductible until written off |
| Interest exceeding thin cap | 30% of EBITDA or AED 12M, whichever higher |

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| Business structure unknown | STOP — determines applicable rules |
| SBR eligibility unclear | Check revenue <= AED 3M; election must be active |
| Entertainment deduction | Apply 50% only |
| Personal vs business expense | Reject personal; flag mixed-use for reviewer |
| QFZP status uncertain | Do NOT apply 0% — flag for verification |
| Loss carry-forward amount unknown | Assume zero; flag |
| Filing deadline calculation | 9 months after FY end |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| Revenue > AED 3M | SBR not available |
| Revenue < AED 1M (natural person) | Not subject to CT |
| SBR not elected despite eligibility | Tax calculated normally — alert client |
| Entertainment fully deducted | Must cap at 50% |
| Personal expenses in business costs | Non-deductible — remove |
| Related party transactions | Flag for transfer pricing review |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

1. **Business structure** — sole establishment, freelancer, civil company, or other entity
2. **Revenue in the tax period** — total turnover
3. **Free zone status** — registered in UAE free zone? QFZP?
4. **Financial year end** — determines filing deadline
5. **Gross income** — total business income
6. **Business expenses** — nature and amount
7. **Related party transactions** — any connected persons
8. **Prior year losses** — tax losses for carry-forward
9. **Registration status** — registered with FTA?
10. **VAT registration status** — affects expense treatment

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-AE-1 | Business structure unknown | Stop — cannot determine applicable rules |
| R-AE-2 | Employee asking about income tax on salary | Stop — UAE has NO personal income tax; salary is not taxable |
| R-AE-3 | Group relief / holding company structure | Escalate — complex group rules outside scope |
| R-AE-4 | Permanent establishment determination for foreign entity | Escalate — requires detailed analysis |
| R-AE-5 | Pillar Two (15% rate for large MNEs) | Escalate — applies to EUR 750M+ consolidated revenue groups |
| R-AE-6 | QFZP claim without full verification | Do not apply 0% rate without confirming all conditions |

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `TRANSFER FROM [client]` / `INCOMING TT [client]` | Gross income — CT taxable | Standard wire/transfer from client |
| I-02 | `SALARY TRANSFER` / `WPS CREDIT` | NOT business income — employment | If sole establishment owner pays themselves; exclude personal salary |
| I-03 | `STRIPE PAYOUT AED` / `STRIPE PAYMENTS` | Gross income — gross-up | Stripe net payout; fee deductible |
| I-04 | `PAYPAL TRANSFER AED` | Gross income — gross-up or foreign | PayPal payout; classify by payer |
| I-05 | `PAYONEER DEPOSIT` | Gross income — foreign source likely | Payoneer settlement |
| I-06 | `NETWORK INTL SETTLEMENT` / `VISA SETTLEMENT` | Gross income — card payment | Card payment processor settlement |
| I-07 | `TABBY SETTLEMENT` / `POSTPAY DEPOSIT` | Gross income — BNPL settlement | Buy now pay later platform payout |
| I-08 | `FTA REFUND` / `TAX REFUND FTA` | NOT income — tax refund | CT or VAT refund |
| I-09 | `INTEREST EARNED` / `PROFIT ON DEPOSIT` | Business income — if business account | Interest/profit on business deposits |
| I-10 | `RENTAL INCOME` / `RENT RECEIVED` | Business income if business property | Real property income |

### 3.2 Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `OFFICE RENT` / `RENT PAYMENT` / `EJARI` | Rent — fully deductible | Business premises rent |
| E-02 | `DEWA` / `SEWA` / `FEWA` / `AADC` / `ADDC` | Utilities — fully deductible | Dubai/Sharjah/Fujairah/Abu Dhabi utilities |
| E-03 | `DU` / `ETISALAT` / `E& BUSINESS` | Telecom — fully deductible | Business phone/internet |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software — fully deductible | Professional tools |
| E-05 | `ACCOUNTING FEE` / `AUDIT FEE` / `TAX AGENT` | Professional fees — fully deductible | |
| E-06 | `EMIRATES` / `FLYDUBAI` / `ETIHAD` / `AIR ARABIA` | Air travel — fully deductible (business) | Document purpose |
| E-07 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation — fully deductible (business) | Business travel |
| E-08 | `RESTAURANT` / `FOOD` / `ENTERTAINMENT` | Entertainment — 50% deductible only | Cap at 50%; flag if fully deducted |
| E-09 | `SALIK` / `DARB` | Road tolls — deductible (business proportion) | Business vehicle use |
| E-10 | `ENOC` / `ADNOC` / `EMARAT` / `EPPCO` | Fuel — deductible (business proportion) | Business vehicle |
| E-11 | `RTA` / `ITC` / `TAXI` / `CAREEM` / `UBER` | Transport — fully deductible (business) | Business travel |
| E-12 | `EMIRATES NBD FEE` / `FAB FEE` / `ADCB FEE` | Bank charges — fully deductible | Business account fees |
| E-13 | `INSURANCE` / `AMAN` / `DAMAN` / `AXA` | Insurance — fully deductible (business) | Business insurance |
| E-14 | `VISA FEE` / `IMMIGRATION` / `MOHRE` | Government fees — deductible if business | Staff visa, labour permits |
| E-15 | `FTA PAYMENT` / `CT PAYMENT` | Tax payment — NOT deductible | Corporate tax payment |
| E-16 | `VAT PAYMENT FTA` | VAT payment — NOT deductible | VAT is separate |
| E-17 | `FINE` / `PENALTY` / `TRAFFIC FINE` | Fines — NOT deductible | Government-imposed penalties |
| E-18 | `OWNER DRAWING` / `PERSONAL TRANSFER` | Personal — NOT deductible | Owner withdrawal |
| E-19 | `MARKETING` / `GOOGLE ADS` / `META ADS` | Marketing — fully deductible | Advertising expenditure |

### 3.3 UAE Bank Fees (Deductible)

| Pattern | Treatment | Notes |
|---|---|---|
| EMIRATES NBD | Deductible for business account fees | Largest UAE bank |
| FAB (First Abu Dhabi Bank) | Deductible for business account fees | |
| ADCB (Abu Dhabi Commercial Bank) | Deductible for business account fees | |
| MASHREQ, MASHREQBANK | Deductible for business account fees | |
| RAK BANK, NATIONAL BANK OF RAS AL KHAIMAH | Deductible for business account fees | |
| DIB (Dubai Islamic Bank) | Deductible for business account fees | |
| CBD (Commercial Bank of Dubai) | Deductible for business account fees | |
| ADIB (Abu Dhabi Islamic Bank) | Deductible for business account fees | |
| ENBD / FAB / ADCB ACCOUNT MAINTENANCE | Deductible | Monthly/quarterly account fees |
| SWIFT CHARGES, TT CHARGES | Deductible | Wire transfer fees |

### 3.4 Government and Regulatory (Exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FTA, FEDERAL TAX AUTHORITY | EXCLUDE | Tax payment |
| DED (Department of Economic Development) | Business licence — deductible | Trade licence renewal fee |
| DMCC, JAFZA, DAFZA, DIFC, ADGM | Free zone authority — deductible | Licence/registration fees |
| RTA, ROADS AND TRANSPORT | EXCLUDE if fines; deductible if tolls | Distinguish fines from fees |

### 3.5 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Internal movement |
| LOAN REPAYMENT | EXCLUDE | Principal repayment |
| PERSONAL EXPENSE, OWNER DRAWING | EXCLUDE | Non-deductible personal |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude; determine purpose |

---

## Section 4 — Worked Examples

### Example 1 — Emirates NBD (Dubai, IT Consultant — SBR)

**Bank:** Emirates NBD business account
**Client:** Ahmed Al-Rashid, freelance IT consultant, Dubai mainland

```
Date;Description;Debit;Credit;Balance
05/01/2025;TT FROM TECH CORP LLC;;85,000;
15/01/2025;ENBD ACCOUNT MAINT FEE;50;;
10/02/2025;TT FROM STARTUP FZE;;62,000;
28/02/2025;DEWA;1,200;;
15/03/2025;STRIPE PAYOUT AED;;34,000;
01/04/2025;GOOGLE ADS;3,500;;
20/04/2025;TT FROM GAMMA CONSULTING;;95,000;
15/06/2025;ACCOUNTING FEE;8,000;;
10/07/2025;EMIRATES FLIGHT;2,800;;
10/10/2025;RESTAURANT CLIENT DINNER;1,500;;
```

Revenue annualised: AED 2,200,000 (below AED 3M).
SBR eligible: YES. Must actively elect on CT return.
If SBR elected: taxable income = nil. Tax = AED 0.

If SBR NOT elected:
Expenses: accounting AED 96,000, DEWA AED 14,400, marketing AED 42,000, travel AED 33,600, entertainment AED 18,000 (50% = AED 9,000 deductible), bank fees AED 600, total AED 195,600.
Taxable income: AED 2,200,000 - AED 195,600 = AED 2,004,400.
Tax: (2,004,400 - 375,000) x 9% = AED 146,646.

ALERT: Client should elect SBR to pay AED 0 instead of AED 146,646.

### Example 2 — FAB (Abu Dhabi, Engineering Consultant — No SBR)

**Bank:** First Abu Dhabi Bank
**Client:** Sara Ibrahim, engineering consultant, Abu Dhabi mainland

Revenue: AED 4,200,000 (above AED 3M — SBR NOT available).
Allowable expenses: AED 1,800,000. Entertainment AED 40,000 (50% = AED 20,000).
Taxable income: AED 4,200,000 - AED 1,820,000 = AED 2,380,000.
Tax: (2,380,000 - 375,000) x 9% = **AED 180,450**.

### Example 3 — ADCB (Dubai, Freelancer Below AED 1M)

**Bank:** ADCB
**Client:** Omar Hassan, freelance designer, Dubai

Revenue: AED 750,000. Below AED 1,000,000 natural person threshold.
NOT subject to corporate tax. No registration required.
Advise: monitor revenue; if approaching AED 1M, register proactively.

### Example 4 — Mashreq (DMCC Free Zone, Qualifying Income)

**Bank:** Mashreq business account
**Client:** TechSolutions FZ-LLC, DMCC free zone company, software development

Revenue: AED 5,000,000 (all from corporate clients outside free zone).
QFZP conditions: adequate substance, qualifying activity (could be manufacturing/distribution/HQ services), no individual customer revenue, transfer pricing compliant.

If QFZP: qualifying income at 0%. Non-qualifying at 9%.
Flag: QFZP determination is complex. Verify all conditions. Audited financials required.

### Example 5 — RAK Bank (Ras Al Khaimah, Personal Expenses Mixed In)

**Bank:** RAK Bank
**Client:** Khalid Mahmoud, sole establishment

Expenses include: personal car lease AED 36,000, family phone AED 6,000, vacation AED 15,000.
Resolution: ALL personal expenses non-deductible. Remove AED 57,000 from deductions.
If car and phone partially business: flag for reviewer to determine reasonable business-use %.

### Example 6 — DIB (Dubai, Loss Carry-Forward with SBR)

**Bank:** Dubai Islamic Bank
**Client:** Fatima Al-Zahra, consultant

2024: tax loss of AED 200,000.
2025: revenue AED 2,500,000 (SBR eligible). Elects SBR.
Result: taxable income deemed nil. Prior loss CANNOT be used in SBR year. Loss of AED 200,000 remains available for future non-SBR years.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-AE-1 — No personal income tax in the UAE**
The UAE does not impose personal income tax on individuals. Salary, wages, investment income earned personally are not taxable. Corporate tax applies only to business activities.

**T1-AE-2 — SBR must be actively elected**
Small business relief is NOT automatic. The election must be made on the CT return via EmaraTax. Without the election, tax is calculated normally.

**T1-AE-3 — Entertainment capped at 50%**
Entertainment expenditure is only 50% deductible. Always apply the 50% cap. Add back the other 50% to taxable income.

**T1-AE-4 — Personal expenses are fully non-deductible**
Owner's personal expenses (personal car, family phone, vacation, personal insurance) are non-deductible. Remove entirely from business deductions.

**T1-AE-5 — Loss carry-forward capped at 75%**
Tax losses can be carried forward indefinitely, but only 75% of current-year taxable income can be offset. The remaining 25% is taxed.

**T1-AE-6 — Fines and penalties are non-deductible**
Government-imposed fines (traffic, regulatory, tax) are never deductible. Remove from deductions.

**T1-AE-7 — Filing deadline is 9 months after FY end**
CT return and payment due within 9 months of financial year end. No provisional payment system.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-AE-1 | QFZP determination | Complex conditions — substance, qualifying activities, de minimis test | Flag — licensed tax agent must verify all conditions |
| T2-AE-2 | Transfer pricing for related party transactions | Arm's length test required; documentation may be needed | Flag — confirm nature and market rate of services |
| T2-AE-3 | Mixed personal/business expenses | Allocation requires documented business-use percentage | Flag — reviewer determines reasonable split |
| T2-AE-4 | Thin capitalisation (interest expense cap) | Net interest capped at 30% EBITDA or AED 12M | Flag if significant interest expenses |
| T2-AE-5 | Free zone company with mainland individual customers | Non-qualifying income; may breach QFZP de minimis test | Flag — 5% / AED 5M threshold check required |
| T2-AE-6 | Withholding tax on cross-border payments | 0% WHT currently but subject to change / treaty interaction | Escalate for treaty analysis |

---

## Section 7 — Excel Working Paper Template

```
UAE CORPORATE TAX WORKING PAPER (FREELANCER / SOLE ESTABLISHMENT)
Taxpayer: _______________  TRN: _______________  FY End: _______________

SECTION A — REVENUE
                                        AED
Service income:                        ___________
Product sales:                         ___________
Other business income:                 ___________
TOTAL REVENUE                          ___________

SECTION B — SBR ELIGIBILITY CHECK
Revenue <= AED 3,000,000?              [ ] Yes  [ ] No
Resident Person?                       [ ] Yes  [ ] No
Not QFZP?                              [ ] Yes  [ ] No
SBR elected on return?                 [ ] Yes  [ ] No
If YES to all: taxable income = nil, tax = AED 0

SECTION C — DEDUCTIBLE EXPENSES (if SBR not elected)
Staff salaries/benefits:               ___________
Rent (business premises):              ___________
Utilities (DEWA/SEWA/etc.):           ___________
Telecom (du/Etisalat):                ___________
Software:                              ___________
Professional fees:                     ___________
Marketing:                             ___________
Travel (business):                     ___________
Insurance (business):                  ___________
Bank charges:                          ___________
Entertainment (50% of total):          ___________
Other deductible:                      ___________
TOTAL DEDUCTIBLE EXPENSES              ___________

SECTION D — NON-DEDUCTIBLE ITEMS (add back)
Entertainment (50% disallowed):        ___________
Personal expenses:                     ___________
Fines/penalties:                       ___________
Other non-deductible:                  ___________
TOTAL ADD-BACKS                        ___________

SECTION E — TAXABLE INCOME
Revenue - deductible expenses + add-backs: ___________
Less loss carry-forward (75% cap):     ___________
TAXABLE INCOME                         ___________

SECTION F — TAX COMPUTATION
AED 0 - 375,000:                       AED 0
Excess x 9%:                           ___________
CORPORATE TAX PAYABLE                  ___________

SECTION G — FILING DEADLINE
FY end + 9 months:                     ___________

SECTION H — REVIEWER FLAGS
[ ] Business structure confirmed?
[ ] Natural person AED 1M threshold checked?
[ ] SBR eligibility assessed and election advised?
[ ] Entertainment capped at 50%?
[ ] Personal expenses excluded?
[ ] Fines/penalties excluded?
[ ] Related party transactions flagged for TP?
[ ] Loss carry-forward limited to 75%?
[ ] Registration status confirmed with FTA?
[ ] QFZP conditions verified (if free zone)?
```

---

## Section 8 — Bank Statement Reading Guide

### Emirates NBD
- Export: CSV/Excel from ENBD Online Business Banking
- Columns: `Date;Description;Debit;Credit;Balance`
- Amount format: comma thousands, period decimal (e.g., `85,000.00`)
- Date: DD/MM/YYYY or YYYY-MM-DD
- Credit narrations: `TT FROM [sender]`, `INCOMING REMITTANCE`

### First Abu Dhabi Bank (FAB)
- Export: CSV from FAB Online
- Columns: `Date;Narrative;Debit;Credit;Balance`
- Standard UAE format
- Credits: `INCOMING TT [sender]`, `CREDIT TRANSFER`

### ADCB (Abu Dhabi Commercial Bank)
- Export: CSV/Excel from ADCB Business Online
- Columns: `Date;Description;Debit Amount;Credit Amount;Balance`
- Credits: `TT CREDIT FROM [sender]`

### Mashreq Bank
- Export: CSV from Mashreq Online
- Standard format: `Date;Description;Debit;Credit;Balance`

### RAK Bank
- Export: CSV/PDF from RAK Business Online
- Standard format

### Dubai Islamic Bank (DIB)
- Export: CSV from DIB Business Online
- Narrations may include Islamic finance terminology (Murabaha, Wakala)
- Profit distributions: `PROFIT ON WAKALA DEPOSIT` (not interest)

### Commercial Bank of Dubai (CBD)
- Export: CSV from CBD Online
- Standard UAE format

### ADIB (Abu Dhabi Islamic Bank)
- Export: CSV from ADIB Online
- Islamic banking narrations

### Key UAE Banking Notes
- All amounts in AED (UAE dirhams); comma thousands, period decimal
- AED is pegged to USD at 3.6725
- International wires often appear as `TT` (telegraphic transfer)
- SWIFT charges appear as separate debit narrations
- WPS (Wage Protection System) credits are salary — exclude from business income
- Many UAE businesses maintain accounts in multiple banks across emirates

---

## Section 9 — Onboarding Fallback

**Business structure confirmation:**
> "Before computing UAE corporate tax, I need to confirm your business structure. Are you a licensed freelancer (with a freelance permit), a sole establishment, or a company (LLC, FZ-LLC, etc.)? Natural persons (freelancers without a trade licence) are only subject to CT if annual turnover exceeds AED 1,000,000. If you are an employee earning a salary, the UAE has no personal income tax and you have no CT obligation."

**SBR eligibility:**
> "If your annual revenue is AED 3,000,000 or less, you may be eligible for Small Business Relief, which would make your taxable income nil (zero tax). However, SBR must be actively elected on your CT return through EmaraTax — it is not automatic. Would you like to check SBR eligibility?"

**Registration status:**
> "Have you registered for corporate tax with the Federal Tax Authority? All UAE businesses (including sole establishments and free zone companies) must register on EmaraTax and obtain a Tax Registration Number (TRN). Late registration incurs a penalty of AED 10,000. If you have not yet registered, I recommend doing so immediately."

**Free zone status:**
> "Is your business registered in a UAE free zone? If so, you may qualify as a Qualifying Free Zone Person (QFZP), which allows 0% tax on qualifying income. QFZP status has strict requirements including adequate substance, qualifying activities only, and audited financial statements. I would need to verify all conditions before advising on the 0% rate."

---

## Section 10 — Reference Material

### Key Legislation
- **Federal Decree-Law No. 47 of 2022** — Taxation of Corporations and Businesses
- **Cabinet Decision No. 116 of 2022** — Small Business Relief
- **Cabinet Decision No. 37 of 2023** — Free Zone rules
- **Ministerial Decision No. 73 of 2023** — Non-Deductible Expenditure
- **Ministerial Decision No. 229 of 2025** — Qualifying Activities (QFZP)
- **Federal Decree-Law No. 28 of 2022** — Tax Procedures
- **Cabinet Decision No. 75 of 2023** — Penalties

### Filing Deadlines

| FY End | CT Return and Payment Due |
|---|---|
| 31 December 2024 | 30 September 2025 |
| 31 March 2025 | 31 December 2025 |
| 30 June 2025 | 31 March 2026 |
| 31 December 2025 | 30 September 2026 |

### Penalties

| Offence | Penalty |
|---|---|
| Failure to register on time | AED 10,000 |
| Late filing | AED 500/month from month after due date |
| Late payment | 14% per annum on outstanding amount |
| Failure to maintain records | AED 10,000 (first); AED 20,000 (repeat) |

### Record Keeping
- Minimum retention: 7 years from end of tax period
- Financial statements, accounting records, contracts, invoices, bank statements
- Audited financial statements required for QFZP

### Useful References
- FTA / EmaraTax: tax.gov.ae
- CT registration: EmaraTax portal
- IFRS guidance: ifrs.org
- Free zone authorities: DMCC, JAFZA, DAFZA, DIFC, ADGM (individual portals)
