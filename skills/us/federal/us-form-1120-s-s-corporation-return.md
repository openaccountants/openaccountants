---
name: us-form-1120-s-s-corporation-return
description: >
  Prepare Form 1120-S, the US income tax return for an S corporation, for tax
  year 2026. Covers who must file, the 15 March 2027 due date for a calendar
  year, Schedule K-1 furnished to each shareholder, stock-basis adjustments
  under section 1367, distributions under section 1368, the 21 percent
  built-in gains tax and the five-year recognition period, the excess net
  passive income tax, and the section 6699 late-filing penalty of USD 260 per
  shareholder per month for a return required to be filed in 2027. Does not
  decide whether to elect S status and does not compute the shareholder loss
  limits. Trigger on "Form 1120-S", "S corporation return", "Schedule K-1
  1120-S", "built-in gains tax", "S corp due date", "AAA". Federal only.
version: "1.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
category: federal
type: computation
---

# US Form 1120-S, S corporation return, tax year 2026

> **Source-cited draft.** Built from the 2025 Instructions for Form 1120-S (the edition on irs.gov when read), Rev. Proc. 2025-32, IRM 20.1.2, and 26 U.S.C. 11, 1367, 1368, 1374 and 6072, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A calendar-year S corporation files Form 1120-S for 2026 by **15 March 2027**. That day is a Monday, so the weekend and holiday rule does not move it. The corporation generally pays no tax on its ordinary income: the income passes through on Schedule K-1. It does pay tax on net recognized built-in gain and on excess net passive income, both at **21 percent**. A return required to be filed in 2027 that is late, and shows no tax due, draws a penalty of **USD 260** for each month or part of a month (up to 12) multiplied by the number of persons who were shareholders at any time during the year. Whether to elect S status, and what salary is reasonable, is `us-s-corp-election-decision`. The shareholder's loss limits are `us-1120-corporation-return-schedule-ordinary-business`.

## Scope and who this is for

In scope: Form 1120-S for a domestic corporation, or an eligible entity treated as an association, whose S election is in effect for a tax year beginning in 2026. The work is the corporation's return: ordinary income, separately stated items, each shareholder's Schedule K-1, stock basis under section 1367, distributions under section 1368, the built-in gains tax, and the excess net passive income tax.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Whether to elect, Form 2553, late-election relief, and what compensation is reasonable | `us-s-corp-election-decision` |
| Shareholder loss limits (basis, at risk, passive, excess business loss) and Form 7203 ordering | `us-1120-corporation-return-schedule-ordinary-business` |
| Qualified business income deduction | `us-qbi-deduction` |
| How long Form 7004 extends the return | `us-corporate-extension-form-7004-and-the` |
| C corporation Form 1120 | `us-form-1120-c-corp` |
| Partnership Form 1065 | `us-form-1065-partnership` |
| Check-the-box before an S election | `us-form-8832-entity-classification` |

## Ask the client first

1. **Election in force.** Was Form 2553 accepted, and is the election in effect for every day of the 2026 year, or did it begin or end mid-year?
2. **C corporation history.** Was the corporation a C corporation before the S election, or did it take assets from a C corporation in a carryover-basis transfer? If yes, the first day of the S period and the net unrealized built-in gain still left.
3. **Earnings and profits and passive receipts.** Accumulated earnings and profits at year end, and gross receipts split between passive investment income and everything else.
4. **Shareholders and basis.** Every person who owned stock at any time in 2026, each one's stock basis at 1 January 2026, and any loans from that shareholder to the corporation.
5. **Entity-level tax.** Will built-in gains tax, excess net passive income tax, and investment credit recapture together be USD 500 or more? Officer pay already run through payroll is a fact for the page 1 deduction; whether that pay is reasonable is decided in `us-s-corp-election-decision`, not here.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Who it applies to | Source |
| --- | --- | --- | --- |
| Calendar-year Form 1120-S due date | 15 March 2027 | S corporation with a tax year that is the 2026 calendar year. 15 March 2027 is a Monday, so the weekend and holiday rule does not move it | [26 U.S.C. 6072(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) |
| Weekend and holiday filing rule | Next day that is not a Saturday, Sunday, or legal holiday | Any due date that lands on one of those days | [Instructions for Form 1120-S (2025), When To File](https://www.irs.gov/instructions/i1120s) |
| Built-in gains tax rate | 21 percent | Net recognized built-in gain of an S corporation in a year that begins in the recognition period. The rate is the highest rate in section 11(b) | [26 U.S.C. 1374(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partIII-sec1374.htm) |
| Corporate rate used by section 1374 | 21 percent of taxable income | Section 11(b), the rate section 1374 applies | [26 U.S.C. 11(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm) |
| Built-in gains recognition period | 5 years | Begins on the first day of the first tax year for which the corporation was an S corporation. A corporation that was an S corporation for every one of its tax years is not subject to the tax | [26 U.S.C. 1374(d)(7)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partIII-sec1374.htm) |
| Net recognized built-in gain cap | The lesser of the built-in-only taxable income and the corporation's taxable income | Each year in the recognition period. Any excess of the built-in-only amount over taxable income carries to the next year as recognized built-in gain | [26 U.S.C. 1374(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partIII-sec1374.htm) |
| Excess net passive income tax rate | 21 percent | An S corporation that has accumulated earnings and profits at year end and passive investment income above 25 percent of gross receipts, and that has taxable income for this purpose | [Instructions for Form 1120-S (2025), line 23a worksheet](https://www.irs.gov/instructions/i1120s) |
| Passive-income termination test | More than 25 percent of gross receipts, for 3 consecutive years, and accumulated earnings and profits | The election ends on the first day of the first tax year that begins after the third consecutive year | [Instructions for Form 1120-S (2025), Termination of Election](https://www.irs.gov/instructions/i1120s) |
| Estimated tax threshold for entity-level taxes | USD 500 | Built-in gains tax, excess net passive income tax, and investment credit recapture, taken together | [Instructions for Form 1120-S (2025), Estimated Tax Payments](https://www.irs.gov/instructions/i1120s) |
| Calendar-year estimated tax dates for 2026 | 15 April, 15 June, 15 September, and 15 December 2026 | The four installments when the USD 500 test is met. A date that is a Saturday, Sunday, or legal holiday moves to the next business day | [Instructions for Form 1120-S (2025), Estimated Tax Payments](https://www.irs.gov/instructions/i1120s) |
| Section 6699 penalty, return required to be filed in 2027 | USD 260 per shareholder per month or part of a month, up to 12 months | Failure to file a timely or complete Form 1120-S, unless reasonable cause. Count every person who was a shareholder at any time during the year. The 2025 instructions state USD 255 for a return required to be filed in 2026; do not use that figure for the 2026 return | [Rev. Proc. 2025-32, section 4.56](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Section 6651 60-day minimum, return required to be filed in 2027 | The lesser of USD 535 and 100 percent of the tax required to be shown | An income tax return filed more than 60 days after the due date, including extensions. If the tax required to be shown is zero, this minimum is zero | [Rev. Proc. 2025-32, section 4.52](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Additional late-filing amount when tax is due | 5 percent of the unpaid tax per month or part of a month, up to 25 percent | Added, in the Form 1120-S instructions, to the per-shareholder penalty when tax is due. Reasonable cause can remove it | [Instructions for Form 1120-S (2025), Late filing of return](https://www.irs.gov/instructions/i1120s) |
| Late payment | 0.5 percent of the unpaid tax per month or part of a month, up to 25 percent | Tax not paid by the due date. An extension of time to file does not extend time to pay. Reasonable cause can remove it | [Instructions for Form 1120-S (2025), Late payment of tax](https://www.irs.gov/instructions/i1120s) |
| Failure to furnish Schedule K-1, statement required to be furnished in 2027 | USD 340 per Schedule K-1 | Each failure to furnish a Schedule K-1 (or Schedule K-3) on time, or to include the required information. Reasonable cause can remove it | [Rev. Proc. 2025-32, section 4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Intentional disregard of the K-1 furnishing requirement, 2027 | The greater of USD 690 and 10 percent of the items required to be reported | Replaces the USD 340 amount when the failure is intentional disregard | [Rev. Proc. 2025-32, section 4.58](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Electronic filing mandate | 10 or more returns of any type in the calendar year | Form 1120-S filed on or after 1 January 2024. Count income tax, employment tax, excise tax, and information returns | [Instructions for Form 1120-S (2025), Electronic Filing](https://www.irs.gov/instructions/i1120s) |
| Distribution, no accumulated earnings and profits | Not included in the shareholder's income to the extent of stock basis | The excess over basis is treated as gain from a sale of property. Basis for this test includes that year's section 1367(a)(1) income increases | [26 U.S.C. 1368(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1368.htm) |

None of the 21 percent rate, the five-year recognition period, the 25 percent passive test, or the 15 March statutory due date is indexed. The penalty dollar amounts are indexed and are tied to the calendar year the return or statement is required to be filed or furnished, not to the number printed on an older form.

### Who files, and what the return reports

1. **File Form 1120-S** if the entity elected S status on Form 2553, the IRS accepted the election, and the election is still in effect. Do not file Form 1120-S for a year before the election takes effect. The election itself, including a late Form 2553, is `us-s-corp-election-decision`. Source: [Instructions for Form 1120-S (2025), Who Must File](https://www.irs.gov/instructions/i1120s).
2. **Page 1 is ordinary business income.** Separately stated items (rental real estate, other rental, interest, portfolio deductions, charitable contributions, foreign taxes, section 179, and anything else that can affect a shareholder's tax differently) go to Schedule K and to each Schedule K-1, not into the page 1 total. Do not put tax-exempt income on page 1. Source: [Instructions for Form 1120-S (2025), income and separately stated items](https://www.irs.gov/instructions/i1120s).
3. **Officer pay is a page 1 deduction** of the amount actually paid. This skill does not decide whether that amount is reasonable compensation. Load `us-s-corp-election-decision` for that question before the return is finished.
4. **Schedule K-1.** Prepare one for each person who was a shareholder at any time during the year. Give it to the shareholder on or before the day Form 1120-S is required to be filed, and attach a copy to the return. Source: [Instructions for Form 1120-S (2025), General Information under Schedule K-1](https://www.irs.gov/instructions/i1120s).

### Stock basis and distributions

5. **Increase stock basis** for the shareholder's share of the income items in section 1366(a)(1), including separately stated income and nonseparately computed income, and for depletion in excess of basis. Source: [26 U.S.C. 1367(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1367.htm).
6. **Decrease stock basis, not below zero,** by distributions that section 1368 keeps out of the shareholder's income, by the shareholder's share of losses and deductions, by non-deductible non-capital expenses, and by the oil and gas depletion amount in section 1367(a)(2)(E). Loss that basis cannot absorb moves to debt basis, and later income restores debt basis before stock basis. The order of the non-distribution decreases, the election to switch non-deductible expenses and losses, and the four loss limits are computed in `us-1120-corporation-return-schedule-ordinary-business` on Form 7203. Do not recompute those limits here. Source: [26 U.S.C. 1367](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1367.htm).
7. **Distributions.** If the corporation has no accumulated earnings and profits, a non-liquidating distribution is not included in the shareholder's income to the extent of stock basis, and the excess is gain from a sale of the stock. Basis for that test includes the year's income increases under section 1367(a)(1). If the corporation has accumulated earnings and profits, the distribution is treated as a no-earnings-and-profits distribution to the extent of the accumulated adjustments account, then as a dividend to the extent of accumulated earnings and profits, then again under the no-earnings-and-profits rule. The accumulated adjustments account tracks S-period adjustments in a manner similar to section 1367, but it is not adjusted for tax-exempt income and the related expenses, and it is not adjusted for federal taxes from a C corporation year. Source: [26 U.S.C. 1368](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1368.htm).

### Built-in gains tax

8. **The tax applies** when, for a year that begins in the five-year recognition period, the corporation has a net recognized built-in gain. It does not apply to a corporation that was an S corporation for every one of its tax years. Net unrealized built-in gain is the excess of the fair market value of the assets at the start of the first S year over their aggregate adjusted bases at that time. Gain recognized in the recognition period on an asset held at that start is recognized built-in gain only up to that asset's built-in amount. The year's net recognized built-in gain is the lesser of the taxable income computed from recognized built-in gains and losses only, and the corporation's taxable income. It also cannot exceed net unrealized built-in gain minus net recognized built-in gain of earlier years in the period. Source: [26 U.S.C. 1374](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partIII-sec1374.htm).
9. **The tax is 21 percent of that net recognized built-in gain.** On the 2025 form, it is entered on Form 1120-S, page 1, line 23b, from line 23 of Part III of Schedule D (Form 1120-S). A C corporation net operating loss carryforward and a business credit carryforward from a C year can reduce this tax. Source: [26 U.S.C. 1374(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partIII-sec1374.htm) and [Instructions for Form 1120-S (2025), line 23b](https://www.irs.gov/instructions/i1120s).
10. **Excess net passive income tax,** when accumulated earnings and profits remain and passive investment income exceeds 25 percent of gross receipts, is 21 percent of excess net passive income, limited by taxable income. On the 2025 form it is line 23a. Each item of passive investment income passed through is reduced by its share of this tax. Three consecutive years of this pattern terminate the election on the first day of the following year. Source: [Instructions for Form 1120-S (2025), line 23a](https://www.irs.gov/instructions/i1120s).

### How the result flows on

The Schedule K-1 amounts are the shareholder's income for the shareholder's tax year in which the S corporation's year ends. The qualified business income deduction on those amounts is `us-qbi-deduction`. Losses the shareholder cannot use this year are carried under the limit that stopped them, in `us-1120-corporation-return-schedule-ordinary-business`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| S election not yet accepted, or the year is before the effective date | Do not file Form 1120-S. Late relief is `us-s-corp-election-decision` |
| Always an S corporation, no C corporation assets | No built-in gains tax under section 1374(c)(1) |
| Sale of a built-in gain asset after the five-year recognition period | No section 1374 tax on that gain. The gain still passes through |
| Recognized built-in gain larger than taxable income | Net recognized built-in gain is limited to taxable income. The excess carries to the next year in the recognition period |
| Installment sale of a built-in gain asset | All payments are governed by the rule for the year of sale, including a sale inside the recognition period |
| No accumulated earnings and profits | Distributions are not dividends. They reduce basis, then they are gain from a sale of the stock |
| Accumulated earnings and profits, and passive investment income over 25 percent | Excess net passive income tax for that year. Three consecutive years end the election |
| Entity-level taxes under USD 500 | No estimated tax installments for those taxes |
| Fewer than 10 returns of all types in the calendar year | Electronic filing is allowed and is not required by the 10-return rule |
| Religious objection to the e-file technology | Exempt. Write "Religious Exemption" at the top of page 1 and file on paper |

## Worked cases

**Case 1, a decision: sell a built-in gain asset inside the recognition period, or wait.** A calendar-year corporation elected S status on 1 January 2024, so 2026 is inside the five-year recognition period, which runs through 2028. At the start of the S period one asset had a fair market value of USD 200,000 and an adjusted basis of USD 80,000. In 2026 the corporation can sell it for USD 200,000. The built-in-only taxable income from that sale is USD 120,000. Taxable income for section 1374 is USD 150,000. There is no recognized built-in loss, no prior recognized built-in gain, and net unrealized built-in gain left is at least USD 120,000. No C year net operating loss or credit carryforward is available.

Net recognized built-in gain is the lesser of USD 120,000 and USD 150,000, which is USD 120,000. Tax at 21 percent is USD 25,200. If the corporation waits and sells in 2029, after the recognition period, the section 1374 tax is zero. The decision figure this return owns is that USD 25,200 of corporate tax. The gain passes through to the shareholders either way; their tax is not computed here. Waiting has a business cost this arithmetic does not measure.

```oa-check
name: Built-in gains tax, sell inside the five-year period or wait (2026)
inputs:
  builtin_only_taxable_income: 120000
  taxable_income: 150000
  rate: 0.21
steps:
  - net_recognized: min(builtin_only_taxable_income, taxable_income)
  - tax_if_sold_in_2026: net_recognized * rate
  - tax_if_sold_after_period: 0
  - corporate_tax_saved_by_waiting: tax_if_sold_in_2026 - tax_if_sold_after_period
expected:
  net_recognized: 120000.00
  tax_if_sold_in_2026: 25200.00
  tax_if_sold_after_period: 0.00
  corporate_tax_saved_by_waiting: 25200.00
```

**Case 2, basis and a non-dividend distribution.** One shareholder starts 2026 with stock basis of USD 10,000. The corporation has no accumulated earnings and profits. The shareholder's 2026 nonseparately computed income is USD 30,000. There is no separately stated income, no loss, and no depletion. The corporation distributes USD 8,000 in cash during the year, and it has USD 1,000 of expenses that are not deductible and not chargeable to capital.

Section 1368(d) tests the distribution against basis after the year's section 1367(a)(1) income increases: USD 10,000 plus USD 30,000 is USD 40,000. The USD 8,000 distribution does not exceed that basis, so none of it is included in the shareholder's income, and it decreases basis. The USD 1,000 non-deductible expense also decreases basis. Ending stock basis is USD 31,000. Because the decreases do not use up basis, this case does not reach debt basis or the loss limits. Those limits, if a later year has a loss, are `us-1120-corporation-return-schedule-ordinary-business`.

```oa-check
name: Stock basis after income, a non-dividend distribution, and a non-deductible expense (2026)
inputs:
  basis_start: 10000
  income: 30000
  distribution: 8000
  nondeductible: 1000
steps:
  - basis_for_distribution_test: basis_start + income
  - distribution_in_excess_of_basis: max(distribution - basis_for_distribution_test, 0)
  - basis_end: basis_for_distribution_test - distribution - nondeductible
expected:
  basis_for_distribution_test: 40000.00
  distribution_in_excess_of_basis: 0.00
  basis_end: 31000.00
```

A late return with no tax due, two shareholders, and four months late, costs USD 260 times 2 times 4, which is USD 2,080, before any reasonable-cause relief. That figure uses the 2027 filing-year amount and is not an `oa-check` because the two cases above are the ones the return turns on.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-1120S-ELECT | The S election is missing, late, or the client is asking whether to elect | `us-s-corp-election-decision` |
| R-1120S-WAGE | Officer pay may be unreasonably low, or the IRS is reclassifying distributions as wages | `us-s-corp-election-decision`. Do not invent a salary |
| R-1120S-LOSS | A K-1 loss, debt basis, at risk, passive activity, or excess business loss | `us-1120-corporation-return-schedule-ordinary-business` |
| R-1120S-QBI | Section 199A on the K-1 amounts | `us-qbi-deduction` |
| R-1120S-TERM | A nonresident alien, a partnership, or a corporation became a shareholder, or the three-year passive test has already run | The election may have ended. Refer. Do not prepare a full-year Form 1120-S until the termination date is fixed |
| R-1120S-INTL | A foreign subsidiary, foreign tax, or a K-2 / K-3 | Schedules K-2 and K-3 may be required. Controlled foreign corporation reporting is `us-form-5471-cfc-information` |
| R-1120S-STATE | State franchise tax, a state S election that does not follow the federal election, or a pass-through entity tax | The state's own skill |

## Filing and payment

File the 2026 Form 1120-S by **15 March 2027** for a calendar year. Pay any tax due by that date. An extension of time to file is Form 7004, filed by the original due date; the length of that extension is `us-corporate-extension-form-7004-and-the`. Form 7004 does not extend the time to pay. Source: [Instructions for Form 1120-S (2025), When To File, Extension, and Tax Payments](https://www.irs.gov/instructions/i1120s).

File electronically if the corporation files 10 or more returns of any type during the calendar year. A waiver request goes to Internal Revenue Service, Ogden Submission Processing Center, Attn: Form 1120 e-file Waiver Request, Mail Stop 1057, Ogden, UT 84201, or by fax to 877-477-0575. The e-Help Desk is 866-255-0654. A religious exemption is marked "Religious Exemption" at the top of page 1 and filed on paper.

Paper Form 1120-S, from the 2025 instructions (the edition posted when this skill was written):

| Principal business location | Assets at year end | Address |
| --- | --- | --- |
| Connecticut, Delaware, District of Columbia, Georgia, Illinois, Indiana, Kentucky, Maine, Maryland, Massachusetts, Michigan, New Hampshire, New Jersey, New York, North Carolina, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Vermont, Virginia, West Virginia, Wisconsin | Under USD 10 million, and Schedule M-3 is not filed | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999-0013 |
| The same states | USD 10 million or more, or Schedule M-3 is filed | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0013 |
| Any other state | Any amount | Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0013 |
| A foreign country or US territory | Any amount | Internal Revenue Service, P.O. Box 409101, Ogden, UT 84409 |

Pay by electronic funds transfer, through EFTPS or the corporation's IRS business tax account. Estimated tax of the entity-level taxes, when the USD 500 test is met, is due on the four 2026 dates in the table above.

The return is signed by the president, vice president, treasurer, assistant treasurer, chief accounting officer, or another authorized corporate officer. A paid preparer who is paid to prepare the return signs, enters a PTIN, and gives the corporation a copy.

## Completion checklist

- Form 2553 was accepted and the election covers the year being filed.
- Page 1 ordinary income excludes separately stated items and tax-exempt income.
- One Schedule K-1 for every person who owned stock at any time during the year, furnished by the day the return is required to be filed.
- Stock basis increased for income before the distribution test, and not decreased below zero.
- Built-in gains tax computed only if the year begins inside the five-year period and the corporation was not always an S corporation.
- Excess net passive income tax and the three-year termination test checked when accumulated earnings and profits remain.
- Estimated tax paid if the entity-level taxes are USD 500 or more.
- Section 6699 measured at USD 260 per shareholder per month if the return is required to be filed in 2027 and is late.
- Reasonable compensation left to `us-s-corp-election-decision`, and loss limits left to `us-1120-corporation-return-schedule-ordinary-business`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form 1120-S (2025), the edition at this URL on the read date. Read for who must file, the 15th day of the 3rd month, the weekend rule, Form 7004, the 10-return e-file rule, waiver address and fax, estimated tax at USD 500 and the 2026 installment dates, late filing and late payment percentages, Schedule K-1 timing, line 23a at 21 percent, line 23b, and the paper filing addresses. | https://www.irs.gov/instructions/i1120s | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.52 (USD 535, returns required to be filed in 2027), section 4.56 (USD 260 under section 6699(b)(1)), and section 4.58 (USD 340, and the greater of USD 690 or 10 percent, for payee statements required to be furnished in 2027). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| IRM 20.1.2, Failure to file S corporation return. Read for the base penalty rate of USD 260 for a return due after 31 December 2026, multiplied by the number of shareholders, for up to 12 months, and for reasonable cause. | https://www.irs.gov/irm/part20/irm_20-001-002r | 2026-11-13 |
| 26 U.S.C. 11(b). Read for the 21 percent corporate rate. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partII-sec11.htm | 2026-11-13 |
| 26 U.S.C. 1374. Read for the tax on net recognized built-in gain, the highest section 11(b) rate, the five-year recognition period, the always-S exception, and the taxable-income limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partIII-sec1374.htm | 2026-11-13 |
| 26 U.S.C. 1367. Read for increases to stock basis, decreases not below zero, and the shift of unused loss to debt basis. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1367.htm | 2026-11-13 |
| 26 U.S.C. 1368. Read for distributions with and without accumulated earnings and profits, the income-first basis rule in subsection (d), and the accumulated adjustments account. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapS-partII-sec1368.htm | 2026-11-13 |
| 26 U.S.C. 6072(b). Read for the 15 March due date of a calendar-year S corporation return, and the 15th day of the third month for a fiscal year. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm | 2026-11-13 |
| Instructions for Form 7004. Read only to confirm that this skill does not restate the extension length, which that form's own skill carries. The 1120-S instructions say to file Form 7004 by the regular due date. | https://www.irs.gov/instructions/i7004 | 2026-11-13 |

Not yet confirmed: the 2026 Form 1120-S and Schedule K-1 had not replaced the 2025 instructions at irs.gov/instructions/i1120s when read, so 2026 form line numbers are not stated as 2026 facts. The reduced section 6722 amounts for correcting a 2027 payee statement within 30 days, or by 1 August, were not used: in Rev. Proc. 2025-32 section 4.58 the two-column layout did not separate those cells cleanly. The section 6621 interest rate for 2027 was not opened. LIFO recapture installments under section 1363(d) are named in the 2025 instructions and were not recomputed here.
