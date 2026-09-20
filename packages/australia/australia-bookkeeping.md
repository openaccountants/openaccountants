---
name: australia-bookkeeping
description: Use this skill whenever asked about Australian bookkeeping for sole traders, partnerships, or small companies. Trigger on phrases like "chart of accounts", "BAS", "GST codes", "bookkeeping", "profit and loss", "balance sheet", "AASB", "simplified disclosures", "Tier 2", "bank reconciliation", "expense categories", "revenue recognition", "depreciation", "instant asset write-off", "small business pool", "ABN", "ATO reporting", "activity statement", "accrual basis", "cash basis", "general ledger", "how do I classify this transaction", "what evidence do I need", "capital or revenue", "private use apportionment", "fix a bookkeeping error", "accounting versus tax treatment", or any question about day-to-day transaction recording, financial statement preparation, or account coding for an Australian business.
version: 1.2
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-17
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia Bookkeeping

## Australia Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD ($) only |
| Financial year | 1 July – 30 June (standard); substituted accounting period available for companies |
| Accounting standards | AASB (full IFRS-based); AASB 1060 Simplified Disclosures (Tier 2); Special Purpose for non-reporting entities |
| Governing body | Australian Accounting Standards Board (AASB) |
| Tax authority | Australian Taxation Office (ATO) |
| Key legislation | Corporations Act 2001 (financial reporting Ch.2M); Income Tax Assessment Act 1936/1997; A New Tax System (GST) Act 1999 |
| GST registration threshold | $75,000 turnover ($150,000 for non-profits) |
| Small business entity threshold | Aggregated turnover < $10 million |
| BAS lodgement | Quarterly (most small businesses) or monthly ($20m+ turnover) |

## Section 2 -- Standard Chart of Accounts

Australian software (Xero, MYOB, QuickBooks) typically uses 3–4 digit codes. The structure below follows common Australian practice.

### Assets (1000–1999)

**Assets (1000–1999)**

| Code | Account | Type |
| --- | --- | --- |
| 1000 | Cash on Hand / Petty Cash | Current asset |
| 1010 | Business Bank Account | Current asset |
| 1020 | Savings Account | Current asset |
| 1030 | Term Deposits (< 12 months) | Current asset |
| 1050 | Undeposited Funds | Current asset |
| 1100 | Accounts Receivable (Trade Debtors) | Current asset |
| 1110 | Other Debtors | Current asset |
| 1120 | Prepayments | Current asset |
| 1150 | GST Receivable (Input Tax Credits) | Current asset |
| 1200 | Inventory / Stock on Hand | Current asset |
| 1300 | Land | Non-current asset |
| 1310 | Buildings | Non-current asset |
| 1311 | Accumulated Depreciation — Buildings | Contra asset |
| 1320 | Plant and Equipment | Non-current asset |
| 1321 | Accumulated Depreciation — Plant & Equipment | Contra asset |
| 1330 | Motor Vehicles | Non-current asset |
| 1331 | Accumulated Depreciation — Motor Vehicles | Contra asset |
| 1340 | Office Equipment | Non-current asset |
| 1341 | Accumulated Depreciation — Office Equipment | Contra asset |
| 1350 | Computer Equipment | Non-current asset |
| 1351 | Accumulated Depreciation — Computer Equipment | Contra asset |
| 1360 | Furniture and Fittings | Non-current asset |
| 1361 | Accumulated Depreciation — Furniture & Fittings | Contra asset |
| 1400 | Small Business Pool | Non-current asset |

### Liabilities (2000–2999)

**Liabilities (2000–2999)**

| Code | Account | Type |
| --- | --- | --- |
| 2000 | Accounts Payable (Trade Creditors) | Current liability |
| 2010 | Other Creditors | Current liability |
| 2020 | Accrued Expenses | Current liability |
| 2050 | GST Payable (Collected) | Current liability |
| 2060 | GST Clearing / Control | Current liability |
| 2100 | PAYG Withholding Payable | Current liability |
| 2110 | Superannuation Payable | Current liability |
| 2120 | Provision for Annual Leave | Current liability |
| 2130 | Provision for Long Service Leave | Current liability |
| 2140 | Provision for Income Tax | Current liability |
| 2200 | Credit Card | Current liability |
| 2300 | Short-Term Loan (< 12 months) | Current liability |
| 2400 | Long-Term Loan (> 12 months) | Non-current liability |
| 2410 | Hire Purchase Liability | Non-current liability |
| 2500 | Director's Loan Account | Non-current liability |

### Equity (3000–3999)

**Equity (3000–3999)**

| Code | Account | Type |
| --- | --- | --- |
| 3000 | Share Capital / Owner's Equity | Equity |
| 3010 | Owner's Drawings | Equity |
| 3020 | Owner's Contributions | Equity |
| 3100 | Retained Earnings | Equity |
| 3200 | Current Year Profit/Loss | Equity |
| 3300 | Reserves | Equity |

### Revenue (4000–4999)

**Revenue (4000–4999)**

| Code | Account | Type |
| --- | --- | --- |
| 4000 | Sales Revenue — Taxable (GST 10%) | Revenue |
| 4010 | Sales Revenue — GST-Free | Revenue |
| 4020 | Sales Revenue — Input Taxed | Revenue |
| 4030 | Sales Revenue — Export (GST-Free) | Revenue |
| 4100 | Service Revenue | Revenue |
| 4200 | Interest Income | Revenue |
| 4300 | Rental Income | Revenue |
| 4400 | Government Grants / Subsidies | Revenue |
| 4500 | Other Income | Revenue |
| 4900 | Discount Allowed | Contra revenue |

### Cost of Goods Sold (5000–5999)

**Cost of Goods Sold (5000–5999)**

| Code | Account | Type |
| --- | --- | --- |
| 5000 | Purchases — Trading Stock | COGS |
| 5010 | Purchases — Materials / Components | COGS |
| 5020 | Freight Inward | COGS |
| 5030 | Direct Labour | COGS |
| 5040 | Subcontractor Costs | COGS |
| 5100 | Opening Stock Adjustment | COGS |
| 5110 | Closing Stock Adjustment | COGS |
| 5200 | Import Duty and Customs | COGS |

### Operating Expenses (6000–6999)

**Operating Expenses (6000–6999)**

| Code | Account | Type |
| --- | --- | --- |
| 6000 | Rent — Business Premises | Expense |
| 6010 | Rates and Body Corporate | Expense |
| 6020 | Electricity and Gas | Expense |
| 6030 | Water | Expense |
| 6040 | Insurance — Business | Expense |
| 6050 | Repairs and Maintenance | Expense |
| 6100 | Wages and Salaries | Expense |
| 6110 | Superannuation Guarantee (12% from Jul 2025) | Expense |
| 6120 | Workers' Compensation Insurance | Expense |
| 6130 | Payroll Tax (state-based) | Expense |
| 6140 | Staff Training | Expense |
| 6200 | Advertising and Marketing | Expense |
| 6210 | Website and Hosting | Expense |
| 6220 | Printing and Stationery | Expense |
| 6230 | Postage and Delivery | Expense |
| 6300 | Motor Vehicle — Fuel | Expense |
| 6310 | Motor Vehicle — Registration and Insurance | Expense |
| 6320 | Motor Vehicle — Repairs | Expense |
| 6330 | Travel — Domestic | Expense |
| 6340 | Travel — International | Expense |
| 6350 | Meals and Entertainment (review FBT election and deductibility) | Expense |
| 6400 | Accounting and Tax Agent Fees | Expense |
| 6410 | Legal Fees | Expense |
| 6420 | Bank Charges | Expense |
| 6430 | Merchant / Payment Processing Fees | Expense |
| 6440 | Interest Expense | Expense |
| 6500 | Telephone and Internet | Expense |
| 6510 | Software Subscriptions (SaaS) | Expense |
| 6520 | Professional Subscriptions and Memberships | Expense |
| 6600 | Depreciation — Buildings | Expense |
| 6610 | Depreciation — Plant and Equipment | Expense |
| 6620 | Depreciation — Motor Vehicles | Expense |
| 6630 | Depreciation — Office/Computer Equipment | Expense |
| 6700 | Bad Debts Written Off | Expense |
| 6800 | General and Sundry Expenses | Expense |

### Other Income / Expenses (7000–7999)

**Other Income / Expenses (7000–7999)**

| Code | Account | Type |
| --- | --- | --- |
| 7000 | Gain on Sale of Assets | Other income |
| 7010 | Loss on Sale of Assets | Other expense |
| 7020 | Foreign Exchange Gain/Loss | Other income/expense |
| 7100 | Extraordinary Items | Other expense |

### Tax (8000–8999)

**Tax (8000–8999)**

| Code | Account | Type |
| --- | --- | --- |
| 8000 | Income Tax Expense | Tax |
| 8010 | Deferred Tax Liability | Tax |
| 8020 | Deferred Tax Asset | Tax |

## Section 3 -- Revenue Recognition

### Cash vs Accrual Rules

**Cash vs Accrual Rules**  _(TR 98/1; s 328-285; ITAA 1936 ss 82KZL and 82KZM)_

| Criterion | Cash Basis (Sole Traders / Small Business) | Accruals Basis |
| --- | --- | --- |
| Eligibility | For income tax, use the method that correctly reflects income under TR 98/1; small-business status alone does not establish a receipts basis | Apply the appropriate income-tax method and separate financial-reporting requirements |
| Income recognised | When cash received | When earned (invoice raised or goods delivered) |
| Expenses recognised | When cash paid | When incurred (liability arises) |
| Trading stock | Eligible small business entities can use s 328-285 where the reasonably estimated stock-value change is $5,000 or less | Otherwise apply the required stock adjustments; this is separate from GST cash accounting |
| Prepaid expenses | Test the 12-month rule and other exceptions under ITAA 1936 ss 82KZL and 82KZM | Apply the relevant tax apportionment and financial-reporting rules separately |

### AASB 15 Revenue from Contracts with Customers

Applies to reporting entities using Tier 1/Tier 2. Five-step model:
1. Identify contract
2. Identify performance obligations
3. Determine transaction price
4. Allocate price to obligations
5. Recognise when obligation satisfied

Small businesses using simplified reporting typically recognise on delivery/completion.

## Section 4 -- Expense Classification

### ATO Individual Tax Return Categories (Sole Trader — Business Schedule)

**ATO Individual Tax Return Categories (Sole Trader — Business Schedule)**

| Item | Category | Nominal Codes |
| --- | --- | --- |
| A | All other business income | 4000–4500 |
| B | Cost of sales | 5000–5200 |
| C | Contractors and commission | 5040 |
| D | Superannuation | 6110 |
| E | Bad debts | 6700 |
| F | Lease expense (plant/equipment) | 6000 |
| G | Interest expense — Australia | 6440 |
| H | Depreciation (excluding SB pool) | 6600–6630 |
| I | Motor vehicle expenses | 6300–6320 |
| J | Repairs and maintenance | 6050 |
| K | All other expenses | 6000–6800 (remainder) |

### Non-Deductible Expenses (ATO)

- Entertainment (not subject to FBT election) — non-deductible portion
- Capital expenditure — must be depreciated or written off via SB pool
- Private portion of mixed expenses — must be apportioned
- Fines and penalties — not deductible
- Clothing (non-compulsory, non-protective) — not deductible
- Traffic infringements — not deductible

### GST Classification for BAS

**GST Classification for BAS**

| GST Code | Description | BAS Label |
| --- | --- | --- |
| GST (10%) | Standard taxable supply | G1, 1A |
| GST-Free | Food (basic), medical, education, exports | G1 (no 1A) |
| Input Taxed | Financial supplies, residential rent | G1 (no credit) |
| BAS Excluded | Wages, drawings, loan principal, private | Not reported |
| No ABN Withholding | Payments to suppliers without ABN (47% w/h) | Separate |

## Section 5 -- Asset vs Expense Thresholds

### Instant Asset Write-Off (IAWO)

**Instant Asset Write-Off (IAWO)**  _(Tax Reform No. 2 Act 2026, schedules 1–2 (https://www.legislation.gov.au/C2026A00071/asmade/text))_

| Period | Threshold | Eligibility |
| --- | --- | --- |
| 1 Jul 2023 – 30 Jun 2026 | < $20,000 per asset | Aggregated turnover < $10m, using simplified depreciation |
| From 1 Jul 2026 application date | Less than $20,000 per eligible asset | Enacted 26 August 2026; schedule 2 commences 1 October 2026. [Tax Reform No. 2 Act 2026, schedules 1–2](https://www.legislation.gov.au/C2026A00071/asmade/text) |

### Small Business Pool (Simplified Depreciation)

**Small Business Pool (Simplified Depreciation)**

| Pool | Rate | Notes |
| --- | --- | --- |
| Year 1 (first use) | 15% | On cost (or adjustable value if added later) |
| Subsequent years | 30% | On opening pool balance |
| Pool balance < IAWO threshold | Write off entire pool | End-of-year check |

### General (Non-SB) Depreciation

**General (Non-SB) Depreciation**

| Method | Application |
| --- | --- |
| Diminishing value | rate = days held ÷ 365 × (200% ÷ effective life) |
| Prime cost (straight-line) | rate = days held ÷ 365 × (100% ÷ effective life) |

### Common effective lives (2025 determination, asset-specific)

**Common effective lives (2025 determination, asset-specific)**  _(Income Tax Assessment (Effective Life of Depreciating Assets) Determination 2025, Table B (https://www.legislation.gov.au/F2025L01097/asmade/text). Choose the determination applicable under s 40-95; the 2025 instrument commenced on 16 September 2025.)_

| Asset | Effective Life | DV Rate | PC Rate |
| --- | --- | --- | --- |
| Desktop computers | 4 years | 50% | 25% |
| Laptops | 2 years | 100% | 50% |
| Printers/Scanners | 5 years | 40% | 20% |
| Office chairs | 10 years | 20% | 10% |
| Office desks | 20 years | 10% | 5% |
| Motor vehicles | 8 years | 25% | 12.5% |
| Air conditioning | 10 years | 20% | 10% |
| Eligible building capital works | Division 43, subject to use and construction dates | No generic diminishing-value deduction | Commonly 2.5%; verify eligibility and applicable statutory rate |

### Car Limit

- **Car cost limit for depreciation** — For 2025-26, the limit is AUD 69,674. For 2026-27, it is AUD 69,883. Only the business-use portion of the applicable limit can be depreciated. AUD  _(Car cost limit for depreciation)_ AUD

## Section 6 -- P&L Format

### Income Statement (AASB Simplified / Tier 2)

```
STATEMENT OF PROFIT OR LOSS
For the year ended 30 June 20XX
                                            $           $
Revenue                                               xxx
Cost of sales                                        (xxx)
                                                     ────
Gross profit                                          xxx

Other income                                          xxx

Expenses:
  Employee benefits expense               (xxx)
  Depreciation and amortisation           (xxx)
  Finance costs                           (xxx)
  Other expenses                          (xxx)
                                                     (xxx)
                                                     ────
Profit before income tax                              xxx
Income tax expense                                   (xxx)
                                                     ────
Profit for the year                                   xxx
                                                     ════
```

### Sole Trader — ATO Business Schedule Format

```
BUSINESS INCOME
  Gross payments subject to withholding       xxx
  All other business income                   xxx
  TOTAL BUSINESS INCOME                       xxx

BUSINESS EXPENSES
  Cost of sales                              (xxx)
  Contractor/subcontractor/commission        (xxx)
  Superannuation expenses                    (xxx)
  Bad debts                                  (xxx)
  Lease expenses within Australia            (xxx)
  Interest expenses within Australia         (xxx)
  Depreciation expenses                      (xxx)
  Motor vehicle expenses                     (xxx)
  Repairs and maintenance                    (xxx)
  All other expenses                         (xxx)
  TOTAL BUSINESS EXPENSES                    (xxx)

NET INCOME OR LOSS FROM BUSINESS              xxx
```

## Section 7 -- Balance Sheet Format

### Statement of Financial Position (Vertical — AASB Tier 2)

```
STATEMENT OF FINANCIAL POSITION
As at 30 June 20XX
                                            $           $
CURRENT ASSETS
  Cash and cash equivalents                           xxx
  Trade and other receivables                         xxx
  Inventories                                         xxx
  Other current assets                                xxx
                                                     ────
Total current assets                                  xxx

NON-CURRENT ASSETS
  Property, plant and equipment                       xxx
  Intangible assets                                   xxx
  Other non-current assets                            xxx
                                                     ────
Total non-current assets                              xxx
                                                     ────
TOTAL ASSETS                                          xxx
                                                     ════

CURRENT LIABILITIES
  Trade and other payables                            xxx
  Current tax liabilities                             xxx
  Provisions (annual leave, etc.)                     xxx
  Short-term borrowings                               xxx
                                                     ────
Total current liabilities                             xxx

NON-CURRENT LIABILITIES
  Long-term borrowings                                xxx
  Provisions (long service leave)                     xxx
                                                     ────
Total non-current liabilities                         xxx
                                                     ────
TOTAL LIABILITIES                                     xxx
                                                     ════

NET ASSETS                                            xxx
                                                     ════

EQUITY
  Issued capital                                      xxx
  Retained earnings                                   xxx
  Reserves                                            xxx
                                                     ────
TOTAL EQUITY                                          xxx
                                                     ════
```

## Section 8 -- Bank Reconciliation Patterns

### Common Australian Bank Formats

**Common Australian Bank Formats**

| Bank | Export Format | Key Fields |
| --- | --- | --- |
| Commonwealth Bank (CBA) | CSV, OFX, QIF | Date, Amount, Description, Balance |
| ANZ | CSV, OFX | Date, Description, Amount, Type |
| Westpac | CSV, OFX, QIF | Date, Narration, Debit, Credit, Balance |
| NAB | CSV, OFX | Date, Narration, Amount, Type, Balance |
| Macquarie | CSV | Date, Description, Amount, Balance |
| Bendigo Bank | CSV, OFX | Date, Description, Debit, Credit, Balance |
| Up Bank / Neobanks | CSV | Date, Description, Amount, Category |

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| DIRECT CREDIT, BPAY CREDIT | Income — customer payment |
| EFTPOS, VISA PURCHASE, DEBIT CARD | Expense — check merchant |
| DIRECT DEBIT, D/D | Regular expense (insurance, subscription, utility) |
| BPAY | Expense — bill payment (utilities, ATO, rates) |
| TRANSFER, INT TFR | Internal transfer or payment — check counterparty |
| ATM WITHDRAWAL | Drawings (sole trader) or petty cash replenishment |
| INTEREST CHARGED | Interest expense (6440) |
| INTEREST PAID | Interest income (4200) |
| ATO PAYMENT, ATO IAS, ATO BAS | Tax payment — not a P&L expense |
| PAYROLL, WAGES | Staff costs (6100) |
| SUPER STREAM, SUPER CLEARING | Superannuation (6110) |
| XERO, STRIPE, SQUARE PAYOUT | Platform payout — match to invoices |

## Section 9 -- Micro-Entity / Small Business Simplifications

### Small Business Entity Concessions (turnover < $10m)

**Small Business Entity Concessions (turnover < $10m)**

| Concession | Detail |
| --- | --- |
| Simplified depreciation | Instant write-off < $20,000; pool balance at 15%/30% |
| Simplified trading stock | No stock-take if estimate change ≤ $5,000 |
| Prepaid expenses | Test the 12-month rule and other exceptions under ITAA 1936 ss 82KZL and 82KZM |
| Simpler BAS | Report only G1, 1A, 1B (no G2, G3, G10, G11) |
| Two-year amendment period | ATO can only amend assessments within 2 years (not 4) |
| Cash accounting for GST | Report GST when paid/received, not invoiced |
| PAYG instalments | Option to pay quarterly amount the ATO calculates |

### Reporting Tiers

**Reporting Tiers**

| Tier | Who | Standards | Required Statements |
| --- | --- | --- | --- |
| Tier 1 (Full AASB / IFRS) | Entities with public accountability or another Tier 1 requirement | Full recognition and disclosure | Determine requirements under AASB 1053; size alone does not force Tier 1 |
| Tier 2 (AASB 1060 Simplified) | Non-publicly accountable entities electing Tier 2 | Full recognition, reduced disclosure | All 5 statements + reduced notes |
| Special purpose | Assess the entity and reporting obligation | The AASB 2020-2 changes apply from periods beginning on or after 1 July 2021 to specified for-profit entities | Use australia-financial-statements-2 and current AASB/ASIC requirements |
| No statutory reporting | Sole traders, small partnerships (non-company) | None mandated | Prepare for ATO/tax purposes only |

### Large Proprietary Thresholds (must be reporting entity)

- **Large Proprietary Thresholds** — Meet 2 of 3: Revenue ≥ $50m, assets ≥ $25m, employees ≥ 100.  _(Large Proprietary Thresholds)_

## Section 10 -- Interaction with Tax Skills

### Income Tax Return

- Sole traders: business schedule in individual return (myTax or tax agent)
- Companies: Company Tax Return (form with labels mapped to financial statements)
- Tax rate: individuals at marginal rates; companies at 25% (base rate entity, turnover < $50m) or 30%
- Franking: company tax paid generates franking credits for shareholder dividends
- Losses: carried forward indefinitely, subject to continuity of ownership test (companies) or non-commercial loss rules (individuals)

### BAS / GST Return

**BAS / GST Return**

| BAS Label | Description | CoA Mapping |
| --- | --- | --- |
| G1 | Total sales (incl. GST-free and input taxed) | 4000–4500 |
| 1A | GST on sales | 2050 |
| 1B | GST on purchases (Input Tax Credits) | 1150 |
| W1 | Total salary/wages and other payments | 6100 |
| W2 | Amounts withheld from payments (PAYG-W) | 2100 |
| T1 | PAYG instalment income | 4000–4500 |
| T2 | PAYG instalment raised | 2140 |

### Superannuation Guarantee

- Rate: 12% from 1 July 2025; 11.5% applied in 2024–25. Use the earnings definition, contribution base and deadline for the pay date. From July 2026 use the payday regime in au-super-guarantee; earlier periods retain the quarterly regime. [ATO super guarantee rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee).
- Due for 2025–26: quarterly deadlines. Use the separately cited payday rules for earnings paid from 1 July 2026.
- Nominal: 6110 (expense) / 2110 (payable)
- SG Charge for quarters before 1 July 2026: non-deductible. Apply the separate redesigned rules to later earnings.

### Fringe Benefits Tax (FBT)

- FBT year: 1 April – 31 March
- Rate: 47% (top marginal + Medicare levy)
- Common items: car fringe benefit, entertainment, loan fringe benefit
- Meals/entertainment: establish whether an available 50/50 valuation election was made and its scope before applying it. Otherwise use the applicable actual-benefit and deduction rules. Do not default every meal to a 50% deduction. [ATO FBT entertainment](https://www.ato.gov.au/law/view/document?docid=SAV/FBTGEMP/00001).

## Section 11 -- Classification, Evidence and Corrections

### 11.1 The classification decision

Every transaction needs four decisions, not one. Answer them in this order, because a later
answer can change an earlier one.

1. **Is it a business transaction at all?** Owner drawings, private spending on a business card
   and internal transfers between the entity's own accounts are not income or expenses. Code them
   to equity or to the relevant balance sheet account.
2. **Revenue or capital?** A cost that acquires, upgrades or extends the life of an asset is
   capital. A cost that restores it to its prior condition is a repair. See Section 5 for the
   thresholds and `au-rental-property.md` for the repairs and improvements tests.
3. **Which account?** Use the chart of accounts in Section 2. Consistency between periods matters
   more than finding a perfect label; a category that changes each year destroys comparatives.
4. **Which GST code?** Only after the first three. See the table in Section 4. A transaction coded
   to the wrong account often carries the wrong GST code with it.

**Private use.** Where an expense serves both business and private purposes, record the full
amount and apportion, rather than guessing a net figure. The apportionment basis must be
documented and consistent: a logbook for a vehicle, a floor area or hours record for a home
office, an itemised bill for a phone. A percentage with no supporting method fails on review.

**Unknown transactions.** Post to a clearing or suspense account and list them for the client.
Never guess a classification to close a period. An unresolved suspense balance at period end means
the BAS and the accounts are both unreliable. See `au-bas-preparation.md` Section 4.

### 11.2 Evidence to hold

**11.2 Evidence to hold**

| Transaction | Evidence required |
| --- | --- |
| Sale | Invoice or point-of-sale record. A tax invoice where GST is charged |
| Purchase where a GST credit is claimed | A valid tax invoice, unless the acquisition is $82.50 including GST or less |
| Purchase with no GST credit | Sufficient record to show the expense was incurred and its purpose |
| Asset acquisition | Invoice, plus the date first used or installed ready for use |
| Asset disposal | Sale document, plus the written down value and any balancing adjustment |
| Vehicle expenses | Logbook for a continuous 12-week period, valid five years, plus odometer readings, or kilometre records for the cents per kilometre method |
| Home office | Hours record and evidence that the expenses were incurred |
| Payroll | Payroll register, timesheets, the employment record and STP submissions |
| Adjustment to a sale or purchase | Adjustment note or credit note |
| Bad debt written off | The board minute or file note recording the write-off and its date |

### 11.3 Reconciliation as a control, not a chore

A reconciliation is what makes the ledger evidence rather than assertion. At minimum, each period:

- Every bank, credit card and loan account reconciled to the statement.
- GST collected and GST paid control accounts agreed to the transaction listing.
- PAYG withholding payable agreed to the payroll register less amounts remitted.
- Accounts receivable and accounts payable subledgers agreed to their control accounts.
- Inventory agreed to a count or a supported roll-forward.
- Loan accounts agreed to the lender statement, with interest and principal split correctly.
- Clearing and suspense accounts at nil or fully explained.

### 11.4 Accounting treatment is not tax treatment

The ledger produces the financial statements. The tax return starts from those statements and then
adjusts. Recording the tax answer in the ledger destroys the financial statements; recording only
the accounting answer and forgetting the adjustment understates or overstates tax. Keep both, and
keep the reconciliation between them.

**11.4 Accounting treatment is not tax treatment**

| Item | Accounting treatment | Tax treatment |
| --- | --- | --- |
| Depreciation | Useful life and residual value under AASB 116 | Effective life under Division 40, the small business pool, or the instant asset write-off |
| Buildings and structural improvements | Depreciated or held at cost under AASB 116 | Division 43 capital works at a fixed rate, and the deduction reduces the CGT cost base |
| Employee leave provisions | Recognised when the obligation arises | Deductible when the leave is paid |
| Doubtful debts allowance | An impairment estimate | Not deductible. Only a debt actually written off as bad is deductible |
| Entertainment | An expense in the profit and loss | Commonly non-deductible, and may instead be a fringe benefit |
| Fines and penalties | An expense | Not deductible |
| General interest charge on a tax debt | An expense | Not deductible where incurred on or after 1 July 2025 |
| Revenue | AASB 15 performance obligations | Derived when earned or received, depending on the accounting basis and the taxpayer |
| Prepayments | An asset, expensed over the period | Prepayment rules can spread the deduction, with a 12-month exception for some taxpayers |
| Borrowing costs | AASB 123 | Deductible over five years or the term of the loan, whichever is shorter |
| Unrealised foreign exchange movements | Revalued at reporting date | Taxed on a realisation event under Division 775 |
| Leases | Right-of-use asset and lease liability under AASB 16 | Depends on whether the arrangement is a lease or a hire purchase for tax |

Record permanent and temporary differences in a tax reconciliation working paper. A company also
needs deferred tax balances where it reports under the full recognition requirements.

### 11.5 Correcting an error

**11.5 Correcting an error**

| Where the error is | What to do |
| --- | --- |
| In the current open period, nothing lodged | Fix the transaction. No further action |
| In a closed period, but no BAS or return lodged | Post a dated correcting journal with a narration explaining it. Do not backdate into a locked period without a record |
| In a lodged BAS, GST affected | Apply the GST error correction rules. See `au-bas-preparation.md` Section 7 |
| In a lodged BAS, PAYG withholding affected | Correct through the PAYG withholding correction process, and check whether STP needs updating |
| In a lodged income tax return | Request an amendment. See `au-lodgment-deadlines-penalties.md` Section 10 |
| Circumstances changed after correct reporting | This is an adjustment, not an error. Record it in the current period |

### 11.6 Common bookkeeping errors

- Coding a transaction by the payee name rather than by what was supplied. The same supplier can
  produce taxable, GST-free and input taxed transactions.
- Claiming a GST credit on wages, superannuation, bank fees, most government charges or stamp duty.
- Coding a director loan drawing to wages, or a wage to a drawing.
- Capitalising a repair, or expensing an improvement.
- Recording a net amount for a transaction that had both a gross figure and a deduction, which
  hides the deduction from both the accounts and the BAS.
- Leaving a suspense balance and lodging anyway.
- Changing the chart of accounts mid-year without restating comparatives.
- Recording the tax depreciation figure in the ledger and calling it the accounting figure.
- Treating an impairment allowance as a deductible bad debt.
- Reconciling the bank but not the GST or PAYG withholding control accounts.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, registered tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

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
