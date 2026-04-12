---
name: sg-income-tax
description: Use this skill whenever asked about Singapore income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay in Singapore", "Form B", "Form B1", "IRAS income tax", "trade income", "capital allowances Singapore", "personal reliefs", "tax residence 183 days", "Section 10(1)(a)", "CPF self-employed", "self-employed tax Singapore", or any question about filing or computing income tax for a Singapore sole proprietor or freelancer. Covers progressive rates (0–24%), trade income computation, capital allowances (s19/s19A), approved deductions, personal reliefs, CPF MediShield Life, tax residence rules, filing deadlines, and penalties.
version: 2.0
---

# Singapore Income Tax — Self-Employed (Form B / B1)

## Section 1 — Quick Reference

### Income Tax Rate Table (YA 2025, residents)
| Chargeable Income (SGD) | Rate | Tax on band |
|---|---|---|
| First $20,000 | 0% | $0 |
| Next $10,000 ($20,001–$30,000) | 2% | $200 |
| Next $10,000 ($30,001–$40,000) | 3.5% | $350 |
| Next $40,000 ($40,001–$80,000) | 7% | $2,800 |
| Next $40,000 ($80,001–$120,000) | 11.5% | $4,600 |
| Next $40,000 ($120,001–$160,000) | 15% | $6,000 |
| Next $40,000 ($160,001–$200,000) | 18% | $7,200 |
| Next $40,000 ($200,001–$240,000) | 19% | $7,600 |
| Next $40,000 ($240,001–$280,000) | 19.5% | $7,800 |
| Next $40,000 ($280,001–$320,000) | 20% | $8,000 |
| Above $320,000 | 22% | — |

**Non-residents:** Flat 22% or withholding tax rates depending on income type (no personal reliefs).

**Formula:** Calculate tax on each bracket cumulatively. Subtract personal reliefs before applying brackets.

### Key Personal Reliefs (YA 2025)
| Relief | Amount |
|---|---|
| Earned Income Relief (below 55) | $1,000 |
| Earned Income Relief (55–59) | $6,000 |
| Earned Income Relief (60+) | $8,000 |
| NSman Relief (active) | $3,000; spouse $750; parent $750 |
| CPF Relief (self-employed on voluntary contributions) | Actual contributions, capped at CPF Annual Limit ($37,740) |
| CPF MediSave Relief | Actual contributions to MediSave, capped at Basic Healthcare Sum ceiling |
| Spouse/Handicapped Spouse Relief | $2,000 / $5,500 |
| Child Relief (each qualifying child) | $4,000 |
| Parent/Handicapped Parent Relief | $9,000 / $14,000 per dependent parent |
| Course Fees Relief | Up to $5,500 |
| Life Insurance Relief | Up to $5,000 |
| SRS Relief | Actual SRS contributions (capped at $15,300 for citizens/PRs) |
| Donations (approved IPC) | 2.5× amount donated |

**Reliefs cap:** Total personal reliefs capped at $80,000 per YA.

### Conservative Defaults
| Item | Default |
|---|---|
| Home office % | Do not assume — ask client for floor area ratio |
| Vehicle business % | Do not assume — S-plated private car: motor expenses disallowed for income tax |
| Phone/internet business % | 50% if dual-use; 100% if dedicated business line |
| S-plated private car | Motor expenses disallowed — IRA rule for private cars |
| Capital allowances election | s19 (3-year write-off) unless client confirms s19A 1-year |
| CPF MediSave | Self-employed must contribute to MediSave if net trade income > $6,000 |

### Red Flag Thresholds
| Situation | Flag |
|---|---|
| Gross turnover > $1M | GST registration mandatory — verify |
| Expenses > 70% of trade income | High ratio — verify documentation |
| Private car expenses claimed | Not deductible for income tax — remove |
| Entertainment > $10,000 | IRAS scrutinises — ensure business connection documented |
| Net trade income < $6,000 | MediSave contribution not required but check |

---

## Section 2 — Required Inputs & Refusal Catalogue

### Minimum Required Inputs
1. Total gross trade income for the year
2. Itemised business expenses with supporting receipts
3. Capital assets purchased (for capital allowance computation)
4. Personal reliefs applicable (spouse, children, parents, NSman, course fees)
5. CPF/MediSave contributions made during the year
6. Whether tax resident (physically present in Singapore ≥ 183 days in the year)
7. Whether any foreign-sourced income was remitted to Singapore

### Refusal Catalogue
**R-SG-1 — No expense documentation**
Refuse to claim expenses without records. State: "IRAS requires supporting documents for all expense claims. Without receipts or records we cannot include these in your trade income computation."

**R-SG-2 — Private car (S-plate) motor expenses**
Motor expenses (fuel, insurance, maintenance) for S-plated private cars are statutorily disallowed under the Income Tax Act. State: "Private car motor expenses are disallowed under Singapore income tax law. Only commercial vehicles (Q-plate vans, etc.) qualify."

**R-SG-3 — Capital receipt treated as income**
One-off disposal proceeds, insurance payouts for capital assets, or sale of investments are capital receipts — not trade income. Refuse to include in trade income computation.

**R-SG-4 — Foreign income not remitted**
Singapore taxes residents on foreign-sourced income only when it is remitted to Singapore (subject to exemptions for certain foreign income). If client earned foreign income that was not remitted, it is generally not taxable. Do not include it unless confirmed remitted.

**R-SG-5 — Penalties or fines**
Penalties, fines, and illegal payments are not deductible. Refuse to include.

**R-SG-6 — Non-tax-resident claiming personal reliefs**
Non-tax-residents (< 183 days) cannot claim personal reliefs. State: "Personal reliefs are only available to Singapore tax residents. Based on days present, you are a non-resident and cannot claim these reliefs."

---

## Section 3 — Transaction Pattern Library

### 3.1 Income Patterns
| Bank Description Pattern | Income Type | Tax Treatment | Notes |
|---|---|---|---|
| FAST transfer / PayNow from client | Trade income | Gross revenue — include | Verify it's client payment not personal |
| SWIFT / TT from overseas client | Trade income (foreign) | Include if remitted; use SGD rate on receipt date | |
| Stripe payout / STRIPE | Platform payout | Trade income (gross received) | Stripe fees → deductible expense |
| PayPal credit | Platform payout | Trade income (SGD equivalent) | Use PayPal statement rate |
| Upwork / Freelancer.com | Freelance platform | Trade income (gross; platform fees = expense) | |
| Grab / Deliveroo earnings | Gig platform | Trade income | Use platform earnings statement |
| Rental income from property | Rental income | Separate Schedule — not trade income | Enter on Form B under "Other income" |
| Dividend from Singapore company | Dividend | Exempt (one-tier tax system) | Do not include as trade income |
| Interest from bank | Interest | Exempt for individuals (Singapore bank interest) | Generally exempt |
| Insurance claim payout | Capital | EXCLUDE — not trade income | |
| Internal bank transfer | — | EXCLUDE | |

### 3.2 Expense Patterns
| Bank Description Pattern | Expense Category | Deductible? | Notes |
|---|---|---|---|
| Singtel / Starhub / M1 / TPG | Phone/internet | Partial — business % only | T2: confirm % |
| Singtel broadband / Starhub fibre | Internet | Partial — business % only | T2: home office ratio |
| SP Services / utility bill | Utilities | Home office % only | T2: floor area |
| HDB / private landlord — RENT | Rent | Home office % only | T2: floor area |
| AWS / Google Cloud / Azure | Cloud/SaaS | Yes — 100% | Document business use |
| Adobe / Slack / Zoom / Notion | SaaS tools | Yes — 100% | |
| Apple.com / App Store (dev tools) | Software | Yes — business tools | Exclude personal apps |
| Courts / Harvey Norman / Gain City | Equipment | Capital allowance (s19/s19A) if >$1,000 | Not immediate expense |
| Challenger / Lazada (office supplies) | Office supplies | Yes — <$1,000 | Immediate deduction |
| SIA / Scoot / Jetstar | Business travel | Yes — business purpose | Document trip purpose |
| SMRT / SBS Transit / ComfortDelGro | Local transport | Yes — business trips | Personal commute excluded |
| GrabCar / Gojek | Taxi/rideshare | Yes — business trips | Keep trip records |
| Hotel / Airbnb | Accommodation | Yes — business purpose | Document |
| Restaurant / food delivery (business meal) | Entertainment | Yes — must document business connection | Private entertaining excluded |
| Professional indemnity insurance | Insurance | Yes — business | |
| IRAS GST payment | GST paid | EXCLUDE — not income tax deductible | |
| IRAS income tax payment | Tax | EXCLUDE — not deductible | |
| CPF contribution | CPF | EXCLUDE from expenses — claim as CPF Relief instead | |
| DBS / OCBC / UOB bank charges | Bank charges | Yes — 100% | |
| Accounting / bookkeeping fees | Professional fees | Yes — 100% | |
| Coursera / Udemy / training | Course fees | Business-related: expense; personal development: Course Fees Relief separately | |

### 3.3 Capital Allowances (s19 / s19A)
| Asset Type | s19 (3-year) | s19A (1-year accelerated) | Notes |
|---|---|---|---|
| Computer / laptop | ¹⁄₃ p.a. | 100% in Year 1 | Must elect s19A |
| Office furniture | ¹⁄₃ p.a. | 100% if elected | |
| Plant & machinery | Based on NTA schedule | Can elect 1-year | |
| Motor vehicle (Q-plate commercial) | ¹⁄₃ p.a. | — | S-plate private car: disallowed |
| Renovation (s14Q) | 1/3 over 3 years | — | Cap: $300,000 per 3-year period |

**Low-value assets:** Items < $1,000 each (up to $30,000 total pool per YA) — full deduction in year of purchase under s19B.

### 3.4 Foreign Currency & Platform Income
| Source | Currency | Treatment |
|---|---|---|
| USD from US clients | USD | Convert to SGD at spot rate on receipt date |
| EUR from EU clients | EUR | Convert to SGD at spot rate on receipt date |
| Stripe USD payouts | USD | Use Stripe statement SGD equivalent or convert using Mas.gov.sg exchange rates |
| PayPal multi-currency | Various | Use PayPal statement conversion |
| Google AdSense | USD | Monthly — convert to SGD |
| Apple / Google Play | USD | Monthly — convert to SGD |

### 3.5 Internal Transfers
| Pattern | Treatment |
|---|---|
| Transfer between own DBS/OCBC/UOB accounts | EXCLUDE |
| Savings to current account | EXCLUDE |
| Credit card bill payment (auto-debit) | EXCLUDE — expenses captured individually |
| Loan proceeds received | EXCLUDE — not income |

---

## Section 4 — Worked Examples

### Example 1 — DBS Bank: Freelance Consultant, Single, Resident
**Scenario:** IT consultant, SGD $180,000 gross revenue, $45,000 expenses, CPF MediSave $6,840

**Bank statement extract (DBS Bank):**
```
Date       | Description                              | Withdrawals | Deposits    | Balance
15/04/2025 | FAST CR TECHCORP ASIA PTE LTD           |             | 28,000.00   | 84,500.00
20/04/2025 | PayNow CR STARTUP SG                    |             |  8,500.00   | 93,000.00
25/04/2025 | AWS EMEA SARL                            |   1,240.00  |             | 91,760.00
28/04/2025 | SINGTEL MOBILE                           |     120.00  |             | 91,640.00
30/04/2025 | DBS BANK CHARGES                         |      10.00  |             | 91,630.00
```

**Trade Income Computation:**
| Line | Amount |
|---|---|
| Gross trade income | $180,000 |
| Less: allowable expenses | ($45,000) |
| Net trade income | $135,000 |
| Less: CPF MediSave Relief | ($6,840) |
| Less: Earned Income Relief (below 55) | ($1,000) |
| **Chargeable income** | **$127,160** |
| Tax on first $120,000 | $7,950 |
| Tax on next $7,160 @ 15% | $1,074 |
| **Total income tax** | **$9,024** |

### Example 2 — OCBC Bank: Designer, Married with Child
**Scenario:** Graphic designer, $80,000 gross, $18,000 expenses, married (spouse no income), 1 child (age 4)

**Bank statement extract (OCBC Bank):**
```
Value Date | Description                               | Debit       | Credit      | Balance
10/03/2025 | PayNow Cr BRIGHT DESIGN STUDIO            |             | 12,000.00   | 34,500.00
15/03/2025 | FAST Cr OVERSEAS REMIT USD TT             |             |  6,450.00   | 40,950.00
20/03/2025 | ADOBE SYSTEMS INC                         |     79.00   |             | 40,871.00
22/03/2025 | OCBC GIRO STARHUB MOBILE                  |    110.00   |             | 40,761.00
28/03/2025 | SCOOT SQ AIRLINES                         |    880.00   |             | 39,881.00
```

**Trade Income Computation:**
| Line | Amount |
|---|---|
| Gross trade income | $80,000 |
| Less: allowable expenses | ($18,000) |
| Net trade income | $62,000 |
| Less: Earned Income Relief | ($1,000) |
| Less: Spouse Relief | ($2,000) |
| Less: Child Relief | ($4,000) |
| Less: CPF MediSave Relief | ($5,760) |
| **Chargeable income** | **$49,240** |
| Tax on first $40,000 | $550 |
| Tax on next $9,240 @ 7% | $647 |
| **Total income tax** | **$1,197** |

### Example 3 — UOB Bank: Developer with SRS Contribution
**Scenario:** Software developer, $240,000 gross, $60,000 expenses, SRS $15,300, iPhones and laptops (capital allowances)

**Bank statement extract (UOB Bank):**
```
Txn Date   | Description                              | Withdrawal  | Deposit     | Balance
05/05/2025 | INCOMING TT USD 45000 COMPANY XYZ        |             | 60,750.00   | 195,000.00
10/05/2025 | PAYPAL TRANSFER                          |             |  8,200.00   | 203,200.00
15/05/2025 | MICROSOFT IRELAND                        |  1,288.00   |             | 201,912.00
20/05/2025 | UOB VISA BILL                            | 12,500.00   |             | 189,412.00
25/05/2025 | SRS CONTRIBUTION OCBC SRS               | 15,300.00   |             | 174,112.00
```

**Capital Allowances:**
- MacBook Pro $3,500: s19A elected → $3,500 deducted Year 1
- Monitor $800: s19B low-value → $800 immediate deduction

**Trade Income Computation:**
| Line | Amount |
|---|---|
| Gross trade income | $240,000 |
| Less: revenue expenses | ($60,000) |
| Less: capital allowances (s19A MacBook + s19B monitor) | ($4,300) |
| Net trade income | $175,700 |
| Less: CPF MediSave Relief | ($6,840) |
| Less: SRS Relief | ($15,300) |
| Less: Earned Income Relief | ($1,000) |
| **Chargeable income** | **$152,560** |
| Tax on first $120,000 | $7,950 |
| Tax on next $32,560 @ 15% | $4,884 |
| **Total income tax** | **$12,834** |

### Example 4 — Citibank Singapore: Photographer with Home Office
**Scenario:** Photographer, $55,000 gross, $12,000 direct expenses, home office (50 sqm apartment, 8 sqm studio)

**Bank statement extract (Citibank Singapore):**
```
Posted     | Description                              | Amount (SGD)
12/06/2025 | CREDIT FAST PMT ZING MEDIA PTE LTD      | +9,000.00
18/06/2025 | CREDIT PAYPAL XFER                      | +3,200.00
22/06/2025 | DEBIT LAZADA ONLINE SHOP                | -380.00
25/06/2025 | DEBIT SP SERVICES PTE LTD               | -185.00
28/06/2025 | DEBIT CITIBANK GIRO STARHUB             | -98.00
```

**Home Office Computation:**
- Floor area: 8/50 = 16%
- Annual rent $24,000 × 16% = $3,840 deductible
- Utilities $2,220 × 16% = $355 deductible

**Trade Income Computation:**
| Line | Amount |
|---|---|
| Gross trade income | $55,000 |
| Direct expenses | ($12,000) |
| Home office — rent portion | ($3,840) |
| Home office — utilities portion | ($355) |
| Net trade income | $38,805 |
| Less: Earned Income Relief | ($1,000) |
| Less: CPF MediSave Relief | ($3,456) |
| **Chargeable income** | **$34,349** |
| Tax on first $30,000 | $550 |
| Tax on next $4,349 @ 3.5% | $152 |
| **Total income tax** | **$702** |

### Example 5 — Standard Chartered Singapore: Trainer with Course Fees
**Scenario:** Corporate trainer, $95,000 gross, $22,000 expenses, attended $3,200 professional training course

**Bank statement extract (Standard Chartered):**
```
Date       | Reference                                | Debits      | Credits     | Balance
08/07/2025 | INCOMING SGD TFRSUPERCORP               |             | 18,000.00   | 67,200.00
12/07/2025 | FAST PAYMENT INNOVA TRAINING             |             |  5,500.00   | 72,700.00
18/07/2025 | POS NTUC FAIRPRICE (SUPPLIES)            |    145.00   |             | 72,555.00
22/07/2025 | BILL PMT SINGTEL ENTERPRISE              |    280.00   |             | 72,275.00
25/07/2025 | COURSERA INC                             |    320.00   |             | 71,955.00
```

**Note on course fees:** $3,200 professional course — claim as Course Fees Relief (up to $5,500) rather than business expense if the course maintains professional skills (both give same deduction but Relief is simpler).

**Trade Income Computation:**
| Line | Amount |
|---|---|
| Gross trade income | $95,000 |
| Less: expenses | ($22,000) |
| Net trade income | $73,000 |
| Less: Earned Income Relief | ($1,000) |
| Less: Course Fees Relief | ($3,200) |
| Less: CPF MediSave Relief | ($6,840) |
| **Chargeable income** | **$61,960** |
| Tax on first $40,000 | $550 |
| Tax on next $21,960 @ 7% | $1,537 |
| **Total income tax** | **$2,087** |

### Example 6 — Maybank Singapore: Creative Agency Sole Proprietor
**Scenario:** Sole proprietor (creative agency), $320,000 gross, $140,000 expenses, employs spouse (spouse CPF contributions)

**Bank statement extract (Maybank Singapore):**
```
Transaction Date | Narration                             | Debit       | Credit      | Balance
03/08/2025      | IBG CREDIT BRANDCO ASIA PTE LTD       |             | 45,000.00   | 210,500.00
08/08/2025      | IBG CREDIT GLOBALINK PTE LTD          |             | 28,000.00   | 238,500.00
15/08/2025      | IBG DEBIT GOOGLE SINGAPORE            |   8,500.00  |             | 230,000.00
20/08/2025      | IBG DEBIT META PLATFORMS INC          |   6,200.00  |             | 223,800.00
25/08/2025      | MAYBANK GIRO PAYROLL SPOUSE           |   5,000.00  |             | 218,800.00
```

**Spouse salary note:** Spouse salary of $5,000/month = $60,000/year. Deductible as employee cost if spouse is genuinely employed and CPF contributions made. Spouse files separate income tax return.

**Trade Income Computation:**
| Line | Amount |
|---|---|
| Gross trade income | $320,000 |
| Less: direct expenses (excl. spouse salary) | ($80,000) |
| Less: spouse salary | ($60,000) |
| Net trade income | $180,000 |
| Less: CPF MediSave Relief | ($6,840) |
| Less: Earned Income Relief | ($1,000) |
| **Chargeable income** | **$172,160** |
| Tax on first $160,000 | $21,550 |
| Tax on next $12,160 @ 18% | $2,189 |
| **Total income tax** | **$23,739** |

---

## Section 5 — Tier 1 Rules (Compressed Reference)

### Tax Residence
- **Resident:** Physically present in Singapore ≥ 183 days in the calendar year, OR tax authority determines Singapore is intended permanent home
- **Non-resident:** < 183 days — flat 22% on trade income, no personal reliefs
- **60-day rule:** Short-term visitors exercising employment < 60 days: employment income exempt. Does not apply to self-employment.

### Trade Income vs Other Income
| Income Type | IRAS Category |
|---|---|
| Freelance / self-employment | Trade income — Section 10(1)(a) |
| Rental from property | Property income — Section 10(1)(f) |
| Bank interest (resident) | Generally exempt |
| Dividends (Singapore companies) | Exempt (one-tier) |
| Foreign dividends (remitted) | Taxable if remitted to Singapore |
| Employment income | Separate employment schedule |

### GST
- Mandatory GST registration: taxable turnover > $1M in last 12 months or expected > $1M in next 12 months
- Voluntary registration possible below threshold
- GST collected ≠ income — separate obligation

### CPF for Self-Employed
- **Compulsory:** MediSave contributions mandatory if net trade income > $6,000/year
- MediSave contribution rate: varies by age (approx. 8%–10.5% of net trade income, capped)
- **Voluntary:** CPF Ordinary/Special Account contributions — eligible for CPF Relief up to $37,740/year

### Capital Allowances
| Rule | Threshold | Deduction |
|---|---|---|
| s19B (low-value) | Each asset < $1,000; total ≤ $30,000 | 100% Year 1 |
| s19A (1-year write-off) | Any qualifying plant — election required | 100% Year 1 |
| s19 (3-year write-off) | Default for qualifying plant | 1/3 per year |
| s14Q (renovation) | Office renovation | 1/3 per year over 3 years, cap $300K |

### Filing Deadlines
| Event | Deadline |
|---|---|
| Form B / B1 (paper) | April 15 |
| Form B / B1 (e-filing) | April 18 |
| Estimated Chargeable Income (companies) | 3 months after FY end |
| Tax payment (NOA issued) | Within 1 month of Notice of Assessment |

### Penalties
| Situation | Penalty |
|---|---|
| Late filing | $200 (first offence) + composition amount |
| Late payment | 5% of unpaid tax + 1% per month (max 12%) |
| Failure to file | Estimated Assessment + penalty |

---

## Section 6 — Tier 2 Catalogue

### T2-SG-1: Home Office (Residential Property)
**Why T2:** Floor area split is a fact only the client knows; IRAS accepts apportionment by floor area.

**Method:** Business floor area ÷ total floor area × rent/utilities/internet
**Required from client:** Total floor area (sqm or sq ft), dedicated office area, confirmation of exclusive/primary business use.
**Caution:** HDB owner-occupiers technically require HDB approval for home office use — flag this to client.

### T2-SG-2: Phone & Internet Split
**Why T2:** Personal/business mix is client-specific.

**Guidance:**
- Dedicated business mobile: 100% deductible
- Dual-use mobile: 50% default unless client documents higher business use
- Home broadband (also home office): proportion by floor area or 50% default

### T2-SG-3: Vehicle — Commercial vs Private
**Why T2:** Vehicle type determines deductibility — only client can confirm.

- **S-plate private car:** Motor expenses **not deductible** — statutory disallowance. No exception.
- **Q-plate commercial vehicle (van, lorry):** Motor expenses deductible — business proportion
- **Car rental (business trip only):** Deductible for specific business trips with documentation

**Required from client:** Vehicle registration plate category; purpose of vehicle use.

### T2-SG-4: Entertainment Expenses
**Why T2:** Business connection and attendee details must come from client.

**Rules:**
- Must be for business purpose (clients, customers, business contacts)
- Private social entertaining: not deductible
- Document: who attended, business purpose, amount

**IRAS standard:** Expenses must be "wholly and exclusively" incurred for business production of income.

### T2-SG-5: Mixed Donations
**Why T2:** Only donations to approved IPCs qualify for 2.5× deduction.

**Required from client:** Name of charity, confirm IPC status (check Charity Portal), amount donated and receipt number.

---

## Section 7 — Excel Working Paper

### Sheet 1: Trade Income Summary
| Column | Content |
|---|---|
| A | Transaction date |
| B | Bank account |
| C | Payer / description |
| D | SGD amount received |
| E | Category (Trade income / Other / Exclude) |
| F | Notes |

**Total trade income:** `=SUMIF(E:E,"Trade income",D:D)`

### Sheet 2: Expense Ledger
| Column | Content |
|---|---|
| A | Date |
| B | Vendor |
| C | Amount (SGD) |
| D | Expense category |
| E | Business % |
| F | Deductible amount (=C×E) |
| G | Revenue expense or capital (for CA) |
| H | Receipt reference |

**Total expenses:** `=SUMIF(G:G,"Revenue",F:F)`

### Sheet 3: Capital Allowances
| Column | Content |
|---|---|
| A | Asset description |
| B | Purchase date |
| C | Cost (SGD) |
| D | s19 or s19A or s19B |
| E | YA2025 allowance |
| F | Tax written-down value (if s19) |

### Sheet 4: Reliefs & Tax Computation
| Line | Amount |
|---|---|
| Net trade income (Sheet 1 − Sheet 2 − Sheet 3) | |
| Earned Income Relief | |
| CPF MediSave Relief | |
| Spouse Relief | |
| Child Relief | |
| SRS Relief | |
| Course Fees Relief | |
| Donations (2.5×) | |
| Total reliefs (cap $80,000) | |
| **Chargeable income** | |
| Tax per bracket table | |
| Less: tax rebates (if any) | |
| **Net income tax payable** | |

---

## Section 8 — Bank Statement Reading Guide

### DBS Bank (Development Bank of Singapore)
- Format: `Date | Description | Withdrawals | Deposits | Balance`
- Date: DD/MM/YYYY
- Income = Deposits column
- Key identifiers: "FAST CR", "PayNow Cr", "INCOMING TT", "IBG CREDIT"

### OCBC Bank
- Format: `Value Date | Description | Debit | Credit | Balance`
- Date: DD/MM/YYYY
- Income = Credit column
- "FAST Cr", "GIRO CR", "IBG INWARD"

### UOB Bank (United Overseas Bank)
- Format: `Txn Date | Description | Withdrawal | Deposit | Balance`
- Date: DD/MM/YYYY
- Income = Deposit column
- "INCOMING TT", "FAST", "PAYPAL TRANSFER"

### Citibank Singapore
- Format: `Posted | Description | Amount (SGD)` — single amount column; positive = credit, negative = debit
- Date: DD/MM/YYYY
- Income: positive amounts with "CREDIT" in description

### Standard Chartered Singapore
- Format: `Date | Reference | Debits | Credits | Balance`
- Date: DD/MM/YYYY
- Income = Credits column

### Maybank Singapore
- Format: `Transaction Date | Narration | Debit | Credit | Balance`
- Date: DD/MM/YYYY
- "IBG CREDIT" = incoming bank transfer; "IBG DEBIT" = outgoing

### Exclusion Patterns (all banks)
| Pattern | Action |
|---|---|
| Transfer to own account | EXCLUDE |
| Credit card payment / GIRO to card | EXCLUDE — captured as individual expenses |
| SRS contribution (debit) | EXCLUDE from expenses — handled as Relief |
| CPF GIRO (debit) | EXCLUDE from expenses — handled as CPF Relief |
| GST payment to IRAS | EXCLUDE — not income tax expense |
| IRAS income tax payment | EXCLUDE |

---

## Section 9 — Onboarding Fallback

**Priority 1 (blocking):**
1. "What was your total gross trade income for YA2025 (year ended 31 Dec 2024)?"
2. "Are you tax resident in Singapore — were you physically present ≥ 183 days in 2024?"
3. "Please provide bank statements and receipts for business expenses."

**Priority 2 (reliefs and deductions):**
4. "Are you married? What was your spouse's income in 2024?"
5. "Do you have children? Ages?"
6. "Did you make CPF voluntary contributions or iCPF? What amount?"
7. "Did you contribute to SRS in 2024? How much?"
8. "Did you make any donations to approved charities? Do you have receipts?"

**Priority 3 (assets and capital):**
9. "Did you purchase any equipment or computers for business use this year costing more than $1,000?"
10. "Do you work from home? What is your apartment floor area and how much is dedicated to work?"

**Conservative approach if data gaps:**
- Exclude undocumented expenses
- Use s19 (3-year) for capital allowances unless s19A election confirmed
- Default phone/internet to 50% business unless confirmed otherwise

---

## Section 10 — Reference Material

### Key IRAS Forms
| Form | Purpose |
|---|---|
| Form B | Self-employed income tax return |
| Form B1 | Simplified Form B (if no business expenses to claim) |
| CP8A / IR8A | Employment income (if also employed) |
| Form C-S / C | Corporate tax (if incorporated — not this skill) |

### Filing Platform
- **myTax Portal:** mytax.iras.gov.sg — SingPass login required
- Paper filing: April 15 deadline; e-filing: April 18 deadline
- IRAS auto-computation (AIS): employment income pre-filled; trade income must be self-entered

### Key IRAS Publications
- IRAS e-Tax Guide: "Business Expenses Deductible Under Section 14"
- IRAS e-Tax Guide: "Capital Allowances"
- IRAS MediSave contribution rates table (updated annually)

### MediSave Contribution Rates (self-employed, YA 2025)
| Age | Contribution Rate |
|---|---|
| Below 35 | 8.0% |
| 35–44 | 9.0% |
| 45–49 | 9.5% |
| 50–54 | 10.0% |
| 55–59 | 10.5% |
| 60–64 | 10.5% |
| 65 and above | 10.5% |
Maximum net trade income subject to contribution: approx. $102,000 (confirm with CPF Board annually).

---

## Prohibitions
- Do not advise on GST registration, filing, or calculation — separate Singapore GST skill required
- Do not advise on corporate income tax (Form C-S/C) — this skill covers sole proprietors and freelancers only
- Do not advise on stamp duty, property tax, or estate duty
- Do not advise on equity or stock option taxation without confirming specific scheme rules
- Do not guarantee IRAS acceptance of any deduction or relief position — IRAS may audit and adjust

## Disclaimer
This skill provides general guidance for informational and planning purposes. It does not constitute tax advice. Singapore tax law is administered by the Inland Revenue Authority of Singapore (IRAS). Clients should consult a registered tax agent or CPA (Singapore) for advice specific to their circumstances. Tax law and relief amounts change annually — verify current rates at iras.gov.sg.
