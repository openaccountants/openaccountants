---
name: canada-bookkeeping
description: Use this skill whenever asked about Canadian bookkeeping for sole proprietors, partnerships, or private corporations. Trigger on phrases like "chart of accounts", "GIFI codes", "bookkeeping", "profit and loss", "balance sheet", "ASPE", "ASNPO", "CRA categories", "bank reconciliation", "expense categories", "revenue recognition", "depreciation", "CCA", "capital cost allowance", "GST/HST", "input tax credits", "T2125", "T2", "general ledger", "HST return", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a Canadian business.
version: 1.2
jurisdiction: CA
tax_year: 2026
tax_year_notes: Current bookkeeping and tax-mapping workflow with 2026 payroll reference rates. The separately labelled 2025 payroll table, 2025 passenger-vehicle cohort, 2025 T2125 references and fictional 2025 worked cases retain their historical dates and inputs. The filing dates concern the 2025 return filed in 2026; no 2026 return form or unverified 2026 capital limit is supplied.
last_updated: 2026-11-26
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Khushboo Talreja"
reviewed_on: 2026-11-03
tier: 1
domain: bookkeeping
---

# Canada Bookkeeping

Use this chart to organize a Canadian business's records and prepare a **2026** bookkeeping and tax-mapping workpaper, using the dated historical references only for their stated years. Establish the entity, fiscal period, reporting framework and business use before choosing return fields. The account numbers are an internal convention; they do not determine deductibility or constitute completed financial statements or returns.

## Section 1 -- Quick Reference

| Field | Treatment |
| --- | --- |
| Currency | Report corporate GIFI information in Canadian funds. An eligible corporation with a filed T1296 election under ITA 261 can report in a functional currency. For election eligibility and conversion: Check this point with one of our partner accountants. [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) |
| Fiscal period | Business income of sole proprietors is generally reported on a calendar-year basis; eligible sole proprietors and all-individual partnerships can elect a non-calendar fiscal period using T1139. A corporation's tax year is its fiscal period, which cannot exceed 53 weeks. For changes of year-end and election-specific adjustments: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) |
| Records | ITA 230(4)(b)'s ordinary minimum is six years after the last tax year to which the records relate. Prescribed records have their own retention period; a late/unfiled return, objection/appeal or CRA retention demand can require longer retention. Do not destroy those records from the six-year shorthand alone. [ITA 230(4)–(7)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-230.html) |
| GST/HST registration | For most ordinary businesses making taxable supplies in Canada, test worldwide taxable revenue before expenses, including zero-rated supplies and associates at the beginning of the quarter; exclude financial services, capital-property sales and goodwill from selling a business. Exceeding $30,000 in one calendar quarter ends small-supplier status on the supply that crosses it: charge tax on that supply and register within 29 days. Exceeding it over four or fewer consecutive quarters, without exceeding it in one quarter, ends that status at the end of the following month: charge from the first subsequent supply and register within 29 days of that effective date. For special registration regimes, charities/public institutions, taxis/ride-sharing and non-residents: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| GIFI | Corporate/partnership financial-statement codes differ from T2125 expense lines. Corporations other than insurers and partnerships can use GIFI, subject to the non-resident exclusions in RC4088. [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) |
| ASPE, ASNPO or IFRS framework selection | Check this point with one of our partner accountants. |

## Section 2 -- Standard Chart of Accounts

This illustrative internal chart preserves the nominal accounts. GIFI is a **statement-level selection**, not a mandatory one-to-one nominal assignment: use the actual financial-statement detail and the specific RC4088 subcode where appropriate. Broad codes below describe grouped statement categories. Do not aggregate away detail present in the statements. For account-specific classification outside these descriptions: Check this point with one of our partner accountants. All GIFI definitions in this section: [RC4088 Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html).

### Assets (1000–1999)

**Assets (1000–1999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 1000 | Cash — Operating Account (Canadian-bank CAD deposit) | 1002 | Current asset |
| 1010 | Cash — Savings Account (Canadian-bank CAD deposit) | 1002 | Current asset |
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
| 1330 | Furniture and Fixtures | 1787 | Non-current asset |
| 1331 | Accumulated Amortization — Furniture | 1788 | Contra asset |
| 1340 | Computer Hardware | 1774 | Non-current asset |
| 1341 | Accumulated Amortization — Computer | 1775 | Contra asset |
| 1350 | Motor Vehicles | 1742 | Non-current asset |
| 1351 | Accumulated Amortization — Vehicles | 1743 | Contra asset |
| 1360 | Leasehold Improvements | 1918 | Non-current asset |
| 1361 | Accumulated Amortization — Leasehold | 1919 | Contra asset |
| 1400 | Intangible Assets — Patents (software uses 1774) | 2020 | Non-current asset |
| 1401 | Accumulated Amortization — Patents (software uses 1775) | 2021 | Contra asset |
| 1500 | Goodwill | 2012 | Non-current asset |

### Liabilities (2000–2999)

**Liabilities (2000–2999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 2000 | Accounts Payable — Trade | 2621 | Current liability |
| 2010 | Accrued Liabilities | 2620 | Current liability |
| 2050 | GST/HST Payable (Collected) | 2680 | Current liability |
| 2060 | GST/HST Net (Control) | 2680 | Current liability |
| 2100 | Income Tax Payable | 2680 | Current liability |
| 2110 | Payroll Liabilities — CPP | 2627 employee deductions; 2620 employer accrual | Current liability |
| 2120 | Payroll Liabilities — EI | 2627 employee deductions; 2620 employer accrual | Current liability |
| 2130 | Payroll Liabilities — Income Tax W/H | 2628 | Current liability |
| 2140 | Vacation Pay Payable | 2624 | Current liability |
| 2150 | Workers’ Compensation Payable | 2620 | Current liability |
| 2200 | Credit Card Payable | 2707 | Current liability |
| 2300 | Current Portion of Long-Term Debt | 2920 | Current liability |
| 2400 | Bank Loan — Long-Term (chartered bank) | 3143 | Non-current liability |
| 2410 | Mortgage Payable | 3141 | Non-current liability |
| 2500 | Shareholder Loan | 3260 if long-term; 2780 if current | Current or non-current liability — use actual maturity |
| 2600 | Deferred Revenue | 2770 | Current liability |

### Equity (3000–3999)

**Equity (3000–3999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 3000 | Share Capital (Common Shares) | 3500 | Equity |
| 3010 | Share Capital (Preferred) | 3520 | Equity |
| 3100 | Retained Earnings | 3600 | Equity |
| 3200 | Owner’s Equity / Capital (sole prop) | N/A — internal sole-proprietor account | Equity |
| 3210 | Owner’s Drawings (sole prop) | N/A — internal sole-proprietor account | Equity |
| 3220 | Owner’s Contributions (sole prop) | N/A — internal sole-proprietor account | Equity |
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
| 6210 | Meals and Entertainment (eligibility and applicable limit required) | 8523 | Expense |
| 6220 | Travel Expenses | 9200 | Expense |
| 6230 | Vehicle Expenses — Fuel | 9281 | Expense |
| 6240 | Vehicle Expenses — Insurance | 9281 | Expense |
| 6250 | Vehicle Expenses — Repairs | 9281 | Expense |
| 6260 | Vehicle Expenses — Lease Payments | 8915 | Expense |
| 6300 | Office Supplies and Stationery | 8811 | Expense |
| 6310 | Postage and Courier | 9275 | Expense |
| 6320 | Telephone and Internet | 9225 | Expense |
| 6330 | Software Subscriptions (SaaS) | 9150 | Expense |
| 6400 | Professional Fees — Accounting | 8860 | Expense |
| 6410 | Professional Fees — Legal | 8860 | Expense |
| 6420 | Professional Fees — Consulting | 8860 | Expense |
| 6500 | Bank Charges and Credit Card Fees | 8710 | Expense |
| 6510 | Interest Expense — Bank | 8710 | Expense |
| 6520 | Interest Expense — Other | 8710 | Expense |
| 6600 | Amortization — Tangible Assets (Book) | 8670 | Expense |
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
| 7200 | Foreign Exchange Gain/Loss | 8231 | Other income/expense |

### Tax (8000–8999)

**Tax (8000–8999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 8000 | Income Tax Expense (Current) | 9990 | Tax |
| 8010 | Deferred Income Tax | 9995 | Tax |


## Section 3 -- Revenue Recognition

### Financial reporting: revenue, interest, royalties, dividends and construction contracts

For ASPE revenue recognition, completion methods, collection/measurability tests and the corresponding ASNPO or IFRS treatment: Check this point with one of our partner accountants.

### Tax accounting methods

Generally report business income using accrual accounting: income in the fiscal period earned and allowable expenses in the fiscal period incurred, regardless of receipt/payment. Farmers, fishers and self-employed commission agents may use cash or accrual, but not a combination. A cash-method taxpayer reports receipts when received and allowable expenses when paid, except prepaid expenses. Method changes have adjustment/request requirements; do not switch merely by changing the bank-feed settings. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html)

For the former billed-basis election, professional work in progress and transition/valuation treatment: Check this point with one of our partner accountants.

## Section 4 -- Expense Classification

### T2125 expense fields

The chart's GIFI codes do not determine T2125 lines. These are field labels, not a finding that an entire nominal balance is deductible. Claim only reasonable current expenses incurred to earn business income, exclude personal use and capital purchases, and reduce expenses by ITCs claimed and applicable assistance. Professional fees for buying capital property belong in its cost, rather than the current-fee line. [CRA T2125 instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html); [CRA business expenses](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html).

| Line | Category | Workpaper selection |
| --- | --- | --- |
| 8521 | Advertising | Eligible advertising costs |
| 8523 | Meals and entertainment | Apply the limitation/exception below |
| 8590 | Bad debts | Establish eligibility before including written-off amounts |
| 8690 | Insurance | Eligible business insurance |
| 8710 | Interest and bank charges | Eligible interest/charges; no duplicate claim at 8871 |
| 8760 | Business taxes, licences and memberships | Eligible business amounts |
| 8810 | Office expenses | Classify the actual item using CRA instructions |
| 8811 | Office stationery and supplies | Keep distinct from the GIFI group |
| 8860 | Professional fees (legal and accounting included) | Eligible current fees, including consulting |
| 8871 | Management and administration fees | Includes business administration/bank charges; exclude employees' salaries/benefits, property taxes and rent, which have separate lines |
| 8910 | Rent | Eligible business rent |
| 8960 | Repairs and maintenance | Current repairs; no own labour, reimbursed repairs or capital improvements |
| 9060 | Salaries, wages and benefits | Eligible employee amounts and employer contributions |
| 9180 | Property taxes | Eligible property taxes |
| 9200 | Travel expenses | Eligible business travel |
| 9220 | Utilities | Eligible business utilities |
| 9281 | Motor vehicle expenses (not CCA) | Eligible business vehicle costs; apply use/vehicle limits |
| 9270 | Other expenses | Not the utilities field |
| 9936 | Capital cost allowance (CCA) | Tax allowance, separate from book amortization |

Field labels: [CRA T2125 expense fields](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html). For a disputed category or special deduction restriction: Check this point with one of our partner accountants.

### Meals, exclusions and unpaid remuneration

Meals/entertainment ordinarily have a maximum claim of 50% of the lesser of the cost incurred and a reasonable amount. Do not apply a fixed half-addback to cases covered by CRA's exceptions (food/entertainment supplied for compensation; separately billed customer costs; specified employee-benefit/remote-site cases; qualifying all-employee events; charity fundraisers; temporary construction camps). For those exceptions, fishers, long-haul drivers and couriers: Check this point with one of our partner accountants. [CRA meals and entertainment](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html).

On T2125, exclude personal expenses and drawings/salary paid to self or partners, charitable donations and political contributions, income-tax interest/penalties, most life-insurance premiums and most statutory fines/penalties. For club dues, collateral life insurance, political-contribution credits and any exception: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html).

Under ITA 78(4), otherwise deductible employment remuneration, pensions/superannuation benefits and retiring allowances unpaid on the day 180 days after year-end are deemed incurred in the payment year instead. Reasonable vacation/holiday pay and deferred amounts under a salary-deferral arrangement are excluded from this rule. [ITA 78(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-78.html).

## Section 5 -- Asset vs Expense Thresholds

Classify current versus capital expenditure from its nature; there is no general $500 rule for all purchases. The $500 boundary below is for specified tools. Capital purchases are not ordinary current-expense deductions. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html); [CRA CCA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html).

### CCA reference classes

The Class 10.1 dollar limit below is an explicitly historical 2025 acquisition reference. For 2026 passenger-vehicle limits and the operative acquisition-year rules: Check this point with one of our partner accountants.

These are ordinary base rates for eligible depreciable property, **not first-year deduction percentages**. Establish the property definition, acquisition date, business use, available-for-use date, UCC and elections before computing CCA. For enhanced first-year allowances, immediate expensing, recapture, terminal loss or unusual property: Check this point with one of our partner accountants.

| Class | Ordinary base rate | Property and boundaries |
| --- | --- | --- |
| 1 | 4% | Most buildings acquired after 1987, subject to the specified Class 3/6 exceptions. For additional manufacturing/non-residential building allowances: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 8 | 20% | Furniture, equipment and other specified property not included in another class; specified tools costing $500 or more. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 10 | 30% | Motor vehicles and passenger vehicles not meeting Class 10.1 conditions; eligible zero-emission vehicles instead fall under Class 54. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 10.1 | 30% | A 2025-acquired passenger vehicle costing more than $38,000 before sales tax goes in its own separate class; prescribed capital cost is capped at $38,000 plus applicable sales taxes. This is not a cap on every vehicle. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 12 | 100% | Specified tools, medical/dental instruments and kitchen utensils costing less than $500 acquired on/after 2 May 2006; qualifying non-systems computer software. Most small tools avoid the half-year rule, but dies, jigs, patterns, moulds, lasts and cutting/shaping machine parts do not; Class 12 software is also subject to that rule before any separately available first-year relief. Electronic communication/data-processing equipment is excluded. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 13 | Leasehold improvements | Check this point with one of our partner accountants. [CRA leasehold guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) |
| 14.1 | 5% | Generally for post-2016 eligible additions, including goodwill, on declining balance. Pre-2017 transitioned property has a 7% rate for tax years ending before 2027, with transition rules. For a transition balance: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 43 | 30% | Eligible machinery/equipment used in Canada primarily to manufacture/process goods for sale or lease, not included in Class 29 or 53; not a universal post-2025 purchase label. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 50 | 55% | General-purpose computer equipment and systems software acquired after 18 March 2007; excludes Class 29/52 property and mainly process-control/monitoring, communications-control or non-ancillary data-handling equipment and the specified related software. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 53 | 50% | Eligible machinery/equipment acquired after 2015 and before 2026, generally otherwise Class 29, used in Canada primarily to manufacture/process goods for sale or lease. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 54 | 30% | Qualifying zero-emission vehicles otherwise Class 10/10.1, acquired after 18 March 2019; not a passenger-only class. For vehicle qualification, passenger-cost caps and election out of this class: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 55 | 40% | Qualifying zero-emission vehicles otherwise Class 16, acquired after 18 March 2019; not every non-passenger vehicle. For vehicle qualification and election out of this class: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |

### Accelerated investment incentive and leaseholds

For original AII versus reaccelerated-investment cohorts, detailed first-year allowances and leasehold terms/renewals: Check this point with one of our partner accountants.

### Repairs, book amortization and deferred tax

Keep current minor repairs separate from capital improvements; exclude own labour and insurance-reimbursed repairs from the current repair claim. [CRA repairs](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html).

For financial-reporting depreciation methods/useful lives, intangible amortization and deferred-tax recognition: Check this point with one of our partner accountants.

## Section 6 -- P&L Format

### Illustrative Income Statement Layout

Workflow illustration only; adapt the headings to the entity. For framework compliance: Check this point with one of our partner accountants.

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

### Illustrative Statement of Financial Position

Workflow illustration only; the shareholder-equity section is corporate. For framework compliance and current/non-current presentation: Check this point with one of our partner accountants.

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

Inspect the actual bank export before importing. Record its date, description, amount, direction and balance conventions; reconcile opening balance plus movements to closing balance. The prior bank-specific format/field assertions are removed because no bank export was supplied.

Treat description strings as search hints, never final classifications. INTERAC/E-TRANSFER needs direction and counterparty; PAD/PAP/card payments need the invoice; a payroll processor debit needs the payroll reconciliation; a platform payout needs gross sales, fees, refunds, taxes and payout reconciliation. Split mortgage/loan payments using the lender's principal/interest breakdown. Investigate CRA payments and credits against the specific tax-account statement. These are workflow instructions, not tax determinations.

## Section 9 -- Micro-Entity / Small Business Simplifications

| Topic | Treatment |
| --- | --- |
| Quick Method (GST/HST) | Check this point with one of our partner accountants. |
| Individual income-tax instalments | Ordinary individuals test net tax owing above $3,000 ($1,800 for a Quebec resident at 31 December) in the current year **and either of the two prior years**. At or below the applicable current-year limit, no instalments are required even after a reminder. For farming/fishing or a special case: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html) |
| Corporate income-tax instalments | The federal Parts I, VI, VI.1 and XIII.1 total, computed before specified future tax consequences and current-year refundable credits, need not be paid by instalments if it is $3,000 or less in either the current or previous year. Apply the separate provincial/territorial total test. All corporations can pay monthly; do not infer that all pay quarterly. For quarterly eligibility, first-year and special tax rules: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t7b-corp/corporation-instalment-guide.html) |
| Simplified ITC claims | Check this point with one of our partner accountants. |
| GIFI-Short | A corporation not using return-preparation software with **both** gross revenue and assets less than $1 million each may use paper T1178. Insurance corporations are excluded. RC4088's non-resident exclusions still apply. This is not a T2125 eligibility rule. [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) |
| T2 Short Return | Check this point with one of our partner accountants. |
| Self-employed 2025 return | June 15, 2026 filing if the taxpayer or spouse/common-law partner carried on a business whose expenditures did not relate mostly to a tax-shelter investment; tax-shelter cases use April 30, 2026. Balance owing is payable April 30, 2026. For deceased persons/surviving spouses and other exceptional deadlines: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals/filing-dates-tax-return.html) |

### ASPE, ASNPO, IFRS and compilation engagements

For framework choice, revenue/goodwill/leases/financial instruments and compilation versus assurance engagements (including historical Notice to Reader terminology): Check this point with one of our partner accountants.

## Section 10 -- Interaction with Tax Skills

### Corporate income tax

Use Schedule 100 for closing balance-sheet information and Schedule 125 for income/expenses; new corporations also need opening balance-sheet information (Schedule 101). Reconcile book profit to tax using Schedule 1 and calculate corporate CCA, recapture and terminal losses using Schedule 8. This is a routing instruction, not a completed tax computation. [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html); [Schedule 1](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2sch1.html); [Schedule 8](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2sch8.html).

For small-business deduction eligibility, business-limit sharing/reductions and provincial rates: Check this point with one of our partner accountants.

For investment-income tax and RDTOH/dividend refunds: Check this point with one of our partner accountants.

### GST/HST return — regular method

| Line | Workpaper amount |
| --- | --- |
| 101 | Sales and other revenue excluding GST/HST/PST  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 103 | GST/HST collected or collectible in the reporting period  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 104 | Adjustments added to net tax  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 105 | 103 + 104  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 106 | Eligible ITCs for the current period and eligible previously unclaimed ITCs  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 107 | Adjustments deducted from net tax  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 108 | 106 + 107  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 109 | Net tax: 105 − 108  [CRA worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |

Reconcile eligible ledger balances rather than copying every balance in a nominal account. Line 109 is not the final payment/refund: other credits/debits feed the final balance. The worked example uses the CRA worksheet line labels; software may combine entry fields. For Quick Method or other special regimes: Check this point with one of our partner accountants. [CRA GST/HST working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Payroll remittances — use the year of payment

The 2026 CPP reference is 5.95%, a $3,500 annual basic exemption, $74,600 maximum pensionable earnings and $4,230.45 annual employee/employer maximum each. [CRA CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html).

For 2026, CPP2 is 4% above $74,600 up to $85,000, with a $416 annual maximum for each employee/employer. [CRA CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html).

For 2026, outside-Quebec EI is 1.63% up to $68,900 insurable earnings, with an employee maximum of $1,123.07 and standard employer maximum of $1,572.30 (1.4 multiplier, unless a reduced employer rate applies). [CRA EI](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html).

The following **historical 2025 references** are retained for 2025 payroll reconciliation, not substituted for 2026 rates:

These rates assume covered pensionable/insurable employment, not every worker. Establish coverage, province of employment, pay period, pensionable/insurable earnings, age/elections and annual maximums before running payroll. For a payroll calculation, Quebec QPP or exceptions: Check this point with one of our partner accountants.

| Item | 2025 reference | Employer portion |
| --- | --- | --- |
| CPP | 5.95%; annual basic exemption $3,500; maximum pensionable earnings $71,300; annual employee maximum $4,034.10 | Matching contribution. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) |
| CPP2 | 4% on pensionable earnings above $71,300 up to $81,200; annual employee maximum $396 | Matching contribution. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html) |
| EI outside Quebec | 1.64% on insurable earnings up to $65,700; annual employee maximum $1,077.48 | Standard employer multiplier 1.4; employer maximum $1,508.47. For a reduced employer rate: Check this point with one of our partner accountants. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) |
| Income-tax withholding | Use the applicable payroll table/calculator | Check this point with one of our partner accountants. |

### Provincial considerations

For taxable supplies, use the supply type, place and recipient rules. Alberta's GST rate is 5%; Quebec's QST reference rate is 9.975%. Ontario, New Brunswick, Newfoundland and Labrador, Nova Scotia and Prince Edward Island participate in HST. These labels do not establish that a particular supply is taxable. [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html).

For provincial-tax recovery/exemptions and whether an unrecovered amount belongs in current expense or capital cost: Check this point with one of our partner accountants.

## Worked mapping examples — fictional 2025 inputs

These examples test the corrected field mapping and arithmetic only. Eligibility/business use is assumed already established for the stated amounts; they do not establish eligibility or complete a filing.

### T2125 vehicle and utilities mapping

Eligible vehicle fuel of 200 and repairs of 100 belong in the vehicle-expense workpaper for line 9281. Eligible utilities of 120 belong in the utilities workpaper for line 9220, not other-expenses field 9270. No CCA or personal expenditure is included. [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

```oa-check
name: Fictional T2125 eligible vehicle and utilities totals
inputs:
  eligible_vehicle_fuel: 200
  eligible_vehicle_repairs: 100
  eligible_utilities: 120
steps:
  - line_9281: eligible_vehicle_fuel + eligible_vehicle_repairs
  - line_9220: eligible_utilities
  - combined_expenses: line_9281 + line_9220
expected:
  line_9281: 300
  line_9220: 120
  combined_expenses: 420
```

### Regular-method GST/HST revenue and tax mapping

Assume reconciled 2025 regular-method ledger amounts: revenue excluding sales taxes of 1000, GST/HST collected/collectible of 130, allowable ITCs of 50, and zero adjustments on lines 104 and 107. Line 101 is 1000, not 130; line 103 is 130. The net tax is 80. The final payable/refundable balance remains uncomputed until the other return lines are established. [GST/HST working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

```oa-check
name: Fictional regular-method revenue versus GST/HST collected
inputs:
  sales_excluding_sales_taxes: 1000
  tax_collected: 130
  allowable_itcs: 50
  adjustments_104: 0
  adjustments_107: 0
steps:
  - line_101: sales_excluding_sales_taxes
  - line_103: tax_collected
  - line_105: line_103 + adjustments_104
  - line_108: allowable_itcs + adjustments_107
  - line_109: line_105 - line_108
expected:
  line_101: 1000
  line_103: 130
  line_105: 130
  line_108: 50
  line_109: 80
```

## Sources

The 21 November 2026 full claim audit and bounded 25 November follow-ups were reused for unchanged scope. On **2026-11-26**, the retained operative passages below were read to recover exact quotations and confirm operative conditions and the stated historical cohorts; the 2026 payroll rows were checked against the authorities’ separate 2026 entries; removed assertions and referrals are not certified rules.

| Official source | Retained scope | Date read |
| --- | --- | --- |
| [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | GIFI definitions, statement detail, currency, schedules and short form | 2026-11-26 |
| [Accounting for earnings](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) | Accrual/cash and fiscal periods | 2026-11-26 |
| [T2125 expense fields](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html) | Field labels, exclusions, current/capital and business use | 2026-11-26 |
| [Business expenses](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html) | Current repairs, professional/admin fees, meals and exceptions | 2026-11-26 |
| [CCA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) | Ordinary rates, property definitions and acquisition cohorts | 2026-11-26 |
| [GST/HST worksheet](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) | Regular-method line labels and arithmetic | 2026-11-26 |
| Official links beside the records, instalments, filing and payroll entries | The specified operative sections/tables and 2025 entries only | 2026-11-26 |

**Not yet confirmed:** this workpaper supplies no operative calculation for the topics carrying the partner-accountant referral, including financial-reporting standards, professional WIP, leasehold/enhanced CCA, special deductions, Quick Method, simplified ITCs, T2 Short, compilation, small-business/investment-income tax, special payroll and provincial-tax recovery. Check this point with one of our partner accountants.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
