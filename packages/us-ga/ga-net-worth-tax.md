---
name: ga-net-worth-tax
description: Compute the Georgia corporate net worth tax for tax year 2026, reported with the income tax on Form 600 (C corporations) or Form 600S (S corporations). Covers who pays (domestic, domesticated and foreign corporations, S corporations, LLCs taxed as corporations; not partnerships or disregarded LLCs), the base of issued capital stock, paid-in surplus and earned surplus, 100% for domestic corporations and the property and gross receipts ratio for foreign ones, the graduated table from $0 at $100,000 or less to $5,000 above $22,000,000, the one-year-later net worth year, initial, short-period and final returns, and the 10% late filing and late payment penalties. Trigger on "Georgia net worth tax", "Form 600 Schedule 2", "Georgia franchise tax", "Georgia S corporation net worth tax".
version: "1.0"
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
type: computation
---

# Georgia corporate net worth tax, tax year 2026

> **Source-cited draft.** Built from the 2025 IT-611 corporate income tax booklet (net worth tax pages and table), DOR's net worth tax FAQ, its corporate income and net worth tax page and its penalty and interest page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Georgia charges corporations a small graduated tax on net worth, separate from income tax but on the same Form 600 or 600S. Net worth is issued capital stock plus paid-in surplus plus earned surplus. A corporation with net worth of **$100,000 or less pays $0 but must still file**; the tax then rises by band to a maximum of **$5,000** above $22,000,000. Domestic and domesticated corporations are taxed on 100% of net worth; foreign corporations on the part employed in Georgia. S corporations pay it too. Partnerships and disregarded single-member LLCs do not.

## Scope and who this is for

In scope: the net worth tax on Form 600 (C corporations) and Form 600S (S corporations) for returns filed in 2026 and 2027, including initial, short-period and final returns. The table has been unchanged since net worth years beginning 1 January 2018 and DOR's 2025 booklet is the latest published; no 2026 change has been found.

Who pays ([DOR net worth tax FAQ](https://dor.georgia.gov/net-worth-tax-corporations-faq); [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download)):

| Entity | Net worth tax |
| --- | --- |
| Georgia (domestic) corporation, C or S | Yes, on 100% of net worth |
| Domesticated foreign corporation | Yes, on 100% of net worth |
| Foreign corporation that does business, owns property or is registered with the Secretary of State in Georgia | Yes, on net worth employed in Georgia (Schedule 8 ratio) |
| LLC that files as a corporation | Yes |
| LLC that files as a partnership; any partnership | No |
| Disregarded single-member LLC | No; but a corporate owner is taxed if the LLC does business or owns property in Georgia |
| Qualified subchapter S subsidiary and its parent | Separate net worth returns; a parent or QSSS with no Georgia registration, business, property or Georgia income (other than through the QSSS) need not file |
| Corporation protected from income tax by Public Law 86-272 | Still taxed; the federal law does not protect against net worth tax |

Out of scope, and where it goes: the corporate income tax on the same return (`ga-corporate-and-ptet`); estimated tax (`ga-estimated-tax-depth`); the Secretary of State annual registration, which is a separate filing (`ga-formation`).

## Ask the client first

1. **Where is the corporation incorporated, and has it domesticated in Georgia?** This decides 100% of net worth or the Georgia ratio.
2. **C or S corporation, and the tax year end?** The initial return is due on a different month for each, and the net worth year runs one year after the income tax year.
3. **The balance sheet (federal Schedule L)** at the end of the prior income tax year: issued capital stock, paid-in surplus and retained earnings (earned surplus).
4. **For a foreign corporation:** assets owned in Georgia and gross receipts from Georgia, against the totals everywhere.
5. **Is this an initial, short-period or final return?** Date of incorporation or qualification, and the year end chosen.

## The method, step by step

### Rates, bands and thresholds

| Net worth | Amount of tax | Source |
| --- | --- | --- |
| Not exceeding $100,000 | $0 (return still required) | [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) |
| Over $100,000, not exceeding $150,000 | $125 | same |
| Over $150,000, not exceeding $200,000 | $150 | same |
| Over $200,000, not exceeding $300,000 | $200 | same |
| Over $300,000, not exceeding $500,000 | $250 | same |
| Over $500,000, not exceeding $750,000 | $300 | same |
| Over $750,000, not exceeding $1,000,000 | $500 | same |
| Over $1,000,000, not exceeding $2,000,000 | $750 | same |
| Over $2,000,000, not exceeding $4,000,000 | $1,000 | same |
| Over $4,000,000, not exceeding $6,000,000 | $1,250 | same |
| Over $6,000,000, not exceeding $8,000,000 | $1,500 | same |
| Over $8,000,000, not exceeding $10,000,000 | $1,750 | same |
| Over $10,000,000, not exceeding $12,000,000 | $2,000 | same |
| Over $12,000,000, not exceeding $14,000,000 | $2,500 | same |
| Over $14,000,000, not exceeding $16,000,000 | $3,000 | same |
| Over $16,000,000, not exceeding $18,000,000 | $3,500 | same |
| Over $18,000,000, not exceeding $20,000,000 | $4,000 | same |
| Over $20,000,000, not exceeding $22,000,000 | $4,500 | same |
| Over $22,000,000 | $5,000 | same |
| Initial return covering less than 6 months | 50% of the table amount | [DOR net worth tax FAQ](https://dor.georgia.gov/net-worth-tax-corporations-faq) |
| Late filing penalty | 10% of the tax due | [DOR penalty and interest rates, O.C.G.A. § 48-13-79](https://dor.georgia.gov/penalty-and-interest-rates) |
| Late payment penalty | 10% of the tax due | same |

Net worth means total net worth for domestic and domesticated corporations (Schedule 2, Line 4) and net worth employed in Georgia for foreign corporations (Schedule 2, Line 6). The $100,000 exemption applies "for net worth years beginning on or after January 1, 2018 (those reported on the 2017 income tax return)": corporations at or below it "are not subject to tax but must file a return".

### Computing the tax

1. **Find the net worth year.** The net worth tax on a return covers the year after the income tax year: DOR says the net worth dates "would be one year later than the income tax beginning and ending dates". A calendar 2026 Form 600 reports income tax for 2026 and net worth tax for 2027.
2. **Measure net worth** on the prior year's ending balance sheet (for that calendar 2026 return, the 31 December 2026 balance sheet): issued capital stock plus paid-in surplus plus earned surplus (retained earnings). Treasury stock is not deducted. A deficit net worth still requires a return but owes no tax.
3. **Domestic or domesticated corporation:** use 100% of net worth (Schedule 2, Line 4).
4. **Foreign corporation:** multiply net worth by the Georgia ratio from Schedule 8, built from property and gross receipts within Georgia against the totals everywhere. For property, the everywhere amount is the ending balance sheet assets from the federal return; the Georgia amount uses assets owned in Georgia ([DOR net worth tax FAQ](https://dor.georgia.gov/net-worth-tax-corporations-faq)).
5. **Look up the band** in the table. Bands are "over" the lower figure and "not exceeding" the upper.
6. **Adjust for the period:**
   - **Initial return:** based on the opening net worth at the date of incorporation or qualification; covers that date to the end of the first income tax year; if that period is under 6 months, 50% of the tax. No income tax is reported on it and it cannot be combined with the first income tax return. The first income tax return then carries a full year's net worth tax for the next year.
   - **Short period** (other than initial or final): net worth from the short period's ending balance sheet, tax prorated by the months in the period. A short period ending on the 1st to 15th of a month is backed up to the last day of the previous month; one ending on the 16th or later moves to the end of that month.
   - **Final return:** a corporation that liquidates and files its final income tax return owes no net worth tax and gets no refund of net worth tax already paid.
7. **Enter it on the same Form 600 or 600S** as the income tax and pay by the return's original due date. Dormant corporations must still file and pay.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Net worth exactly $100,000 | $0 ("not exceeding $100,000"), return still due |
| Net worth $100,001 | $125 |
| Net worth exactly $150,000 | $125 (the band is "not exceeding $150,000") |
| S corporation owner says "my S corporation pays no Georgia tax" | Income passes through, but net worth tax is charged on the corporation |
| Negative net worth | Return filed, no tax |
| Consolidated income tax group | Each subsidiary files its own net worth return; no consolidation |
| Foreign corporation considering domestication | Domestication moves it to 100% of net worth; compare before deciding (Case 1) |
| Initial period from 18 March to 31 October | More than 6 months, so the full table amount is due (DOR's own example) |

## Worked cases

Client facts are invented; the table and rules are DOR's.

**Case 1, a decision: should a foreign corporation domesticate?** A Delaware corporation registered in Georgia has total net worth of $10,000,000 and a Georgia Schedule 8 ratio of 25%. As a foreign corporation, net worth employed in Georgia is $2,500,000, in the $2,000,000 to $4,000,000 band: $1,000. If it domesticated, it would be taxed on the full $10,000,000, in the $8,000,000 to $10,000,000 band: $1,750. Staying foreign saves $750 a year of net worth tax; domestication needs a non-tax reason.

```oa-check
name: GA net worth tax, foreign against domesticated corporation
inputs:
  total_net_worth: 10000000
  georgia_ratio: 0.25
  band_tax_foreign: 1000
  band_tax_domesticated: 1750
steps:
  - georgia_net_worth: total_net_worth * georgia_ratio
  - extra_cost_if_domesticated: band_tax_domesticated - band_tax_foreign
expected:
  georgia_net_worth: 2500000
  extra_cost_if_domesticated: 750
```

The band amounts are read from the table: $2,500,000 is over $2,000,000 and not over $4,000,000; $10,000,000 is over $8,000,000 and not over $10,000,000.

**Case 2: short period and initial return.** DOR's own example: a three-month short period with Georgia taxable net worth of $900,000 (the $750,000 to $1,000,000 band, $500) owes $500 x 3/12 = $125. A new corporation whose initial period runs four months, with opening net worth of $900,000, owes 50% of $500 = $250 because the period is under 6 months.

```oa-check
name: GA net worth tax, short period and initial return under 6 months
inputs:
  band_tax: 500
  short_period_months: 3
  initial_period_months: 4
steps:
  - short_period_tax: band_tax * short_period_months / 12
  - initial_tax: band_tax * 0.5
expected:
  short_period_tax: 125
  initial_tax: 250
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GANW-RATIO | Foreign corporation with complex property or receipts sourcing for Schedule 8 | Refer |
| R-GANW-REORG | Mergers, conversions, domestications and liquidations mid-year | Refer: the period rules interact with the Secretary of State filings |
| R-GANW-SPECIAL | Insurance companies, financial institutions, exempt organizations | Refer |
| R-GANW-NOTICE | DOR notice for unfiled net worth returns over several years | Refer; consider voluntary disclosure |

## Filing and payment

Source: [2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download); [DOR net worth tax FAQ](https://dor.georgia.gov/net-worth-tax-corporations-faq); [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates).

1. **With the annual return:** the 15th day of the 4th month after the income tax year end for C corporations (Form 600; 15 April 2027 for calendar 2026) and the 15th day of the 3rd month for S corporations (Form 600S; 15 March 2027). File through the Georgia Tax Center or approved software.
2. **Initial net worth return:** the 15th day of the 4th month after incorporation or qualification for C corporations (net worth years beginning on or after 1 January 2017), and the 15th day of the 3rd month for S corporations.
3. **Payment** by the original due date; an extension of the return does not extend payment.
4. **Penalties:** late filing 10% of the tax due; late payment 10% of the tax due, whether or not the return is filed (O.C.G.A. § 48-13-79). Interest at the Federal Reserve prime rate plus 3% a year, reviewed each January.

## Completion checklist

- Net worth year is the year after the income tax year; balance sheet is the prior year-end one.
- Base is issued capital stock plus paid-in surplus plus earned surplus; treasury stock not deducted.
- 100% for domestic and domesticated corporations; Schedule 8 ratio for foreign ones.
- Band read with "over" and "not exceeding"; return filed even at $0.
- Initial return under 6 months at 50%; short period prorated by months; final return owes none.
- Paid by the original due date with the income tax.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 IT-611 corporate income tax booklet. Read for the net worth tax general information pages, the net worth tax table, the initial and short-period rules and DOR's $900,000 short-period example. | https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download | 2026-11-13 |
| DOR net worth tax for corporations FAQ. Read for the net worth year, initial and short-period returns, the 6-month 50% rule, QSSS, LLCs and the foreign corporation ratio. | https://dor.georgia.gov/net-worth-tax-corporations-faq | 2026-11-13 |
| DOR corporate income and net worth tax page. Read for the page as a whole. | https://dor.georgia.gov/taxes/corporate-income-and-net-worth-tax | 2026-11-13 |
| DOR penalty and interest rates. Read for the corporate net worth penalties (10% late filing, 10% late payment, O.C.G.A. § 48-13-79) and the interest rule. | https://dor.georgia.gov/penalty-and-interest-rates | 2026-11-13 |

Not yet confirmed: the 2026 IT-611 booklet was not published when read, so the table is taken from the 2025 booklet (2025-2026 filing cycle); no change to O.C.G.A. § 48-13-73 for 2026 was found, but the statute itself was not opened. The older file's claims that the base is the greater of capital stock plus paid-in capital or net worth, that there is a $10 minimum and that short periods are never prorated are not supported by DOR's pages and were dropped.
