---
name: ny-llc-filing-fee-it-204-ll
description: New York annual filing fee for LLCs, LLPs and partnerships on Form IT-204-LL (Tax Law 658(c)(3)), for tax year 2026. Who must file (a disregarded single-member LLC with any New York source income, gain, loss or deduction; an LLC or LLP treated as a partnership with New York source items; a regular partnership with New York source gross income of at least $1 million in the preceding year), who does not (no New York source items, an LLC taxed as a corporation), the fee ($25 for a disregarded LLC; $25 to $4,500 on preceding-year New York source gross income for LLCs and LLPs; $500 to $4,500 for regular partnerships), no proration, the due date (15th day of the third month, 15 March 2027 for calendar 2026) and no extension. Trigger on "IT-204-LL", "New York LLC fee", "NY LLC filing fee", "LLC annual fee New York", "partnership filing fee New York". New York only.
version: "1.0"
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: computation
---

# New York LLC, LLP and partnership filing fee (Form IT-204-LL), tax year 2026

> **Source-cited draft.** Built from Tax Law 658(c)(3), the Tax Department's annual filing fee page, its current Form IT-204-LL instructions page and the 2025 instructions for Form IT-204-LL, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A New York LLC is not taxed on its income, but it may owe a yearly filing fee on Form IT-204-LL.

- A **single-member LLC disregarded for federal tax** pays a flat **USD 25** for any year in which it has any income, gain, loss or deduction from New York sources.
- An **LLC or LLP treated as a partnership** with New York source items pays **USD 25 to USD 4,500**, set by its New York source gross income for the **preceding** tax year (USD 25 if it had none).
- A **regular partnership** (not an LLC or LLP) pays only if its preceding-year New York source gross income was **at least USD 1 million**: USD 500 to USD 4,500.
- No New York source items in the year, or an LLC taxed as a corporation: no form, no fee.

The fee for calendar 2026 is due **Monday 15 March 2027**. There is **no extension**, and the fee is not prorated for a short year.

## Scope and who this is for

In scope: whether Form IT-204-LL must be filed for a 2026 tax year, the fee amount for each kind of filer, the New York source gross income used for the fee, the due date, payment and the consequences of not paying.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Forming the LLC, publication, biennial statement | `ny-formation` |
| The member's own New York return (Schedule C income of a disregarded LLC) | `ny-it-201-resident-return` |
| The partnership return, Form IT-204, and nonresident partner estimates | `us-form-1065-partnership` (federal); refer for IT-204 |
| New York City unincorporated business tax | `nyc-ubt` |
| Pass-through entity tax election | `ny-pte-tax-ptet` |
| LLCs taxed as corporations (Article 9-A) | `ny-corporate-franchise-article-9a` |

## Ask the client first

1. **How is the entity classified for federal tax?** Disregarded single-member LLC, partnership (LLC, LLP or regular partnership), or an LLC that elected to be taxed as a corporation (Form 8832 or 2553).
2. **Did it have any income, gain, loss or deduction from New York sources in 2026?** A New York office, shop or other place where its affairs are regularly carried on, regular business transactions in New York, New York real property, or a sale of an interest in an entity owning New York real property.
3. **For a partnership-taxed LLC, LLP or regular partnership: what was its New York source gross income for 2025** (the preceding tax year), from the Form 1065 lines on the IT-204-LL worksheet?
4. **What is its tax year?** Calendar or fiscal, and was 2026 a short year (formed or ended in the year)?
5. **Is this the final year?** A final IT-204-LL also needs the Department of State registration ended.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Fee, LLC disregarded for federal tax, with any New York source income, gain, loss or deduction | USD 25 | [Tax Law 658(c)(3)](https://www.nysenate.gov/legislation/laws/TAX/658) |
| Fee, LLC or LLP treated as a partnership: preceding-year New York source gross income not more than USD 100,000 (or none) | USD 25 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, LLC or LLP: more than USD 100,000, not more than USD 250,000 | USD 50 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, LLC or LLP: more than USD 250,000, not more than USD 500,000 | USD 175 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, LLC or LLP: more than USD 500,000, not more than USD 1,000,000 | USD 500 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, LLC, LLP or regular partnership: more than USD 1,000,000, not more than USD 5,000,000 | USD 1,500 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, LLC, LLP or regular partnership: more than USD 5,000,000, not more than USD 25,000,000 | USD 3,000 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, LLC, LLP or regular partnership: more than USD 25,000,000 | USD 4,500 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Fee, regular partnership: preceding-year New York source gross income of exactly USD 1,000,000 | USD 500 | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Regular partnership: no fee and no form if preceding-year New York source gross income is less than | USD 1,000,000 | [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf) |
| Due date | 15th day of the third month after the tax year ends (15 March 2027 for calendar 2026) | [Tax Law 658(c)(3)](https://www.nysenate.gov/legislation/laws/TAX/658) |

The fee table has applied to taxable years beginning in 2008 and after and is not indexed ([Tax Law 658(c)(3)(B)](https://www.nysenate.gov/legislation/laws/TAX/658)).

### Steps

1. **Classify the entity.** An LLC or LLP that elected to be treated as a corporation for federal tax does not file IT-204-LL. New York follows the federal classification of LLCs and LLPs ([IT-204-LL instructions page](https://www.tax.ny.gov/forms/current-forms/it/it204lli.htm)).
2. **Test New York source items for the current year (2026).** The fee is due only if the entity had income, gain, loss or deduction from New York sources in the year, determined under Tax Law 631 as for a nonresident individual ([Tax Law 658(c)(3)(A)](https://www.nysenate.gov/legislation/laws/TAX/658)). A net loss from New York sources still counts: mark Yes on line 1 ([IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf)). New York source items include:
   - income from a business, trade, profession or occupation carried on in New York: the entity keeps an office, shop, store, warehouse, factory, agency or other place in New York where its affairs are systematically and regularly carried on, or performs a series of acts in New York with regularity and continuity for livelihood or profit;
   - income from real property in New York, including gain or loss on selling an interest in an entity whose New York real property and cooperative shares are at least 50% of the fair market value of the assets it has owned for at least two years;
   - income from intangible property used in a business carried on in New York;
   - gain on the sale of a partnership interest subject to IRC 1060, on or after 10 April 2017.
   Source: [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf).
3. **Do not file when** the entity has no New York source items in the year, even if it is formed in New York or dormant, or files a New York partnership return only because it has a New York resident partner ([Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm)).
4. **Find the fee.**
   - Disregarded LLC: USD 25 (Part 3, line 7). Skip Part 2.
   - LLC or LLP treated as a partnership: compute New York source gross income for the **preceding** tax year (2025 for the 2026 fee) on the worksheet (line 4), and take the fee from the LLC/LLP table (line 5). New York source gross income is the members' shares of federal gross income from New York sources, with no deduction for cost of goods sold. If the entity did not exist in the preceding year, or had no New York source gross income, the fee is USD 25.
   - Regular partnership: the same worksheet; if line 4 is under USD 1,000,000, no fee is due and the form is not filed.
   Sources: [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm); [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf).
5. **Do not prorate.** The fee is the full amount even for a short federal tax year ([IT-204-LL instructions page](https://www.tax.ny.gov/forms/current-forms/it/it204lli.htm)).
6. **No credit offsets the fee** ([Tax Law 658(c)(3)(C)](https://www.nysenate.gov/legislation/laws/TAX/658)).
7. **File and pay** (Part 4, line 8, the amount from line 5 or line 7) by the due date (see "Filing and payment").

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Disregarded LLC owned by a New York resident, running a business from a Brooklyn home office | New York source business income: file, USD 25 | [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf) |
| Disregarded LLC with no activity at all in 2026 (dormant) | No New York source items: do not file | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Disregarded LLC whose only item is bank interest | Interest is sourced as for a nonresident: not New York source unless from intangibles used in a New York business. If it has no other New York items, do not file; if in doubt, refer | [Tax Law 658(c)(3)(A)](https://www.nysenate.gov/legislation/laws/TAX/658); [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf) |
| New York-formed LLC doing all its business in New Jersey | No New York source items: do not file, even though formed in New York | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Out-of-state LLC with a New York office | Has New York source items: file | [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf) |
| Partnership-taxed LLC formed in 2026 | No preceding-year New York source gross income: USD 25 | [Tax Law 658(c)(3)(B)](https://www.nysenate.gov/legislation/laws/TAX/658) |
| Partnership-taxed LLC with a New York loss in 2026 | Still files (a loss is a New York source item); fee on 2025 gross income | [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf) |
| LLC that elected S corporation or C corporation treatment | Does not file IT-204-LL; corporate tax rules apply | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Regular partnership with USD 900,000 of 2025 New York source gross income | No fee, do not file | [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf) |
| Gross income exactly on a band edge (for example USD 250,000) | The lower band: "not more than" | [Tax Department, annual filing fee](https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm) |
| Disregarded LLC with no EIN or New York temporary number | Enter the member's Social Security number | [IT-204-LL instructions page](https://www.tax.ny.gov/forms/current-forms/it/it204lli.htm) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Federal classification | Ask; do not assume disregarded if there may be two members or an election |
| Whether there was New York activity | Ask what the LLC did and where; file if there is any New York business, property or loss |
| Preceding-year New York source gross income | Ask for the 2025 Form 1065 and IT-204; do not use 2026 figures |
| Prior years not filed | Flag as a past-due item; file the current year on time and refer the catch-up |

### Red flags

| Flag | Why it matters |
| --- | --- |
| Fee paid late or not paid | Assessed and collected like a tax, with penalty and interest |
| Partnership near a band edge in the preceding year | The fee is set by the preceding year's figure, not the current year |
| The client thinks the biennial statement or publication covers this | They are Department of State filings; IT-204-LL is a separate Tax Department fee |
| LLC with New York City activity | New York City unincorporated business tax may also apply: `nyc-ubt` |

## Worked cases

**Case 1, the fee for three entities, tax year 2026.** (a) A disregarded single-member LLC of a Brooklyn designer with New York business income in 2026: USD 25. (b) A two-member LLC treated as a partnership with 2025 New York source gross income of USD 640,000: more than USD 500,000 and not more than USD 1,000,000, so USD 500. (c) A regular general partnership with 2025 New York source gross income of USD 3,200,000: at least USD 1,000,000, and more than USD 1,000,000 but not more than USD 5,000,000, so USD 1,500. All three are due 15 March 2027. Total fees: USD 2,025.

```oa-check
name: IT-204-LL fees for a disregarded LLC, an LLC partnership and a regular partnership, 2026
inputs:
  disregarded_fee: 25
  llc_prior_gross: 640000
  partnership_prior_gross: 3200000
steps:
  - llc_in_500_band: min(1, ceil(max(llc_prior_gross - 500000, 0) / 100000000)) * (1 - min(1, ceil(max(llc_prior_gross - 1000000, 0) / 100000000)))
  - llc_fee: llc_in_500_band * 500
  - partnership_in_1500_band: min(1, ceil(max(partnership_prior_gross - 1000000, 0) / 100000000)) * (1 - min(1, ceil(max(partnership_prior_gross - 5000000, 0) / 100000000)))
  - partnership_fee: partnership_in_1500_band * 1500
  - total: disregarded_fee + llc_fee + partnership_fee
expected:
  llc_in_500_band: 1
  llc_fee: 500
  partnership_in_1500_band: 1
  partnership_fee: 1500
  total: 2025
```

**Case 2, a decision: must these two LLCs file for 2026?** LLC A, a disregarded LLC formed in New York in 2024, did nothing in 2026: no income, no expenses, no property. LLC B, a disregarded LLC, sold nothing in 2026 but paid USD 400 of rent for a storage unit in Queens used for its New York business, so it has a New York source deduction (a loss). Decision: A does not file (no New York source items, even though it is a New York LLC); B files and pays USD 25 by 15 March 2027, because a loss or deduction from New York sources triggers the fee.

```oa-check
name: Whether a disregarded LLC must file IT-204-LL (decision)
inputs:
  a_ny_source_items: 0
  b_ny_source_deductions: 400
steps:
  - a_files: min(1, ceil(abs(a_ny_source_items) / 1000000))
  - b_files: min(1, ceil(abs(b_ny_source_deductions) / 1000000))
  - a_fee: a_files * 25
  - b_fee: b_files * 25
expected:
  a_files: 0
  b_files: 1
  a_fee: 0
  b_fee: 25
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-LL-SOURCE | New York source is unclear (remote work, intangibles, interest, sale of an interest in a real property entity) | Refer: Tax Law 631 sourcing as for a nonresident needs the facts |
| R-LL-TIER | Tiered partnerships (the worksheet's lower-tier income lines) | Refer |
| R-LL-PAST | Prior years not filed, or a bill received | Refer; do not file an amended form to dispute a bill |
| R-LL-AMEND | Amended IT-204-LL or refund request | Refer; a refund request is due within three years of filing or two years of payment, whichever is later |
| R-LL-CORP | LLC taxed as a corporation | Use `ny-corporate-franchise-article-9a`; IT-204-LL does not apply |
| R-LL-FISCAL | Fiscal-year or short-year entity with questions on which year is "preceding" | Refer |

## Filing and payment

- **Form:** IT-204-LL, Partnership, Limited Liability Company, and Limited Liability Partnership Filing Fee Payment Form. Part 1 general information and line 1 (New York source items, Yes or No), lines 2 and 3; Part 2 for partnerships, LLCs and LLPs treated as partnerships (line 4 New York source gross income, line 5 fee); Part 3 for disregarded LLCs (line 6, the member; line 7, USD 25); Part 4, line 8, payment.
- **Due:** on or before the 15th day of the third month after the tax year ends; the next business day if that is a Saturday, Sunday or legal holiday. Calendar 2026: Monday 15 March 2027. Calendar 2025 was due 16 March 2026.
- **No extension** of time to file the form or pay the fee.
- **E-file:** required for a filer that prepares its own documents without a tax professional, uses approved e-file software and has broadband; otherwise mail the form and a check payable to "NYS filing fee" (write the EIN or SSN and the year on it) to State Processing Center, PO Box 15310, Albany NY 12212-5310.
- **Not paid on time:** the fee is assessed, collected and paid in the same manner as tax, so penalties and interest apply ([Tax Law 658(c)(3)(D)](https://www.nysenate.gov/legislation/laws/TAX/658)). Use the Tax Department's penalty and interest calculator for amounts.
- **Final year:** mark the final box and contact the Department of State (518-473-2492) to end the registration.
- **Related filings:** domestic LLCs and LLPs register with the Department of State; a partnership-taxed LLC also files Form IT-204 if it meets that form's requirements (calendar 2025 returns were due 16 March 2026).

Sources: [IT-204-LL-I (2025)](https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf); [IT-204-LL instructions page](https://www.tax.ny.gov/forms/current-forms/it/it204lli.htm).

## Completion checklist

- Federal classification confirmed; corporate-taxed LLCs excluded.
- New York source items in 2026 tested as for a nonresident; dormant or New York-only-by-formation LLCs not filed.
- Disregarded LLC: USD 25 on line 7.
- Partnership-taxed LLC or LLP: 2025 New York source gross income on line 4, fee from the LLC/LLP table on line 5 (USD 25 if none).
- Regular partnership: filed only if 2025 New York source gross income was at least USD 1,000,000.
- No proration for a short year; no credits applied.
- Paid by 15 March 2027 (calendar 2026); e-filed where required.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Tax Law 658(c)(3), New York Senate (read through Firecrawl). Read for who pays, the USD 25 minimum and disregarded LLC fee, the preceding-year base, the regular partnership USD 1 million exemption, the fee table, no credits and collection as tax. | https://www.nysenate.gov/legislation/laws/TAX/658 | 2026-11-13 |
| Tax Department, Partnership, LLC, and LLP annual filing fee. Read for who files and who does not, and the LLC/LLP and regular partnership tables. | https://www.tax.ny.gov/pit/efile/annual_filing_fee.htm | 2026-11-13 |
| Tax Department, Instructions for Form IT-204-LL (current forms page). Read for when to file, no proration, Department of State registration, classification and identification numbers. | https://www.tax.ny.gov/forms/current-forms/it/it204lli.htm | 2026-11-13 |
| Instructions for Form IT-204-LL (2025). Read for no extension, the e-file mandate, line 1 New York source income, the line 4 worksheet, line 5 tables, amended returns, refunds and where to file. | https://www.tax.ny.gov/pdf/2025/inc/it204lli_2025.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form IT-204-LL and its instructions were not yet published when read; the line numbers and filing details above are from the 2025 form (2025-2026 filing cycle). The fee amounts come from Tax Law 658(c)(3) and do not change by year.
