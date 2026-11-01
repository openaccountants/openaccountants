---
name: zm-corporate-income-tax
description: "Corporate income tax for Zambia, charge year 2026: 30% standard rate, sector rates, new 1% minimum alternative tax, turnover tax boundary, provisional instalments, withholding on dividends, interest and royalties. Trigger on Zambia company tax, CIT rate, minimum alternative tax, MAT Zambia, provisional tax, ITF56, company annual return ZRA, dividend withholding. Covers resident and non-resident companies. Mining fiscal regimes and ZDA incentive claims are flagged for referral."
jurisdiction: ZM
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zambia Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Charge year: 1 January to 31 December 2026. Law: Income Tax Act, Cap. 323, as amended by Acts 10 and 17 of 2025.

## Who this applies to

Companies with annual turnover above K5,000,000, and regardless of turnover: management and consultancy businesses, partnerships, mining, approved public benefit organisations. At K5,000,000 or less, companies pay turnover tax: see [Income tax](zm-income-tax.md). The system is source based.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate, manufacturing and other companies | 30% | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-Income-Tax.pdf |
| Mining, mineral processing | 30% (rate read for 2023; mineral royalty also applies) | 2026 | https://www.zra.org.zm/wp-content/uploads/2023/02/Practice-Notes-2023.pdf |
| Electronic communication business | 35% | 2026 | same |
| Farming, agro-processing | 10% | 2026 | same |
| Non-traditional exports | 10% agro and farming; 15% others | 2026 | same |
| Fertiliser manufacture (chemical or organic) | 15% | 2026 | same |
| Copper cathode product manufacture | 15% | 2026 | same |
| Lapidary and jewellery | 25% | 2026 | same |
| Approved PBO on business income | 15% | 2026 | same |
| Minimum alternative tax (MAT) | 1% of total turnover, credit against income tax, carried at most 5 charge years; not for presumptive or turnover tax payers or railway SPVs in first 12 years | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf |
| Interest cap, railway SPV | Deduction limited to 70% of tax EBITDA; excess carried forward | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf |
| Railway SPV rates | 0% years 1 to 5; 10% years 6 to 15; 12% years 16 to 25; lower of 30% or para 3(1)(b) years 26 to 28 | 2026 | same |
| WHT dividends | 15% resident; 20% non-resident | 2026 | https://www.zra.org.zm/wp-content/uploads/2023/02/Practice-Notes-2023.pdf |
| WHT interest to non-resident | 20% | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf |
| WHT interest on Treasury Bills and Government bonds | 20% | 2026 | same |

Rates dated 2023 are the latest published table found; Acts 10 and 17 of 2025 did not change them.

## The base

Business profits, with deductions under Part IV (ss. 29 to 44): expenditure wholly and exclusively for the business, revenue not capital; capital allowances; bad debts; skills levy; donations to approved PBOs; professional subscriptions. Losses carry forward five years from the same source (s. 30). Add back entertainment, depreciation, general provisions, unrealised exchange losses, tax and penalties. Mining and processing may keep USD books only if 75% or more of gross income is foreign exchange from outside Zambia (s. 55(4), from 1 January 2026).

## Deadlines and filing

Provisional return by 31 March (within 90 days of registration if later). Instalments due 31 March, 30 June, 30 September, 31 December, payable by 10 April, 10 July, 10 October, 10 January. Annual return and balance by 21 June of the following year.

**How to file the annual return.** Log in at the ZRA portal (www.zra.org.zm, tax portal) with TPIN, password and captcha, enter the one-time password sent to email and phone, then choose Returns, File a return. Enter tax type Income Tax, account name and return period (1 January of the charge year; year end fills in). Click Next. Complete the balance sheet (it turns green when balanced) and income statement. Click Next. Choose income sources and enter income and expenditure summaries. Complete the tax computation and remaining schedules. Confirm the summary. Upload certificate ITF 56 A or B signed by you or the preparer. Click Submit. The return can be amended.

**Provisional return.** Same login, tax type Income Tax, return period as above, Next, choose income source, enter expected taxable income, Next, confirm, Submit. A reference number is generated. It can be amended as often as needed.

## Penalties and interest

Late return: 2,000 penalty units (K800) per month or part month for a company; one penalty unit is K0.40. Income understated so tax is underpaid by at least one-third: 25% of the underpayment. Late payment: 5% plus interest at the Bank of Zambia discount rate plus 2%. From 1 January 2026, failure to pay tax under s. 77(4) carries 0.5% per month (s. 78(2A)). Incorrect returns per ZRA penalties page: negligence 17.5%, wilful default 35%, fraud 52.5%. New s. 91A: no penalty on voluntary disclosure before ZRA finds the error.

## Cross-border points

A non-resident's fixed place of business is no longer preparatory or auxiliary if related activity at it combines into something more (s. 81AA(2A), from 1 January 2026). Remittances above USD 2,000 without a valid tax clearance certificate draw advance income tax. Treaty rates: ZRA DTA table. Transfer pricing and treaty method: no skill yet.

## Two worked examples that recompute

**Simple.** ZRA example: profit K1,150,000 plus K100,000 staff entertainment added back.

```oa-check
name: Company at 30%
inputs:
  profit: 1150000
  addback: 100000
steps:
  - taxable: profit + addback
  - tax: taxable * 0.30
expected:
  tax: 375000.00
```

**Decision: does MAT bite?** Turnover K10,000,000, taxable profit K100,000. Income tax is K30,000; MAT is K100,000. If MAT exceeds income tax, the unused credit carries forward. Treatment of the unused credit against a later year is read from s. 14A(3) and (4).

```oa-check
name: MAT against income tax
inputs:
  turnover: 10000000
  taxable: 100000
steps:
  - mat: turnover * 0.01
  - cit: taxable * 0.30
  - unused_credit: max(mat - cit, 0)
expected:
  mat: 100000.00
  unused_credit: 70000.00
```

## Ask the client first

- Turnover, and is any of it management or consultancy?
- Sector (mining, farming, telecoms, manufacturing)?
- ZDA licence and its date?
- Resident, or a branch of a non-resident?
- Payments to non-residents, and is there a treaty?
- Losses or MAT credits brought forward?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) (No. 2) Act No. 17 of 2025, whole Act; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf | 2026-11-01 |
| Income Tax (Amendment) Act No. 10 of 2025, whole Act; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf | 2026-11-01 |
| ZRA Payment Due Dates page; read: full text of the pages listed | https://www.zra.org.zm/payment-due-dates/ | 2026-11-01 |
| ZRA Penalties page (penalty unit K0.30: stale against the 2026 leaflets); read: full text of the pages listed | https://www.zra.org.zm/penalties/ | 2026-11-01 |
| ZRA Guide to Filing Tax Returns (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Guide-to-Filing-Tax-Returns.pdf | 2026-11-01 |
| ZRA leaflet Introduction to Income Tax (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-Income-Tax.pdf | 2026-11-01 |
| ZRA Practice Notes 2023, section 48 tax rates (latest notes found); read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2023/02/Practice-Notes-2023.pdf | 2026-11-01 |
| ZRA DTA rates table; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2023/09/DTA-Rates.pdf | 2026-11-01 |
| ZRA Advance Income Tax on remittances leaflet (2026), first page; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/08/Refunds-of-Advance-Income-Tax-on-Remittance.pdf | 2026-11-01 |

Not yet confirmed: the MAT regulations under s. 14A(6), and when MAT is paid; WHT on royalties and management fees (old file 15% and 20%); WHT on resident interest (old 15%); telecoms threshold (old file said higher rate above a threshold, 2023 note says a single 35%); old 15% agriculture rate (ZRA now says 10%); consolidated Income Tax Act not opened; whether 5% late payment still applies beside new s. 78(2A).

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
