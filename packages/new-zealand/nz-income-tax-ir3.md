---
name: nz-income-tax-ir3
description: >
  Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "IETC", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", "schedular withholding NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. This skill covers NZ tax brackets (10.5%-39%), IR3 return structure, allowable deductions, ACC levies, provisional tax, IETC, penalties, and interaction with GST. ALWAYS read this skill before touching any NZ income tax work.
version: 2.0
jurisdiction: NZ
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# New Zealand Income Tax -- Self-Employed IR3 v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | New Zealand (Aotearoa) |
| Tax | Income Tax (progressive 10.5%-39%) + ACC Earner Levy |
| Currency | NZD only |
| Tax year | 1 April to 31 March (FY 2025 = 1 April 2024 to 31 March 2025) |
| Primary legislation | Income Tax Act 2007 (NZ) |
| Supporting legislation | Tax Administration Act 1994; Goods and Services Tax Act 1985 |
| Tax authority | Inland Revenue (Te Tari Taake) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Filing deadline | 7 July (self-filers); 31 March of following year (with tax agent) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a NZ Chartered Accountant (CA ANZ) |
| Skill version | 2.0 |

### Income Tax Brackets FY 2025 (1 April 2024 - 31 March 2025) [T1]

| Taxable Income (NZD) | Rate | Tax on Band | Cumulative Tax |
|---|---|---|---|
| 0 -- 14,000 | 10.5% | 1,470 | 1,470 |
| 14,001 -- 48,000 | 17.5% | 5,950 | 7,420 |
| 48,001 -- 70,000 | 30% | 6,600 | 14,020 |
| 70,001 -- 180,000 | 33% | 36,300 | 50,320 |
| Over 180,000 | 39% | on excess | 50,320 + 39% |

**Formula:** Tax = cumulative tax for lower bracket + (income - lower bracket threshold) x marginal rate

### ACC Levies 2025 [T1]

| Levy | Rate | Base | Cap |
|---|---|---|---|
| Work levy (sole traders) | ~NZD 1.33 per NZD 100 of liable earnings | Net self-employment income | NZD 139,384 (maximum liable earnings) |
| Working safer levy | NZD 0.08 per NZD 100 | Same base | Same cap |
| Earner levy | ~NZD 1.33 per NZD 100 | Same base | Same cap |

**Total ACC rate ~NZD 2.74 per NZD 100 of liable earnings (varies by industry -- confirm ACC invoice).**

ACC earner levy is assessed by IRD alongside income tax. ACC work levy is a separate invoice from ACC and IS a deductible expense.

### Provisional Tax [T1]

Self-employed taxpayers with Residual Income Tax (RIT) > NZD 5,000 must pay provisional tax.

| Method | Rule |
|---|---|
| Standard method | 105% of prior-year RIT, spread over 3 instalments |
| Estimation method | Estimate current-year tax, pay in 3 instalments |
| Ratio method (GST registered) | Available for GST-registered taxpayers; proportional to GST turnover |

**RIT = Income tax + ACC earner levy - PAYE and withholding tax credits**

Provisional tax dates (most taxpayers, March balance date): 28 August, 15 January, 7 May.

### Independent Earner Tax Credit (IETC) [T1]

| Income | IETC Amount |
|---|---|
| NZD 24,000 -- NZD 44,000 | NZD 520/year |
| Phases out above NZD 44,000 | Reduces by NZD 13/NZD 1 above NZD 44,000 |
| NZD 48,000+ | NZD 0 |

Conditions: no Working for Families, not receiving NZ Super, income between NZD 24,000-48,000.

### Conservative Defaults [T1]

| Situation | Default Assumption |
|---|---|
| GST-exclusive vs GST-inclusive unclear | Flag -- income tax uses GST-exclusive amounts (for GST-registered) |
| Mixed personal/business expense | Non-deductible -- flag for reviewer |
| Home office deduction claimed | Apply only if dedicated workspace; use floor area proportion |
| Motor vehicle: business % unclear | Use actual logbook records; if no logbook, default 25% business |
| Schedular payment withholding rate unknown | Apply 20% default (standard schedular rate) |
| ACC levy amount uncertain | Use ~2.74% of liable earnings; flag -- actual invoice may differ |
| Provisional tax method not specified | Standard method (105% of prior year) |

### Red Flag Thresholds [T1]

| Flag | Threshold |
|---|---|
| RIT > NZD 5,000 | Provisional tax required -- check if paid |
| Gross income > NZD 60,000 | GST registration mandatory -- verify |
| Motor vehicle expenses > 50% of all expenses | Logbook scrutiny -- flag |
| Cash income with no trail | Document carefully; Inland Revenue audit risk |
| Single contractor relationship (regular, directed work) | Possible employment -- flag |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full tax year (1 April - 31 March) in CSV, PDF, or pasted text. Confirmation of GST registration status.

**Recommended:** All client invoices, schedular payment withholding certificates, motor vehicle logbook (if claiming > 25%), ACC levy invoice, provisional tax payment receipts, prior year IR3.

**Ideal:** Complete accounting records (Xero/MYOB export), GST return summary, depreciation schedule, prior year Notice of Assessment.

### Refusal Catalogue

**R-NZ-1 -- Income figures include GST but taxpayer is GST-registered.** "Stop -- strip GST from all income and expense figures before computing. Mixed amounts distort the computation."

**R-NZ-2 -- Company (Ltd) income mixed with personal IR3.** "Company income is not personal income. Only dividends/salary from the company appear in the IR3. Escalate."

**R-NZ-3 -- Non-resident with NZ-source income.** "Non-resident withholding tax (NRWT) and different rate schedule applies. Escalate."

**R-NZ-4 -- No motor vehicle logbook but large vehicle claim.** "Reject undocumented vehicle claim > 25% default. Flag for Inland Revenue."

**R-NZ-5 -- Client relationship appears to be employment.** "Inland Revenue employment test may apply. Do not treat as self-employment without review."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| PAYMENT FROM [client] / TFR FROM [client] | Self-employment income | Gross revenue | Standard bank credit from client |
| INTERNET TFR / ONLINE PAYMENT [client] | Self-employment income | Revenue | NZ online transfer from business client |
| STRIPE PAYOUT / STRIPE PAYMENTS | Self-employment income -- gross-up | Revenue | Stripe NZ payout; gross-up to pre-fee; fee deductible |
| PAYPAL TRANSFER / PAYPAL NZ | Self-employment income -- gross-up | Revenue | PayPal net; fee deductible |
| WINDCAVE SETTLEMENT / EFTPOS NZ SETTLEMENT | Self-employment income -- gross-up | Revenue | NZ card payment providers; gross-up |
| SQUARESPACE PAYMENTS / SQUARE NZ | Self-employment income -- gross-up | Revenue | Square NZ / Squarespace; gross-up |
| SCHEDULAR PAYMENT (line annotation) | Schedular income -- gross-up | Revenue | Withholding deducted by payer; gross = net / (1 - WHT rate) |
| SALARY CREDIT [employer] | Employment income | NOT self-employment income | Separate income category; Form IR4 employer |
| INTEREST PAID / BANK INTEREST | Interest income | Reportable income | Usually subject to RWT deduction |
| DIVIDEND [company] | Dividend income | Include gross + imputation credits | Separate income type |
| IRD REFUND / INLAND REVENUE REFUND | EXCLUDE | Not income | Tax refund |
| GST REFUND IRD | EXCLUDE | Not income | GST refund -- separate tax |
| RENTAL INCOME [property] | Rental income -- Schedule E | NOT self-employment income | Different return section |

### 3.2 Expense Patterns (Debits)

| Pattern | Tax Category | Treatment | Notes |
|---|---|---|---|
| RENT [office/workspace] / COMMERCIAL RENT | Office rent -- 100% deductible | Fully deductible | Home office: floor area proportion only |
| GENESIS ENERGY / MERIDIAN ENERGY / CONTACT ENERGY / MERCURY | Utilities -- business proportion | Deductible | Home office: floor area %; dedicated office: 100% |
| SPARK NZ / ONE NZ / 2DEGREES | Phone/internet -- business proportion | Deductible | Document business % (commonly 50-80%) |
| ADOBE / MICROSOFT 365 / GOOGLE WORKSPACE / XERO / MYOB | Software subscriptions -- 100% deductible | Fully deductible | Professional software |
| CHARTERED ACCOUNTANTS / ACCOUNTANT / TAX AGENT | Accounting/tax fees -- 100% deductible | Fully deductible | Tax preparation fees are deductible |
| INTERISLANDER / BLUEBRIDGE / AIR NZ / JETSTAR | Travel -- 100% deductible (business purpose) | Fully deductible | Require purpose note; personal travel = 0% |
| HILTON / IBIS / NOVOTEL / AIRBNB | Accommodation -- 100% deductible (business travel) | Fully deductible | Personal = 0%; require business purpose |
| Z ENERGY / BP NZ / MOBIL NZ / GULL | Fuel -- deductible (business proportion) | Business portion | Require logbook or 25% default |
| AA NZ / VEHICLE REGISTRATION / NZTA | Vehicle costs -- deductible (business %) | Business portion | Same logbook rule as fuel |
| ACC LEVY / ACC INVOICE | ACC work levy -- 100% deductible | Fully deductible | Work levy paid to ACC is deductible; earner levy is in tax computation |
| INLAND REVENUE PROV TAX / IRD PROVISIONAL TAX | Provisional tax -- NOT deductible | EXCLUDE | Tax prepayments are not expenses |
| GST PAYMENT IRD | GST payment -- NOT deductible | EXCLUDE | Separate tax; not income tax expense |
| PROFESSIONAL INDEMNITY INS / PUBLIC LIABILITY INS | Business insurance -- 100% deductible | Fully deductible | Professional and business policies |
| LINKEDIN PREMIUM / SEEK ADVERTISE / TRADEME JOBS | Business platform subscriptions | Fully deductible | Marketing and recruitment platforms |
| COURIER POST / NZ POST / DHL NZ | Postage/courier -- 100% deductible | Fully deductible | Business deliveries |
| BANK FEE / ACCOUNT FEE / ANZ MONTHLY FEE | Bank charges -- 100% deductible | Fully deductible | Business account fees |
| XERO SUBSCRIPTION / MYOB SUBSCRIPTION | Accounting software -- 100% deductible | Fully deductible | Financial software |
| TRAINING / COURSE / CONFERENCE | Professional development -- deductible | Fully deductible | Must maintain/improve existing skills; new career = not deductible |
| SUBCONTRACTOR PAYMENT / CONTRACTOR INVOICE | Subcontract expenses -- deductible | Fully deductible | Schedular withholding obligation may apply |
| STRIPE FEES / PAYPAL FEES / SQUARE FEES | Payment processing fees -- deductible | Fully deductible | Deduct the gross-up difference |
| ENTERTAINMENT / MEALS CLIENT | Entertainment -- 50% deductible | 50% only | Entertainment deduction limitation |

---

## Section 4 -- Worked Examples

### Example 1 -- ANZ NZ (Auckland, IT Consultant)

**Input line (ANZ Business One CSV):**
`03/01/2025,,PAYMENT FROM ACME LTD,,11500.00,`

**Reasoning:**
Payment from business client. If James is GST-registered, this NZD 11,500 may be GST-inclusive. Ex-GST amount = NZD 11,500 / 1.15 = NZD 10,000. For income tax, use the ex-GST figure.

**Classification:** Self-employment income NZD 10,000 (ex-GST if registered).

### Example 2 -- Westpac NZ (Auckland, Photographer -- Vehicle Claim)

**Input line (Westpac Business Online CSV):**
`10/08/2025,SHELL SELECT QUEENSTOWN,120.00,,`

**Reasoning:**
Petrol NZD 120. Emma drives a personal car for client shoots. Business km logged: 8,400/14,000 total = 60% business (logbook maintained for 90+ days). Deductible portion: NZD 120 x 60% = NZD 72. Without logbook, default is 25% = NZD 30.

**Classification:** Motor vehicle expense NZD 72 (60% business per logbook). If no logbook: NZD 30 (25% default).

### Example 3 -- ASB Bank (Christchurch, Plumber -- Schedular Payment)

**Input line (ASB Business Edge CSV):**
`15/03/2025,SCHEDULAR PAYMENT BUILDCO LTD,-,4000.00,`

**Reasoning:**
Schedular payment received NZD 4,000. Building company withheld 20% tax before paying. Gross income = NZD 4,000 / (1 - 0.20) = NZD 5,000. Withholding tax credit = NZD 1,000. Report NZD 5,000 as gross income and claim NZD 1,000 as withholding credit.

**Classification:** Self-employment income NZD 5,000 (gross). Withholding credit NZD 1,000.

### Example 4 -- BNZ (Wellington, Marketing Consultant)

**Input line (BNZ Business CSV):**
`28/02/2025,TT,STRIPE PAYOUT,CODE,REF,2185.00,`

**Reasoning:**
Stripe NZ payout NZD 2,185. Stripe collected approximately NZD 2,254 from clients and deducted ~NZD 69 in fees. Gross revenue = NZD 2,254 (ex-GST if GST-registered). Stripe fee NZD 69 is deductible.

**Classification:** Gross revenue NZD 2,254. Stripe fees NZD 69 deductible.

### Example 5 -- Kiwibank (Dunedin, Freelance Writer -- Foreign Income)

**Input line (Kiwibank CSV):**
`20/05/2025,PAYPAL TRANSFER USD,,,1850.00,`

**Reasoning:**
PayPal payout NZD 1,850 from overseas clients paid in USD. Foreign currency income must be converted to NZD at the Reserve Bank mid-rate on the date of receipt (or annual average rate by agreement). The NZD equivalent at receipt date is the income figure.

**Classification:** Self-employment income NZD 1,850 (converted at receipt-date rate).

### Example 6 -- ANZ (Hamilton, E-commerce Seller -- GST Check)

**Input line (ANZ FastNet Business CSV):**
`01/09/2025,,WINDCAVE SETTLEMENT,,8500.00,`

**Reasoning:**
Windcave card payment settlement NZD 8,500. Rachel's annual gross revenue is NZD 95,000 -- above the NZD 60,000 GST registration threshold. She must be GST-registered. All figures must be ex-GST for income tax: NZD 8,500 / 1.15 = NZD 7,391.30.

**Classification:** Revenue NZD 7,391.30 (ex-GST). RED FLAG: verify GST registration.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 GST-Registered: Always Use Ex-GST Amounts

For GST-registered taxpayers, all income and expenses in the IR3 must be reported exclusive of GST. Strip 3/23 (for 15% GST) from GST-inclusive amounts. Apply without escalating.

### 5.2 ACC Earner Levy Is Included in Tax Payment

The ACC earner levy (~1.33% of liable earnings) is assessed by IRD alongside income tax and paid with the IR3 balance. It is NOT a separate payment to ACC. The ACC work levy IS a separate invoice from ACC and IS a deductible expense. Apply this distinction consistently.

### 5.3 Entertainment: 50% Limitation

Business meals and entertainment are limited to 50% deductible under the Income Tax Act. Apply 50% to all restaurant, cafe, and entertainment narrations where a business purpose is noted. Social/personal entertainment = 0%.

### 5.4 Provisional Tax Is Not Deductible

Provisional tax instalments paid to IRD are not deductible business expenses. They are advance payments of income tax. Always exclude them from the expense calculation.

### 5.5 Motor Vehicle Logbook Required for > 25% Business Use

Claims above the default 25% business use require a logbook maintained for a minimum of 90 consecutive days at least once every three years. If no logbook is available, cap business use at 25%. Never claim > 25% without logbook evidence.

### 5.6 Schedular Payments: Always Gross Up

When income was subject to schedular withholding, gross income = amount received / (1 - withholding rate). The withheld amount is a tax credit. Always gross up before entering in the income section.

### 5.7 Foreign Currency Income: Use NZD at Date of Receipt

Income received in foreign currencies must be converted to NZD at the exchange rate on the date of receipt (or annual average rate by agreement). Use Reserve Bank of NZ indicative rates. Do not convert at year-end rate.

### 5.8 Tax Computation Flow

```
Gross self-employment receipts (ex-GST if registered)
Less: Allowable business expenses
= Net taxable income
Apply bracket rates
Less: IETC (if income NZD 24,000-48,000)
= Net income tax
Plus: ACC earner levy (~1.33% of liable earnings)
= Total tax
Less: Schedular withholding credits
Less: Provisional tax paid
= Residual Income Tax (RIT) / refund
```

### 5.9 Filing Deadlines

| Item | Deadline |
|---|---|
| IR3 due (self-filers) | 7 July of following year |
| IR3 due (with tax agent) | 31 March of second following year |
| Terminal tax | 7 February of following year |
| Provisional tax (March balance date) | 28 August, 15 January, 7 May |

### 5.10 Penalties

| Offence | Penalty |
|---|---|
| Late filing | NZD 50/month up to NZD 300 |
| Late payment | 1% initial + 4% incremental (after 7 days) + 1.5%/month ongoing |
| Shortfall penalties (not taking reasonable care) | 20% of shortfall |
| Shortfall (unacceptable interpretation) | 20% |
| Shortfall (gross carelessness) | 40% |
| Shortfall (evasion) | 150% |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed Company/Personal Income

Company income not reportable in IR3; only salary/dividends from the company appear. Clarify business structure before proceeding.

### 6.2 Rental Property Income

Separate schedule in IR3. Different deductibility rules -- interest deductibility limited post-Brightline reform. Ring-fenced rental losses may apply.

### 6.3 Brightline Property Sale

10-year Brightline test: gains on residential property sold within 10 years are taxable. Complex rules; confirm purchase and sale dates.

### 6.4 Working for Families Tax Credits

IETC cannot be claimed alongside WFF. Complex abatement on WFF. Confirm eligibility before applying either IETC or WFF.

### 6.5 Non-Resident NZ-Source Income

Non-resident withholding tax (NRWT) applies with different rates. Do not apply resident rates.

### 6.6 Imputation Credits on Dividends

Dividends gross + imputation credits both reportable. Imputation credit is a tax credit. Require dividend statement from company.

### 6.7 Losses in Prior Years

NZ allows carrying forward business losses. Prior-year losses reduce current taxable income if criteria met. Confirm with prior year return.

---

## Section 7 -- Excel Working Paper Template

```
NEW ZEALAND INCOME TAX WORKING PAPER (IR3 -- SELF-EMPLOYED)
Taxpayer: _______________  IRD Number: _______________  FY: 1 April 2024 - 31 March 2025

SECTION A -- SELF-EMPLOYMENT INCOME (ex-GST)
                                        NZD
Gross self-employment receipts         ___________
Less: GST component (if incl.)         (___________)
Net ex-GST income                      ___________
Schedular income (grossed up)          ___________
Other business income                  ___________
TOTAL INCOME                           ___________

SECTION B -- DEDUCTIBLE EXPENSES
Rent / workspace (business portion)    ___________
Utilities (business proportion)        ___________
Phone / internet (business %)          ___________
Software subscriptions                 ___________
Accounting / tax agent fees            ___________
Legal fees                             ___________
Travel (business trips)                ___________
Accommodation (business travel)        ___________
Meals & entertainment (50%)            ___________
Business insurance                     ___________
Bank charges (business account)        ___________
Motor vehicle (logbook %)              ___________
ACC work levy                          ___________
Depreciation                           ___________
Subcontractor costs                    ___________
Payment processor fees                 ___________
Other business expenses                ___________
TOTAL DEDUCTIBLE EXPENSES              ___________

SECTION C -- NET TAXABLE INCOME
Total income - Total expenses          ___________

SECTION D -- INCOME TAX
Tax at bracket rates (see table)       ___________
Less: IETC (if income NZD 24k-48k)    (___________)
NET INCOME TAX                         ___________

SECTION E -- ACC EARNER LEVY
Net income x 1.33%                     ___________

SECTION F -- RIT AND PROVISIONAL TAX
Income tax + ACC - withholding credits ___________
Less: provisional tax paid             (___________)
RIT BALANCE DUE / (REFUND)             ___________
Next year provisional (105% of RIT):   ___________

SECTION G -- REVIEWER FLAGS
[ ] GST stripped from income/expenses (if GST-registered)?
[ ] Schedular payments grossed up and withholding credit recorded?
[ ] Motor vehicle logbook reviewed -- business % substantiated?
[ ] Entertainment capped at 50%?
[ ] Home office -- floor area proportion documented?
[ ] ACC work levy invoice included as expense?
[ ] Provisional tax instalments reconciled against IRD account?
[ ] Foreign income converted to NZD at receipt-date rate?
```

---

## Section 8 -- Bank Statement Reading Guide

### New Zealand Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| ANZ NZ | CSV | Date,Description,Debit,Credit,Balance |
| BNZ (Bank of New Zealand) | CSV | Date,Tran Type,Particulars,Code,Reference,Amount,Balance |
| ASB Bank | CSV | Date,Unique Id,Tran Type,Cheque Number,Payee,Memo,Amount |
| Westpac NZ | CSV | Date,Narrative,Debit Amount,Credit Amount,Balance |
| Kiwibank | CSV | Date,Description,Debit,Credit,Balance |

### Key NZ Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| PAYMENT FROM [name] / TFR FROM [name] | Bank transfer in | Potential business income |
| INTERNET TFR | Online transfer | Income or expense |
| D/C (Direct Credit) | Direct credit | Potential income |
| D/D (Direct Debit) | Direct debit | Recurring expense |
| ATM WITHDRAWAL | Cash withdrawal | Personal -- investigate |
| IRD PROV TAX / INLAND REVENUE | Tax payment | Tax prepayment -- exclude |
| GST PAYMENT | GST remittance | Separate tax -- exclude |
| INTEREST | Bank interest | Other income |
| ACC LEVY | ACC payment | Work levy deductible; earner levy in tax |

### NZ Three-Part Narration (Particulars/Code/Reference)

NZ bank-to-bank transfers allow three fields the sender fills in:
- **Particulars:** Usually the payer's name or invoice reference
- **Code:** Account code or project reference
- **Reference:** Invoice number, date, or other identifier

Combine all three to identify transaction source.

### Amount Format Notes

- Date format: DD/MM/YYYY
- Amount format: no thousands separator, period decimal (e.g., 11500.00)
- ANZ/Westpac: separate Debit/Credit columns
- BNZ/ASB: single Amount column (positive = credit, negative = debit)

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all PAYMENT FROM / TFR FROM credits from non-personal sources as potential self-employment income
2. Apply conservative defaults: non-GST registered (use face value), 25% vehicle default, no IETC
3. Exclude all IRD PROV TAX and GST PAYMENT debits from expenses
4. Mark all Stripe/PayPal/Windcave for gross-up
5. Flag all entertainment at 50% pending confirmation
6. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- NEW ZEALAND INCOME TAX (IR3)
1. Are you GST-registered? If so, are your bank statement amounts GST-inclusive or exclusive?
2. Tax year: are we preparing FY ended 31 March 2025?
3. Do you use a vehicle for work? If so, do you have a logbook (90+ consecutive days)?
4. Do you work from a dedicated home office? What % of floor area?
5. Did any clients deduct schedular withholding tax before paying you? At what rate?
6. Prior year RIT: did you pay provisional tax this year? How much?
7. Do you receive Working for Families tax credits?
8. Any income from rental properties?
9. Did you receive dividends from NZ companies? (Imputation credits)
10. Any foreign currency income? From which countries?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Income tax (general) | Income Tax Act 2007 (NZ) |
| Filing and penalties | Tax Administration Act 1994 |
| GST (separate) | Goods and Services Tax Act 1985 |
| Schedular payments | Income Tax Act 2007 Part R |
| Entertainment limitation | Income Tax Act 2007 subpart DD |
| Depreciation | Income Tax Act 2007 subpart EE |
| ACC levies | Accident Compensation Act 2001 |

### Known Gaps / Out of Scope

- Company (Ltd) income tax
- Non-resident NZ-source income (NRWT)
- Brightline property gains (complex)
- Working for Families calculations
- GST return computation
- KiwiSaver employer contribution calculations

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats (ANZ, BNZ, ASB, Westpac, Kiwibank); transaction pattern library; Windcave/PayNow patterns; worked examples; PROHIBITIONS and disclaimer added |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] GST stripped from all amounts for GST-registered taxpayers?
- [ ] Schedular payments grossed up (not net bank receipt)?
- [ ] Motor vehicle claim supported by logbook or capped at 25%?
- [ ] Entertainment limited to 50%?
- [ ] ACC earner levy added to tax (not as a separate expense)?
- [ ] ACC work levy included as deductible expense?
- [ ] Provisional tax excluded from expenses?
- [ ] Foreign currency converted at receipt-date rate?
- [ ] RIT correctly computed (income tax + ACC earner levy - withholding)?

---

## PROHIBITIONS

- NEVER include GST-inclusive amounts in income or expenses for GST-registered taxpayers -- always strip GST first
- NEVER claim motor vehicle business use above 25% without a qualifying logbook (90+ consecutive days)
- NEVER allow entertainment deductions above 50% of the cost
- NEVER include provisional tax or GST payments as deductible business expenses
- NEVER apply IETC if the taxpayer receives Working for Families tax credits or NZ Super
- NEVER confuse ACC earner levy (in tax computation) with ACC work levy (deductible expense)
- NEVER convert foreign currency income at year-end rate -- use receipt-date rate
- NEVER treat schedular payment net receipts as gross income -- always gross up
- NEVER apply resident rates to non-residents -- escalate
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Chartered Accountant for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant CA ANZ, or equivalent licensed practitioner in New Zealand) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
