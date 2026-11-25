---
name: canada-bookkeeping
description: Use this skill whenever asked about Canadian bookkeeping for sole proprietors, partnerships, or private corporations. Trigger on phrases like "chart of accounts", "GIFI codes", "bookkeeping", "profit and loss", "balance sheet", "ASPE", "ASNPO", "CRA categories", "bank reconciliation", "expense categories", "revenue recognition", "depreciation", "CCA", "capital cost allowance", "GST/HST", "input tax credits", "T2125", "T2", "general ledger", "HST return", or any question about day-to-day transaction recording, financial statement preparation, or account coding for a Canadian business.
version: 1.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: This remains a 2025 skill. Corrections reuse the 21 November 2026 claim audit; the 2025 payroll and passenger-vehicle figures have not been relabelled as 2026 figures. Unresolved framework, classification and eligibility checks below block the affected outputs.
last_updated: 2026-11-25
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

This is a **2025 bookkeeping and tax-mapping workpaper**, not a completed return or a certification of financial-statement compliance. Preserve the actual entity, reporting framework, fiscal period and business-use facts. A **HOLD** below means that the affected classification or calculation must not be used until its stated check is completed; it never means a zero balance or an automatic disallowance. The unresolved checks from the existing audit have not been certified as correct by this correction.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Canada |
| Currency | CAD workpapers only. **HOLD:** an eligible corporation using elected functional-currency reporting needs its own reporting/conversion treatment; this is not a universal CAD prohibition. [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) |
| Financial year | Establish the actual fiscal period and applicable elections before mapping a return. **HOLD:** the original corporation/sole-proprietor shorthand does not resolve ITA 249.1 or a change of year-end. [ITA 249.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-249.1.html) |
| Governing body | Accounting Standards Board (AcSB) of CPA Canada |
| Tax authority | Canada Revenue Agency (CRA) |
| Key legislation | Income Tax Act (ITA); Excise Tax Act (GST/HST); Canada Business Corporations Act |
| GST/HST registration threshold | **HOLD:** do not decide registration solely from the $30,000 headline. The single-quarter and four-consecutive-quarter tests, associates, exclusions and other registration regimes must be resolved. [CRA registration](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) |
| Record keeping requirement | 6 years from end of the last tax year to which records relate |
| GIFI codes | General Index of Financial Information — CRA's standardized code system for T2 filing |

**Framework verification hold:** establish the applicable ASPE, ASNPO or IFRS framework before producing a compliance conclusion. Operative standards and framework-selection conditions were not verified in this audit; they remain blocked and are listed under Sources: Not yet confirmed.

## Section 2 -- Standard Chart of Accounts

The four-digit nominal codes below are an illustrative internal chart, not a statutory chart imposed on every Canadian business. GIFI reporting for corporate financial statements is different from T2125 line coding; use Section 4 for the latter. Select GIFI against the actual statement detail, entity and account maturity. **HOLD** entries are not approved filing mappings. [CRA RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html).

### Assets (1000–1999)

**Assets (1000–1999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 1000 | Cash — Operating Account | **HOLD — 1001; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current asset |
| 1010 | Cash — Savings Account | **HOLD — 1001; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current asset |
| 1020 | Petty Cash | **HOLD — 1001; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current asset |
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
| 1320 | Machinery and Equipment | **HOLD — 1740; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Non-current asset |
| 1321 | Accumulated Amortization — Equipment | **HOLD — 1741; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Contra asset |
| 1330 | Furniture and Fixtures | **HOLD — 1740; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Non-current asset |
| 1331 | Accumulated Amortization — Furniture | **HOLD — 1741; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Contra asset |
| 1340 | Computer Hardware | 1774 | Non-current asset |
| 1341 | Accumulated Amortization — Computer | 1775 | Contra asset |
| 1350 | Motor Vehicles | 1742 | Non-current asset |
| 1351 | Accumulated Amortization — Vehicles | 1743 | Contra asset |
| 1360 | Leasehold Improvements | 1918 | Non-current asset |
| 1361 | Accumulated Amortization — Leasehold | 1919 | Contra asset |
| 1400 | Intangible Assets (Software, Patents) | **HOLD — 2010; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Non-current asset |
| 1401 | Accumulated Amortization — Intangibles | 2011 | Contra asset |
| 1500 | Goodwill | 2012 | Non-current asset |

### Liabilities (2000–2999)

**Liabilities (2000–2999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 2000 | Accounts Payable | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2010 | Accrued Liabilities | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2050 | GST/HST Payable (Collected) | 2680 | Current liability |
| 2060 | GST/HST Net (Control) | 2680 | Current liability |
| 2100 | Income Tax Payable | 2680 | Current liability |
| 2110 | Payroll Liabilities — CPP | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2120 | Payroll Liabilities — EI | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2130 | Payroll Liabilities — Income Tax W/H | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2140 | Vacation Pay Payable | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2150 | Workers' Compensation Payable | **HOLD — 2620; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Current liability |
| 2200 | Credit Card Payable | 2707 | Current liability |
| 2300 | Current Portion of Long-Term Debt | 2920 | Current liability |
| 2400 | Bank Loan — Long-Term | **HOLD — 3140; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Non-current liability |
| 2410 | Mortgage Payable | 3141 | Non-current liability |
| 2500 | Shareholder Loan | **HOLD — 3260; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Non-current liability |
| 2600 | Deferred Revenue | 2770 | Current liability |

### Equity (3000–3999)

**Equity (3000–3999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 3000 | Share Capital (Common Shares) | **HOLD — 3500; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Equity |
| 3010 | Share Capital (Preferred) | 3520 | Equity |
| 3100 | Retained Earnings | 3600 | Equity |
| 3200 | Owner's Equity / Capital (sole prop) | **HOLD — 3500; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Equity |
| 3210 | Owner's Drawings | **HOLD — no automatic GIFI assignment; entity-specific equity mapping required** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Equity |
| 3220 | Owner's Contributions | **HOLD — 3500; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Equity |
| 3300 | Dividends Declared | 3700 | Equity |
| 3400 | Current Year Net Income/Loss | 3680 | Equity |

The held nominal rows cover cash versus deposits; equipment versus furniture and related accumulated amortization; software/intangible type; trade versus payroll liabilities; bank-loan type and shareholder-loan maturity; corporate share capital versus proprietors' equity; foreign exchange; tangible amortization; and office/postage/software classification. RC4088's definition is not enough to settle those facts. The former drawings code was not listed in the source and has been removed rather than replaced with another guess.

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
| 4500 | Other Income | **HOLD — 8230; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Revenue |
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
| 6300 | Office Supplies and Expenses | **HOLD — 8810; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Expense |
| 6310 | Postage and Courier | **HOLD — 8810; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Expense |
| 6320 | Telephone and Internet | 9225 | Expense |
| 6330 | Software Subscriptions (SaaS) | **HOLD — 8810; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Expense |
| 6400 | Professional Fees — Accounting | 8860 | Expense |
| 6410 | Professional Fees — Legal | 8860 | Expense |
| 6420 | Professional Fees — Consulting | 8860 | Expense |
| 6500 | Bank Charges and Credit Card Fees | 8710 | Expense |
| 6510 | Interest Expense — Bank | 8710 | Expense |
| 6520 | Interest Expense — Other | 8710 | Expense |
| 6600 | Amortization (Book Depreciation) | **HOLD — 8670; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Expense |
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
| 7200 | Foreign Exchange Gain/Loss | **HOLD — 8230; confirm classification** [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Other income/expense |

### Tax (8000–8999)

**Tax (8000–8999)**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

| Code | Account | GIFI | Type |
| --- | --- | --- | --- |
| 8000 | Income Tax Expense (Current) | 9990 | Tax |
| 8010 | Deferred Income Tax | 9995 | Tax |

## Section 3 -- Revenue Recognition

### ASPE Section 3400 Revenue — HOLD

**HOLD — do not use the following legacy recognition assumptions to make an ASPE-compliance conclusion. Operative ASPE 3400 was not read. Each recognition method requires its applicable paragraph, contract facts and framework before use.**

- **HOLD — unverified legacy revenue recognition criteria** — The original assumptions were: Performance is achieved (goods delivered / services rendered); Collection is reasonably assured; Amount is measurable  _(ASPE Section 3400)_

**Revenue recognition by type**  _(ASPE Section 3400)_

| Revenue Type | Unverified legacy recognition assumption — blocked from use |
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
| Accrual | General business-income method: income when earned and allowable expenses when incurred; an invoice date alone does not determine recognition. [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) |
| Cash | CRA identifies farmers, fishers **and self-employed commission agents** as users of the cash method. Do not apply an exclusive farming/fishing list or infer that every other business can elect it. [CRA accounting methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) |
| Billed-basis | The former election was repealed for tax years beginning **on or after 22 March 2017**. **HOLD:** full WIP valuation and transition conditions were not confirmed; do not apply the former blanket lesser-of-cost/FMV instruction. [ITA 34](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-34.html), [Finance history](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2025/part-5.html) |

Use the applicable accounting method and the actual earning/incurrence facts; do not equate an invoice, bank deposit or payout date with income earned in every case.

## Section 4 -- Expense Classification

### T2125 Categories (Statement of Business Activities)

**T2125 Categories (Statement of Business Activities)**

| Line | Category | Description | Nominal Codes |
| --- | --- | --- | --- |
| 8521 | Advertising | Marketing, advertising, signage | 6200 |
| 8523 | Meals and entertainment | **HOLD:** determine eligible amount and the applicable limit/exception; do not apply a universal 50% deduction | 6210 |
| 8590 | Bad debts | Written-off uncollectable accounts | 6610 |
| 8690 | Insurance | Business insurance premiums | 6030 |
| 8710 | Interest and bank charges | Loan interest, service charges | 6500–6520 |
| 8760 | Business taxes, licences, dues, memberships | Professional dues, municipal permits | 6700 |
| 9281 | Motor vehicle expenses (not CCA) | Eligible business-use fuel, insurance, repairs and lease costs; check applicable limits [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) | 6230–6260 |
| 8810 | Office expenses | **HOLD:** this nominal group spans supplies, postage and software; line 8810 is office expenses, while line 8811 separately covers office stationery and supplies. Classify each amount rather than importing the whole GIFI group. [CRA expense fields](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html) | 6300–6330 |
| 8860 | Professional fees | Accounting, legal, consulting | 6400–6420 |
| 8871 | Management and admin fees | Business management/administration category, not restricted universally to related-party fees; **HOLD** actual expense classification and eligibility | 6420 |
| 8910 | Rent | Business premises rent | 6000 |
| 8960 | Repairs and maintenance | Building/equipment repairs | 6040 |
| 9180 | Property taxes | Municipal/provincial property tax | 6010 |
| 9200 | Travel | Airfare, hotels, transport | 6220 |
| 9220 | Utilities | Eligible utilities; classify telephone/internet and any mixed use against the actual form instructions [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) | 6020, 6320 |
| 9936 | Capital cost allowance (CCA) | Tax depreciation (not book) | See Section 5 |

The corrected vehicle and utilities fields are from the [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf). Field 9270 is **other expenses**, not utilities. The expense-category and eligibility holds above remain subject to the [CRA expense instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html).

### Non-Deductible Expenses (CRA)

- Separate book posting from tax deductibility. Personal expenses/drawings, clubs, political contributions, fines, capital expenditure and life-insurance exceptions require the actual entity and statutory facts. A political contribution does not automatically produce a credit for every entity. **HOLD:** do not turn this list into blanket automatic tax adjustments. [CRA expenses](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html).
- The ordinary meals/entertainment limitation has exceptions, including separately conditioned long-haul cases. **HOLD:** determine the actual applicable rule before adding back a fixed proportion; do not label every meal 50% deductible. [CRA business expenses](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html).
- Capital expenditure is not an ordinary current-expense deduction. CCA is a separate **maximum elective claim**, not a mandatory write-off of every capital purchase.
- The unpaid-remuneration timing rule concerns amounts remaining unpaid 180 days after year-end, subject to the operative exceptions; the deduction is normally deferred to the payment year, not permanently denied. [ITA 78(4)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-78.html).

## Section 5 -- Asset vs Expense Thresholds

### Capital Cost Allowance (CCA) — Key Classes

**Capital Cost Allowance (CCA) — Key Classes**

| Class | Rate | Method | Typical Assets |
| --- | --- | --- | --- |
| 1 | 4% | Declining balance | Commercial buildings (post-1987) |
| 1 (M&P) | **HOLD — conditional allowance, not a universal 10%** | Verify acquisition/use and separate-class conditions | Manufacturing buildings [CRA T5013](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) |
| 8 | 20% | Declining balance | Office furniture, equipment, tools ≥ $500 |
| 10 | 30% base rate | Declining balance; first-year rules separate | Qualifying Class 10 vehicles; the 2025 passenger-vehicle limit is not a universal cap on all motor vehicles [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 10.1 | 30% | Declining balance | Passenger vehicles > $38,000 limit (separate class per vehicle) |
| 12 | 100% base rate | **Not an automatic full first-year write-off**: software generally falls under the half-year rule, while most qualifying small tools below $500 do not; applicable first-year relief and property-specific conditions must be checked | Qualifying small tools below $500 and application software; not every low-value asset [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 13 | **HOLD — verify leasehold allowance maximum** | Term, type and renewal conditions required; not a universal straight-line remaining-lease calculation | Leasehold improvements [CRA T5013](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html) |
| 14.1 | 5% general base rate | **HOLD** transition treatment for pre-2017 property; do not apply 5% universally to every historic balance | Goodwill and eligible capital property [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 43 | 30% | Declining balance | Manufacturing and processing machinery (post-2025) |
| 50 | 55% | Declining balance | Computer hardware and systems software |
| 53 | 50% | Declining balance | M&P machinery (acquired 2016–2025) |
| 54 | 30% base rate | First-year allowance and eligibility separate | Qualifying zero-emission vehicles that would otherwise be Class 10 or 10.1; not restricted to passenger vehicles [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| 55 | 40% base rate | First-year allowance and eligibility separate | Qualifying zero-emission vehicles that would otherwise be Class 16; not every non-passenger vehicle [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |

Base rates and Class 12/54/55 descriptions: [CRA depreciable-property classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html). The retained $38,000 Class 10.1 passenger limit is for **2025 acquisitions**, not a 2026 refresh. [2025 regulation](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html). The Class 1 M&P and Class 13 holds require the detailed conditions in [CRA T5013 guidance](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4068/guide-partnership-information-return-t5013-forms.html).

### Accelerated Investment Incentive and acquisition cohorts

**HOLD — enhanced first-year CCA:** do not apply the original AII phase-out to every 2025 acquisition. Original AII and qualifying post-2024 reaccelerated-investment property have different acquisition/available-for-use cohorts and conditions. Resolve those facts and the operative rule before computing a first-year claim. No enhanced-allowance calculation is certified here. [Regulation 1104](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-1104.html).

### Practical Thresholds

**Practical Thresholds**

| Threshold | Treatment |
| --- | --- |
| Current versus capital | Establish whether the expense is current or capital; the general expense instructions exclude purchases of capital property from ordinary current deductions. [CRA expense instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html) |
| Tool-class boundary | The $500 boundary applies to specified tools under the prescribed class rules, not every asset or expense [CRA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) |
| Repairs / improvements | **HOLD:** detailed current/capital classification depends on the actual expenditure and remains unresolved here; no automatic posting from amount alone. [CRA expense instructions — general distinction only](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html) |

### Book Amortization vs Tax CCA

**HOLD — book amortization and deferred tax:** the operative accounting standards were not read. Do not prescribe universal straight-line book amortization or infer a deferred-tax entry solely because book and tax amounts differ. Keep the book schedule, tax CCA election and applicable framework analysis separate.

## Section 6 -- P&L Format

### Illustrative Income Statement Layout — framework review required

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

### Illustrative Statement of Financial Position — framework review required

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

The formats and description patterns below are workflow illustrations, not verified bank specifications or evidence of tax treatment. Confirm the actual export fields, transaction direction, counterparty and gross/net settlement reconciliation before classification.

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
| Quick Method (GST/HST) | **HOLD:** the $400,000 headline alone does not establish eligibility; tax-inclusive supplies, associates, testing period, exclusions and permanent-establishment conditions matter | Remittance and reduced ITC entitlement require the actual election/supply rules; do not treat the difference as unrestricted profit |
| Instalments | **HOLD:** individual and corporate tests are separate; current/prior-year amounts, the exact boundary and exceptions must be resolved | Do not infer one universal quarterly schedule or exemption; corporate monthly/quarterly and first-year rules differ |
| Simplified ITC claims | **HOLD:** the $1,000,000 / $4,000,000 headlines require associates, testing-period/current-quarter, exclusion and entity checks | Calculation method is distinct from documentary requirements; do not infer entitlement from the amounts alone |
| GIFI-Short | **HOLD:** resolve RC4088 entity and filing-method restrictions before selecting the short form | Not a T2125 rule; the approximate code count was not independently verified and is not used here |
| T2 Short Return | **HOLD:** specific eligibility was not verified | Do not select the return or infer filing readiness solely from business size |
| Filing deadline | Ordinary self-employed individual: June 15 return; April 30 payment | Use the actual dates and applicable calendar adjustments, not an assumed two-full-calendar-month extension |

Quick Method conditions: [RC4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html). Instalment conditions: [individuals](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [corporations](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t7b-corp/corporation-instalment-guide.html). Simplified ITC conditions: [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-methods.html). GIFI-Short: [RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html).

### ASPE vs IFRS Choice — HOLD

**ASPE vs IFRS Choice**  _([CRA Guide RC4088, Appendix A](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html))_

**HOLD — this comparison was not verified against operative standards. Do not use these legacy shorthand assumptions to select a framework or determine recognition, goodwill, lease, instrument measurement or engagement cost.**

| Factor | Unverified ASPE assumption — blocked | Unverified IFRS assumption — blocked |
| --- | --- | --- |
| Who | Any private company | Publicly accountable entities |
| Complexity | Simplified (no fair value for most items) | Full fair value, complex disclosures |
| Goodwill | Not amortized — impairment-only model (ASPE 3064) | Annual impairment test (no amortization) |
| Leases | Operating vs finance classification | IFRS 16: all on balance sheet |
| Financial instruments | Cost/amortized cost (default) | FVTPL or FVOCI or amortized cost |
| Cost | Lower professional fees | Higher — more disclosures |

### Compilation Engagement (NTR)

**HOLD — compilation:** the operative compilation standard and engagement-specific conditions were not read. Do not equate the historical "Notice to Reader" label with current compliance, select an engagement solely from size, or certify assurance/filing readiness from this skill.

## Section 10 -- Interaction with Tax Skills

### Corporate Income Tax (T2 Return)

- Map the actual corporate financial statements through GIFI to Schedules 100/125, reconcile book profit to tax on Schedule 1, and calculate the elective CCA claim separately on Schedule 8. Do not use a fixed meals addback without its actual limitation and exceptions. [Schedule 1](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2sch1.html), [Schedule 8](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t2sch8.html).
- **HOLD — small-business tax:** the $500,000 headline is not a universal entitlement. The former approximately 12.2% figure describes 9% federal plus 3.2% Ontario for qualifying **2025 Ontario** income, not every province/entity or a 2026 update. Ontario’s lower rate changed effective 1 July 2026, and provincial business limits can differ from the federal headline. Resolve the actual eligibility, business-limit and province facts before computing tax. [CRA corporation rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html).
- **HOLD — investment income/RDTOH:** there is no universal approximately 50% rate or automatic refund of all investment-income tax. Resolve the entity, province, income type, refundable account balances and taxable dividends; only the applicable refundable portion is potentially recovered. [CRA dividend-refund rules](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/federal-government-budgets/budget-2018-equality-growth-strong-middle-class/passive-investment-income/dividend-refund-rules.html).

### GST/HST Return

**GST/HST Return**

| Line | Description | CoA Mapping |
| --- | --- | --- |
| 101 | Regular-method sales and other revenue **excluding GST/HST/PST** | Eligible revenue accounts, not the tax-payable control |
| 103 | GST/HST collected or collectible | Reconciled eligible tax amounts, including 2050 |
| 105 | Total GST/HST and adjustments | 2050 + adjustments |
| 106 | Input Tax Credits (ITCs) | 1150 |
| 108 | Total ITCs and adjustments | 1150 + adjustments |
| 109 | Net tax (remit or refund) | 2060 |

The mappings above follow the [GST/HST working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf). Net tax on 109 is not automatically the final amount payable/refundable: the remaining return credits/debits and final balance must be reconciled separately. Quick Method and special-regime differences are not resolved by this regular-method example.

### Payroll Remittances

**Payroll Remittances (2025)**

| Item | Rate (2025) | Employer Portion |
| --- | --- | --- |
| CPP (employee) | 5.95% on pensionable earnings $3,500–$71,300 | Employer matches 1:1 |
| CPP2 (second ceiling) | 4.0% on $71,300–$81,200 | Employer matches 1:1 |
| EI (employee) | 1.64% on insurable earnings up to $65,700 | Employer pays 1.4× employee amount |
| Federal income tax | Per tax tables (withholding) | Employer remits to CRA |

### Provincial Considerations

- Quebec: separate QST (9.975%) and QPP (instead of CPP); establish the actual filing obligations. HST provinces (ON, NB, NS, NL, PE) and Alberta GST (5%) use the applicable supply/place rules, not a headquarters default. **HOLD — provincial sales tax:** a provincial tax is not automatically a GST/HST ITC; current expense versus asset cost, exemptions, refunds and recoverability require the actual province and expenditure facts. Do not automatically post every provincial-tax amount to unrecoverable cost.

## Worked mapping examples — fictional 2025 inputs

These examples test the corrected field mapping and arithmetic only. Eligibility/business use is assumed already established for the stated amounts; they do not clear any HOLD or complete a filing.

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

The correction reuses the completed **21 November 2026** reads below; this is not a claim that the entire skill or the operative accounting standards were verified on 25 November. No fresh date is attached to unchanged research. The two explicitly bounded follow-up reads dated 25 November below resolve review-evidence gaps; they are not a repeat audit.

| Official source | Scope of the completed read reused here | Date read |
| --- | --- | --- |
| [CRA RC4088](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | GIFI definitions; 3750 absent; held classifications remain conditional | 2026-11-21 |
| [CRA accounting methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/small-businesses-self-employed-income/business-income-tax-reporting/accounting-your-earnings.html) | Accrual/cash methods, including self-employed commission agents | 2026-11-21 |
| [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf) | Previously read form; disputed vehicle 9281 and utilities 9220 fields rechecked on 21 November | 2026-11-21 |
| [CRA CCA classes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/claiming-capital-cost-allowance/classes-depreciable-property.html) | Base rates; Class 12 first-year qualification and Class 54/55 classification; not an unrestricted enhanced-allowance computation | 2026-11-21 |
| [GST/HST working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) | Revenue 101 versus tax 103 and core net-tax relationships | 2026-11-21 |
| [CRA T2125 expense fields](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/expenses-section-form-t2125.html) | Expense line headings and general current-versus-capital restriction only: 8810 versus 8811, vehicle 9281, utilities 9220 and other expenses 9270; independent reviewer also used this HTML because its PDF fetch was blocked | 2026-11-25 |
| [Finance 2025 historical measure](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2025/part-5.html) | Archived billed-basis measure and implementation/history paragraph: designated professionals, tax years beginning on or after 22 March 2017; not a full WIP valuation/transition read | 2026-11-25 |
| [RC4088 currency subsection](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4088/general-index-financial-information-gifi.html) | Reporting in Canadian funds: eligible corporation with filed T1296 election; this supports the currency qualification, not a full ITA 261 election/conversion analysis | 2026-11-25 |
| Other official links adjacent to affected rows | Existing audit's bounded conditions and source reads; unresolved aspects remain HOLD | 2026-11-21 (bounded existing reads; not a new full read) |

**Not yet confirmed:** operative ASPE/ASNPO/IFRS provisions and framework choice; held GIFI account classifications; full WIP transition/valuation; detailed leasehold/enhanced CCA calculations; the short-return/compilation conditions and the other eligibility/measurement holds explicitly attached to their rows. No bank export or client statement was verified.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
