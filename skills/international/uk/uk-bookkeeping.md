---
name: uk-bookkeeping
description: Use this skill whenever asked about UK bookkeeping for sole traders, micro-entities, or small companies. Trigger on phrases like "chart of accounts", "nominal codes", "bookkeeping", "profit and loss", "balance sheet", "FRS 105", "FRS 102 Section 1A", "Making Tax Digital", "MTD", "MTD ITSA bookkeeping", "April 2026 quarterly", "VAT threshold £90,000", "bank reconciliation", "double-entry", "expense categories", "revenue recognition", "depreciation", "capital allowances", "micro-entity accounts", "small company accounts", "accrual basis", "cash basis", "general ledger", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a UK business.
version: 1.1
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Bookkeeping

## UK Bookkeeping Skill v1.1

## Section 1 -- Quick Reference

Year applicability: Rules in this skill apply across 2024-25, 2025-26, and 2026-27 unless specified. The biggest 2026-27 change is mandatory MTD ITSA quarterly bookkeeping for in-scope sole traders and landlords.

**Quick Reference Fields**

| Field | Value |
| --- | --- |
| Country | United Kingdom (England, Wales, Scotland, Northern Ireland) |
| Currency | GBP (£) only |
| Financial year | Flexible — companies choose their own year-end; sole traders on tax-year basis 6 April -- 5 April (basis period reform complete; clean tax-year basis for 2025-26 and 2026-27, no transitional adjustments) |
| Accounting standards | FRS 105 (micro-entities), FRS 102 Section 1A (small entities), full FRS 102 |
| Governing body | Financial Reporting Council (FRC) |
| Tax authority | HM Revenue & Customs (HMRC) |
| Key legislation | Companies Act 2006 (Part 15, s.382-384 for size thresholds); The Small Companies and Groups Regulations 2008 (SI 2008/409); Taxes Management Act 1970 |
| MTD VAT | In force for ALL VAT-registered businesses (regardless of turnover) |
| MTD ITSA | From 6 April 2026 for sole traders + landlords with gross income > £50,000 in 2024-25 |
| Size thresholds (from 6 Apr 2025) | Micro: turnover ≤£1m, assets ≤£500k, ≤10 employees; Small: turnover ≤£15m, assets ≤£7.5m, ≤50 employees |

### 3-Year Thresholds at a Glance

**3-Year Thresholds at a Glance**

| Item | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| VAT registration threshold | £90,000 (from 1 Apr 2024) | £90,000 | £90,000 |
| VAT deregistration threshold | £88,000 (from 1 Apr 2024) | £88,000 | £88,000 |
| MTD VAT | All VAT-registered | All VAT-registered | All VAT-registered |
| MTD ITSA — Phase 1 (>£50k) | Not yet in force | Not yet in force | **Mandatory from 6 April 2026** (quarterly updates via compatible software) |
| MTD ITSA — Phase 2 (>£30k) | n/a | n/a | From 6 April 2027 (out of scope window) |
| Cash basis for sole traders / partnerships | Default (no income cap; election out by formal election) | Default | Default |
| Basis period reform | Transitional year already completed; tax-year basis from 2024-25 | Clean tax-year basis — no transitional adjustments | Clean tax-year basis — no transitional adjustments |
| Small company (Companies Act) | Turnover ≤ £10.2m | **Turnover ≤ £15m** (from 6 Apr 2025), BS ≤ £7.5m, ≤50 employees | Turnover ≤ £15m, BS ≤ £7.5m, ≤50 employees |
| Micro-entity (FRS 105) | Turnover ≤ £632k | **Turnover ≤ £1m** (from 6 Apr 2025), BS ≤ £500k, ≤10 employees | Turnover ≤ £1m, BS ≤ £500k, ≤10 employees |

## Section 2 -- Standard Chart of Accounts (Nominal Codes)

UK practice uses 4-digit nominal codes. Ranges below follow the Sage/Xero/QuickBooks convention widely adopted.

### Assets (0001–1999)

**Assets (0001–1999)**

| Code | Account | Type |
| --- | --- | --- |
| 0010 | Freehold Property | Non-current asset |
| 0020 | Leasehold Property | Non-current asset |
| 0030 | Plant and Machinery | Non-current asset |
| 0040 | Furniture and Fittings | Non-current asset |
| 0050 | Motor Vehicles | Non-current asset |
| 0060 | Office Equipment | Non-current asset |
| 0070 | Computer Equipment | Non-current asset |
| 0011–0071 | Accumulated Depreciation (paired) | Contra asset |
| 1001 | Stock / Inventory | Current asset |
| 1100 | Trade Debtors (Accounts Receivable) | Current asset |
| 1101 | Other Debtors | Current asset |
| 1102 | Prepayments | Current asset |
| 1200 | Bank Current Account | Current asset |
| 1210 | Bank Deposit Account | Current asset |
| 1220 | Building Society Account | Current asset |
| 1230 | Petty Cash | Current asset |
| 1240 | PayPal / Stripe Account | Current asset |

### Liabilities (2000–2999)

**Liabilities (2000–2999)**

| Code | Account | Type |
| --- | --- | --- |
| 2100 | Trade Creditors (Accounts Payable) | Current liability |
| 2101 | Other Creditors | Current liability |
| 2102 | Accruals | Current liability |
| 2200 | VAT Control Account | Current liability |
| 2201 | VAT Input (Purchases) | Current liability |
| 2202 | VAT Output (Sales) | Current liability |
| 2210 | PAYE / NIC Liability | Current liability |
| 2220 | Corporation Tax Liability | Current liability |
| 2300 | Bank Loan (< 1 year portion) | Current liability |
| 2310 | HP / Finance Lease (< 1 year) | Current liability |
| 2400 | Bank Loan (> 1 year) | Non-current liability |
| 2410 | Director's Loan Account | Non-current liability |
| 2500 | Hire Purchase (> 1 year) | Non-current liability |

### Equity (3000–3999)

**Equity (3000–3999)**

| Code | Account | Type |
| --- | --- | --- |
| 3000 | Share Capital (Ordinary) | Equity |
| 3001 | Share Premium | Equity |
| 3100 | Retained Earnings | Equity |
| 3200 | Dividends Paid | Equity |
| 3300 | Owner's Capital Introduced (sole trader) | Equity |
| 3301 | Owner's Drawings (sole trader) | Equity |

### Revenue (4000–4999)

**Revenue (4000–4999)**

| Code | Account | Type |
| --- | --- | --- |
| 4000 | Sales — Standard Rate (20% VAT) | Revenue |
| 4001 | Sales — Reduced Rate (5% VAT) | Revenue |
| 4002 | Sales — Zero Rate (0% VAT) | Revenue |
| 4003 | Sales — Exempt | Revenue |
| 4004 | Sales — Exports (outside UK) | Revenue |
| 4100 | Other Operating Income | Revenue |
| 4200 | Discount Allowed | Contra revenue |

### Cost of Goods Sold (5000–5999)

**Cost of Goods Sold (5000–5999)**

| Code | Account | Type |
| --- | --- | --- |
| 5000 | Purchases — Goods for Resale | COGS |
| 5001 | Purchases — Materials | COGS |
| 5100 | Carriage Inward | COGS |
| 5200 | Direct Labour / Subcontractor Costs | COGS |
| 5300 | Stock Adjustments | COGS |

### Operating Expenses (6000–6999)

**Operating Expenses (6000–6999)**

| Code | Account | Type |
| --- | --- | --- |
| 6000 | Rent | Overhead |
| 6001 | Rates | Overhead |
| 6010 | Light, Heat and Power | Overhead |
| 6020 | Insurance | Overhead |
| 6030 | Repairs and Maintenance | Overhead |
| 6040 | Cleaning | Overhead |
| 6100 | Wages and Salaries | Overhead |
| 6110 | Employer's NIC | Overhead |
| 6120 | Employer's Pension Contributions | Overhead |
| 6200 | Advertising and Marketing | Overhead |
| 6210 | Printing, Postage and Stationery | Overhead |
| 6220 | Telephone and Internet | Overhead |
| 6230 | Computer Software / SaaS | Overhead |
| 6240 | Professional Subscriptions | Overhead |
| 6300 | Travel and Subsistence | Overhead |
| 6310 | Motor Expenses — Fuel | Overhead |
| 6311 | Motor Expenses — Insurance | Overhead |
| 6312 | Motor Expenses — Repairs | Overhead |
| 6400 | Accountancy Fees | Overhead |
| 6410 | Legal Fees | Overhead |
| 6420 | Bank Charges and Interest | Overhead |
| 6430 | Bad Debts Written Off | Overhead |
| 6500 | Entertaining (non-deductible for tax) | Overhead |
| 6510 | Staff Welfare | Overhead |
| 6600 | Sundry Expenses | Overhead |

### Other Income / Expenses (7000–7999)

**Other Income / Expenses (7000–7999)**

| Code | Account | Type |
| --- | --- | --- |
| 7000 | Interest Received | Other income |
| 7010 | Rental Income | Other income |
| 7100 | Profit/Loss on Disposal of Assets | Other income/expense |
| 7200 | Grants Received | Other income |

### Depreciation and Tax (8000–8999)

**Depreciation and Tax (8000–8999)**

| Code | Account | Type |
| --- | --- | --- |
| 8000 | Depreciation — Property | Expense |
| 8010 | Depreciation — Plant and Machinery | Expense |
| 8020 | Depreciation — Fixtures and Fittings | Expense |
| 8030 | Depreciation — Motor Vehicles | Expense |
| 8040 | Depreciation — Computer Equipment | Expense |
| 8100 | Corporation Tax Charge | Tax expense |
| 8200 | Dividends Receivable | Other income |

## Section 3 -- Revenue Recognition

### Cash Basis vs Accruals Basis

**Cash Basis vs Accruals Basis**

| Criterion | Cash Basis (Sole Traders) | Accruals Basis |
| --- | --- | --- |
| Eligibility | Default for sole traders & partnerships from 2024-25 (no income cap since reform); election out by formal election | All entities; mandatory for companies |
| Income recognised | When cash received | When earned (invoice date) |
| Expenses recognised | When cash paid | When incurred |
| Debtors / Creditors | Not used | Required |
| Stock adjustments | Not required | Required (opening/closing stock) |
| Capital items | Treated as expense when paid (except cars) | Capitalised and depreciated |
| Interest restriction | £500 for cash basis | No restriction for accruals |

### Companies Act Recognition

- **Revenue recognition under FRS 102/105** — Under FRS 102/105, revenue is recognised when: Goods: risks and rewards of ownership transferred; Services: percentage of completion or when service delivered; Long-term contracts: stage of completion method  _(FRS 102/105)_

## Section 4 -- Expense Classification

### HMRC Self-Assessment Categories (SA103)

For sole traders, HMRC groups expenses on form SA103:

**HMRC Self-Assessment Categories (SA103)**

| SA103 Box | Category | Nominal Codes |
| --- | --- | --- |
| Box 17 | Cost of goods sold | 5000–5300 |
| Box 18 | Construction industry subcontractor costs | 5200 |
| Box 19 | Wages, salaries and other staff costs | 6100–6120 |
| Box 20 | Car, van and travel expenses | 6300–6312 |
| Box 21 | Rent, rates, power and insurance | 6000–6020 |
| Box 22 | Repairs and maintenance | 6030 |
| Box 23 | Phone, fax, stationery, other office costs | 6210–6230 |
| Box 24 | Advertising and business entertainment | 6200, 6500 |
| Box 25 | Interest on bank/business loans | 6420 |
| Box 26 | Bank charges, credit card charges | 6420 |
| Box 27 | Irrecoverable debts written off | 6430 |
| Box 28 | Accountancy, legal, professional fees | 6400–6410 |
| Box 29 | Depreciation and loss on sale of assets | 8000–8040 |
| Box 30 | Other business expenses | 6600 |
| Box 31 | Total allowable expenses | Sum |

### Non-Deductible Expenses (UK Tax)

- **Non-deductible expenses list** — Business entertaining (clients) — disallowed for income tax/CT; Personal expenses — not wholly and exclusively for trade; Fines and penalties — public policy; Capital expenditure — must go through capital allowances; General provisions — only specific bad debts are allowable

## Section 5 -- Asset vs Expense Thresholds

### Capital Allowances (Not Accounting Depreciation)

UK tax does NOT use accounting depreciation — it adds back book depreciation and substitutes capital allowances.

**Capital Allowances (Not Accounting Depreciation)**

| Allowance | Rate | Notes |
| --- | --- | --- |
| Annual Investment Allowance (AIA) | 100% up to £1,000,000 | Most plant & machinery; NOT cars |
| First Year Allowance (40%) | 40% | From 1 Jan 2026 for unincorporated businesses |
| Full Expensing | 100% | Companies only, new P&M (from April 2023) |
| Main Pool WDA | 18% reducing balance (14% from April 2026) | Items not covered by AIA |
| Special Rate Pool WDA | 6% reducing balance | Long-life assets, integral features, high-emission cars |
| Cars: CO₂ ≤ 0 g/km | 100% FYA | Electric/zero-emission |
| Cars: CO₂ 1–50 g/km | 18% main pool |  |
| Cars: CO₂ > 50 g/km | 6% special rate |  |
| Small Pools Allowance | Write off pool balance ≤ £1,000 |  |

### Accounting Depreciation (Book Purposes)

For FRS 105/102 accounts, depreciate over useful life:

**Accounting Depreciation (Book Purposes)**

| Asset Class | Typical Book Rate | Method |
| --- | --- | --- |
| Freehold property | 2% | Straight-line |
| Leasehold improvements | Over lease term | Straight-line |
| Plant and machinery | 15–25% | Reducing balance or straight-line |
| Fixtures and fittings | 15–20% | Straight-line |
| Motor vehicles | 25% | Reducing balance |
| Computer equipment | 33% | Straight-line (3-year life) |

### Low-Value Items

- **Low-value item policy** — No statutory de minimis in UK GAAP, but common practice: items under £100–£500 expensed directly. Firms should set and document their own capitalisation policy.

## Section 6 -- Profit & Loss Format

### FRS 105 Micro-Entity Format (Format 2 — by nature)

PROFIT AND LOSS ACCOUNT
                                    This Year (£)    Prior Year (£)
Turnover                                xxx              xxx
Other income                            xxx              xxx
                                       ────             ────
Raw materials and consumables          (xxx)            (xxx)
Staff costs                            (xxx)            (xxx)
Depreciation and amortisation          (xxx)            (xxx)
Other charges                          (xxx)            (xxx)
                                       ────             ────
Tax                                    (xxx)            (xxx)
                                       ────             ────
Profit (loss) for the financial year    xxx              xxx

### FRS 102 Section 1A Small Company (Format 1 — by function)

PROFIT AND LOSS ACCOUNT
Turnover                                xxx
Cost of sales                          (xxx)
                                       ────
Gross profit                            xxx
Administrative expenses                (xxx)
Distribution costs                     (xxx)
                                       ────
Operating profit                        xxx
Interest receivable                     xxx
Interest payable                       (xxx)
                                       ────
Profit before tax                       xxx
Tax on profit                          (xxx)
                                       ────
Profit for the financial year           xxx

## Section 7 -- Balance Sheet Format

### FRS 105 / Small Company Balance Sheet (Vertical Format)

BALANCE SHEET as at [date]
                                        £           £
FIXED ASSETS
Intangible assets                                  xxx
Tangible assets                                    xxx
                                                   ────
                                                   xxx
CURRENT ASSETS
Stocks                              xxx
Debtors                             xxx
Cash at bank and in hand            xxx
                                    ────
                                    xxx
CREDITORS: amounts falling
  due within one year              (xxx)
                                    ────
NET CURRENT ASSETS                                 xxx
                                                   ────
TOTAL ASSETS LESS CURRENT LIABILITIES              xxx

CREDITORS: amounts falling
  due after more than one year                    (xxx)
PROVISIONS FOR LIABILITIES                        (xxx)
                                                   ────
NET ASSETS                                         xxx
                                                   ════

CAPITAL AND RESERVES
Called up share capital                            xxx
Profit and loss account (retained earnings)       xxx
                                                   ────
SHAREHOLDERS' FUNDS                                xxx
                                                   ════

## Section 8 -- Bank Reconciliation Patterns

### Common UK Bank Formats

**Common UK Bank Formats**

| Bank | Export Format | Key Fields |
| --- | --- | --- |
| Barclays | CSV, OFX | Date, Description, Amount, Balance |
| HSBC | CSV, PDF | Date, Payment Type, Description, Paid Out, Paid In, Balance |
| Lloyds | CSV, OFX | Transaction Date, Description, Debit, Credit, Balance |
| NatWest / RBS | CSV, OFX | Date, Type, Description, Value, Balance |
| Starling | CSV, QIF | Date, Counter Party, Reference, Type, Amount, Balance |
| Monzo Business | CSV | Date, Name, Amount, Category, Notes |
| Tide | CSV | Date, Description, Money In, Money Out, Balance |

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| FPO / FPI (Faster Payment Out/In) | Transfer — check counterparty |
| DD (Direct Debit) | Regular expense (insurance, utility, subscription) |
| STO (Standing Order) | Regular expense (rent, loan repayment) |
| BGC (Bank Giro Credit) | Income — customer payment |
| CHQ (Cheque) | Varies — check payee |
| DEB / VIS / MC (Card Payment) | Expense — check merchant |
| HMRC VAT, HMRC PAYE, HMRC CT | Tax payment — exclude from P&L expenses |
| STRIPE, PAYPAL, GOCARDLESS | Payment processor — match to invoices |
| TFR (Transfer) | Internal — possible own-account transfer |

## Section 9 -- Micro-Entity / Small Business Simplifications

### FRS 105 Simplifications (Micro-Entities)

**FRS 105 Simplifications (Micro-Entities)**

| Feature | Simplification |
| --- | --- |
| Financial statements | Balance sheet + P&L only (no cash flow, no directors' report) |
| Disclosures | Minimal — only advances/credits to directors, guarantees |
| Revaluation | Prohibited — historical cost only |
| Deferred tax | Not recognised |
| Financial instruments | All at cost or amortised cost |
| Leases | All treated as operating leases |
| Government grants | Recognised when receivable |
| Filing | Abbreviated accounts at Companies House (P&L not public) |

### Qualifying Thresholds (from 6 April 2025)

**Qualifying Thresholds (from 6 April 2025)**

| Regime | Turnover | Balance Sheet | Employees |
| --- | --- | --- | --- |
| Micro-entity (FRS 105) | ≤ £1,000,000 | ≤ £500,000 | ≤ 10 |
| Small company (FRS 102 s.1A) | ≤ £15,000,000 | ≤ £7,500,000 | ≤ 50 |

### Cash Basis for Sole Traders

- **Cash basis default and features** — From 2024-25 onwards, cash basis is the default for sole traders and partnerships, with no income cap following the reform. Taxpayers may elect out via a formal election to use the accruals basis. Under cash basis: No debtors/creditors accounting; No depreciation (capital items expensed — except cars); Interest expense capped at £500; Loss relief restricted to current trade only

### MTD ITSA — From 6 April 2026

- **MTD ITSA mandate details** — Sole traders and landlords with gross income > £50,000 in 2024-25 are mandated into MTD ITSA from 6 April 2026. This is the largest bookkeeping change in the 3-year window: Quarterly updates (digital records of income and expenses) submitted via MTD-compatible software; End-of-period statement and final declaration replace the traditional SA return for in-scope taxpayers; Digital record-keeping requirement — paper ledgers no longer sufficient for in-scope businesses; Phase 2 (>£30,000) follows from 6 April 2027. Bookkeeping software choice and chart-of-accounts mapping should be MTD-ITSA-ready for any client expected to cross the £50,000 threshold for 2024-25.  _(6 April 2026)_

## Section 10 -- Interaction with Tax Skills

### Income Tax (Self-Assessment SA103/SA105)

- **Bookkeeping to income tax mapping** — Bookkeeping P&L feeds directly into SA103 (self-employment) or SA105 (property); Add back: entertaining, depreciation, personal element of mixed expenses; Deduct: capital allowances (in place of depreciation), trading losses brought forward; Cash basis taxpayers report income/expenses as per bank, with no accruals adjustments

### Corporation Tax (CT600)

- **Bookkeeping to CT600 mapping** — Start with accounting profit per FRS 105/102; Adjust: add back book depreciation, non-deductible entertainment, general provisions; Deduct: capital allowances, R&D enhanced deduction if eligible; GAAR / transfer pricing for connected parties

### VAT Return (Making Tax Digital)

**VAT Return (Making Tax Digital)**

| BAS Box | Description | CoA Mapping |
| --- | --- | --- |
| Box 1 | VAT due on sales | 2202 (output VAT) |
| Box 2 | VAT due on acquisitions from EU | 2202 |
| Box 3 | Total VAT due (Box 1 + 2) | Calculated |
| Box 4 | VAT reclaimed on purchases | 2201 (input VAT) |
| Box 5 | Net VAT to pay or reclaim | 2200 (control) |
| Box 6 | Total sales excl. VAT | 4000–4004 |
| Box 7 | Total purchases excl. VAT | 5000–5300 + 6000–6600 |
| Box 8 | Supplies of goods to EU | 4004 (subset) |
| Box 9 | Acquisitions from EU | 5000 (subset) |

### Payroll (RTI — Real Time Information)

- **Payroll RTI reporting rules** — Report PAYE/NIC to HMRC on or before each pay date via Full Payment Submission (FPS); Employer Payment Summary (EPS) for recoverable amounts; Nominal 6100 (gross wages) + 6110 (employer NIC) + 6120 (employer pension) = total staff cost

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant, ACCA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
