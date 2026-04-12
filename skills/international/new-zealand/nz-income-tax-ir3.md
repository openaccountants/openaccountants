---
name: nz-income-tax-ir3
description: >
  Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "IETC", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", "schedular withholding NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. This skill covers NZ tax brackets (10.5%–39%), IR3 return structure, allowable deductions, ACC levies, provisional tax, IETC, penalties, and interaction with GST. ALWAYS read this skill before touching any NZ income tax work.
version: 2.0
---

# New Zealand Income Tax — Self-Employed IR3 v2.0

## Section 1 — Quick Reference

### Income Tax Brackets 2025 (FY ended 31 March 2025)

| Taxable Income (NZD) | Rate | Tax on Band | Cumulative Tax |
|---|---|---|---|
| 0 – 14,000 | 10.5% | 1,470 | 1,470 |
| 14,001 – 48,000 | 17.5% | 5,950 | 7,420 |
| 48,001 – 70,000 | 30% | 6,600 | 14,020 |
| 70,001 – 180,000 | 33% | 36,300 | 50,320 |
| Over 180,000 | 39% | on excess | 50,320 + 39% |

**Formula:** Tax = cumulative tax for lower bracket + (income − lower bracket threshold) × marginal rate

**Tax year:** 1 April to 31 March (FY 2025 = 1 April 2024 to 31 March 2025)

### ACC Levies 2025

| Levy | Rate | Base | Cap |
|---|---|---|---|
| Work levy (sole traders) | ~NZD 1.33 per NZD 100 of liable earnings | Net self-employment income | NZD 139,384 (maximum liable earnings) |
| Working safer levy | NZD 0.08 per NZD 100 | Same base | Same cap |
| Earner levy | ~NZD 1.33 per NZD 100 | Same base | Same cap |

**Total ACC rate ~NZD 2.74 per NZD 100 of liable earnings (varies by industry — confirm ACC invoice).**

ACC is charged by Accident Compensation Corporation; invoiced separately. Self-employed pay via IR3 (earner levy included with income tax) + separate ACC invoice (work levy).

### Provisional Tax

Self-employed taxpayers with Residual Income Tax (RIT) > NZD 5,000 must pay provisional tax.

| Method | Rule |
|---|---|
| Standard method | 105% of prior-year RIT, spread over 3 instalments |
| Estimation method | Estimate current-year tax, pay in 3 instalments |
| Ratio method (GST registered) | Available for GST-registered taxpayers; proportional to GST turnover |

**RIT = Income tax + ACC earner levy − PAYE and withholding tax credits**

Provisional tax dates (most taxpayers, March balance date):
- 28 August
- 15 January
- 7 May

### Independent Earner Tax Credit (IETC)

| Income | IETC Amount |
|---|---|
| NZD 24,000 – NZD 44,000 | NZD 520/year |
| Phases out above NZD 44,000 | Reduces by NZD 13/NZD 1 above NZD 44,000 |
| NZD 48,000+ | NZD 0 |

Conditions: no Working for Families, not receiving NZ Super, income between NZD 24,000–48,000.

### Conservative Defaults

| Situation | Default Assumption |
|---|---|
| GST-exclusive vs. GST-inclusive unclear | Flag — income tax uses GST-exclusive amounts (for GST-registered) |
| Mixed personal/business expense | Non-deductible — flag for reviewer |
| Home office deduction claimed | Apply only if dedicated workspace; use floor area proportion |
| Motor vehicle: business % unclear | Use actual logbook records; if no logbook, default 25% business |
| Schedular payment withholding rate unknown | Apply 20% default (standard schedular rate) |
| ACC levy amount uncertain | Use ~2.74% of liable earnings; flag — actual invoice may differ |
| Provisional tax method not specified | Standard method (105% of prior year) |

### Red Flag Thresholds

| Flag | Threshold |
|---|---|
| RIT > NZD 5,000 | Provisional tax required — check if paid |
| Gross income > NZD 60,000 | GST registration mandatory — verify |
| Motor vehicle expenses > 50% of all expenses | Logbook scrutiny — flag |
| Cash income with no trail | Document carefully; Inland Revenue audit risk |
| Single contractor relationship (regular, directed work) | Possible employment — flag |

---

## Section 2 — Required Inputs + Refusal Catalogue

### Required Inputs

Before computing New Zealand income tax, collect:

1. **Total gross income** — all self-employment receipts, ex-GST (if registered)
2. **Itemised deductible expenses** — with receipts or bank evidence
3. **Motor vehicle logbook** — if claiming vehicle expenses (or no logbook: use default)
4. **Prior-year RIT** — for provisional tax standard method
5. **Bank statements** — 12 months (1 April–31 March)
6. **Schedular payment withholding certificates** — if income subject to schedular deductions
7. **GST return summary** — to cross-check income (if GST registered)
8. **ACC levy invoice** — actual work levy charged by ACC
9. **Provisional tax instalments paid** — dates and amounts
10. **Other income sources** — salary/wages (IR4 employers), rental (Schedule E), interest, dividends

### Refusal Catalogue

| Code | Situation | Action |
|---|---|---|
| R-NZ-1 | Income figures include GST but taxpayer is GST-registered | Stop — strip GST from all income and expense figures before computing; mixed amounts distort the computation |
| R-NZ-2 | Company (Ltd) income mixed with personal IR3 | Stop — company income is not personal income; only dividends/salary from company appear in IR3 |
| R-NZ-3 | Non-resident with NZ-source income | Flag — non-resident withholding tax (NRWT) and different rate schedule applies |
| R-NZ-4 | No motor vehicle logbook available but large vehicle claim made | Reject undocumented vehicle claim > 25% default; flag for Inland Revenue |
| R-NZ-5 | Client relationship appears to be employment (regular hours, tools provided by payer) | Flag — Inland Revenue employment test may apply; do not treat as self-employment without review |

---

## Section 3 — Transaction Pattern Library

### Income Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| I-01 | `PAYMENT FROM [client]` / `TFR FROM [client]` | Self-employment income | Standard bank credit from client |
| I-02 | `INTERNET TFR` / `ONLINE PAYMENT [client]` | Self-employment income | NZ online transfer from business client |
| I-03 | `STRIPE PAYOUT` / `STRIPE PAYMENTS` | Self-employment income — gross-up | Stripe NZ payout; gross-up to pre-fee; fee deductible |
| I-04 | `PAYPAL TRANSFER` / `PAYPAL NZ` | Self-employment income — gross-up | PayPal net; fee deductible |
| I-05 | `WINDCAVE SETTLEMENT` / `EFTPOS NZ SETTLEMENT` | Self-employment income — gross-up | NZ card payment providers; gross-up |
| I-06 | `SQUARESPACE PAYMENTS` / `SQUARE NZ` | Self-employment income — gross-up | Square NZ / Squarespace; gross-up |
| I-07 | `SCHEDULAR PAYMENT` (line annotation) | Schedular income — gross-up | Withholding deducted by payer; gross = net ÷ (1 − WHT rate) |
| I-08 | `IRD REFUND` / `INLAND REVENUE REFUND` | NOT income — tax refund | Provisional tax refund from Inland Revenue |
| I-09 | `GST REFUND IRD` | NOT income — GST refund | GST is separate; not income tax income |
| I-10 | `RENTAL INCOME [property]` | Rental income — Schedule E | Separate from self-employment; different return section |
| I-11 | `INTEREST PAID` / `BANK INTEREST` | Interest income | Reportable income; usually subject to RWT deduction |
| I-12 | `DIVIDEND [company]` | Dividend income | Include gross dividend + imputation credits in return |

### Expense Patterns

| # | Narration Pattern | Tax Line | Notes |
|---|---|---|---|
| E-01 | `RENT [office/workspace]` / `COMMERCIAL RENT` | Office rent — 100% deductible | Home office: floor area proportion only |
| E-02 | `GENESIS ENERGY` / `MERIDIAN ENERGY` / `CONTACT ENERGY` / `MERCURY` | Utilities — business proportion | Home office: floor area %; dedicated office: 100% |
| E-03 | `SPARK NZ` / `ONE NZ` / `2DEGREES` | Phone/internet — business proportion | Document business % (commonly 50–80%) |
| E-04 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` / `XERO` / `MYOB` | Software subscriptions — 100% deductible | Professional software |
| E-05 | `CHARTERED ACCOUNTANTS` / `ACCOUNTANT` / `TAX AGENT` | Accounting/tax fees — 100% deductible | Tax preparation fees are deductible |
| E-06 | `INTERISLANDER` / `BLUEBRIDGE` / `AIR NZ` / `JETSTAR` | Travel — 100% deductible (business purpose) | Require purpose note; personal travel = 0% |
| E-07 | `HILTON` / `IBIS` / `NOVOTEL` / `AIRBNB` | Accommodation — 100% deductible (business travel) | Personal = 0%; require business purpose evidence |
| E-08 | `Z ENERGY` / `BP NZ` / `MOBIL NZ` / `GULL` | Fuel — deductible (business proportion) | Require logbook or 25% default if no logbook |
| E-09 | `AA NZ` / `VEHICLE REGISTRATION` / `NZTA` | Vehicle costs — deductible (business %) | Same logbook rule as fuel |
| E-10 | `ACC LEVY` / `ACC INVOICE` | ACC work levy — 100% deductible | ACC earner levy is embedded in tax computation; work levy paid to ACC is a deductible expense |
| E-11 | `INLAND REVENUE PROV TAX` / `IRD PROVISIONAL TAX` | Provisional tax — NOT deductible | Tax prepayments are not expenses |
| E-12 | `GST PAYMENT IRD` | GST payment — NOT deductible | Separate tax; not income tax expense |
| E-13 | `PROFESSIONAL INDEMNITY INS` / `PUBLIC LIABILITY INS` | Business insurance — 100% deductible | Professional and business policies |
| E-14 | `LINKEDIN PREMIUM` / `SEEK ADVERTISE` / `TRADEME JOBS` | Business platform subscriptions — 100% deductible | Marketing and recruitment platforms |
| E-15 | `COURIER POST` / `NZ POST` / `DHL NZ` | Postage/courier — 100% deductible | Business deliveries |
| E-16 | `BANK FEE` / `ACCOUNT FEE` / `ANZ MONTHLY FEE` | Bank charges — 100% deductible | Business account fees |
| E-17 | `DEPRECIATION` (journal entry) | Capital allowance — via depreciation schedule | IRD depreciation rates apply; do not expense >NZD 1,000 assets outright |
| E-18 | `XERO SUBSCRIPTION` / `MYOB SUBSCRIPTION` | Accounting software — 100% deductible | Financial software |
| E-19 | `TRAINING` / `COURSE` / `CONFERENCE` | Professional development — deductible | Must maintain or improve existing skills; new career = not deductible |
| E-20 | `SUBCONTRACTOR PAYMENT` / `CONTRACTOR INVOICE` | Subcontract expenses — deductible | Schedular withholding obligation may apply if subcontractor |
| E-21 | `STRIPE FEES` / `PAYPAL FEES` / `SQUARE FEES` | Payment processing fees — deductible | Deduct the gross-up difference |
| E-22 | `ENTERTAINMENT` / `MEALS CLIENT` | Entertainment — 50% deductible | Entertainment deduction limitation: 50% of costs for business meals/entertainment |

---

## Section 4 — Worked Examples

### Example 1 — ANZ NZ (Auckland, IT Consultant)

**Bank:** ANZ Business One CSV export
**Client:** James Tane, IT consultant, Auckland, GST registered

```
Date,Description,Debit,Credit,Balance
03/01/2025,,PAYMENT FROM ACME LTD,,11500.00,
15/01/2025,ANZ MONTHLY FEE,10.00,,
10/02/2025,,PAYMENT FROM TECHCO NZ,,8050.00,
28/02/2025,SPARK NZ INVOICE,115.00,,
15/03/2025,,STRIPE PAYOUT,,2185.00,
01/04/2025,ADOBE CREATIVE CLOUD,69.00,,
20/04/2025,,PAYMENT FROM STARTUP LTD,,5750.00,
15/06/2025,IRD PROVISIONAL TAX,4500.00,,
10/07/2025,CHARTERED ACCOUNTANTS NZ,920.00,,
10/10/2025,AIR NZ CHRISTCHURCH,245.00,,
```

**Step 1 — Income (ex-GST)**

| Narration | Pattern | Amount (ex-GST) |
|---|---|---|
| PAYMENT FROM ACME LTD | I-01 | NZD 10,000 (÷ 1.15 if GST-inclusive) |
| PAYMENT FROM TECHCO NZ | I-01 | NZD 7,000 |
| STRIPE PAYOUT | I-03 | NZD 2,185 net → gross ~NZD 2,254 ex-Stripe fees |
| PAYMENT FROM STARTUP LTD | I-01 | NZD 5,000 |
| **Total income (ex-GST)** | | **NZD 24,254** |

Note: Amounts above show ex-GST (GST registered client invoices + GST, receives + GST, remits to IRD). If not GST registered: face value = income.

**Step 2 — Deductible Expenses**

| Narration | Pattern | Amount | Deductible |
|---|---|---|---|
| ANZ MONTHLY FEE | E-16 | NZD 120/yr | NZD 120 |
| SPARK NZ | E-03 | NZD 1,380/yr | NZD 1,104 (80% business) |
| ADOBE | E-04 | NZD 828/yr | NZD 828 |
| CHARTERED ACCOUNTANTS | E-05 | NZD 920 | NZD 920 |
| AIR NZ | E-06 | NZD 245 | NZD 245 (business trip) |
| Stripe fees (gross-up) | E-21 | ~NZD 69 | NZD 69 |
| IRD PROVISIONAL TAX | E-11 | NZD 4,500 | NZD 0 |
| **Total deductible** | | | **NZD 3,286** |

**Step 3 — Net Income**

```
Total income (ex-GST):   NZD 24,254
Less expenses:           NZD  3,286
Net taxable income:      NZD 20,968
```

**Step 4 — Income Tax**

```
NZD 14,000 × 10.5% = NZD 1,470.00
NZD 6,968 × 17.5%  = NZD 1,219.40
Income tax:            NZD 2,689.40

IETC: income NZD 20,968 (in NZD 24,000–44,000 band): NZD 520
Net income tax: NZD 2,689.40 − NZD 520 = NZD 2,169.40
```

**Step 5 — ACC Earner Levy**

```
NZD 20,968 × 1.33% = NZD 278.87
```

**Step 6 — Residual Income Tax (RIT)**

```
Income tax + ACC earner levy − withholding credits
= NZD 2,169.40 + NZD 278.87 − NZD 0 = NZD 2,448.27
RIT < NZD 5,000 → no provisional tax required for next year
Less provisional tax paid: NZD 4,500 → refund NZD 2,051.73
```

---

### Example 2 — BNZ (Wellington, Marketing Consultant)

**Bank:** BNZ Business CSV
**Client:** Sarah O'Brien, marketing consultant, Wellington

Revenue: NZD 85,000 (ex-GST, multiple clients)
Expenses: Rent (home office 15% floor area × NZD 24,000 rent = NZD 3,600), utilities NZD 600, phone 70% × NZD 1,200 = NZD 840, software NZD 1,500, accounting NZD 1,200, travel NZD 2,000
Total expenses: NZD 9,740

Net income: NZD 85,000 − NZD 9,740 = **NZD 75,260**

Income tax:
NZD 14,000 × 10.5% = NZD 1,470
NZD 34,000 × 17.5% = NZD 5,950
NZD 22,000 × 30%   = NZD 6,600
NZD 5,260 × 33%    = NZD 1,735.80
Total: NZD 15,755.80

IETC: NZD 0 (income > NZD 48,000)
ACC earner levy: NZD 75,260 × 1.33% = NZD 1,000.96
RIT: NZD 15,755.80 + NZD 1,000.96 = NZD 16,756.76

RIT > NZD 5,000 — provisional tax required next year (standard: 105% × NZD 16,756.76 = NZD 17,594.60 over 3 instalments).

---

### Example 3 — ASB Bank (Christchurch, Tradespeople/Contractor)

**Bank:** ASB Business Edge CSV
**Client:** Mike Henderson, plumber, Christchurch, schedular payments received

Schedular income: Mike receives schedular payments from building company. Withholding deducted at 20%.

Received (net): NZD 48,000
Gross income: NZD 48,000 ÷ (1 − 0.20) = NZD 60,000
Withholding tax credit: NZD 12,000

Net income after expenses (NZD 8,000 tools/equipment/vehicle): NZD 52,000

Income tax: NZD 14,020 (for NZD 48,000) + (NZD 52,000 − NZD 48,000) × 30% = NZD 14,020 + NZD 1,200 = NZD 15,220
ACC earner levy: NZD 52,000 × 1.33% = NZD 691.60
RIT = NZD 15,220 + NZD 691.60 − NZD 12,000 = **NZD 3,911.60**

RIT < NZD 5,000 → no provisional tax next year.

Note: ACC work levy (industry rate for plumbers ~NZD 1.53/$100) charged separately by ACC on NZD 52,000 = ~NZD 795.60 deductible expense.

---

### Example 4 — Westpac NZ (Auckland, Photographer)

**Bank:** Westpac Business Online CSV
**Client:** Emma Liu, photographer, Auckland, motor vehicle claim

Motor vehicle: Emma drives her personal car for client shoots. Business km logged: 8,400/14,000 total = 60% business.

Vehicle expenses: fuel NZD 3,200, registration NZD 300, WOF NZD 80, insurance NZD 1,200, depreciation NZD 2,500
Total vehicle: NZD 7,280 × 60% = NZD 4,368 deductible

Note: Must have maintained logbook for at least 90 consecutive days to establish business %. Log requirement by IRD.

Net income: NZD 62,000 − NZD 12,000 (all expenses incl. NZD 4,368 vehicle) = **NZD 50,000**

Income tax: NZD 14,020 + (NZD 50,000 − NZD 48,000) × 30% = NZD 14,020 + NZD 600 = NZD 14,620
IETC: NZD 0 (income > NZD 48,000)

---

### Example 5 — Kiwibank (Dunedin, Freelance Writer)

**Bank:** Kiwibank CSV
**Client:** Tom Walker, freelance writer, Dunedin

Revenue: NZD 28,000 (mix of NZ and overseas clients via PayPal)
PayPal note: overseas clients paid in USD; NZD equivalent at time of receipt = income. Use IRD-accepted rate (Reserve Bank of NZ mid-rate on payment date or average rate method).

Net income: NZD 28,000 − NZD 3,500 (home office, phone, software, accounting) = **NZD 24,500**

Income tax:
NZD 14,000 × 10.5% = NZD 1,470
NZD 10,500 × 17.5% = NZD 1,837.50
Total: NZD 3,307.50

IETC: income NZD 24,500 (in range NZD 24,000–44,000): NZD 520
Net tax: NZD 3,307.50 − NZD 520 = **NZD 2,787.50**

---

### Example 6 — ANZ (Hamilton, E-commerce Seller)

**Bank:** ANZ FastNet Business CSV
**Client:** Rachel Park, e-commerce seller, Hamilton

Note: If Rachel has a trading company (Ltd), revenue flows through company — IR3 only for salary/dividends. Confirm structure.

Assuming sole trader (no company):
Gross revenue: NZD 95,000 (Shopify/Windcave settlements)

Check GST: NZD 95,000 > NZD 60,000 threshold → must be GST registered. All figures ex-GST.

COGS (cost of goods sold): NZD 42,000 (purchases)
Gross margin: NZD 53,000
Other expenses: NZD 11,000 (postage, packaging, platform fees, accounting)
Net income: **NZD 42,000**

Income tax: NZD 14,020 + (NZD 42,000 − NZD 48,000... wait: NZD 42,000 < NZD 48,000)
NZD 14,000 × 10.5% + NZD 28,000 × 17.5% = NZD 1,470 + NZD 4,900 = NZD 6,370
IETC: NZD 0 (NZD 42,000 > NZD 24,000 but < NZD 44,000): NZD 520
Net: NZD 6,370 − NZD 520 = **NZD 5,850**

RIT = NZD 5,850 + ACC → likely > NZD 5,000 → provisional tax required.

---

## Section 5 — Tier 1 Rules (Apply Directly)

**T1-NZ-1 — GST-registered: always use ex-GST amounts**
For GST-registered taxpayers, all income and expenses in the IR3 must be reported exclusive of GST. Amounts shown in bank statements may be inclusive of GST. Strip 3/23 (for 15% GST) from GST-inclusive amounts to get ex-GST. Apply without escalating.

**T1-NZ-2 — ACC earner levy is included in income tax payment**
The ACC earner levy (~1.33% of liable earnings) is assessed by IRD alongside income tax and paid with the IR3 balance. It is NOT a separate payment to ACC. The ACC work levy IS a separate invoice from ACC and IS a deductible expense. Apply this distinction consistently.

**T1-NZ-3 — Entertainment: 50% limitation**
Business meals and entertainment are limited to 50% deductible under the Income Tax Act. Apply 50% to all restaurant, cafe, and entertainment narrations where a business purpose is noted. Social/personal entertainment = 0%.

**T1-NZ-4 — Provisional tax is not a deductible expense**
Provisional tax instalments paid to IRD (appearing as `IRD PROV TAX` in bank statements) are not deductible business expenses — they are advance payments of income tax. Always exclude them from the expense calculation.

**T1-NZ-5 — Motor vehicle logbook required for >25% business use claims**
Claims above the default 25% business use require a logbook maintained for a minimum of 90 consecutive days at least once every three years. If no logbook is available, cap the business use at 25%. Never claim >25% without logbook evidence.

**T1-NZ-6 — Schedular payments: always gross up**
When income was subject to schedular withholding (the payer deducted tax), the gross income = amount received ÷ (1 − withholding rate). The withheld amount is a tax credit against the final liability. Always gross up before entering in the income section.

**T1-NZ-7 — Foreign currency income: use NZD at date of receipt**
Income received in foreign currencies must be converted to NZD at the exchange rate on the date of receipt (or annual average rate by agreement). Use Reserve Bank of NZ indicative rates. Do not convert at the year-end rate.

---

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

| Code | Situation | Escalation Reason | Suggested Treatment |
|---|---|---|---|
| T2-NZ-1 | Mixed company/personal income (trading company + sole trader) | Company income not reportable in IR3; only salary/dividends from company | Flag — clarify business structure |
| T2-NZ-2 | Rental property income | Separate schedule in IR3; different deductibility rules (interest deductibility limited post-Brightline reform) | Flag — ring-fence rental losses may apply |
| T2-NZ-3 | Brightline property sale | 10-year Brightline test: gains on residential property sold within 10 years are taxable | Flag — complex rules; confirm purchase and sale dates |
| T2-NZ-4 | Working for Families Tax Credits | IETC cannot be claimed alongside WFF; complex abatement on WFF | Flag — confirm eligibility before applying either IETC or WFF |
| T2-NZ-5 | Non-resident earning NZ-source income | Non-resident withholding tax (NRWT) applies; different rates | Flag — do not apply resident rates |
| T2-NZ-6 | Imputation credits on dividends | Dividends gross + imputation credits both reportable; imputation credit is a tax credit | Flag — require dividend statement from company |
| T2-NZ-7 | Losses in prior years (tax loss carry-forward) | NZ allows carrying forward business losses | Flag — prior-year losses reduce current taxable income if criteria met |

---

## Section 7 — Excel Working Paper Template

```
NEW ZEALAND INCOME TAX WORKING PAPER (IR3 — SELF-EMPLOYED)
Taxpayer: _______________  IRD Number: _______________  FY: 1 April 2024 – 31 March 2025

SECTION A — SELF-EMPLOYMENT INCOME (ex-GST)
                                        NZD
Gross self-employment receipts         ___________
Less: GST component (if incl.)         (___________)
Net ex-GST income                      ___________
Schedular income (grossed up)          ___________
Other business income                  ___________
TOTAL INCOME                           ___________

SECTION B — DEDUCTIBLE EXPENSES
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
Other business expenses                ___________
Payment processor fees                 ___________
TOTAL DEDUCTIBLE EXPENSES              ___________

SECTION C — NET TAXABLE INCOME
Total income − Total expenses          ___________

SECTION D — INCOME TAX
Tax at bracket rates (see table)       ___________
Less: IETC (if income NZD 24k–48k)    (___________)
NET INCOME TAX                         ___________

SECTION E — ACC EARNER LEVY
Net income × 1.33%                     ___________

SECTION F — RIT AND PROVISIONAL TAX
Income tax + ACC − withholding credits ___________
Less: provisional tax paid             (___________)
RIT BALANCE DUE / (REFUND)             ___________
Next year provisional (105% of RIT):   ___________

SECTION G — REVIEWER FLAGS
[ ] GST stripped from income/expenses (if GST-registered)?
[ ] Schedular payments grossed up and withholding credit recorded?
[ ] Motor vehicle logbook reviewed — business % substantiated?
[ ] Entertainment capped at 50%?
[ ] Home office — floor area proportion documented?
[ ] ACC work levy invoice included as expense?
[ ] Provisional tax instalments reconciled against IRD account?
[ ] Foreign income converted to NZD at receipt-date rate?
```

---

## Section 8 — Bank Statement Reading Guide

### ANZ New Zealand
- Export: CSV via ANZ Internet Banking ("Download transactions")
- Columns: `Date,Description,Debit,Credit,Balance`
- Date format: DD/MM/YYYY
- Amount format: no thousands separator, period decimal (e.g., `11500.00`)
- Credit = positive Credit column; Debit = positive Debit column

### BNZ (Bank of New Zealand)
- Export: CSV from BNZ Online Banking
- Columns: `Date,Tran Type,Particulars,Code,Reference,Amount,Balance`
- Positive Amount = credit; negative Amount = debit
- Particulars/Code/Reference: three-part narration on NZ bank transfers

### ASB Bank
- Export: CSV from ASB FastNet ("Export")
- Columns: `Date,Unique Id,Tran Type,Cheque Number,Payee,Memo,Amount`
- Positive Amount = credit; negative = debit
- Date: DD/MM/YYYY

### Westpac NZ
- Export: CSV from Westpac Online ("Download Statement")
- Columns: `Date,Narrative,Debit Amount,Credit Amount,Balance`
- Separate debit/credit columns (similar to AU banks)

### Kiwibank
- Export: CSV from Kiwibank Online ("Download")
- Columns: `Date,Description,Debit,Credit,Balance`
- Standard NZ format; date DD/MM/YYYY

### ASB / BNZ three-part narration (Particulars/Code/Reference)
NZ bank-to-bank transfers allow three fields the sender fills in:
- **Particulars:** Usually the payer's name or invoice reference
- **Code:** Account code or project reference
- **Reference:** Invoice number, date, or other identifier
Combine all three to identify transaction source.

---

## Section 9 — Onboarding Fallback

**GST registration unclear:**
> "To correctly prepare your IR3, I need to know whether you are GST-registered. If your gross annual income from self-employment exceeds NZD 60,000, GST registration is compulsory. If you are registered, your income and expenses are reported exclusive of GST. If you are unsure, check your IRD myIR account or GST registration certificate."

**Motor vehicle logbook missing:**
> "You've claimed vehicle expenses. To support a business use percentage above 25%, IRD requires a logbook maintained for at least 90 consecutive days showing each trip, distance, and business purpose. If you don't have a logbook, I'll apply the default 25% business use rate. Would you like to provide the logbook, or shall I proceed with 25%?"

**Provisional tax instalments:**
> "Do you have records of provisional tax payments made to IRD during the 2025 tax year? These would have been debited from your bank account as 'IRD Provisional Tax' on three dates: 28 August 2024, 15 January 2025, and 7 May 2025. I need these to calculate your final balance owing (or refund) and to determine next year's provisional tax obligation."

**Schedular payment withholding:**
> "I see payments that may have had tax withheld (schedular payments). Do you have withholding tax certificates from your clients, or a summary from IRD myIR? The gross income and the withheld amount will appear in your myIR account. I need the gross figures to correctly report your income."

---

## Section 10 — Reference Material

### Key Legislation
- **Income Tax Act 2007 (NZ)** — primary income tax legislation
- **Tax Administration Act 1994** — filing, penalties, provisional tax
- **Goods and Services Tax Act 1985** — GST (separate from income tax)

### Filing Deadlines (FY ended 31 March 2025)
| Deadline | Event |
|---|---|
| 7 July 2025 | IR3 due for self-filers (without tax agent) |
| 31 March 2026 | Extended deadline with registered tax agent |
| 7 February 2026 | Terminal tax due (for standard March balance date) |

### Useful Rates 2025
- Top bracket: 39% (income > NZD 180,000)
- GST rate: 15%
- Default schedular payment rate: 20%
- ACC earner levy ~1.33% (confirm current ACC schedule)
- Provisional tax: 105% of prior RIT (standard method)

### Useful References
- Inland Revenue: ird.govt.nz
- myIR (secure IRD portal): myir.ird.govt.nz
- Reserve Bank NZ FX rates: rbnz.govt.nz/statistics/exchange-rates
- ACC levy rates: acc.co.nz/for-business/self-employed
