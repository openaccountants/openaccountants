---
name: canada-bookkeeping
description: Use this skill whenever asked about Canadian bookkeeping for sole proprietors, partnerships, or private corporations. Trigger on phrases like "chart of accounts", "GIFI codes", "bookkeeping", "profit and loss", "balance sheet", "ASPE", "ASNPO", "CRA categories", "bank reconciliation", "expense categories", "revenue recognition", "depreciation", "CCA", "capital cost allowance", "GST/HST", "input tax credits", "T2125", "T2", "general ledger", "HST return", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a Canadian business.
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Khushboo Talreja, CPA
review_status: current
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Canada Bookkeeping

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD ($) only |
| Financial year | Corporations: any year-end; Sole proprietors: calendar year (Jan 1 – Dec 31) |
| Accounting standards | ASPE (Part II — private enterprises); ASNPO (Part III — not-for-profits); IFRS (Part I — public) |
| Governing body | Accounting Standards Board (AcSB) of CPA Canada |
| Tax authority | Canada Revenue Agency (CRA) |
| Key legislation | Income Tax Act (ITA); Excise Tax Act (GST/HST); Canada Business Corporations Act |
| GST/HST registration threshold | $30,000 in four consecutive quarters (small supplier threshold) |
| Record keeping requirement | 6 years from end of the last tax year to which records relate |
| GIFI codes | General Index of Financial Information — CRA's standardized code system for T2 filing |

## Section 2 -- Standard Chart of Accounts

Canadian small businesses use 4-digit codes mapped to GIFI for T2/T2125 reporting.

### Assets (1000–1999)

**Assets (1000–1999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 1000 | Cash — Operating Account | 1001 | Current asset |
| 1010 | Cash — Savings Account | 1001 | Current asset |
| 1020 | Petty Cash | 1001 | Current asset |
| 1050 | Short-Term Investments | 1180 | Current asset |
| 1100 | Accounts Receivable | 1060 | Current asset |
| 1110 | Allowance for Doubtful Accounts | 1061 | Contra asset |
| 1150 | GST/HST Receivable (ITC) | 1066 | Current asset |
| 1200 | Inventory | 1120 | Current asset |
| 1210 | Prepaid Expenses | 1484 | Current asset |
| 1220 | Prepaid Insurance | 1484 | Current asset |
| 1300 | Land | 1600 | Non-current asset |
| 1310 | Buildings | 1680 | Non-current asset |
| 1311 | Accumulated Amortization — Buildings | 1681 | Contra asset |
| 1320 | Machinery and Equipment | 1740 | Non-current asset |
| 1321 | Accumulated Amortization — Equipment | 1741 | Contra asset |
| 1330 | Furniture and Fixtures | 1740 | Non-current asset |
| 1331 | Accumulated Amortization — Furniture | 1741 | Contra asset |
| 1340 | Computer Hardware | 1774 | Non-current asset |
| 1341 | Accumulated Amortization — Computer | 1775 | Contra asset |
| 1350 | Motor Vehicles | 1742 | Non-current asset |
| 1351 | Accumulated Amortization — Vehicles | 1743 | Contra asset |
| 1360 | Leasehold Improvements | 1918 | Non-current asset |
| 1361 | Accumulated Amortization — Leasehold | 1919 | Contra asset |
| 1400 | Intangible Assets (Software, Patents) | 2010 | Non-current asset |
| 1401 | Accumulated Amortization — Intangibles | 2011 | Contra asset |
| 1500 | Goodwill | 2012 | Non-current asset |

### Liabilities (2000–2999)

**Liabilities (2000–2999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 2000 | Accounts Payable | 2620 | Current liability |
| 2010 | Accrued Liabilities | 2620 | Current liability |
| 2050 | GST/HST Payable (Collected) | 2680 | Current liability |
| 2060 | GST/HST Net (Control) | 2680 | Current liability |
| 2100 | Income Tax Payable | 2680 | Current liability |
| 2110 | Payroll Liabilities — CPP | 2620 | Current liability |
| 2120 | Payroll Liabilities — EI | 2620 | Current liability |
| 2130 | Payroll Liabilities — Income Tax W/H | 2620 | Current liability |
| 2140 | Vacation Pay Payable | 2620 | Current liability |
| 2150 | Workers' Compensation Payable | 2620 | Current liability |
| 2200 | Credit Card Payable | 2707 | Current liability |
| 2300 | Current Portion of Long-Term Debt | 2920 | Current liability |
| 2400 | Bank Loan — Long-Term | 3140 | Non-current liability |
| 2410 | Mortgage Payable | 3141 | Non-current liability |
| 2500 | Shareholder Loan | 3260 | Non-current liability |
| 2600 | Deferred Revenue | 2770 | Current liability |

### Equity (3000–3999)

**Equity (3000–3999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 3000 | Share Capital (Common Shares) | 3500 | Equity |
| 3010 | Share Capital (Preferred) | 3520 | Equity |
| 3100 | Retained Earnings | 3600 | Equity |
| 3200 | Owner's Equity / Capital (sole prop) | 3500 | Equity |
| 3210 | Owner's Drawings | 3750 | Equity |
| 3220 | Owner's Contributions | 3500 | Equity |
| 3300 | Dividends Declared | 3700 | Equity |
| 3400 | Current Year Net Income/Loss | 3680 | Equity |

### Revenue (4000–4999)

**Revenue (4000–4999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 4000 | Sales Revenue — Taxable (GST/HST) | 8000 | Revenue |
| 4010 | Sales Revenue — Zero-Rated | 8000 | Revenue |
| 4020 | Sales Revenue — Exempt | 8000 | Revenue |
| 4100 | Service Revenue | 8000 | Revenue |
| 4200 | Professional Fees Earned | 8000 | Revenue |
| 4300 | Rental Income | 8140 | Revenue |
| 4400 | Interest and Investment Income | 8090 | Revenue |
| 4500 | Other Income | 8230 | Revenue |
| 4600 | Gain on Disposal of Assets | 8210 | Revenue |
| 4900 | Sales Returns and Allowances | 8000 | Contra revenue |
| 4910 | Sales Discounts | 8000 | Contra revenue |

### Cost of Goods Sold (5000–5999)

**Cost of Goods Sold (5000–5999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 5000 | Purchases — Merchandise | 8320 | COGS |
| 5010 | Purchases — Raw Materials | 8320 | COGS |
| 5020 | Freight-In / Shipping Costs | 8457 | COGS |
| 5030 | Direct Labour | 8340 | COGS |
| 5040 | Subcontractor Costs | 8360 | COGS |
| 5100 | Opening Inventory Adjustment | 8300 | COGS |
| 5110 | Closing Inventory Adjustment | 8500 | COGS |
| 5200 | Manufacturing Overhead | 8450 | COGS |

### Operating Expenses (6000–6999)

**Operating Expenses (6000–6999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 6000 | Rent | 8910 | Expense |
| 6010 | Property Tax | 9180 | Expense |
| 6020 | Utilities (Hydro, Gas, Water) | 9220 | Expense |
| 6030 | Insurance — Business | 8690 | Expense |
| 6040 | Repairs and Maintenance | 8960 | Expense |
| 6100 | Salaries and Wages | 9060 | Expense |
| 6110 | Employer CPP Contributions | 8622 | Expense |
| 6120 | Employer EI Premiums | 8622 | Expense |
| 6130 | Employee Benefits (Health, Dental) | 8620 | Expense |
| 6140 | Workers' Compensation | 8622 | Expense |
| 6200 | Advertising and Promotion | 8520 | Expense |
| 6210 | Meals and Entertainment (50% deductible) | 8523 | Expense |
| 6220 | Travel Expenses | 9200 | Expense |
| 6230 | Vehicle Expenses — Fuel | 9281 | Expense |
| 6240 | Vehicle Expenses — Insurance | 9281 | Expense |
| 6250 | Vehicle Expenses — Repairs | 9281 | Expense |
| 6260 | Vehicle Expenses — Lease Payments | 8915 | Expense |
| 6300 | Office Supplies and Expenses | 8810 | Expense |
| 6310 | Postage and Courier | 8810 | Expense |
| 6320 | Telephone and Internet | 9225 | Expense |
| 6330 | Software Subscriptions (SaaS) | 8810 | Expense |
| 6400 | Professional Fees — Accounting | 8860 | Expense |
| 6410 | Professional Fees — Legal | 8860 | Expense |
| 6420 | Professional Fees — Consulting | 8860 | Expense |
| 6500 | Bank Charges and Credit Card Fees | 8710 | Expense |
| 6510 | Interest Expense — Bank | 8710 | Expense |
| 6520 | Interest Expense — Other | 8710 | Expense |
| 6600 | Amortization (Book Depreciation) | 8670 | Expense |
| 6610 | Bad Debts | 8590 | Expense |
| 6700 | Business Tax and Licences | 8760 | Expense |
| 6800 | Miscellaneous / Sundry Expenses | 9270 | Expense |

### Other Income / Expenses (7000–7999)

**Other Income / Expenses (7000–7999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 7000 | Interest Income | 8090 | Other income |
| 7010 | Dividend Income | 8095 | Other income |
| 7100 | Loss on Disposal of Assets | 8210 | Other expense |
| 7200 | Foreign Exchange Gain/Loss | 8230 | Other income/expense |

### Tax (8000–8999)

**Tax (8000–8999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 8000 | Income Tax Expense (Current) | 9990 | Tax |
| 8010 | Deferred Income Tax | 9995 | Tax |

## Section 3 -- Revenue Recognition

### ASPE Section 3400 Revenue

- **Revenue recognition criteria** — Revenue is recognised when: Performance is achieved (goods delivered / services rendered); Collection is reasonably assured; Amount is measurable  _(ASPE Section 3400)_

**Revenue recognition by type**  _(ASPE Section 3400)_

| Revenue Type | Recognition Point |
| --- | --- |
| Sale of goods | Risks and rewards transferred, amount measurable, collection probable |
| Rendering of services | Percentage of completion, or completed contract if outcome uncertain |
| Interest income | Accrued over time on effective interest basis |
| Royalties | Accrued per agreement terms |
| Dividends | When right to receive established |
| Construction contracts | Percentage of completion (ASPE 3400) |

### Cash vs Accrual for Sole Proprietors

**Cash vs Accrual for Sole Proprietors**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Method | CRA Requirement |
| --- | --- |
| Accrual | Default for all businesses |
| Cash (modified) | Permitted for farming and fishing businesses only (ITA s.28) |
| Billed-basis | ELIMINATED — s.34 election repealed (Budget 2017) for tax years beginning after 22 Mar 2017; WIP included in income under s.10(5)(a) at lesser of cost and FMV |

Most sole proprietors must use the accrual method — income when invoiced/earned, expenses when incurred.

## Section 4 -- Expense Classification

### T2125 Categories (Statement of Business Activities)

**T2125 Categories (Statement of Business Activities)**

| Line | Category | Description | Nominal Codes |
| --- | --- | --- | --- |
| 8521 | Advertising | Marketing, advertising, signage | 6200 |
| 8523 | Meals and entertainment | 50% deductible for tax | 6210 |
| 8590 | Bad debts | Written-off uncollectable accounts | 6610 |
| 8690 | Insurance | Business insurance premiums | 6030 |
| 8710 | Interest and bank charges | Loan interest, service charges | 6500–6520 |
| 8760 | Business taxes, licences, dues, memberships | Professional dues, municipal permits | 6700 |
| 8764 | Motor vehicle expenses (not CCA) | Fuel, insurance, repairs, lease | 6230–6260 |
| 8810 | Office expenses | Supplies, stationery, postage | 6300–6330 |
| 8860 | Professional fees | Accounting, legal, consulting | 6400–6420 |
| 8871 | Management and admin fees | Fees paid to related parties | 6420 |
| 8910 | Rent | Business premises rent | 6000 |
| 8960 | Repairs and maintenance | Building/equipment repairs | 6040 |
| 9180 | Property taxes | Municipal/provincial property tax | 6010 |
| 9200 | Travel | Airfare, hotels, transport | 6220 |
| 9270 | Utilities | Electricity, gas, water, phone | 6020, 6320 |
| 9936 | Capital cost allowance (CCA) | Tax depreciation (not book) | See Section 5 |

### Non-Deductible Expenses (CRA)

- **Non-deductible items** — Personal expenses and owner's drawings; 50% of meals and entertainment (only 50% deductible); Club membership dues (golf, fitness) — Not deductible (ITA para 18(1)(l)); Political contributions — claim as federal/provincial tax credit instead; Fines and penalties imposed by law; Capital expenditures (must claim CCA); Life insurance premiums (unless collateral for loan); Accrued bonuses not paid within 180 days of year-end  _(CRA)_

## Section 5 -- Asset vs Expense Thresholds

### Capital Cost Allowance (CCA) — Key Classes

**Capital Cost Allowance (CCA) — Key Classes**

| Class | Rate | Method | Typical Assets |
| --- | --- | --- | --- |
| 1 | 4% | Declining balance | Commercial buildings (post-1987) |
| 1 (M&P) | 10% | Declining balance | Manufacturing buildings |
| 8 | 20% | Declining balance | Office furniture, equipment, tools ≥ $500 |
| 10 | 30% | Declining balance | Motor vehicles (cost ≤ $38,000 + tax in 2025) |
| 10.1 | 30% | Declining balance | Passenger vehicles > $38,000 limit (separate class per vehicle) |
| 12 | 100% | Full write-off | Small tools < $500, computer software (not systems) |
| 13 | Lease term | Straight-line | Leasehold improvements |
| 14.1 | 5% | Declining balance | Goodwill and other eligible capital property |
| 43 | 30% | Declining balance | Manufacturing and processing machinery (post-2025) |
| 50 | 55% | Declining balance | Computer hardware and systems software |
| 53 | 50% | Declining balance | M&P machinery (acquired 2016–2025) |
| 54 | 30% | Declining balance | Zero-emission passenger vehicles |
| 55 | 40% | Declining balance | Zero-emission non-passenger vehicles |

### Accelerated Investment Incentive (from 2025)

- **Accelerated Investment Incentive** — For eligible property acquired after 20 Nov 2018; enhanced first-year deduction phases out for property available for use after 2023 and is eliminated after 2027.  _(unsure)_

### Practical Thresholds

**Practical Thresholds**

| Threshold | Treatment |
| --- | --- |
| < $500 | Expense immediately (supplies); or Class 12 at 100% |
| $500 – above | Capitalize: Class 8 (20%) or appropriate class |
| Current expense test | Repair vs improvement — repairs maintain; improvements extend/enhance |

### Book Amortization vs Tax CCA

- **Book amortization vs CCA** — Book amortization (ASPE Section 3061) uses straight-line over useful life. CCA is a separate tax schedule. They rarely match — the difference creates a deferred tax timing difference.  _(ASPE Section 3061)_

## Section 6 -- P&L Format

### Income Statement (ASPE Multi-Step)

```
INCOME STATEMENT
For the year ended [date]
                                            $           $
Revenue                                               xxx
Cost of goods sold                                   (xxx)
                                                     ────
Gross profit                                          xxx

Operating expenses:
  Salaries and wages                      (xxx)
  Rent                                    (xxx)
  Advertising                             (xxx)
  Office expenses                         (xxx)
  Professional fees                       (xxx)
  Insurance                               (xxx)
  Utilities                               (xxx)
  Amortization                            (xxx)
  Vehicle expenses                        (xxx)
  Other operating expenses                (xxx)
                                                     (xxx)
                                                     ────
Operating income                                      xxx

Other income (expenses):
  Interest income                          xxx
  Interest expense                        (xxx)
  Gain (loss) on disposal of assets        xxx
  Foreign exchange gain (loss)             xxx
                                                      xxx
                                                     ────
Income before income taxes                            xxx
Provision for income taxes                           (xxx)
                                                     ────
Net income                                            xxx
                                                     ════
```

## Section 7 -- Balance Sheet Format

### Statement of Financial Position (ASPE — Vertical / Report Form)

```
BALANCE SHEET
As at [date]
                                            $           $
ASSETS
Current assets:
  Cash                                               xxx
  Accounts receivable                                xxx
  Allowance for doubtful accounts                   (xxx)
  Inventory                                          xxx
  Prepaid expenses                                   xxx
  GST/HST receivable                                 xxx
                                                     ────
Total current assets                                  xxx

Capital assets:
  Land                                    xxx
  Buildings (net of amortization)         xxx
  Equipment (net of amortization)         xxx
  Vehicles (net of amortization)          xxx
  Leasehold improvements (net)            xxx
  Computer hardware (net)                 xxx
                                                      xxx
Intangible assets (net)                               xxx
Goodwill (net)                                        xxx
                                                     ────
TOTAL ASSETS                                          xxx
                                                     ════

LIABILITIES
Current liabilities:
  Accounts payable                                   xxx
  Accrued liabilities                                xxx
  GST/HST payable                                    xxx
  Income taxes payable                               xxx
  Current portion of long-term debt                  xxx
  Deferred revenue                                   xxx
                                                     ────
Total current liabilities                             xxx

Long-term liabilities:
  Bank loan                                          xxx
  Mortgage payable                                   xxx
  Shareholder loan                                   xxx
                                                     ────
Total long-term liabilities                           xxx
                                                     ────
TOTAL LIABILITIES                                     xxx

SHAREHOLDERS' EQUITY
  Share capital                                      xxx
  Retained earnings                                  xxx
                                                     ────
TOTAL SHAREHOLDERS' EQUITY                            xxx
                                                     ────
TOTAL LIABILITIES AND EQUITY                          xxx
                                                     ════
```

## Section 8 -- Bank Reconciliation Patterns

### Common Canadian Bank Formats

**Common Canadian Bank Formats**

| Bank | Export Format | Key Fields |
| --- | --- | --- |
| RBC Royal Bank | CSV, OFX, QFX | Account Type, Date, Description 1, Description 2, CAD, USD |
| TD Canada Trust | CSV, OFX, QIF | Date, Transaction Description, Withdrawals, Deposits, Balance |
| BMO | CSV, OFX | Date, Description, Amount, Balance |
| Scotiabank | CSV, OFX | Date, Description, Debit, Credit, Balance |
| CIBC | CSV, QFX | Date, Description, Withdrawals, Deposits, Balance |
| Desjardins | CSV, OFX | Date, Description, Montant/Amount, Balance |
| National Bank | CSV | Date, Description, Debit, Credit, Balance |

### Common Transaction Descriptions

**Common Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| E-TRANSFER, INTERAC | Income or personal — check direction and counterparty |
| PAD (Pre-Authorized Debit) | Regular expense (insurance, loan, subscription) |
| PAP (Pre-Authorized Payment) | Regular expense (utility, rent) |
| POS, VISA, MC, DEBIT | Card expense — check merchant name |
| CRA FED TAX, CRA GST/HST | Tax payment — not operating expense |
| PAYROLL, ADP, CERIDIAN | Wages / payroll processing |
| SHOPIFY PAYOUT, STRIPE CA | Platform income — match to invoices |
| BILL PAYMENT, BPMT | Expense — utility or service provider |
| NSF FEE, SERVICE CHARGE | Bank charges (6500) |
| INTEREST | Income (if credit) or expense (if debit) |
| MORTGAGE PMT | Split: principal (2410 reduction) + interest (6510) |

## Section 9 -- Micro-Entity / Small Business Simplifications

### CRA Small Business Concessions

**CRA Small Business Concessions**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Concession | Eligibility | Detail |
| --- | --- | --- |
| Quick Method (GST/HST) | Taxable revenue ≤ $400,000 | Remit flat percentage of revenue; keep the difference |
| Instalment threshold | Tax owing < $3,000 (individuals; $1,800 for Québec residents) or < $3,000 (corporations) | No quarterly instalments required |
| Simplified ITC claims | Worldwide taxable supplies ≤ $1,000,000 AND taxable purchases in Canada ≤ $4,000,000 | Simplified METHOD for calculating ITCs; separate documentary thresholds apply to receipts |
| GIFI-Short | Revenue and assets each < $1 million | ~100 common codes instead of full GIFI list |
| T2 Short Return | Various small corporation criteria | Reduced filing requirements |
| Filing deadline | Sole prop: June 15 (return); April 30 (payment) | 2-month extension for filing but not paying |

### ASPE vs IFRS Choice

**ASPE vs IFRS Choice**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Factor | ASPE (Private Enterprises) | IFRS (Public / Large) |
| --- | --- | --- |
| Who | Any private company | Publicly accountable entities |
| Complexity | Simplified (no fair value for most items) | Full fair value, complex disclosures |
| Goodwill | Not amortized — impairment-only model (ASPE 3064) | Annual impairment test (no amortization) |
| Leases | Operating vs finance classification | IFRS 16: all on balance sheet |
| Financial instruments | Cost/amortized cost (default) | FVTPL or FVOCI or amortized cost |
| Cost | Lower professional fees | Higher — more disclosures |

### Compilation Engagement (NTR)

Most small Canadian businesses engage a CPA for a "compilation" (Notice to Reader) — the CPA compiles financial statements from client-provided information without performing audit or review procedures. No assurance is expressed.

## Section 10 -- Interaction with Tax Skills

### Corporate Income Tax (T2 Return)

- **T2 return mapping and considerations** — Financial statements mapped via GIFI codes to T2; Schedule 1: Net Income Reconciliation (add back: amortization, meals 50%, non-deductible items; deduct: CCA, eligible capital deductions); Schedule 8: CCA calculation (separate from book amortization); Schedule 125: Income Statement Information (GIFI); Schedule 100: Balance Sheet Information (GIFI); Active business income ≤ $500,000: small business deduction (combined federal/provincial ~12.2% varies by province); Investment income: taxed at ~50%, refundable upon dividend distribution (RDTOH)  _(unsure)_

### GST/HST Return

**GST/HST Return**

| Line | Description | CoA Mapping |
| --- | --- | --- |
| 101 | GST/HST collected (or collectible) | 2050 |
| 105 | Total GST/HST and adjustments | 2050 + adjustments |
| 106 | Input Tax Credits (ITCs) | 1150 |
| 108 | Total ITCs and adjustments | 1150 + adjustments |
| 109 | Net tax (remit or refund) | 2060 |

### Payroll Remittances

**Payroll Remittances (2025)**

| Item | Rate (2025) | Employer Portion |
| --- | --- | --- |
| CPP (employee) | 5.95% on pensionable earnings $3,500–$71,300 | Employer matches 1:1 |
| CPP2 (second ceiling) | 4.0% on $71,300–$81,200 | Employer matches 1:1 |
| EI (employee) | 1.64% on insurable earnings up to $65,700 | Employer pays 1.4× employee amount |
| Federal income tax | Per tax tables (withholding) | Employer remits to CRA |

### Provincial Considerations

- **Provincial tax considerations** — Quebec: separate QST (9.975%) and QPP (instead of CPP); file with Revenu Québec; PST provinces (BC, SK, MB): PST is not an input tax credit — it becomes part of the asset/expense cost; HST provinces (ON, NB, NS, NL, PE): combined rate; single return to CRA; Alberta: GST only (5%), no provincial sales tax  _(unsure)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
