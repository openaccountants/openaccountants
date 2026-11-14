---
name: pa-corporate-tax
description: "Use this skill for Pennsylvania corporate net income tax (CNIT) on Form RCT-101 for tax year 2026. It covers who must file (C corporations, LLCs taxed as corporations, PA S corporations with built-in gains, the $500,000 economic nexus presumption), the 7.49% rate for tax years beginning in 2026 on the scheduled phase-down to 4.99% in 2031, the starting point at federal taxable income before the NOL and special deductions, the main additions and deductions (bonus depreciation, Act 45 of 2025 research and qualified production property decoupling, the section 163(j) freeze), single sales factor apportionment, the net operating loss caps of 40% and 50%, due dates, extensions, estimated payments and penalties. Trigger on \"Pennsylvania corporate tax\", \"PA CNIT\", \"RCT-101\", \"corporate net income tax Pennsylvania\", \"PA corporate rate 2026\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pa-corporate-tax"
  jurisdiction: "US-PA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Pennsylvania corporate net income tax (RCT-101), tax year 2026

> **Built from the law, not yet approved by an accountant.** Written from the Pennsylvania Department of Revenue (DOR) corporate net income tax page, the 2025 RCT-101 instructions (REV-1200), the 2025 RCT-103 and the DOR Tax Compendium, read on 13 November 2026. Review by a qualified professional before filing.

**Quick reference, tax year 2026**

| Item | 2026 figure | Condition |
| --- | --- | --- |
| Rate | 7.49% | Tax years beginning 1 January 2026 to 31 December 2026 ([DOR CNIT page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax)) |
| Base | Federal taxable income (Form 1120 line 28, before NOL and special deductions), with PA additions and deductions | Separate company basis ([REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf)) |
| Apportionment | Single sales factor (100% sales) | Only if taxable in at least one other state ([REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf)) |
| NOL cap | 40% of taxable income for losses from before 2025; up to 50% in total once losses from 2025 on are used | 2026 tax years, Act 56 of 2024 ([DOR Tax Compendium](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/reportsstats/taxcompendium/documents/2025_tax_compendium.pdf)) |
| Return | RCT-101, e-filed through IRS MeF (Fed/State e-File) | Due the 15th day of the month after the federal due date ([REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf)) |
| Calendar 2026 due date | 17 May 2027 (15 May 2027 is a Saturday) | Federal extension extends the RCT-101 automatically ([REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf)) |

## Scope and who this is for

- **In:** corporations subject to CNIT for 2026: domestic and foreign corporations doing business, carrying on activities, having capital or property employed or used in Pennsylvania, owning property here, or having substantial nexus. "Any entity classified as a corporation for federal income tax purposes is considered a corporation in Pennsylvania", so an LLC taxed as a C corporation files ([DOR CNIT page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax)).
- **Also in:** PA S corporations with built-in gains, which file RCT-101 and pay CNIT on net recognized built-in gains under IRC 1374(d)(2) ([REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf)).
- **Exempt (DOR CNIT page):** certain qualifying not-for-profit organizations, homeowners' associations, membership organizations, agricultural cooperatives, business trusts, and non-PA companies that limit activity to solicitation of orders for tangible personal property; and corporations subject to bank and trust company shares tax, mutual thrift tax or title insurance company shares tax.
- **Out:** a federal S corporation that stays a PA S corporation pays no CNIT on ordinary income; its owners are taxed under `pa-income-tax`. The capital stock and foreign franchise tax was phased out for tax years beginning on or after 1 January 2016 (REV-1200). Gross receipts, gross premiums, bank shares and other corporate taxes are out of scope. Philadelphia's Business Income and Receipts Tax is a city tax and out of scope.
- **Federal starting figures** come from `us-form-1120-c-corp`; this skill does not restate them.

## Ask the client first

1. **Tax year and entity:** the first day of the tax year (it picks the rate), and whether the company files federal Form 1120, or is a federal S corporation that has elected out of PA S status on REV-976 or has built-in gains.
2. **Pennsylvania activity:** property, payroll or people in Pennsylvania, or Pennsylvania-sourced gross receipts of $500,000 or more (the economic nexus presumption). Solicitation of orders only?
3. **Other states:** is the company taxable in at least one other state? If not, it does not apportion.
4. **Sales by destination:** total sales everywhere and sales sourced to Pennsylvania, for the single sales factor.
5. **Federal items Pennsylvania adjusts:** bonus depreciation under IRC 168(k), qualified production property under 168(n), research expenditures under 174 or 174A, the 163(j) interest limit, taxes on income deducted federally, related-party intangible or interest expenses.
6. **Loss history:** PA net loss carryforwards by year of origin, split into losses from before 2025 and losses from 2025 on, and any section 381 or 382 limit.

## The method, step by step

1. **Decide whether the company files.** Corporations with nexus file every year, "even if no business activity was conducted" (REV-1200). A non-PA corporation claiming exemption with $500,000 or more of PA-sourced gross receipts still files the RCT-101 and explains its position.
2. **Start from federal taxable income** on a separate company basis: "federal taxable income as reported on line 28 of the Federal Form 1120" (DOR CNIT page), which is before the federal NOL deduction and special deductions (REV-1200, Schedule C-1 and line 1). A company in a federal consolidated return files a pro forma 1120 for itself.
3. **Recalculate the interest limit.** Act 45 of 2025: for tax years beginning after 31 December 2024, taxable income is figured "as if Section 163(j) of the Internal Revenue Code applied as it was in effect on December 31, 2024". Show it on the pro forma 1120; there is no separate RCT-101 line ([DOR Act 45 of 2025](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax/act-45-of-2025)).
4. **Additions (RCT-101 Section C line 3):** taxes imposed on or measured by net income and deducted federally (with REV-860), including the net income portion of Philadelphia BIRT; federal bonus depreciation under 168(k) (REV-1834 Schedule C-8); 168(n) qualified production property depreciation (Schedule C-10); research expenditures deducted federally under 174, 174A, 59(e) or 481 (REV-1826 Schedule C-15); related-party intangible and interest expenses (Act 52 of 2013) (REV-1200).
5. **Deductions (line 2):** the PA depreciation allowed for 168(k) property in place of bonus (Schedule C-8, Act 89 of 2002 and Act 72 of 2018), PA depreciation on 168(n) property under 167 and 168 without 168(n) (Schedule C-10), research expenditures at 20% a year (Schedule C-15), exempt US obligation interest net of related expenses, dividends received, and wages disallowed federally under IRC 45B or 51 ([DOR Tax Compendium, CNIT tax base](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/reportsstats/taxcompendium/documents/2025_tax_compendium.pdf)).
6. **Apportion if taxable elsewhere.** A taxpayer "must have income from business activities taxable by Pennsylvania and at least one other state to allocate and apportion income" (REV-1200, Apportionment and Allocation). The factor is sales only: PA sales over sales everywhere (RCT-106). Nonbusiness income is allocated on REV-934. If all business is in Pennsylvania, skip lines 5 to 9.
7. **Net operating loss deduction (line 11, RCT-103)** under the 2026 caps below.
8. **Tax (line 12 and on):** PA taxable income times 7.49%, less restricted credits (RCT-101 credits schedule) and estimated payments.

### Rates, bands and thresholds

| Item | Amount | Condition | Source |
| --- | --- | --- | --- |
| CNIT rate, tax years beginning in 2026 | 7.49% | "January 1, 2026 through December 31, 2026: 7.49 percent" | [DOR CNIT page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax) |
| Rate, tax years beginning in 2025 | 7.99% | A fiscal year beginning in 2025 keeps 7.99% for its whole year | same |
| Scheduled rates after 2026 | 6.99% (2027), 6.49% (2028), 5.99% (2029), 5.49% (2030), 4.99% (2031 and later) | Already enacted; no trigger | same |
| Sales factor weight | 100% | 2022 to 2029 tax periods | [REV-1200 rate table](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf) |
| NOL cap, losses from before 2025 | 40% of taxable income | Every year | [DOR Tax Compendium 2025, NOL cap table](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/reportsstats/taxcompendium/documents/2025_tax_compendium.pdf) |
| NOL cap, adding losses from 2025 on | Bring total usage to 50% of taxable income | Tax year 2026; 60% in 2027, 70% in 2028, 80% in 2029 and later (Act 56 of 2024) | same |
| Economic nexus presumption | $500,000 of PA-sourced gross receipts | Rebuttable; 72 P.S. 7402 and Corporation Tax Bulletin 2019-04 | [REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf) |
| Research expenditure deduction | 20% a year of the amount added back | Tax years beginning after 31 December 2024 | [DOR Act 45 of 2025](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax/act-45-of-2025) |
| Late filing penalty | $500 minimum, plus 1% of any determined liability over $25,000 | Per late report | [REV-1200](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf) |
| Electronic payment | Required for payments of $1,000 or more | All corporation tax payments | same |
| Interest on late tax, 2026 | 7% a year (daily 0.000192) | Tax due 1 January 2025 to 31 December 2026 | [REV-1611](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/otherforms/documents/rev-1611.pdf) |

The 2026 RCT-101 and REV-1200 were not published when read. The 2025 instructions apply the 2026 rate and caps only in their rate table; the 2026 line numbers may move.

### Net operating loss ordering for 2026

From the Tax Compendium table for 2026: "Losses before tax year 2025: 40% of taxable income. Losses in tax years 2025 and after: bring total usage to 50% of taxable income." So deduct pre-2025 losses first up to 40% of PA taxable income, then 2025 and later losses until the total reaches 50%. If the company has no pre-2025 losses, 2025 and later losses alone can reach 50%. Short periods count as one tax year for the carryforward (REV-1200, line 11).

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Fiscal year 1 July 2025 to 30 June 2026 | 7.99%: the rate follows the year the tax period begins | DOR CNIT page |
| Fiscal year beginning 1 February 2026 | 7.49% for the whole year | DOR CNIT page |
| No other state can tax the company | No apportionment; all business income is PA income | REV-1200 |
| PA sales factor left as 0/0 | Not allowed; REV-1200 cautions against completing the sales factor as 0/0 | REV-1200, Schedule C-1 |
| Federal S corporation, no REV-976 | PA S corporation: no CNIT except on built-in gains | REV-1200 |
| Federal S corporation wanting C treatment in PA | REV-976 signed by all shareholders, by the due date or extended due date of the first year | REV-1200 |
| Federal extension granted | RCT-101 extended automatically; include the federal extension request | REV-1200 |
| No federal extension | 60-day PA extension on myPATH or REV-853, filed by the due date | REV-1200 |
| Bonus depreciation taken federally | Add back on Schedule C-8; recover through PA depreciation and, on disposal, Schedule C-9 | REV-1200 |
| 168(n) qualified production property | Add back; depreciate under 167 and 168 without 168(n) | DOR Act 45 of 2025 |
| Small business that re-expensed 2022 to 2024 domestic research federally | File RCT-128C within six months of the amended federal return | DOR Act 45 of 2025 |
| Other businesses with unamortized 2022 to 2024 research costs | Amortize for PA at 20% a year over five years from 2025 | DOR Act 45 of 2025 |
| Pre-2025 NOL only, 2026 | Deduction capped at 40% | Tax Compendium |
| 2025 loss only, 2026 | Deduction capped at 50% | Tax Compendium |
| Report filed late | Wait for the assessment to pay the penalty; do not add it to RCT-101 | REV-1200 |
| Change in federal taxable income | Report it to DOR on RCT-128C | REV-1200 |

## Worked cases

Illustrations with assumed facts; the rate and caps are the 2026 figures above.

**Case 1: all business in Pennsylvania, two layers of losses.** A calendar 2026 corporation has PA taxable income before the NOL of $1,000,000. It carries a $600,000 loss from 2023 and a $300,000 loss from 2025. Pre-2025 cap: 40% x $1,000,000 = $400,000, so $400,000 of the 2023 loss is used. Total cap: 50% = $500,000, so $100,000 of the 2025 loss is used. NOL deduction $500,000; PA taxable income $500,000; **tax $500,000 x 7.49% = $37,450.** Carried forward: $200,000 of the 2023 loss and $200,000 of the 2025 loss.

```oa-check
name: PA CNIT 2026, NOL caps 40% and 50%
inputs:
  income: 1000000
  nol_pre2025: 600000
  nol_2025: 300000
steps:
  - use_old: min(nol_pre2025, income * 0.40)
  - use_new: min(nol_2025, income * 0.50 - use_old)
  - taxable: income - use_old - use_new
  - tax: taxable * 0.0749
expected:
  use_old: 400000
  use_new: 100000
  taxable: 500000
  tax: 37450.00
```

**Case 2: multistate company, and which rate year applies.** A corporation taxable in several states has apportionable business income of $4,000,000, PA sales of $2,000,000 and sales everywhere of $8,000,000. Factor 25%; PA income $1,000,000; no losses. If its tax year began 1 January 2026, **tax is $1,000,000 x 7.49% = $74,900.** If instead its fiscal year began 1 July 2025, the whole year is at 7.99%: $79,900. The beginning date of the year, not the filing date, decides the rate, so the fiscal-year filer pays $5,000 more on the same income.

```oa-check
name: PA CNIT single sales factor, 2026 vs FY beginning 2025
inputs:
  income: 4000000
  pa_sales: 2000000
  all_sales: 8000000
steps:
  - factor: pa_sales / all_sales
  - pa_income: income * factor
  - tax_2026: pa_income * 0.0749
  - tax_fy2025: pa_income * 0.0799
  - difference: tax_fy2025 - tax_2026
expected:
  factor: 0.25
  pa_income: 1000000
  tax_2026: 74900.00
  tax_fy2025: 79900.00
  difference: 5000.00
```

## When to refuse or refer

- Unitary or nonbusiness income disputes, alternative apportionment petitions, and market sourcing of services or intangibles where the customer location is unclear.
- Related-party addback exceptions and the related party income election.
- Section 381 or 382 limited losses, mergers and liquidations (RCT-103 ML).
- Restricted credits (Keystone Opportunity Zone, research and development, manufacturing credits) and the Qualified Manufacturing Innovation and Reinvestment Deduction.
- Bank shares, mutual thrift, insurance premiums and gross receipts taxpayers.
- Assessments, Board of Appeals petitions and voluntary disclosure.
- Philadelphia BIRT and other local business taxes.

## Filing and payment

1. **Register** the corporation for corporation taxes through myPATH (Pennsylvania Online Business Tax Registration) if it is not already registered.
2. **Prepare RCT-101** with the schedules that apply: complete copy of the federal return on a separate company basis; RCT-103 for losses; RCT-106 for the sales factor; REV-1834 Schedules C-8, C-9 and C-10; REV-1826 Schedule C-15; REV-860 for taxes deducted; REV-934 for nonbusiness income; REV-798 Schedule X for parent and subsidiary details (REV-1200, filing requirements).
3. **File** through IRS Modernized e-File (Fed/State e-File) with approved software ([DOR CNIT page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax)).
4. **Due date:** "on or before the 15th day of the month following the due date of the return to the Federal Government for both calendar and fiscal year filers"; next business day for a weekend or holiday (REV-1200). For a calendar 2026 year with a federal due date of 15 April 2027, that is 17 May 2027.
5. **Extension:** automatic with a federal extension (include the request); otherwise a 60-day extension on myPATH or REV-853, filed by the due date. An extension does not extend payment; interest runs from the original due date.
6. **Estimated payments:** equal installments on or before the 15th day of the third, sixth, ninth and twelfth months of the tax year, on myPATH or with REV-857; the safe harbour is in 72 P.S. 10003.3 ([PA Tax Update No. 226](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/taxupdate/documents/taxupdate_226.pdf)). For a calendar 2026 year: 15 March, 15 June, 15 September and 15 December 2026.
7. **Pay** balances of $1,000 or more electronically. Choose on the report whether to transfer any overpayment to next year or refund it; DOR does not refund $1.00 or less.
8. **Afterwards:** DOR forecasts interest and sends a notice; late filing penalties are assessed, not self-reported. Amended reports must be filed within three years of the due date of the original (or extended) report; DOR has one year from filing an amended report to tell the taxpayer whether it accepts it (REV-1200).

## Completion checklist

- [ ] Nexus and exemption tested, including the $500,000 presumption.
- [ ] Rate picked from the first day of the tax year (7.49% for years beginning in 2026).
- [ ] Federal taxable income taken before NOL and special deductions, separate company basis, with 163(j) as in effect on 31 December 2024.
- [ ] Bonus, 168(n) and research adjustments made on the right schedules.
- [ ] Taxes on income added back with REV-860.
- [ ] Single sales factor used only if taxable in another state; no 0/0 factor.
- [ ] NOLs split by origin year and capped at 40% and 50%.
- [ ] RCT-101 e-filed by the 15th of the month after the federal due date, or extended.
- [ ] 2027 estimates scheduled at the 2027 rate of 6.99%.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR, Corporate Net Income Tax page. Read for the rate schedule 2023 to 2031 (7.49% for 2026), the base (Form 1120 line 28), exempt entities, the federal classification rule and MeF filing. | https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax | 2026-11-13 |
| DOR, Act 45 of 2025 CNIT provisions. Read for research expenditure addback and 20% deduction, 168(n) decoupling and the 163(j) freeze. | https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/corporation-taxes/corporate-net-income-tax/act-45-of-2025 | 2026-11-13 |
| REV-1200, 2025 RCT-101 instructions. Read for the rate and NOL percentage table, due date, extension, late filing penalty, interest, S corporations, $500,000 presumption, line 2 and 3 adjustments, apportionment, line 11 NOL and amended reports. | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rev-1200.pdf | 2026-11-13 |
| 2025 RCT-103, Net Operating Loss Schedule. Read for the 40% limit line. | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/corporationtax/documents/2025/2025_rct-103.pdf | 2026-11-13 |
| DOR Tax Compendium, March 2025. Read for the CNIT tax base list and the NOL cap table (2026: 40% and 50%). | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/reportsstats/taxcompendium/documents/2025_tax_compendium.pdf | 2026-11-13 |
| DOR 2026-27 Estimate Documentation. Read for Act 56 of 2024: loss usage rising ten points a year to 80% by 2029, effective for tax year 2026. | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/reportsstats/estimatedoc/documents/2026_27_est_doc.pdf | 2026-11-13 |
| PA Tax Update No. 226. Read for the CNIT estimated payment dates and the 72 P.S. 10003.3 safe harbour reference. | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/news-and-statistics/taxupdate/documents/taxupdate_226.pdf | 2026-11-13 |
| REV-1611, interest rates. Read for 7% (0.000192 daily) for 2025 to 2026. | https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/otherforms/documents/rev-1611.pdf | 2026-11-13 |

Not yet confirmed: the 2026 RCT-101, REV-1200 and RCT-103 (not published when read; the 2025 editions are used for line numbers); the estimated tax safe harbour percentages in 72 P.S. 10003.3 (statute not read); the PA depreciation method for 168(k) property on Schedule C-8 (the schedule itself not read); market-based sourcing rules for services and intangibles; the rate of any underpayment penalty on estimated tax.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pa-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pa-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
