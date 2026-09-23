---
name: uk-bookkeeping
description: Use this skill whenever asked about UK bookkeeping for sole traders, micro-entities, or small companies. Trigger on phrases like "chart of accounts", "nominal codes", "bookkeeping", "profit and loss", "balance sheet", "FRS 105", "FRS 102 Section 1A", "Making Tax Digital", "MTD", "MTD ITSA bookkeeping", "April 2026 quarterly", "VAT threshold £90,000", "bank reconciliation", "double-entry", "expense categories", "revenue recognition", "depreciation", "capital allowances", "micro-entity accounts", "small company accounts", "accrual basis", "cash basis", "general ledger", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a UK business.
version: 1.1
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bookkeeping in the UK for sole traders, micro-entities and small companies

How a UK business keeps its books, from records and cash basis to Making Tax Digital, VAT, capital allowances, the chart of accounts and the accounts layouts. Figures are for tax year 2026. In the UK that is 6 April 2026 to 5 April 2027 ("2026 to 2027"). VAT and company size figures apply from a stated date until replaced. The SA103F box numbers come from the notes for the 2025 to 2026 return, the latest published, and the FRS 105 wording from the current September 2024 edition, whose Periodic Review 2024 amendments apply to accounting periods beginning on or after 1 January 2026.

## UK Bookkeeping Guide v1.1

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | United Kingdom (England, Wales, Scotland, Northern Ireland) |
| Financial year | Companies choose their year end. Sole traders and partnerships are taxed on the tax year, 6 April to 5 April, but may draw accounts to any date; profits are then apportioned to the tax year |
| Accounting standards | FRS 105 (micro-entities), FRS 102 Section 1A (small), full FRS 102. Set by the Financial Reporting Council |
| Tax authority | HM Revenue and Customs (HMRC) |
| Key legislation | Companies Act 2006 (sections 382 and 384A, size); Small Companies and Groups (Accounts and Directors' Report) Regulations 2008; Taxes Management Act 1970 |
| MTD for VAT | All VAT-registered businesses, whatever their turnover, unless HMRC accepts an exemption (Section 10) |

### 3-Year Thresholds at a Glance

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/how-vat-works/vat-thresholds |
| VAT registration: taxable turnover over the last 12 months above this, or expected to pass it in the next 30 days. A cliff | GBP 90,000 | "Total taxable turnover More than £90,000 Register for VAT" |
| VAT deregistration: a registered business may cancel below this. Optional | GBP 88,000 | "Less than £88,000 Cancel VAT registration" |

The 12 month and 30 day tests: https://www.gov.uk/register-for-vat.

**Making Tax Digital for Income Tax: qualifying income over the amount in the year shown**

| Tax year tested | Value | Must use MTD from | Note |
| --- | --- | --- | --- |
| Source | all figures below | | https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax |
| 2024 to 2025 | GBP 50,000 | 6 April 2026 | "£50,000 for the 2024 to 2025 tax year" |
| 2025 to 2026 | GBP 30,000 | 6 April 2027 | "£30,000 for the 2025 to 2026 tax year" |
| 2026 to 2027 | GBP 20,000 | 6 April 2028 | "£20,000 for the 2026 to 2027 tax year" |

Qualifying income is self-employment and property income before expenses (turnover), from the return for the tested year. Employment, a partnership share, dividends and pensions do not count: https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax.

### Section 1A: Record keeping

| Who | Keep records for | Note |
| --- | --- | --- |
| Source | sole traders and partners | https://www.gov.uk/self-employed-records/how-long-to-keep-your-records |
| Sole traders and partners | At least 5 years after the 31 January submission deadline of the tax year | "at least 5 years after the 31 January submission deadline" |
| Source | companies | https://www.gov.uk/running-a-limited-company/company-and-accounting-records |
| Limited companies | 6 years from the end of the last company financial year they relate to, or longer (a transaction spanning periods, an asset expected to last more than 6 years, a late return, an open compliance check) | "You must keep records for 6 years from the end of the last company financial year" |
| Source | all figures below | https://www.legislation.gov.uk/ukpga/1970/9/section/12B |
| Failure to keep records for a tax return: maximum penalty, not a fixed charge | GBP 3,000 | "a penalty not exceeding £3,000." |

## Section 2: Standard Chart of Accounts (Nominal Codes)

This chart is our own working convention, not an official list. HMRC and Companies House prescribe no nominal codes, and each software package ships its own. The ranges were not checked against any vendor's list. Map them to the client's software.

### Assets (0001-1999)


| Code | Account | Type |
| --- | --- | --- |
| 0010 | Freehold Property | Non-current asset |
| 0020 | Leasehold Property | Non-current asset |
| 0030 | Plant and Machinery | Non-current asset |
| 0040 | Furniture and Fittings | Non-current asset |
| 0050 | Motor Vehicles | Non-current asset |
| 0060 | Office Equipment | Non-current asset |
| 0070 | Computer Equipment | Non-current asset |
| 0011 to 0071 | Accumulated Depreciation (paired) | Contra asset |
| 1001 | Stock / Inventory | Current asset |
| 1100 | Trade Debtors (Accounts Receivable) | Current asset |
| 1101 | Other Debtors | Current asset |
| 1102 | Prepayments | Current asset |
| 1200 | Bank Current Account | Current asset |
| 1210 | Bank Deposit Account | Current asset |
| 1220 | Building Society Account | Current asset |
| 1230 | Petty Cash | Current asset |
| 1240 | PayPal / Stripe Account | Current asset |

### Liabilities (2000-2999)


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
| 2300 | Bank Loan (due within one year) | Current liability |
| 2310 | HP / Finance Lease (due within one year) | Current liability |
| 2400 | Bank Loan (due after one year) | Non-current liability |
| 2410 | Director's Loan Account | Liability (current or non-current, by terms) |
| 2500 | Hire Purchase (due after one year) | Non-current liability |

### Equity (3000-3999)


| Code | Account | Type |
| --- | --- | --- |
| 3000 | Share Capital (Ordinary) | Equity |
| 3001 | Share Premium | Equity |
| 3100 | Retained Earnings | Equity |
| 3200 | Dividends Paid | Equity |
| 3300 | Owner's Capital Introduced (sole trader) | Equity |
| 3301 | Owner's Drawings (sole trader) | Equity |

### Revenue (4000-4999)

The VAT rates in the names are those in the VAT rates table in Section 10.

| Code | Account | Type |
| --- | --- | --- |
| 4000 | Sales: Standard Rate (20% VAT) | Revenue |
| 4001 | Sales: Reduced Rate (5% VAT) | Revenue |
| 4002 | Sales: Zero Rate (0% VAT) | Revenue |
| 4003 | Sales: Exempt | Revenue |
| 4004 | Sales: Exports (outside UK) | Revenue |
| 4100 | Other Operating Income | Revenue |
| 4200 | Discount Allowed | Contra revenue |

### Cost of Goods Sold (5000-5999)


| Code | Account | Type |
| --- | --- | --- |
| 5000 | Purchases: Goods for Resale | COGS |
| 5001 | Purchases: Materials | COGS |
| 5100 | Carriage Inward | COGS |
| 5200 | Direct Labour / Subcontractor Costs | COGS |
| 5300 | Stock Adjustments | COGS |

### Operating Expenses (6000-6999)


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
| 6310 | Motor Expenses: Fuel | Overhead |
| 6311 | Motor Expenses: Insurance | Overhead |
| 6312 | Motor Expenses: Repairs | Overhead |
| 6400 | Accountancy Fees | Overhead |
| 6410 | Legal Fees | Overhead |
| 6420 | Bank Charges and Interest | Overhead |
| 6430 | Bad Debts Written Off | Overhead |
| 6500 | Entertaining (client entertaining is not deductible for tax) | Overhead |
| 6510 | Staff Welfare | Overhead |
| 6600 | Sundry Expenses | Overhead |

### Other Income / Expenses (7000-7999)


| Code | Account | Type |
| --- | --- | --- |
| 7000 | Interest Received | Other income |
| 7010 | Rental Income | Other income |
| 7100 | Profit/Loss on Disposal of Assets | Other income/expense |
| 7200 | Grants Received | Other income |

### Depreciation and Tax (8000-8999)


| Code | Account | Type |
| --- | --- | --- |
| 8000 | Depreciation: Property | Expense |
| 8010 | Depreciation: Plant and Machinery | Expense |
| 8020 | Depreciation: Fixtures and Fittings | Expense |
| 8030 | Depreciation: Motor Vehicles | Expense |
| 8040 | Depreciation: Computer Equipment | Expense |
| 8100 | Corporation Tax Charge | Tax expense |
| 8200 | Dividends Receivable | Other income |

## Section 3: Revenue Recognition

### Cash Basis vs Accruals Basis

Since 2024 to 2025, cash basis is the standard method for sole traders and partnerships without corporate partners, with no turnover limit. Traditional (accruals) accounting is the opt-out, declared on the tax return: https://www.gov.uk/simpler-income-tax-cash-basis.

| Criterion | Cash basis | Traditional accounting |
| --- | --- | --- |
| Who | Sole traders and partnerships without corporate partners. Not companies, LLPs, partnerships with a corporate partner, or listed trades such as Lloyd's underwriters and farmers with a herd basis election: https://www.gov.uk/simpler-income-tax-cash-basis/who-can-use-cash-basis | Anyone. Companies and LLPs must |
| Income | When money is received | When invoiced or earned |
| Expenses | When the bill is paid | When billed or incurred |
| Debtors, creditors, stock | Not used | Required |
| Capital items | An allowable expense, except cars, land and the other exclusions in BIM72035: https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim72035. Capital allowances only on cars | Capitalised and depreciated; capital allowances for tax |
| Interest and losses | The old interest cap and loss restrictions were removed from 2024 to 2025: https://www.gov.uk/government/publications/expanding-the-cash-basis/expanding-the-cash-basis | No special restriction |

### Companies Act Recognition

- **Revenue under FRS 105.** For accounting periods beginning on or after 1 January 2026, Section 18 Revenue from Contracts with Customers applies: identify the contract with the customer, identify the performance obligations in it, determine the transaction price, allocate that price to the obligations, and recognise revenue as each obligation is satisfied. The older wording about risks and rewards passing and stage of completion is not in the current edition. The same Periodic Review 2024 amendments changed FRS 102, so read the current FRS 102 edition before applying older wording to a small company. Standards: https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-105/.

## Section 4: Expense Classification

### HMRC Self-Assessment Categories (SA103)

Boxes from the SA103F notes for 2025 to 2026, the latest published; recheck when the 2026 to 2027 notes appear: https://www.gov.uk/government/publications/self-assessment-self-employment-full-sa103f. MTD quarterly updates use the same categories. Box 27 is for traditional accounting only.

| SA103F box | Category | Our codes |
| --- | --- | --- |
| Box 17 | Cost of goods bought for resale or goods used | 5000 to 5300 |
| Box 18 | Construction industry: payments to subcontractors | 5200 |
| Box 19 | Wages, salaries and other staff costs | 6100 to 6120 |
| Box 20 | Car, van and travel expenses | 6300 to 6312 |
| Box 21 | Rent, rates, power and insurance costs | 6000 to 6020 |
| Box 22 | Repairs and maintenance of property and equipment | 6030 |
| Box 23 | Phone, fax, stationery and other office costs | 6210 to 6230 |
| Box 24 | Advertising and business entertainment costs | 6200, 6500 |
| Box 25 | Interest on bank and other loans | 6420 (interest) |
| Box 26 | Bank, credit card and other financial charges | 6420 (charges) |
| Box 27 | Irrecoverable debts written off | 6430 |
| Box 28 | Accountancy, legal and other professional fees | 6400 to 6410 |
| Box 29 | Depreciation and loss or profit on sale of assets | 8000 to 8040 |
| Box 30 | Other business expenses | 6600 |
| Box 31 | Total expenses | Sum |

### Non-Deductible Expenses (UK Tax)

- Common add-backs: client entertaining; personal costs not wholly and exclusively for the trade; fines and penalties; capital spending (capital allowances instead, except under cash basis); general provisions (only specific bad debts are allowable). Tax paid to HMRC is not a P&L expense. Not re-read in HMRC's manuals.

### Simplified expenses (flat rates)

Optional flat rates for vehicles, working from home and living at the premises. For sole traders and partnerships with no company partners; not for limited companies: https://www.gov.uk/simpler-income-tax-simplified-expenses. No flat rate for a vehicle already given capital allowances.

| Item | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/vehicles |
| Car or goods vehicle, first 10,000 business miles | 55p per mile | "first 10,000 miles 55p" |
| Car or goods vehicle, after 10,000 miles | 25p per mile | "after 10,000 miles 25p" |
| Motorcycle | 24p per mile | "Motorcycles 24p" |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/working-from-home |
| Home, 25 to 50 business hours in the month | GBP 10 a month | "25 to 50 £10" |
| Home, 51 to 100 hours | GBP 18 a month | "51 to 100 £18" |
| Home, 101 hours and more | GBP 26 a month | "101 and more £26" |
| Source | all figures below | https://www.gov.uk/simpler-income-tax-simplified-expenses/living-at-your-business-premises |
| Living at the premises, 1 person: SUBTRACTED from premises costs for private use | GBP 350 a month | "1 £350" |
| 2 people | GBP 500 a month | "2 £500" |
| 3 or more | GBP 650 a month | "3+ £650" |

### Trading and property allowances

| Allowance | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income |
| Trading allowance, per individual per tax year, against gross trading income | GBP 1,000 | "up to £1,000 each tax year in tax-free allowances" |
| Property allowance, a separate one against gross property income | GBP 1,000 | "you’ll get a £1,000 allowance for each" |

Gross income at or below the allowance is fully relieved. Above it, the allowance replaces actual expenses (never both) and cannot create a loss. Joint property owners each get one against their share. Not for a partnership share, or for income from a company or partnership you or a connected person controls, or from your or your spouse's employer. The property allowance cannot be combined with the finance cost reducer or Rent a Room.

## Section 5: Asset vs Expense Thresholds

### Capital Allowances (Not Accounting Depreciation)

Tax adds back depreciation and gives capital allowances instead.

| Allowance | Rate or amount | Who and what | Note |
| --- | --- | --- | --- |
| Source | all figures below | | https://www.gov.uk/capital-allowances/annual-investment-allowance |
| Annual Investment Allowance (AIA), yearly limit | GBP 1 million | Sole traders, partnerships, companies. Most plant and machinery, not cars | "The AIA amount is £1 million." |
| Source | all figures below | | https://www.gov.uk/capital-allowances/full-expensing |
| Full expensing, new main-rate plant bought from 1 April 2023 | 100% | Companies only. Not cars | "Full expensing lets you deduct 100% of the cost" |
| First-year allowance, new special-rate plant from 1 April 2023 | 50% | Companies only. Not cars | "The 50% first-year allowance lets you deduct 50%" |
| Source | all figures below | | https://www.gov.uk/capital-allowances/40-first-year-allowance |
| First-year allowance: bought on or after 1 January 2026, new and unused, main rate, not a car | 40% | Open to anyone charged to corporation tax or income tax, and to mixed partnerships. The general exclusions still apply, and it is refused under disqualifying arrangements | "you can deduct 40% of the cost" |
| Source | all figures below | | https://www.gov.uk/work-out-capital-allowances/rates-and-pools |
| Main pool writing down allowance from 1 April 2026 (corporation tax) and 6 April 2026 (income tax) | 14% | Reducing balance. A period spanning the change uses a hybrid rate | "main pool with a rate of 14% from April 2026, and 18% before" |
| Main pool rate before those dates | 18% | Earlier periods | "changed from 18% to 14%" |
| Special rate pool | 6% | Integral features, long-life assets, higher-emission cars | "special rate pool with a rate of 6%" |
| Source | all figures below | | https://www.gov.uk/work-out-capital-allowances/work-out-what-you-can-claim |
| Small pools allowance: write off a pool balance at or below this. Not single asset pools | GBP 1,000 | Main or special rate pool | "rate pool is £1,000 or less" |
| Source | all figures below | | https://www.gov.uk/capital-allowances/business-cars |
| Car bought from April 2021, new, 0g/km or electric | 100% | First-year allowance | "(or car is electric) 100% first-year allowances" |
| Second hand electric car, or 50g/km or less | 14% | Main rate allowances | "14% (or 18% before April 2026)" |
| Car over 50g/km | 6% | Special rate allowances | "6% of the car’s value each year" |

Cars never get AIA, full expensing or the 40% allowance.

The conditions and the exclusions for the 40% allowance are set out at https://www.gov.uk/hmrc-internal-manuals/capital-allowances-manual/ca23195a.

### Accounting Depreciation (Book Purposes)

Depreciate each asset over its useful economic life, on a method that matches how it is used up. No official page sets rates, so the firm documents a policy per class: land is not depreciated, leasehold improvements go over the lease term or shorter life, and plant, fixtures, vehicles and computers follow the firm's policy (straight-line or reducing balance).

### Low-Value Items

- UK GAAP sets no statutory de minimis. The firm sets, documents and applies its own capitalisation limit.

## Section 6: Profit & Loss Format

### FRS 105 Micro-Entity Format (Format 2: by nature)

Items as in the micro-entity format, Schedule 1 Section C of the 2008 Regulations: https://www.legislation.gov.uk/uksi/2008/409/schedule/1.

~~~
PROFIT AND LOSS ACCOUNT
                                    This Year (GBP)  Prior Year (GBP)
Turnover                                xxx              xxx
Other income                            xxx              xxx
Cost of raw materials and consumables  (xxx)            (xxx)
Staff costs                            (xxx)            (xxx)
Depreciation and other amounts
  written off assets                   (xxx)            (xxx)
Other charges                          (xxx)            (xxx)
Tax                                    (xxx)            (xxx)
Profit or loss                          xxx              xxx
~~~

### FRS 102 Section 1A Small Company (Format 1: by function)

~~~
PROFIT AND LOSS ACCOUNT
Turnover                                xxx
Cost of sales                          (xxx)
Gross profit                            xxx
Distribution costs                     (xxx)
Administrative expenses                (xxx)
Other operating income                  xxx
Operating profit                        xxx
Interest receivable                     xxx
Interest payable                       (xxx)
Profit before tax                       xxx
Tax on profit                          (xxx)
Profit for the financial year           xxx
~~~

## Section 7: Balance Sheet Format

### FRS 105 / Small Company Balance Sheet (Vertical Format)

~~~
BALANCE SHEET as at year end date
                                        GBP         GBP
FIXED ASSETS
Intangible assets                                  xxx
Tangible assets                                    xxx
CURRENT ASSETS
Stocks                              xxx
Debtors                             xxx
Cash at bank and in hand            xxx
CREDITORS: amounts falling
  due within one year              (xxx)
NET CURRENT ASSETS                                 xxx
TOTAL ASSETS LESS CURRENT LIABILITIES              xxx
CREDITORS: amounts falling
  due after more than one year                    (xxx)
PROVISIONS FOR LIABILITIES                        (xxx)
NET ASSETS                                         xxx
CAPITAL AND RESERVES
Called up share capital                            xxx
Profit and loss account                            xxx
SHAREHOLDERS' FUNDS                                xxx
~~~

This is the small company layout. A micro-entity may use the shorter balance sheet in Schedule 1 Section C. A bought intangible asset still appears; an internally generated one does not, because FRS 105 charges that spending to profit or loss.

## Section 8: Bank Reconciliation Patterns

### Common UK Bank Formats

These export layouts are from practice and were not checked against the banks' own pages. Confirm them against a real export.

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

| Pattern | Likely Classification |
| --- | --- |
| FPO / FPI (Faster Payment Out/In) | Transfer: check counterparty |
| DD (Direct Debit) | Regular expense (insurance, utility, subscription) |
| STO (Standing Order) | Regular expense (rent, loan repayment) |
| BGC (Bank Giro Credit) | Income: customer payment |
| CHQ (Cheque) | Varies: check payee |
| DEB / VIS / MC (Card Payment) | Expense: check merchant |
| HMRC VAT, HMRC PAYE, HMRC CT | Tax payment: post to the liability account, not to P&L expenses |
| STRIPE, PAYPAL, GOCARDLESS | Payment processor: match to invoices, book fees separately |
| TFR (Transfer) | Internal: possible own-account transfer |

## Section 9: Micro-Entity / Small Business Simplifications

### FRS 105 Simplifications (Micro-Entities)

| Feature | Simplification |
| --- | --- |
| Source | https://www.frc.org.uk/library/standards-codes-policy/accounting-and-reporting/uk-accounting-standards/frs-105/ |
| Standards | FRS 105 (micro-entities); FRS 102 (others, Section 1A for small) |
| Statements | Balance sheet and P&L with limited notes; no cash flow statement |
| Revaluation | Company law prohibits it for micro-entities; historical cost only |
| Deferred tax | Never recognised: "A micro-entity shall not recognise deferred tax" (24.7) |
| Intangible assets | A separately bought intangible asset is recognised. An internally generated one never is: the spending goes to profit or loss. In a business combination they are not separately identified, so they fall into goodwill |
| Leases | Finance or operating, not all operating: "A lease is classified as a finance lease if it transfers substantially all the risks and rewards incidental to ownership" (15.5) |
| Filing | Small companies and micro-entities may file without the P&L. From 1 April 2028 a micro-entity must deliver its P&L but may opt out of publishing it: https://www.gov.uk/government/publications/life-of-a-company-annual-requirements/life-of-a-company-part-1-accounts |
| Audit | A micro-entity claims audit exemption as a small company. It is not available to a public company, a bank or e-money issuer, an insurer or insurance market business, a MiFID or UCITS firm, or a company in a group that is not small or is ineligible; members holding enough shares can also require an audit (section 11 of the Companies House page above) |

### Qualifying Thresholds (from 6 April 2025)

Micro or small means meeting at least two of the three conditions, for financial years beginning on or after 6 April 2025. After the first year, a change counts only if it happens in two consecutive financial years. Public companies, charities and some others cannot use micro-entity accounts (section 9.2 of the Companies House page above).

| Condition | Not more than | Note |
| --- | --- | --- |
| Source | micro-entity, all figures below | https://www.legislation.gov.uk/ukpga/2006/46/section/384A |
| Turnover | GBP 1 million | "Turnover [ F2 Not more than £1 million ]" |
| Balance sheet total | GBP 500,000 | "Balance sheet total [ F3 Not more than £500,000 ]" |
| Average employees | 10 employees | "Number of employees Not more than 10" |
| Source | small company, all figures below | https://www.legislation.gov.uk/ukpga/2006/46/section/382 |
| Turnover | GBP 15 million | "Turnover [ F3 Not more than £15 million ]" |
| Balance sheet total | GBP 7.5 million | "Balance sheet total [ F4 Not more than £7.5 million ]" |
| Average employees | 50 employees | "Number of employees Not more than 50" |

Audit exemption follows the small company test: https://www.legislation.gov.uk/ukpga/2006/46/section/477.

### Cash Basis for Sole Traders

- See Section 3: the default, no turnover limit.

### MTD ITSA: From 6 April 2026

- **Who.** Sole traders and landlords in Self Assessment whose qualifying income passed the threshold in the Section 1 table.
- **What.** Digital records in compatible software, and quarterly updates of totals per category, with no accounting adjustments needed. A tax return is still filed after the year end.
- **Deadlines.** 7 August, 7 November, 7 February and 7 May. A business may use standard update periods, which follow the tax year, or calendar update periods ending on the last day of the month; the deadlines are the same either way: https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates.
- **Penalties.** No penalties for missing a quarterly update deadline for 2026 to 2027. But digital records and quarterly updates are still needed before the return can be submitted, and late return and late payment penalties still apply. Points-based penalties follow in later years: https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax.
- **Accounts to another date.** Profit is apportioned to the tax year. A trader who changed over is still spreading transition profit, up to the tax year 2027 to 2028: https://www.gov.uk/guidance/changes-to-reporting-income-from-self-employment-and-partnerships.

## Section 10: Interaction with the other UK Guides

### Income Tax (Self-Assessment SA103/SA105)

- The P&L feeds the self-employment (SA103) or property (SA105) pages, or the MTD updates. Add back entertaining, depreciation and private use. Deduct capital allowances (cash basis: cars only).

### Corporation Tax (CT600)

- Start from FRS 105 or FRS 102 profit. Add back depreciation, client entertaining and general provisions. Deduct capital allowances (Section 5) and any research and development relief. Connected party transactions: refer.

### VAT Return (Making Tax Digital)

Making Tax Digital for VAT requires all VAT-registered businesses to keep records digitally and file returns using software, with digital links between programs. HMRC may accept an exemption where it is not practical to use digital tools, for reasons such as age, disability or location, where the business is in an insolvency procedure, where it is run entirely by practising members of a religious society whose beliefs are incompatible with electronic records, or where the business is already exempt from filing VAT returns online: https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat. Reconcile the VAT control account to each return and check the VAT scheme.

| Rate | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.uk/vat-rates |
| Standard | 20% | "Standard rate 20%" |
| Reduced | 5% | "Reduced rate 5%" |
| Zero | 0% | "Zero rate 0%" |

Box wording from VAT Notice 700/12: https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012.

| VAT Return box | Description | Our codes |
| --- | --- | --- |
| Box 1 | VAT due on sales and other outputs | 2202 |
| Box 2 | VAT due on acquisitions of goods made in Northern Ireland from EU member states | 2202 |
| Box 3 | Total VAT due (Box 1 plus Box 2) | Calculated |
| Box 4 | VAT reclaimed on purchases and other inputs | 2201 |
| Box 5 | Net VAT to pay or reclaim | 2200 |
| Box 6 | Total sales and other outputs excluding VAT | 4000 to 4004 |
| Box 7 | Total purchases and other inputs excluding VAT | 5000 to 5300, 6000 to 6600 |
| Box 8 | Supplies of goods from Northern Ireland to EU member states | 4004 (subset) |
| Box 9 | Acquisitions of goods from EU member states into Northern Ireland | 5000 (subset) |

Boxes 2, 8 and 9 are for goods moving between Northern Ireland and the EU only.

### Payroll (RTI: Real Time Information)

- Send a Full Payment Submission on or before each payday, and an Employer Payment Summary to claim reductions such as statutory pay: https://www.gov.uk/running-payroll/reporting-to-hmrc. Workplace pension duties: https://www.thepensionsregulator.gov.uk/en/employers. Rates are in the UK payroll Guide. In our chart, 6100, 6110 and 6120 make up staff cost.

## The method, step by step

1. Identify the entity and the record period from Section 1A.
2. Choose the method. Unincorporated: cash basis unless traditional accounting is chosen, after checking the exclusions in Section 3. Companies: accruals.
3. Test Making Tax Digital for Income Tax on the Section 1 table.
4. Test VAT registration and, if registered, MTD for VAT, on the Section 1 table.
5. Set up the Section 2 chart in the client's software, mapped to the SA103F boxes or the accounts format.
6. Reconcile the bank monthly. At year end, work out capital allowances from Section 5.
7. For a company, test size under sections 382 and 384A (Section 9) and prepare FRS 105 or FRS 102 Section 1A accounts.

## Ask the client first

- Sole trader, partnership (any company partner?), LLP or company?
- Self-employment and property turnover, before expenses, on the last return?
- Taxable turnover in the last 12 months, and expected in the next 30 days? Already VAT registered, and on which scheme?
- Cash basis or traditional accounting? Flat-rate expenses or actual costs?
- Equipment or a car bought this year: when, new or used, and the car's CO2 emissions?
- Any employees, including directors?

## When to refuse or refer

- A partnership with a corporate partner, an LLP, a group, or a company near a size limit.
- An audit is needed or demanded.
- An MTD exemption request or a penalty dispute.
- Goods between Northern Ireland and the EU, or a special VAT scheme.
- Trades on the cash basis exclusion list.
- Connected party transactions, research and development claims, employment status.
- Never produce filing-ready accounts or returns without a qualified accountant's sign-off.

## Sources

- https://www.gov.uk/simpler-income-tax-cash-basis
- https://www.gov.uk/government/publications/expanding-the-cash-basis/expanding-the-cash-basis
- https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax
- https://www.gov.uk/register-for-vat
- https://www.gov.uk/simpler-income-tax-simplified-expenses
- https://www.legislation.gov.uk/uksi/2008/409/schedule/1
- https://www.gov.uk/hmrc-internal-manuals/capital-allowances-manual/ca23195a
- Every other page is linked in its table or step above.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant, ACCA member, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

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
