---
name: malta-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for a Maltese entity. Trigger on phrases like "chart of accounts Malta", "nominal codes", "GAPSME financial statements", "P&L format", "balance sheet Malta", "expense account", "capitalise or expense", "depreciation Malta", "bank reconciliation", "micro-entity Malta", "small company accounts", "bookkeeping Malta", or any question about recording transactions, classifying expenses, or preparing management accounts under Maltese law. ALWAYS read this skill before touching any bookkeeping work for Malta.
version: 1.0
jurisdiction: MT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**  _(Companies Act (Cap. 386); Legal Notice 289 of 2015 (GAPSME); Income Tax Act (Cap. 123))_

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Currency | EUR |
| Financial year | Typically calendar year (1 Jan -- 31 Dec); companies may choose any 12-month period |
| Accounting standards | GAPSME (default for SMEs); IFRS as adopted by the EU (by board resolution) |
| Governing body | Accountancy Board (Malta), Commissioner for Revenue (CFR) |
| Key legislation | Companies Act (Cap. 386); Legal Notice 289 of 2015 (GAPSME); Income Tax Act (Cap. 123) |
| Standard chart of accounts | None mandated — entities design their own CoA provided it supports GAPSME/IFRS financial statements |
| Record retention | 6 years from end of the relevant financial year |

## Section 2 -- Recommended Chart of Accounts

Malta does not mandate a standard chart of accounts. The following is a recommended structure that maps cleanly to GAPSME financial statement presentation and Maltese tax return requirements.

### Assets (1xxx)

**Assets (1xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 1000 | Non-current assets (control) |  |
| 1010 | Intangible assets -- software | Capitalise if > EUR 1,160 (VAT CGS threshold) |
| 1020 | Intangible assets -- goodwill | Rare for sole traders |
| 1100 | Property, plant and equipment |  |
| 1110 | Land and buildings |  |
| 1120 | Motor vehicles |  |
| 1130 | Computer hardware |  |
| 1140 | Furniture and fittings |  |
| 1150 | Office equipment |  |
| 1160 | Leasehold improvements |  |
| 1199 | Accumulated depreciation | Contra-asset |
| 1200 | Current assets (control) |  |
| 1210 | Trade receivables |  |
| 1220 | Other receivables |  |
| 1230 | Prepayments |  |
| 1240 | VAT input (recoverable) | Article 10 entities only |
| 1300 | Bank -- current account |  |
| 1310 | Bank -- savings account |  |
| 1320 | Cash in hand |  |
| 1330 | Petty cash |  |

### Liabilities (2xxx)

**Liabilities (2xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 2000 | Non-current liabilities (control) |  |
| 2010 | Bank loans (long-term) |  |
| 2020 | Hire purchase obligations (long-term) |  |
| 2100 | Current liabilities (control) |  |
| 2110 | Trade payables |  |
| 2120 | Other payables |  |
| 2130 | Accruals |  |
| 2140 | VAT output (payable) |  |
| 2150 | VAT control | Net position for CFR |
| 2160 | Income tax payable |  |
| 2170 | SSC payable |  |
| 2180 | Bank overdraft |  |
| 2190 | Bank loans (current portion) |  |
| 2200 | Directors' loan account |  |

### Equity (3xxx)

**Equity (3xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 3000 | Share capital / owner's capital |  |
| 3010 | Share premium |  |
| 3100 | Retained earnings |  |
| 3200 | Current year profit/loss | Clearing account |
| 3300 | Drawings (sole trader) |  |

### Revenue (4xxx)

**Revenue (4xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 4000 | Sales -- services | Main revenue for service businesses |
| 4010 | Sales -- goods |  |
| 4020 | Sales -- exports / intra-EU | Zero-rated or exempt |
| 4100 | Other operating income |  |
| 4200 | Government grants (revenue) | Malta Enterprise grants |

### Cost of Goods Sold (5xxx)

**Cost of Goods Sold (5xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 5000 | Purchases -- goods for resale |  |
| 5010 | Direct materials |  |
| 5020 | Direct labour (subcontractors) |  |
| 5030 | Import duties |  |
| 5100 | Opening stock |  |
| 5110 | Closing stock |  |

### Operating Expenses (6xxx)

**Operating Expenses (6xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 6000 | Rent -- business premises | Fully deductible |
| 6010 | Rates and local council levies |  |
| 6020 | Electricity and water (ARMS) | Apportion if home office |
| 6030 | Telecoms and internet | Apportion if mixed use |
| 6040 | Insurance -- business |  |
| 6050 | Repairs and maintenance |  |
| 6100 | Salaries and wages |  |
| 6110 | Employer SSC (Class 1) |  |
| 6120 | SSC Class 2 (self-employed) | Maps to TA24 Box 20 |
| 6200 | Accountancy fees |  |
| 6210 | Legal and professional fees |  |
| 6220 | Bank charges |  |
| 6230 | Payment processing fees | Stripe, PayPal etc. |
| 6300 | Marketing and advertising |  |
| 6310 | Travel -- flights and accommodation | Business travel only |
| 6320 | Travel -- local transport |  |
| 6330 | Motor vehicle expenses | Business % only |
| 6340 | Motor vehicle fuel | Business % only |
| 6400 | Office supplies and stationery |  |
| 6410 | Software subscriptions (SaaS) | Recurring < EUR 1,160 |
| 6420 | Training and CPD |  |
| 6430 | Professional subscriptions | MIA, ACCA etc. |
| 6440 | Postage and courier |  |
| 6500 | Depreciation -- computer hardware | 25% straight-line |
| 6510 | Depreciation -- motor vehicles | 20% straight-line |
| 6520 | Depreciation -- furniture/fittings | 10% straight-line |
| 6530 | Depreciation -- office equipment | 20% straight-line |
| 6600 | Bad debts written off |  |
| 6700 | Entertainment | NOT deductible for tax |
| 6800 | Sundry expenses |  |

### Other Income / Expenses (7xxx)

**Other Income / Expenses (7xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 7000 | Interest received |  |
| 7010 | Interest paid |  |
| 7020 | Bank loan interest |  |
| 7100 | Profit/loss on disposal of assets |  |
| 7200 | Foreign exchange gains/losses |  |

### Tax (8xxx)

**Tax (8xxx)**

| Code | Account | Notes |
| --- | --- | --- |
| 8000 | Income tax expense | Current year charge |
| 8010 | Deferred tax | GAPSME medium entities |
| 8020 | Provisional tax paid | Credit against liability |

## Section 3 -- Revenue Recognition

**Revenue Recognition**

| Scenario | Treatment |
| --- | --- |
| **Default under GAPSME** | Accruals basis — revenue recognised when earned, not when cash received |
| **Sole traders (TA24)** | Tax return uses accruals basis; however CFR accepts cash basis for very small operations if consistently applied |
| **Article 10 VAT-registered** | Record revenue net of 18% VAT; VAT goes to 2140 |
| **Article 11 (exempt)** | Record revenue gross — no VAT component |
| **Advance payments received** | Credit to 2130 (Accruals) until service delivered, then transfer to 4000 |
| **Multi-period contracts** | Recognise revenue proportionally over the service period |
| **Bad debts** | Write off to 6600 only when irrecoverable; reverse the original revenue if not yet reported |

## Section 4 -- Expense Classification

**Expense Classification**

| Expense Type | Nominal Code | Tax Deductibility | Notes |
| --- | --- | --- | --- |
| Office rent | 6000 | Fully deductible | Dedicated business premises |
| Home office utilities | 6020 | Proportional (dedicated room %) | Default 0% until confirmed |
| Motor vehicle costs | 6330/6340 | Business % only | Mileage log required |
| Entertainment | 6700 | NOT deductible | Blocked under Article 14 ITA |
| Software subscriptions | 6410 | Fully deductible | Recurring SaaS under EUR 1,160 |
| Professional fees | 6200/6210 | Fully deductible | Accountant, lawyer (business) |
| Travel (business) | 6310/6320 | Fully deductible | Wholly business purpose |
| Training and CPD | 6420 | Fully deductible | Must relate to current business |
| SSC Class 2 | 6120 | Deductible (Box 20) | NOT in Box 2 of TA24 |
| Fines and penalties | — | NOT deductible | Do not record as business expense |
| Personal drawings | 3300 | NOT deductible | Equity movement, not expense |

## Section 5 -- Asset vs Expense Thresholds

**Asset vs Expense Thresholds**

| Rule | Threshold | Treatment |
| --- | --- | --- |
| **Tax depreciation (capital allowances)** | No statutory minimum — all business assets must be depreciated per 6th Schedule | Straight-line over minimum years |
| **VAT Capital Goods Scheme** | EUR 1,160 gross | Separate system; affects VAT Box 30 only |
| **Practical low-value expensing** | Some practitioners expense items under ~EUR 700 immediately | Flag for reviewer; strictly all assets should be depreciated |

### Depreciation Rates (Income Tax Act, 6th Schedule)

**Depreciation Rates (Income Tax Act, 6th Schedule)**  _(Income Tax Act, 6th Schedule)_

| Asset Category | Minimum Years | Annual Rate |
| --- | --- | --- |
| Computers and electronic equipment | 4 | 25% |
| Computer software | 4 | 25% |
| Motor vehicles | 5 | 20% |
| Plant and machinery | 5 | 20% |
| Office equipment | 5 | 20% |
| Air conditioning | 6 | ~17% |
| Furniture, fixtures, fittings | 10 | 10% |
| Electrical/plumbing installations | 15 | ~7% |
| Industrial buildings | 50 | 2% |

Depreciation is straight-line on cost. First-year depreciation starts in the year the asset is first used in business. Industrial buildings qualify for an additional 10% initial allowance in the acquisition year.

## Section 6 -- Profit and Loss Format

GAPSME requires an income statement with the following minimum structure:

```
INCOME STATEMENT
For the year ended [date]

Revenue                                          xxx
Cost of sales                                   (xxx)
                                                -----
GROSS PROFIT                                     xxx

Other operating income                           xxx
Administrative expenses                         (xxx)
Distribution costs                              (xxx)
Other operating expenses                        (xxx)
                                                -----
OPERATING PROFIT                                 xxx

Finance income                                   xxx
Finance costs                                   (xxx)
                                                -----
PROFIT BEFORE TAX                                xxx

Income tax expense                              (xxx)
                                                -----
PROFIT FOR THE YEAR                              xxx
```

Small entities under GAPSME may combine administrative and distribution costs into a single "operating expenses" line.

## Section 7 -- Balance Sheet Format

GAPSME prescribes a vertical (report) format:

```
BALANCE SHEET
As at [date]

NON-CURRENT ASSETS
  Intangible assets                              xxx
  Property, plant and equipment                  xxx
                                                -----
                                                 xxx

CURRENT ASSETS
  Inventories                                    xxx
  Trade and other receivables                    xxx
  Cash and cash equivalents                      xxx
                                                -----
                                                 xxx
                                                -----
TOTAL ASSETS                                     xxx

EQUITY
  Share capital                                  xxx
  Retained earnings                              xxx
                                                -----
                                                 xxx

NON-CURRENT LIABILITIES
  Borrowings                                     xxx
                                                -----
                                                 xxx

CURRENT LIABILITIES
  Trade and other payables                       xxx
  Current tax liabilities                        xxx
  Borrowings (current portion)                   xxx
                                                -----
                                                 xxx
                                                -----
TOTAL EQUITY AND LIABILITIES                     xxx
```

Small entities: balance sheet, income statement, and simplified notes only. Medium entities must add statement of changes in equity and cash flow statement.

## Section 8 -- Bank Reconciliation Patterns

### Maltese Bank Statement Formats

**Maltese Bank Statement Formats**

| Bank | Format | Date Format | Key Fields |
| --- | --- | --- | --- |
| BOV (Bank of Valletta) | PDF, CSV | DD/MM/YYYY | Date, Description, Debit, Credit, Balance |
| HSBC Malta | PDF, CSV | DD/MM/YYYY | Value Date, Description, Amount, Balance |
| APS Bank | PDF | DD/MM/YYYY | Date, Particulars, Withdrawals, Deposits |
| Revolut Business | CSV | YYYY-MM-DD | Date, Counterparty, Amount, Currency |
| Wise Business | CSV | YYYY-MM-DD | Date, Description, Amount, Currency, Balance |

### Common Maltese Transaction Descriptions

**Common Maltese Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| TRASFERIMENT / TRF IN | Incoming payment — check if revenue |
| DD / DEBIT DIRETT | Direct debit — utility, subscription, or insurance |
| SO / STANDING ORDER | Standing order — rent or loan repayment |
| KARTA / CARD | Card payment — expense, check merchant |
| SPEJJEZ / CHARGES | Bank charges (6220) |
| ARMS / ARMS LTD | Electricity/water utility (6020) |
| CFR / TAX / SSC | Tax or SSC payment — exclude from P&L expense |
| INTERNAL TRANSFER | Own-account transfer — exclude |

## Section 9 -- Micro-Entity / Small Business Simplifications

### GAPSME Size Thresholds (must meet 2 of 3 for two consecutive years)

**GAPSME Size Thresholds (must meet 2 of 3 for two consecutive years)**

| Criterion | Small | Medium |
| --- | --- | --- |
| Balance sheet total | ≤ EUR 4,000,000 | ≤ EUR 20,000,000 |
| Revenue | ≤ EUR 8,000,000 | ≤ EUR 40,000,000 |
| Average employees | ≤ 50 | ≤ 250 |

### Simplifications by Entity Size

**Simplifications by Entity Size**

| Requirement | Small Entity | Medium Entity |
| --- | --- | --- |
| Balance sheet | Required (abbreviated) | Required (full) |
| Income statement | Required | Required |
| Notes to accounts | Simplified (limited disclosures) | Full disclosures |
| Statement of changes in equity | NOT required | Required |
| Cash flow statement | NOT required | Required |
| Directors' report | NOT required (private company) | Required |
| Audit | Exempt if small private company | Required |
| Filing with Registry | Abbreviated balance sheet; income statement may be withheld | Full filing |

Sole traders filing TA24 are not required to prepare GAPSME financial statements, but must maintain adequate books and records for CFR inspection.

## Section 10 -- Interaction with Tax Skills

**Interaction with Tax Skills**

| Tax Skill | How Bookkeeping Connects |
| --- | --- |
| **malta-income-tax** | P&L profit feeds TA24 Box 3 (net profit). Depreciation per 6th Schedule goes to Box 15. SSC Class 2 goes to Box 20 (not operating expenses for tax). Entertainment in 6700 must be added back. |
| **malta-vat-return** | VAT accounts (1240, 2140, 2150) feed the VAT return. Article 10 entities: output VAT (Box 1) from 2140; input VAT (Box 6) from 1240. Reconcile VAT control (2150) quarterly. |
| **malta-ssc** | SSC Class 2 payments recorded in 6120 feed TA24 Box 20. Employer Class 1 contributions in 6110 are a deductible operating expense in Box 2. |
| **mt-estimated-tax** | Provisional tax payments recorded in 8020 feed TA24 Box 36 as credits against the final tax liability. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
