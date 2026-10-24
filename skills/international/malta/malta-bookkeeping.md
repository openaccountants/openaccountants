---
name: malta-bookkeeping
description: "Use this skill whenever asked about bookkeeping, a chart of accounts, expense classification, asset capitalisation, depreciation against tax wear and tear, bank reconciliation, record keeping or management accounts for a Maltese company or self-employed person in 2026. Covers a recommended chart of accounts mapped to GAPSME statements, revenue and VAT recording, which expenses fail the Income Tax Act test, the S.L. 123.01 minimum years for wear and tear and the EUR 14,000 car cap, the EUR 1,160 VAT capital goods threshold, record retention (10 years Companies Act, 9 years income tax, 6 years VAT), and the GAPSME and Companies Act size tests. Trigger on: chart of accounts Malta, nominal codes, bookkeeping Malta, capitalise or expense, depreciation Malta, wear and tear, bank reconciliation, GAPSME, small company accounts Malta."
version: 1.2
jurisdiction: MT
tax_year: 2026
last_updated: 2026-10-24
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Bookkeeping v1.2

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.**

Tax year 2026. This skill is the day-to-day bookkeeping workflow. Statutory accounts, size tests and audit are in `malta-financial-statements`; individual tax in `malta-income-tax`; company tax in `mt-corporate-tax`; provisional tax in `mt-estimated-tax`; VAT in `malta-vat-return`; social security in `malta-ssc`; payroll in `malta-payroll`.

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Currency | EUR (a company may have share capital in another currency; accounts follow it, art. 187) | Companies Act, Cap. 386 |
| Financial year | Any accounting reference date; 31 December if none notified within nine months of registration | Cap. 386 art. 164 |
| Frameworks | GAPSME for entities within its limits, unless the board resolves to use IFRS as adopted by the EU | Accountancy Profession (GAPSME) Regulations, S.L. 281.05 reg. 4 |
| Chart of accounts | None prescribed. Records must show and explain the transactions and let the directors prepare compliant accounts | Cap. 386 art. 163(1), (2) |
| Records to keep (companies) | Receipts and payments, assets and liabilities, stock statements where goods are dealt in | Cap. 386 art. 163(1) |
| Records to keep (any business, for tax) | Proper accounts of receipts, payments and all transactions; a profit and loss account; a statement of assets and liabilities (a balance sheet for a company) | Income Tax Management Act, Cap. 372, art. 19(1), (2) |
| Retention | Companies: 10 years (art. 163(5) Cap. 386). Income tax: at least 9 years after the transaction (art. 19(5) Cap. 372). VAT: at least 6 years (VAT Act art. 48) | as stated |
| VAT standard rate | 18% | VAT Act, Cap. 406, art. 19 |

## Section 2: Recommended Chart of Accounts

Malta does not prescribe a chart of accounts. The structure below maps to GAPSME statements and to the adjustments the tax return needs.

### Assets (1xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 1000 | Non-current assets (control) | |
| 1010 | Intangible assets: software | Capitalise under the entity's written capitalisation policy |
| 1020 | Intangible assets: goodwill | |
| 1100 | Property, plant and equipment | |
| 1110 | Land and buildings | |
| 1120 | Motor vehicles | Keep cost; tax cost is capped at EUR 14,000 for cars (S.L. 123.07 rule 3) |
| 1130 | Computer hardware | |
| 1140 | Furniture and fittings | |
| 1150 | Office equipment and other machinery | |
| 1160 | Leasehold improvements | |
| 1199 | Accumulated depreciation | Contra-asset |
| 1200 | Current assets (control) | |
| 1210 | Trade receivables | |
| 1220 | Other receivables | |
| 1230 | Prepayments | |
| 1240 | VAT input (recoverable) | Article 10 registrants only |
| 1250 | Provisional tax paid | Credit against the final tax |
| 1300 | Bank: current account | |
| 1310 | Bank: savings account | |
| 1320 | Cash in hand | |
| 1330 | Petty cash | |

### Liabilities (2xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 2000 | Non-current liabilities (control) | |
| 2010 | Bank loans (long-term) | |
| 2020 | Hire purchase and lease obligations (long-term) | |
| 2100 | Current liabilities (control) | |
| 2110 | Trade payables | |
| 2120 | Other payables | |
| 2130 | Accruals | |
| 2135 | Deferred income | Advance payments for work not yet done |
| 2140 | VAT output (payable) | |
| 2150 | VAT control | Net position for MTCA |
| 2160 | Income tax payable | |
| 2165 | FSS tax and Class 1 SSC withheld | Payroll |
| 2170 | SSC payable (employer share) | |
| 2180 | Bank overdraft | |
| 2190 | Bank loans (current portion) | |
| 2200 | Directors' loan account | |

### Equity (3xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 3000 | Share capital or owner's capital | |
| 3010 | Share premium | |
| 3100 | Retained earnings | |
| 3200 | Current year profit or loss | Clearing account |
| 3300 | Drawings (sole trader) | |
| 3400 | Dividends paid | Record the tax account the dividend is paid from (`mt-corporate-tax`) |

### Revenue (4xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 4000 | Sales: services | |
| 4010 | Sales: goods | |
| 4020 | Sales: exports and intra-EU | Exempt with credit or outside scope; see `malta-vat-return` |
| 4100 | Other operating income | |
| 4200 | Government grants (revenue) | |

### Cost of sales (5xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 5000 | Purchases: goods for resale | |
| 5010 | Direct materials | |
| 5020 | Subcontractors | |
| 5030 | Import duties | |
| 5100 | Opening stock | |
| 5110 | Closing stock | Stock statements are a legal record where goods are dealt in (art. 163(1)(c)) |

### Operating expenses (6xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 6000 | Rent: business premises | |
| 6010 | Rates and local levies | |
| 6020 | Electricity and water | Apportion if home office |
| 6030 | Telecoms and internet | Apportion if mixed use |
| 6040 | Insurance: business | |
| 6050 | Repairs and maintenance | Improvements are capital (art. 26 Cap. 123) |
| 6100 | Salaries and wages | Deductible only if run through FSS (S.L. 123.07 rule 4) |
| 6110 | Employer SSC (Class 1) and Maternity Leave Fund | |
| 6120 | SSC Class 2 (self-employed) | Memo for tax; see Section 4 |
| 6200 | Accountancy and audit fees | |
| 6210 | Legal and professional fees | Split capital (for example share issue, property) from revenue |
| 6220 | Bank charges | |
| 6230 | Payment processing fees | |
| 6300 | Marketing and advertising | |
| 6310 | Travel: flights and accommodation | Business purpose only |
| 6320 | Travel: local transport | |
| 6330 | Motor vehicle running costs | Business share only |
| 6340 | Motor vehicle fuel | Business share only |
| 6400 | Office supplies and stationery | |
| 6410 | Software subscriptions | |
| 6420 | Training | |
| 6430 | Professional subscriptions | |
| 6440 | Postage and courier | |
| 6500 | Depreciation | Accounting charge; added back for tax and replaced by wear and tear |
| 6600 | Bad debts written off | Specific debts only for tax |
| 6610 | Provision for doubtful debts (movement) | Added back for tax |
| 6700 | Entertainment | Flag for tax; see Section 4 |
| 6710 | Fines and penalties | Not deductible |
| 6800 | Sundry expenses | |

### Other income and expenses (7xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 7000 | Interest received | |
| 7010 | Interest paid | |
| 7100 | Profit or loss on disposal of assets | Replaced by the article 24 balancing statement for tax |
| 7200 | Foreign exchange gains and losses | |

### Tax (8xxx)

| Code | Account | Notes |
| --- | --- | --- |
| 8000 | Income tax expense (current) | |
| 8010 | Deferred tax | |

## Section 3: Revenue Recognition

| Scenario | Treatment |
| --- | --- |
| Default | Accruals basis under GAPSME or IFRS: revenue when earned |
| Article 10 VAT registrant | Record revenue net of VAT; output VAT to 2140 |
| Article 11 small enterprise | No VAT charged; record the amount invoiced as revenue |
| Advance payments | Credit 2135 deferred income until the work is done, then transfer to 4000 |
| Contracts spanning periods | Recognise over the service period |
| Bad debts | Write off to 6600 when specific and irrecoverable; do not reverse revenue |

A self-employed person's records must still meet article 19 of Cap. 372 (receipts, payments, a profit and loss account and a statement of assets and liabilities), whatever basis is used.

## Section 4: Expense Classification and Tax

The tax test is article 14(1) of the Income Tax Act: outgoings "wholly and exclusively incurred in the production of the income". Article 26 bars private or domestic spending, capital spending, improvements, recoverable amounts and voluntary payments.

| Expense | Code | Tax treatment | Source |
| --- | --- | --- | --- |
| Office rent | 6000 | Deductible | art. 14(1) |
| Home office utilities | 6020 | Business share only; default 0% until documented | art. 14(1), 26 |
| Car running costs | 6330, 6340 | Business share only; keep a log | art. 14(1), 26 |
| Leased car listed above EUR 14,000 | 6330 | Lease payments × 14,000 ÷ listed price, then business share | S.L. 123.07 rule 3(2) |
| Wages | 6100 | Deductible if run through FSS | S.L. 123.07 rule 4 |
| Entertainment | 6700 | No specific rule in the Act; treat as private unless the article 14(1) test is clearly met, and flag | art. 14(1), 26 |
| Fines and penalties | 6710 | Not deductible | art. 26 |
| Depreciation | 6500 | Added back; wear and tear deducted instead | art. 14(1)(f); S.L. 123.01 |
| General bad debt provision | 6610 | Added back; specific bad debts proved to the Commissioner are deductible | art. 14(1)(d) |
| SSC Class 2 | 6120 | No deduction in the Income Tax Act; `malta-income-tax` treats it as a memo. Confirm on the MTCA return | Cap. 123 Part IV |
| Drawings | 3300 | Not an expense | |

## Section 5: Asset or Expense

| Rule | Threshold | Treatment |
| --- | --- | --- |
| Accounts | No statutory threshold | Set and document a capitalisation policy under the framework |
| Income tax | No de minimis in S.L. 123.01 | Capital items go through wear and tear, not expenses (art. 26) |
| VAT capital goods | EUR 1,160 for equipment, tools and office furniture; all immovable property | Keep the capital goods list; input VAT is adjusted over 5 or 20 years if use changes (S.L. 406.12) |

### Tax wear and tear: minimum years (S.L. 123.01 Schedule)

These are tax minimums, not accounting lives. Accounting depreciation follows the framework and the asset's useful life.

| Category | Minimum years |
| --- | --- |
| Computers and electronic equipment; computer software | 4 |
| Motor vehicles; other machinery | 5 |
| Catering equipment; air-conditioners; medical equipment; communication and broadcasting equipment; construction and excavation equipment | 6 |
| Furniture, fixtures, fittings and soft furnishings; lifts and escalators; ships; other plant | 10 |
| Electrical and plumbing installations and sanitary fittings | 15 |
| Cable and pipeline infrastructure | 20 |

Rules: straight line on cost (rule 3); a full year's allowance in the year of acquisition and none in the year of disposal (rule 7); only with proper cost records (rule 5); cut to the business-use share (rule 11). Industrial buildings: at most 2% of cost a year, excluding the land (Cap. 123 art. 14(1)(f), proviso (i)), plus a one-tenth initial deduction in the first year of use (art. 14(1)(j)). Cars: cost capped at EUR 14,000 (S.L. 123.07 rule 3(1)).

## Section 6: Profit and Loss Layout

The Companies Act prescribes no general format for a small company's profit and loss account; the layout follows the framework (see `malta-financial-statements`). An illustrative GAPSME layout:

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

## Section 7: Balance Sheet Layout

Illustrative:

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
CURRENT LIABILITIES
  Trade and other payables                       xxx
  Current tax liabilities                        xxx
  Borrowings (current portion)                   xxx
                                                -----
TOTAL EQUITY AND LIABILITIES                     xxx
```

## Section 8: Bank Reconciliation Patterns

Statement layouts differ by bank and change over time. Map the columns from the client's own export before importing.

| Pattern in description | Likely classification |
| --- | --- |
| Incoming transfer | Check whether it is revenue, a loan, capital or a refund |
| Direct debit or standing order | Utility, subscription, insurance, rent or loan repayment |
| Card payment | Expense; check the merchant and the receipt |
| Bank charges | 6220 |
| Utility company | 6020 |
| MTCA (tax, VAT, SSC) payment | Balance sheet (2140 to 2170, 1250), never a P&L expense |
| Own-account transfer | Exclude |

## Section 9: Size Tests (summary)

Two separate tests apply. The detail and the two-year rules are in `malta-financial-statements`.

| Test | Balance sheet total | Turnover | Employees | Effect | Source |
| --- | --- | --- | --- | --- | --- |
| GAPSME small entity | EUR 4,000,000 | EUR 8,000,000 | 50 | Balance sheet, income statement, notes | S.L. 281.05 reg. 5(1)(a) |
| GAPSME medium-sized entity | EUR 20,000,000 | EUR 40,000,000 | 250 | Adds statement of changes in equity and cash flow statement | S.L. 281.05 reg. 5(1)(b) |
| Companies Act small company, new limits (in force 20 March 2026) | EUR 5,000,000 | EUR 10,000,000 | 50 | No directors' report | Cap. 386 art. 185(1), as substituted by Act I of 2026 art. 26; L.N. 61 of 2026 |
| Companies Act small company, previous limits | EUR 4,000,000 | EUR 8,000,000 | 50 | No directors' report | Cap. 386 art. 185(1) before Act I of 2026 |
| Companies Act micro, private companies only | EUR 46,600 | EUR 93,000 | 2 | No audit under the Act | Cap. 386 art. 185(2) |

A limit is met when the entity does not exceed at least two of the three. Every company not micro-exempt is audited. A self-employed person files no GAPSME accounts but keeps the article 19 records.

## Section 10: Interaction with Tax Skills

| Skill | How the books feed it |
| --- | --- |
| `malta-income-tax` | Net profit, add back depreciation (6500), provisions (6610), fines (6710) and private shares; deduct S.L. 123.01 wear and tear. Class 2 (6120) is a memo item |
| `mt-corporate-tax` | Profit before tax to chargeable income; allocation of profits to the tax accounts; dividends (3400) and refunds |
| `mt-estimated-tax` | Provisional tax paid (1250) is credited against the final tax |
| `malta-vat-return` | 1240, 2140 and 2150 tie to each return; keep the capital goods list |
| `malta-payroll` | 6100, 6110 and 2165 tie to the FSS returns |

## Section 11: Worked Examples

### Example 1: laptop, accounting depreciation against tax wear and tear

A company with a 31 December year end buys a laptop for EUR 1,600 (net of recoverable VAT) on 1 October 2026. Its policy depreciates computers over 3 years from the month of purchase.

- Accounting depreciation for 2026: 1,600 ÷ 3 × 3 ÷ 12 = EUR 133.33.
- Tax wear and tear for 2026: 1,600 ÷ 4 = EUR 400, a full year under S.L. 123.01 rule 7(a).
- Tax adjustment: add back EUR 133.33 and deduct EUR 400, a net reduction of EUR 266.67 in chargeable income.

```oa-check
name: Laptop bought 1 October 2026, depreciation against wear and tear
inputs:
  cost: 1600
  accounting_years: 3
  months_owned: 3
  tax_years: 4
steps:
  - accounting_depreciation: round(cost / accounting_years * months_owned / 12, 2)
  - wear_and_tear: cost / tax_years
  - net_reduction: wear_and_tear - accounting_depreciation
expected:
  accounting_depreciation: 133.33
  wear_and_tear: 400
  net_reduction: 266.67
```

### Example 2: recording an Article 10 sale and a capital good purchase

An Article 10 registrant invoices EUR 2,360 including 18% VAT and buys a printer-copier for EUR 1,416 including 18% VAT.

- Sale: 2,360 ÷ 1.18 = EUR 2,000 to 4000; EUR 360 to 2140.
- Purchase: 1,416 ÷ 1.18 = EUR 1,200 to 1150; EUR 216 to 1240.
- The printer costs at least EUR 1,160 whether or not VAT is counted, so it goes on the VAT capital goods list (S.L. 406.12). It is "other machinery" for tax: minimum 5 years, EUR 240 wear and tear in 2026.
- Net VAT for these two lines: 360 − 216 = EUR 144 payable.

```oa-check
name: Article 10 sale and capital good purchase at 18%
inputs:
  sale_gross: 2360
  purchase_gross: 1416
  rate: 0.18
steps:
  - sale_net: sale_gross / (1 + rate)
  - output_vat: sale_gross - sale_net
  - purchase_net: purchase_gross / (1 + rate)
  - input_vat: purchase_gross - purchase_net
  - net_vat_payable: output_vat - input_vat
  - wear_and_tear: purchase_net / 5
expected:
  sale_net: 2000
  output_vat: 360
  purchase_net: 1200
  input_vat: 216
  net_vat_payable: 144
  wear_and_tear: 240
```

## Section 12: Ask the Client First

1. Company or self-employed? If a company, its accounting reference date and whether the board chose IFRS.
2. VAT registration: Article 10, 11 or 12?
3. Any cars, and their cost or listed price and business use?
4. Does anyone use business assets or premises privately?
5. Payroll: are all wages run through FSS?
6. Which bank exports are available, and in what format?

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act, Cap. 386 (arts. 163, 164, 185, 187) | https://legislation.mt/eli/cap/386/eng/pdf | 2026-10-23 |
| Income Tax Management Act, Cap. 372 (art. 19) | https://legislation.mt/eli/cap/372/eng/pdf | 2026-10-23 |
| Income Tax Act, Cap. 123 (arts. 14, 24, 26) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-10-23 |
| Deduction for Wear and Tear of Plant and Machinery Rules, S.L. 123.01 | https://legislation.mt/eli/sl/123.1/eng/pdf | 2026-10-23 |
| Income Tax (Deductions) Rules, S.L. 123.07 | https://legislation.mt/eli/sl/123.7/eng/pdf | 2026-10-23 |
| Accountancy Profession (GAPSME) Regulations, S.L. 281.05 (regs. 4, 5) | https://legislation.mt/eli/sl/281.5/eng/pdf | 2026-10-23 |
| Commencement Notice, L.N. 61 of 2026 (Act I of 2026 arts. 17, 26 to 29, 31, 41, 42 in force 20 March 2026) | https://legislation.mt/eli/ln/2026/61/eng | 2026-10-24 |
| MBR, Informative note: entry into force of legislation (L.N. 61 of 2026) | https://www.mbr.mt/post/informative-note-entry-into-force-of-legislation-1 | 2026-10-24 |
| VAT Act, Cap. 406 (arts. 19, 48) | https://legislation.mt/eli/cap/406/eng/pdf | 2026-10-23 |
| VAT (Adjustments relating to Input Tax on Capital Goods) Regulations, S.L. 406.12 | https://legislation.mt/eli/sl/406.12/eng/pdf | 2026-10-23 |

Not yet confirmed:
- Whether Class 2 social security contributions are deductible on the 2026 return.
- Whether the VAT capital goods threshold of EUR 1,160 is tested with or without VAT (see `malta-vat-return`).
- Which accounts use the new article 185(1) limits. L.N. 61 of 2026 brought article 26 of Act I of 2026 into force on 20 March 2026 with no transitional rule. MBR's informative note on L.N. 61 says the new limits are mandatory for financial reporting periods starting on or after 20 March 2026 and bars early or retroactive use; on that reading a 31 December 2026 year end still uses the previous limits. `malta-financial-statements` reads it by balance sheet date instead.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
