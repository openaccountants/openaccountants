---
name: nz-income-tax-ir3
description: >
  Use this skill whenever asked about New Zealand income tax for self-employed individuals filing an IR3 return. Trigger on phrases like "how much tax do I pay in NZ", "IR3", "income tax return New Zealand", "allowable deductions NZ", "provisional tax NZ", "schedular payments", "independent earner tax credit", "ACC levies", "Working for Families", "residual income tax", "self-employed tax NZ", or any question about filing or computing income tax for a self-employed individual in New Zealand. Covers NZ tax brackets (10.5%–39%), IR3 return structure, allowable deductions, ACC levies, provisional tax (3 instalments), IETC, schedular payments, GST interaction, and penalties.
version: 2.0
---

# New Zealand Income Tax — Self-Employed (IR3 Return)

## Section 1 — Quick Reference

### Income Tax Brackets (2025–26 tax year, 1 April – 31 March)
| Taxable income (NZD) | Rate |
|---|---|
| 0 – $14,000 | 10.5% |
| $14,001 – $48,000 | 17.5% |
| $48,001 – $70,000 | 30% |
| $70,001 – $180,000 | 33% |
| Above $180,000 | 39% |

**Formula:** Tax is calculated cumulatively on each band. No standard personal allowance — use Independent Earner Tax Credit (IETC) instead.

### ACC Earner Levy
- **Rate (2025–26):** $1.60 per $100 of liable earnings (1.60%)
- **Liable earnings cap:** $142,283 per year
- Maximum levy: $2,277
- Collected with income tax via IR3 or PAYE

### Key Tax Credits
| Credit | Amount |
|---|---|
| Independent Earner Tax Credit (IETC) | Up to $520/year — phases out $48K–$70K (full self-employment income) |
| Donation tax credit | 33.33% of donations to approved donee organisations |
| Working for Families (WFF) | Depends on family income, children — administered by Inland Revenue |
| Paid parental leave | Not a tax credit — separate entitlement |

**IETC:** Available if no student loan repayments, no WFF, income $24K–$70K. Full $520 at $24K–$48K; tapers to $0 at $70K.

### Provisional Tax Thresholds
| Residual income tax (RIT) | Provisional tax obligation |
|---|---|
| RIT ≤ $5,000 | No provisional tax (standard taxpayer) |
| RIT > $5,000 | Provisional tax payer — 3 instalments |

**RIT = Total income tax for the year − tax already deducted at source (PAYE, RWT, etc.)**

### Conservative Defaults
| Item | Default |
|---|---|
| Home office % | Do not assume — ask for floor area or hours |
| Vehicle business % | Do not assume — ask for logbook |
| Phone/internet | 50% if mixed use |
| GST registration | Assumed not registered unless confirmed (threshold NZD $60,000) |
| Provisional tax method | Standard (105% of prior year RIT) unless client confirms estimation |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Revenue > $60,000 (12 months) | GST registration mandatory — verify |
| RIT > $5,000 | Provisional tax required |
| Revenue > $180,000 | 39% marginal rate bracket |
| Expenses > 70% of revenue | High ratio — verify documentation |
| No ACC levy provision | Will be charged on IR3 — plan for this |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross self-employment income (business revenue) for the tax year (1 April – 31 March)
2. Deductible business expenses with documentation
3. Whether GST-registered (if yes: revenue should be GST-exclusive)
4. Any tax already paid: schedular payments, RWT, PAYE from part-time employment
5. Personal situation: other income, partner income (if WFF claim), dependant children
6. Prior year residual income tax (for provisional tax calculation)

### Refusal Catalogue
**R-NZ-1 — No expense documentation**
Refuse undocumented deductions. State: "Inland Revenue requires documentation for all business expense deductions. Without receipts or records, we cannot include these in your IR3."

**R-NZ-2 — GST included in income**
If GST-registered: revenue must exclude GST. State: "Your gross income on IR3 must exclude GST. Remove GST from all revenue figures before computing your taxable income."

**R-NZ-3 — Personal expenses claimed as business**
Refuse private costs. State: "These are private expenses and cannot be deducted. Only expenses incurred wholly or partly for business purposes are deductible under the Income Tax Act 2007."

**R-NZ-4 — Schedular payment income treated as business income**
Schedular payments (paid by clients under contract for service): withholding tax already deducted. Must include gross amount in income and claim withholding as a credit. Do not net off.

**R-NZ-5 — Non-resident claiming resident credits**
Non-residents cannot claim IETC or WFF. State: "IETC and WFF credits are only available to New Zealand tax residents."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| CR / deposit from client | Business income | Include gross (excl. GST if registered) | |
| Online transfer from client | Business income | Include | |
| International wire / SWIFT | Foreign client | Include — convert to NZD at transaction date | |
| Stripe deposit / STRIPE | Platform income | Include net; add Stripe fees as expense | |
| PayPal transfer | Platform income | NZD equivalent | |
| Upwork / Fiverr | Freelance platform | Gross earnings; platform fee = expense | |
| ACC Work Safe NZ credit | ACC levy refund / compensation | Check nature — refund of levy = not income; compensation may be | |
| Bank interest | Interest income | Include — subject to resident withholding tax (RWT) at 17.5%–39% | Enter on IR3 interest schedule |
| Rental income | Rental | May be separate schedule (IR3/IR3R) | Not business income if passive |
| Schedular payment (net) | Contract service | Gross up: net ÷ (1 − withholding rate) | Withholding = tax credit |
| Personal transfer / family gift | — | EXCLUDE — not income | |

### 3.2 Expense Patterns (Deductible Business Expenses)
| Bank Description Pattern | Expense Category | Deductible? | Notes |
|---|---|---|---|
| Spark / One NZ (Vodafone) / 2degrees | Phone | Partial — business % | T2: confirm % |
| Spark / One NZ broadband | Internet | Business % | T2: home office ratio |
| Mercury / Genesis / Contact Energy | Electricity | Home office % | T2: floor area |
| Landlord / rent | Rent | Home office % only if working from home | T2 |
| AWS / Google Cloud / Azure | Cloud/SaaS | 100% | Business use |
| Adobe / Figma / Slack / Notion | Software | 100% | |
| Countdown / Pak'nSave (office supplies) | Office supplies | Yes — office-specific items | Personal groceries: excluded |
| Air NZ / Jetstar / flights | Business travel | 100% — purpose documented | |
| NZRail / InterCity / bus | Travel | 100% — business trips | |
| Hotel / motel / Airbnb (business) | Accommodation | 100% — business purpose | |
| Restaurant (business meal) | Entertainment | 50% of entertainment expenses | Document business purpose |
| Professional development / course | Training | 100% — business-related | |
| Accounting / bookkeeping | Professional fees | 100% | |
| Public liability insurance | Insurance | 100% | |
| Domain / hosting / website | IT/marketing | 100% | |
| IRD income tax payment | Tax | EXCLUDE — not deductible | |
| GST payment to IRD | GST | EXCLUDE — if GST-registered, separate | |
| ACC levy payment | ACC | Yes — deductible as business expense | ACC non-earner levy = personal; earner levy = deductible |
| Bank charges / merchant fees | Bank | 100% | |
| Loan interest (business loan) | Interest | Yes — if loan for business purposes | Personal mortgage: not deductible |

### 3.3 Schedular Payments (Withholding Tax)
| Activity | Standard Withholding Rate | Notes |
|---|---|---|
| Contract work (most services) | 20% (standard) | Client deducts; claim as credit on IR3 |
| Labour hire | 20% | |
| Commission (sales agent) | 20% | |
| Payments to non-residents | Variable (15%–30%) | Depends on DTA |

**Gross up formula:** If net received NZD 8,000 at 20% withholding → gross = NZD 8,000 ÷ 0.80 = NZD 10,000. Declare NZD 10,000 as income; claim NZD 2,000 as credit.

### 3.4 Foreign Currency
| Source | Currency | Treatment |
|---|---|---|
| USD from US clients | USD | Convert to NZD at Reserve Bank of NZ TTM rate on receipt date |
| AUD from Australian clients | AUD | Convert at receipt date |
| GBP / EUR | Various | Convert at receipt date |
| Stripe USD | USD | Use Stripe statement NZD equivalent |
| PayPal multi-currency | Various | PayPal statement NZD equivalent |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| Transfer to personal savings | EXCLUDE |
| Owner's drawing | EXCLUDE — not expense (just withdrawal of own money) |
| Credit card payment | EXCLUDE — individual expenses captured |
| Loan repayment received | EXCLUDE — not income |
| Personal transfer in | EXCLUDE — not revenue |

---

## Section 4 — Worked Examples

### Example 1 — ANZ Bank: IT Consultant, Standard Taxpayer
**Scenario:** IT consultant, NZD $95,000 gross income, $22,000 expenses, no prior provisional tax, GST-registered

**Bank statement extract (ANZ Business):**
```
Date         | Details                                    | Debit (NZD)   | Credit (NZD)  | Balance
15/04/2025   | Credit - TechCorp NZ Ltd                  |               | 17,250.00     | 84,500.00
20/04/2025   | Credit - StartupNZ                        |               |  8,050.00     | 92,550.00
25/04/2025   | Debit - Adobe Inc                         | 75.00         |               | 92,475.00
28/04/2025   | Debit - Spark NZ Limited                  | 120.00        |               | 92,355.00
30/04/2025   | Debit - ANZ Fees                          | 12.00         |               | 92,343.00
```

**GST note:** Credits above are GST-inclusive. GST-exclusive income: $95,000 (as stated). Credits include GST which goes to separate GST return.

**Tax Computation:**
| Line | Amount |
|---|---|
| Gross business income (GST excl.) | $95,000 |
| Deductible expenses | ($22,000) |
| **Net taxable income** | **$73,000** |
| Tax: 10.5%×$14K + 17.5%×$34K + 30%×$22K + 33%×$3K | $1,470 + $5,950 + $6,600 + $990 = **$15,010** |
| ACC earner levy: $73,000 × 1.60% | $1,168 |
| IETC | $0 (income > $70,000) |
| **Total tax + ACC** | **$16,178** |
| Prior tax deducted | $0 |
| **RIT = $16,178 > $5,000 → provisional tax required next year** | |

### Example 2 — BNZ Bank: Designer, With IETC
**Scenario:** Freelance designer, $42,000 gross income, $9,000 expenses, not GST-registered

**Bank statement extract (BNZ Business):**
```
Date         | Transaction details                        | Debit (NZD)   | Credit (NZD)  | Balance (NZD)
10/03/2025   | TRSF CR DESIGN STUDIO NZ                  |               | 6,500.00      | 28,400.00
15/03/2025   | TRSF CR CREATIVE AGENCY                   |               | 3,800.00      | 32,200.00
20/03/2025   | POS OFFICEWORKS STATIONERY                | 145.00        |               | 32,055.00
22/03/2025   | DIRECT DEBIT ADOBE CREATIVE               | 79.00         |               | 31,976.00
28/03/2025   | BNZ ACCOUNT FEE                           | 10.00         |               | 31,966.00
```

**Tax Computation:**
| Line | Amount |
|---|---|
| Gross income | $42,000 |
| Expenses | ($9,000) |
| **Net taxable income** | **$33,000** |
| Tax: 10.5%×$14K + 17.5%×$19K | $1,470 + $3,325 = **$4,795** |
| ACC earner levy: $33,000 × 1.60% | $528 |
| IETC (income $24K–$48K, full $520) | ($520) |
| **Total tax** | **$4,803** |
| RIT = $4,803 < $5,000 → no provisional tax | |

### Example 3 — Westpac NZ: Developer, Schedular Payments
**Scenario:** Developer, $80,000 income (all schedular, 20% withheld by clients = $16,000 deducted), $15,000 expenses

**Bank statement extract (Westpac Business):**
```
Date         | Description                                | Withdrawals   | Deposits      | Balance
05/05/2025   | Electronic Credit TECHSTARTUP NZ          |               | 16,000.00     | 54,000.00
12/05/2025   | Electronic Credit SOFTCO LTD              |               |  8,000.00     | 62,000.00
18/05/2025   | Autopay GITHUB                            | 200.00        |               | 61,800.00
22/05/2025   | Eftpos NOEL LEEMING MONITOR               | 890.00        |               | 60,910.00
28/05/2025   | Monthly Account Fee Westpac               | 10.00         |               | 60,900.00
```

**Note:** $16,000 deposit = $20,000 gross − 20% withholding $4,000. Gross up: $16,000 ÷ 0.80 = $20,000.

**Tax Computation:**
| Line | Amount |
|---|---|
| Gross income (schedular — grossed up) | $80,000 |
| Expenses | ($15,000) |
| **Net taxable income** | **$65,000** |
| Tax: 10.5%×$14K + 17.5%×$34K + 30%×$17K | $1,470 + $5,950 + $5,100 = **$12,520** |
| ACC levy | $1,040 |
| IETC (income $48K–$70K range, partially phased) | ~$220 |
| Less: schedular tax credits | ($16,000) |
| **Tax refund** | **~$2,220** |

### Example 4 — ASB Bank: Photographer with Home Office
**Scenario:** Photographer, $55,000 gross income, home office (house 130m², office 15m²)

**Bank statement extract (ASB Business):**
```
Date         | Particulars                                | Amount (NZD)  | Balance (NZD)
08/06/2025   | Internet Transfer BRIGHT MEDIA NZ         | +12,000.00    | 46,500.00
12/06/2025   | Internet Transfer AUCKLAND EVENTS         | +5,500.00     | 52,000.00
15/06/2025   | Bill Pay GENESIS ENERGY                   | -280.00       | 51,720.00
20/06/2025   | Card Purchase CAMERA HOUSE NZ             | -650.00       | 51,070.00
25/06/2025   | ASB Business Service Fee                  | -10.00        | 51,060.00
```

**Home office calculation:**
- % business: 15/130 = 11.5%
- Annual rent $24,000 × 11.5% = $2,760
- Electricity $3,360 × 11.5% = $386
- Internet $780 × 11.5% = $90

**Tax Computation:**
| Line | Amount |
|---|---|
| Gross income | $55,000 |
| Direct expenses | ($8,000) |
| Home office (rent + power + internet) | ($3,236) |
| **Net taxable income** | **$43,764** |
| Tax: 10.5%×$14K + 17.5%×$29,764 | $1,470 + $5,209 = **$6,679** |
| ACC levy: $43,764 × 1.60% | $700 |
| IETC (phased: $43,764 < $48K — eligible for partial) | ($520) |
| **Total tax** | **$6,859** |

### Example 5 — Kiwibank: Writer with Donation Credit
**Scenario:** Freelance writer, $38,000 gross income, $6,500 expenses, donated $1,000 to approved charity

**Bank statement extract (Kiwibank):**
```
Date         | Description                                | Payments      | Receipts      | Balance
12/07/2025   | Credit PUBLISHER NZ LTD                   |               | 5,500.00      | 22,000.00
18/07/2025   | Credit MAGAZINE GROUP NZ                  |               | 3,000.00      | 25,000.00
22/07/2025   | Debit HOSPICE NZ DONATION                 | 1,000.00      |               | 24,000.00
26/07/2025   | Debit WHITCOULLS BOOKS                    | 145.00        |               | 23,855.00
30/07/2025   | Kiwibank Monthly Fee                      | 10.00         |               | 23,845.00
```

**Note on donation:** Hospice NZ is an approved donee. Donation tax credit = 33.33% × $1,000 = **$333**.

**Tax Computation:**
| Line | Amount |
|---|---|
| Gross income | $38,000 |
| Expenses | ($6,500) |
| **Net taxable income** | **$31,500** |
| Tax: 10.5%×$14K + 17.5%×$17,500 | $1,470 + $3,063 = **$4,533** |
| ACC levy | $504 |
| Donation credit | ($333) |
| IETC (income $31,500 — eligible) | ($520) |
| **Total tax** | **$4,184** |

### Example 6 — TSB Bank: Consultant, Provisional Tax Calculation
**Scenario:** Consultant, $120,000 gross income, $30,000 expenses, prior year RIT $9,200 (provisional tax payer)

**Bank statement extract (TSB):**
```
Date         | Narration                                  | Dr (NZD)      | Cr (NZD)      | Bal (NZD)
03/08/2025   | Credit CORPORATECLIENT A                  |               | 25,000.00     | 195,000.00
10/08/2025   | Credit CORPORATECLIENT B                  |               | 18,000.00     | 213,000.00
15/08/2025   | Debit IRD Provisional Tax                 | 3,220.00      |               | 209,780.00
20/08/2025   | Debit XERO ACCOUNTING                     | 78.00         |               | 209,702.00
25/08/2025   | TSB Transaction Fee                       | 8.00          |               | 209,694.00
```

**Tax Computation:**
| Line | Amount |
|---|---|
| Gross income | $120,000 |
| Expenses | ($30,000) |
| **Net taxable income** | **$90,000** |
| Tax: 10.5%×$14K + 17.5%×$34K + 30%×$22K + 33%×$20K | $1,470 + $5,950 + $6,600 + $6,600 = **$20,620** |
| ACC levy (capped at $142,283 liable): $90,000 × 1.60% | $1,440 |
| **Total** | **$22,060** |

**Provisional tax for next year (standard method):**
- Prior year RIT: $9,200 (this year's RIT expected ~$22,060)
- Next year instalments: $22,060 × 105% ÷ 3 = **$7,721 per instalment** (or use ratio method)
- Instalment dates: 28 August, 15 January, 7 May

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Tax Residency
- **NZ tax resident:** Present in NZ > 183 days in any 12-month period OR has permanent place of abode in NZ → worldwide income taxable
- **Non-resident:** NZ-source income only; different withholding rates; cannot claim IETC/WFF

### IR3 Income Types
| Income Type | IR3 Schedule |
|---|---|
| Self-employment income | Business income schedule |
| Schedular (contract) income | Schedular payments schedule |
| Rental income | Rental income schedule |
| Interest (bank) | Interest schedule (RWT) |
| Dividends | Dividend schedule |
| PIE income | Separate — Portfolio Investment Entity |

### GST Interaction
- If GST-registered: all income figures on IR3 must be GST-exclusive
- GST threshold: taxable supplies > $60,000/12 months → mandatory registration
- Common error: including GST in IR3 income — overstates taxable income significantly

### Depreciation (Inland Revenue Depreciation Rates)
- Assets < $1,000: write off immediately (low-value asset threshold)
- Assets ≥ $1,000: depreciate using IR published rates
- Computers: 40% DV (diminishing value) / 30% SL (straight-line)
- Motor vehicles: 21–30% DV
- Office furniture: 10–20% DV

### ACC Earner Levy
- 1.60% on liable earnings (up to $142,283 cap)
- Included on income tax assessment
- Invoiced separately for self-employed who don't pay PAYE
- Deductible as business expense on IR3

### Provisional Tax Methods
| Method | How it works | Best for |
|---|---|---|
| Standard | 105% of prior year RIT ÷ 3 instalments | Stable income |
| Estimation | Estimate current year liability; pay accordingly | Income varies |
| Ratio (AIM) | Pay each period based on accounting income | Use accounting software |

**Instalment dates (standard year: 31 March):**
- 28 August (1st)
- 15 January (2nd)
- 7 May (3rd = same as terminal tax)

### Filing Deadlines
| Event | Deadline |
|---|---|
| IR3 (tax agent client) | 31 March following year + extension |
| IR3 (self-filing) | 7 July following year |
| Terminal tax (final payment) | 7 April (or 7 February if > $60K) |
| Provisional tax 1st | 28 August |
| Provisional tax 2nd | 15 January |
| Provisional tax 3rd | 7 May |

### Penalties
| Situation | Penalty |
|---|---|
| Late filing | $50 (first offence); $250 + thereafter |
| Late payment | 1% on day 1 + 4% at day 7 + 1%/month ongoing |
| Shortfall penalty (not taking reasonable care) | 20%–40% of shortfall |
| Evasion | 150% of shortfall |

---

## Section 6 — Tier 2 Catalogue

### T2-NZ-1: Home Office
**Why T2:** Floor area split and exclusive/mixed use are facts only the client knows.

**Two methods:**
1. **Floor area method:** Business m² ÷ total m² × rent/rates/power/internet
2. **Time-based method:** Hours used for business ÷ total hours in day × relevant costs (for single-person home)

**Required from client:** Total floor area (m²), office area (m²), or hours per day used for business.
**Caution:** Must be a dedicated working space — not the kitchen table used occasionally.

### T2-NZ-2: Motor Vehicle
**Why T2:** Business-use proportion depends on actual trips — only the client knows.

**Methods:**
1. **Logbook (3-month representative period):** Establish business % → apply for year. Logbook must be renewed every 3 years.
2. **50% rule:** If actual business use likely > 50% and no logbook → can claim 25% flat (conservative); logbook preferred.
3. **Business-only vehicle:** Claim 100% — must be commercially-plated or demonstrably non-private.

**Required from client:** Total km driven, business km (from logbook or estimate), vehicle make/model/year (for depreciation).

### T2-NZ-3: Phone & Internet
**Why T2:** Personal/business mix is client-specific.

**Guidance:** Dedicated business phone: 100%. Dual-use: typically 50–75% for knowledge workers. Home broadband: proportion = home office %.

### T2-NZ-4: Entertainment — 50% Rule
**Why T2:** Entertainment expenses subject to 50% limit — only deductible when business purpose is established and client knows who attended.

**Rule:** Entertainment expenses (meals, functions, etc.) with a business connection: 50% deductible.
Exceptions: 100% deductible if the entertainment happens away from home on a business trip.

### T2-NZ-5: Provisional Tax Method Selection
**Why T2:** Choice depends on client's income volatility and accounting software — client must decide.

**Guidance:** Use estimation if income is dropping significantly vs prior year (saves interest cost). Use standard if income is stable or growing. AIM (accounting income method) works well with Xero/MYOB integrated IR.

---

## Section 7 — Excel Working Paper

### Sheet 1: Business Income
| Column | Content |
|---|---|
| A | Date |
| B | Client |
| C | Invoice/description |
| D | Gross amount (NZD, GST excl.) |
| E | GST amount (if registered) |
| F | Net received |
| G | Category (Business income / Schedular / Other / Exclude) |
| H | Withholding tax deducted (if schedular) |

**Total business income:** `=SUMIF(G:G,"Business income",D:D)`
**Schedular gross-up:** `=F/(1-0.20)` where 0.20 = withholding rate

### Sheet 2: Expense Ledger
| Column | Content |
|---|---|
| A | Date |
| B | Vendor |
| C | Amount (NZD, GST excl.) |
| D | Category |
| E | Business % |
| F | Deductible amount (=C×E) |
| G | Receipt reference |

### Sheet 3: Tax Computation
| Line | Amount |
|---|---|
| Gross business income | |
| Plus: schedular income (gross) | |
| Less: expenses | |
| Less: depreciation | |
| **Net taxable income** | |
| Income tax (bracket table) | |
| ACC earner levy (×1.60%) | |
| IETC (if applicable) | |
| Donation tax credit | |
| **Gross tax payable** | |
| Less: schedular withholding credits | |
| Less: RWT credits (bank interest) | |
| Less: provisional tax paid | |
| **Terminal tax / Refund** | |

---

## Section 8 — Bank Statement Reading Guide

### ANZ Bank (Business)
- Format: `Date | Details | Debit (NZD) | Credit (NZD) | Balance`
- Date: DD/MM/YYYY
- Income = Credit column
- Key: "Credit" = payment received; "Debit" = expense paid

### BNZ (Bank of New Zealand)
- Format: `Date | Transaction details | Debit (NZD) | Credit (NZD) | Balance (NZD)`
- Date: DD/MM/YYYY
- "TRSF CR" = transfer credit (incoming)

### Westpac NZ
- Format: `Date | Description | Withdrawals | Deposits | Balance`
- Date: DD/MM/YYYY
- Income = Deposits column; "Electronic Credit" = incoming wire

### ASB Bank
- Format: `Date | Particulars | Amount (NZD) | Balance (NZD)` — single column; positive = credit
- Date: DD/MM/YYYY
- "Internet Transfer" = incoming payment; "Bill Pay" = outgoing

### Kiwibank
- Format: `Date | Description | Payments | Receipts | Balance`
- Date: DD/MM/YYYY
- Income = Receipts column

### TSB
- Format: `Date | Narration | Dr (NZD) | Cr (NZD) | Bal (NZD)`
- Date: DD/MM/YYYY
- Income = Cr column

### Exclusion Patterns (all NZ banks)
| Pattern | Action |
|---|---|
| Transfer to savings / term deposit | EXCLUDE — personal |
| Credit card payment | EXCLUDE — individual expenses captured |
| Loan proceeds credit | EXCLUDE — not income |
| IRD provisional / terminal tax payment | EXCLUDE from expenses — captured as tax credit |
| Owner's drawing | EXCLUDE — withdrawal |
| GST refund from IRD | EXCLUDE — GST return item |

---

## Section 9 — Onboarding Fallback

**Priority 1 (blocking):**
1. "What was your total gross business income for the tax year (April 1 – March 31)?"
2. "Are you GST-registered? If yes, please confirm all income figures are GST-exclusive."
3. "Do you have receipts and records for your business expenses?"

**Priority 2 (for accurate calculation):**
4. "Did any clients deduct schedular payments (withholding tax) from payments to you?"
5. "Did you pay any provisional tax during the year? Dates and amounts?"
6. "Do you work from home? If yes: total floor area and dedicated office area?"
7. "Do you use a personal vehicle for business? Approximate business km per year?"

**Priority 3 (credits and additional income):**
8. "Do you have any bank interest, dividends, or rental income to declare?"
9. "Did you make any donations to charities? Which ones and amounts?"
10. "Do you have any dependant children? (Working for Families eligibility check)"

**Conservative defaults:**
- Exclude home office if floor area not confirmed
- Exclude vehicle if no logbook — or apply conservative 25% if clearly some business use
- Default phone/internet to 50%
- Do not assume GST-exclusive figures without confirmation

---

## Section 10 — Reference Material

### Key IR Forms
| Form | Purpose |
|---|---|
| IR3 | Individual tax return (self-employed) |
| IR3B | Business income schedule |
| IR3R | Rental income schedule |
| IR4 | Company income tax return (not this skill) |
| IR10 | Financial statements summary |
| IR307 | Schedular payment certificate (from payer) |
| IR526 | Donation tax credit claim |

### Filing Platform
- **myIR:** Inland Revenue's online portal (ird.govt.nz)
- **Tax agents:** Most NZ accountants file via tax agency software (Practice Bridge, MYOB)
- Standard tax year: 1 April – 31 March

### Key References
- Inland Revenue (IRD): ird.govt.nz
- ACC: acc.co.nz
- Inland Revenue depreciation rates: ird.govt.nz/depreciation
- GST registration: ird.govt.nz/gst

---

## Prohibitions
- Do not advise on GST (goods and services tax) registration, filing, or calculation — separate NZ GST skill required
- Do not advise on company (IR4) or trust (IR6) income tax — this skill covers IR3 individual returns only
- Do not advise on FBT (fringe benefit tax) for employers
- Do not advise on KiwiSaver beyond noting it exists — KiwiSaver employer obligations are separate
- Do not guarantee IRD acceptance of deduction positions — every situation may be reviewed

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. New Zealand tax law is administered by Inland Revenue (Te Tari Taake). Clients should consult a Chartered Accountant (CA) or tax agent registered with the Tax Agents' Licensing Board for advice specific to their circumstances. Tax rates, thresholds, and depreciation rates change annually — verify current rules at ird.govt.nz.
