---
name: montenegro-tax-optimization
description: >-
  Tax planning for a self-employed person or small company owner in Montenegro
  for tax year 2026. Covers the progressive tax on a sole trader's principal
  business income (0% up to EUR 8,400, 9% up to EUR 12,000, 15% above), the
  annual lump-sum (pausal) regime for principal business turnover below
  EUR 30,000.01 with its application dates, payment rule, excluded activities
  and VAT bar, the contribution base for sole traders, the municipal surtax
  ceilings (13%, or 15% in Podgorica and Cetinje), the company route (corporate
  tax 9% / 12% / 15% plus 15% tax on dividends to individuals) and the red
  lines. Trigger phrases: reduce tax Montenegro, pausal, lump-sum tax
  Montenegro, preduzetnik or d.o.o., self-employed vs company Montenegro,
  Montenegro 9% tax, tax planning Montenegro. Rates must agree with
  montenegro-income-tax, me-corporate-income-tax and
  montenegro-social-contributions.
version: 0.2
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro tax optimisation, tax year 2026

This skill compares the ways a Montenegrin business owner can be taxed in 2026: as a sole trader (preduzetnik) taxed on actual profit, as a sole trader on the annual lump sum, or through a company (d.o.o.). The detailed computations live in the companion skills: [personal income tax](montenegro-income-tax.md), [corporate income tax](me-corporate-income-tax.md), [payroll](montenegro-payroll.md) and [social contributions](montenegro-social-contributions.md). Figures here must agree with them.

## Section 1: Quick reference

| Item | Amount (2026) | Source |
|---|---|---|
| Sole trader, principal business income | 0% up to EUR 8,400; 9% on EUR 8,400.01 to 12,000; 15% above EUR 12,000 | [PIT Law art. 10(1)(2)][pit] |
| Supplementary business and occasional self-employment income | 15% | [PIT Law art. 10(1)(3)][pit] |
| Lump-sum regime, turnover test | prior-year turnover (or planned turnover when starting) below EUR 30,000.01 | [PIT Law art. 49(1)][pit] |
| Lump-sum application | by the end of January of the tax year; within 5 days of registration for a new business | [PIT Law art. 49(4)][pit] |
| Lump-sum payment | 1/12 of the annual amount each month, by the end of the month for the previous month; seasonal business of up to 6 months pays by the 5th of the current month | [PIT Law art. 49(3), (8)][pit] |
| Lump-sum amount | annual amount from a scale set by the Ministry of Finance | [PIT Law art. 49(2)][pit] |
| Undeclared income found from growth in assets | 80% tax | [PIT Law art. 10a][pit] |
| Corporate profit tax | 9% up to EUR 100,000; EUR 9,000 + 12% up to EUR 1,500,000; EUR 177,000 + 15% above | [CPTL art. 28][cit] |
| Dividends paid to an individual | 15% of the gross dividend, withheld by the company | [PIT Law arts. 37(1)(4), 37(3)-(4), 50][pit] |
| Municipal surtax (prirez) | up to 13% of the tax; up to 15% in the Capital City (Podgorica) and the Old Royal Capital (Cetinje); each municipality sets its own rate | [Local Self-Government Financing Law arts. 8, 9][local] |
| Contribution base, sole trader on actual profit | by realised or estimated yearly turnover: up to EUR 9,000, 60% of the average monthly gross wage; up to EUR 15,000, 100%; over EUR 15,000, 150% (a higher pension base can be chosen) | [Contributions Law arts. 9(7), 11(5)][social] |
| Average monthly gross wage used in 2026 (the 2025 average) | EUR 1,206, so monthly bases of EUR 723.60 / 1,206.00 / 1,809.00 | [Contributions Law art. 4(1)(23)][social]; [MONSTAT release, 30 January 2026][monstat] |
| Contribution base, sole trader on the lump sum | the taxable income set under the PIT rules | [Contributions Law arts. 9(7), 11(5)][social] |

Montenegro taxes business income at low progressive rates. The main lever for a small trade is the lump sum, which is closed to professional and intellectual work, trade, catering and several other activities.

## Section 2: The lump-sum (pausal) regime

- **Who can use it.** A taxpayer whose principal independent activity had turnover below EUR 30,000.01 in the previous year, or plans turnover below that when starting, can apply to pay income tax as an annual lump sum (PIT Law art. 49(1)). It is never automatic: the tax authority grants it by ruling within 15 days of a well-founded application (art. 49(6)).
- **What it replaces.** Only the personal income tax on that business income. The amount comes from the Ministry's scale (art. 49(2)), not from actual profit. Social contributions are separate: for a lump-sum sole trader the contribution base is the taxable income set under the PIT rules (Contributions Law arts. 9(7), 11(5)).
- **Excluded activities (art. 49(9)).** Lawyers, notaries, auditors, accountants, health services, consulting, design (projektantska), surveyors, public enforcement officers, other professional and intellectual occupations, hairdressers, billiard clubs, amusement games, retail and wholesale trade, catering, hotels, financial intermediation and real estate activities. IT, marketing and online services are not named: if the actual activity is consulting, design or another professional or intellectual occupation, the lump sum is not available. Classify the actual activity, not the label.
- **Kiosks.** The tax authority can approve the lump sum for trade or catering from a kiosk, trailer or mobile unit (art. 49(10)), but only for a taxpayer who produces and sells exclusively its own products (art. 49(11)).
- **VAT.** A taxpayer registered for VAT cannot pay income tax as a lump sum (art. 49(12)).
- **Records.** Lump-sum taxpayers must keep books of turnover (art. 49(5)). If circumstances justify it, the tax authority orders a change of method by ruling (art. 49(7)).

## Section 3: Sole trader on actual profit, and the surtax

- **Bands.** Principal business income: 0% up to EUR 8,400, 9% on the next EUR 3,600, 15% above EUR 12,000 (PIT Law art. 10(1)(2)). Supplementary business and occasional self-employment income: flat 15% (art. 10(1)(3)). The profit computation is in the [income tax skill](montenegro-income-tax.md).
- **Municipal surtax.** A municipality can charge a surtax on the tax on employment income, self-employment income, income from property and property rights, and capital income (Local Self-Government Financing Law art. 8). The ceiling is 13% of the tax, or 15% in Podgorica and Cetinje; the rate is the one set by the municipality's own decision (art. 9). Never omit it, and use the municipality's actual rate, not the ceiling.
- **Contributions.** The base for a sole trader on actual profit depends on yearly turnover (60%, 100% or 150% of the 2025 average monthly gross wage of EUR 1,206; see the table above). Rates are in the [contributions skill](montenegro-social-contributions.md).

## Section 4: Company route and extraction

- **Corporate tax.** 9% on profit up to EUR 100,000, 12% on the next EUR 1,400,000 and 15% above EUR 1,500,000 (CPTL art. 28).
- **Dividends.** A dividend to an individual is capital income taxed at 15% of the gross amount, withheld by the company when it pays; no costs are deductible (PIT Law arts. 37, 50). The surtax also applies to capital income tax (Local Self-Government Financing Law art. 8).
- **Combined burden.** On distributed profit in the first corporate band, the burden before surtax is 9% + 15% x 91% = 22.65%. A sole trader with the same profit pays 0% to 15% on it (plus surtax), so the company is not automatically cheaper for a small business. It defers the 15% dividend tax while profit stays in the company.
- **Salary route.** Paying the owner a salary moves the income into employment tax and contributions: see the [payroll skill](montenegro-payroll.md).

### Worked example: EUR 20,000 profit, sole trader or company

A business makes a profit of EUR 20,000 in 2026. As a sole trader on actual profit (principal activity), the tax is 9% x 3,600 = 324 plus 15% x 8,000 = 1,200, a total of 1,524. Through a company that pays out all its after-tax profit, corporate tax is 9% x 20,000 = 1,800, the dividend is 18,200, and dividend tax is 15% x 18,200 = 2,730, a total of 4,530. Both figures exclude the municipal surtax and social contributions, which must be added from the companion skills before comparing.

```oa-check
name: Montenegro 2026 sole trader versus company on EUR 20,000 profit
inputs:
  profit: 20000
steps:
  - pit_band_9: max(0, min(profit, 12000) - 8400) * 0.09
  - pit_band_15: max(0, profit - 12000) * 0.15
  - sole_trader_tax: pit_band_9 + pit_band_15
  - corporate_tax: min(profit, 100000) * 0.09 + max(0, min(profit, 1500000) - 100000) * 0.12
  - dividend: profit - corporate_tax
  - dividend_tax: dividend * 0.15
  - company_route_tax: corporate_tax + dividend_tax
expected:
  pit_band_9: 324
  pit_band_15: 1200
  sole_trader_tax: 1524
  corporate_tax: 1800
  dividend: 18200
  dividend_tax: 2730
  company_route_tax: 4530
```

## Section 5: Red lines (do not cross)

- **Lump sum for an excluded activity.** Never place consulting, design, accounting, legal or other professional or intellectual work, or trade or catering (outside the kiosk rule), in the lump sum (PIT Law art. 49(9)-(11)).
- **Turnover suppression.** Never under-report turnover to stay below EUR 30,000.01. The tax authority can change the method by ruling (art. 49(7)), and undeclared income found from growth in assets is taxed at 80% (art. 10a).
- **VAT and the lump sum.** A VAT-registered taxpayer cannot use the lump sum (art. 49(12)).
- **Surtax.** Never leave out the municipal surtax when computing the burden of an individual.

## PROHIBITIONS

- **Prohibition 1.** NEVER recommend the lump sum without the activity classification, the turnover evidence and the tax authority's ruling.
- **Prohibition 2.** NEVER present single-client work for one principal under employer-like control as safe self-employment; the reclassification rule is on the Not yet confirmed line below.
- **Prohibition 3.** NEVER omit the municipal surtax or social contributions when comparing routes.
- **Prohibition 4.** NEVER contradict the rates in montenegro-income-tax, me-corporate-income-tax or montenegro-social-contributions.
- **Prohibition 5.** NEVER present an item on the Not yet confirmed line as settled, or a planning comparison as definitive advice. Route the decision to a licensed Montenegrin tax adviser.

## Ask the client first

1. What exactly does the business do, for whom, and under what contracts (activity classification and single-client risk)?
2. What was last year's turnover, or what is planned turnover for a new business?
3. Is the business registered for VAT?
4. In which municipality does the business operate, and what is that municipality's surtax rate?
5. What profit does it make, and how does the owner want to take money out (drawings, salary or dividends)?

[pit]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[cit]: https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0
[local]: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0
[social]: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0
[monstat]: https://www.monstat.org/cg/novosti.php?id=4638

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Law, consolidated text through 160/25: arts. 10, 10a, 12, 37, 49, 50 | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-30 |
| Law amending the Personal Income Tax Law, Official Gazette 160/25: arts. 14 and 21 (lump-sum wording; applies from 1 January 2026) | https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0 | 2026-10-30 |
| Law amending the Personal Income Tax Law, Official Gazette 70/26 (in force 21 May 2026): changes only art. 10(1)(4) (games of chance) and art. 50f | https://www.sluzbenilist.me/propisi/394390/download | 2026-10-30 |
| Corporate Profit Tax Law, Ministry of Finance consolidation through 88/24: art. 28 (the 104/26 amendment applies from 1 January 2027 and does not change art. 28) | https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 | 2026-10-30 |
| Law on Financing Local Self-Government, consolidated through 149/2025: arts. 8, 9 | https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 | 2026-10-30 |
| Law on Compulsory Social Insurance Contributions, consolidated through 160/2025: arts. 4(1)(23), 5(1)(12), 9(7), 11(5) | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-30 |
| Law amending the Corporate Profit Tax Law, Official Gazette 104/26 (applies from 1 January 2027) | https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0 | 2026-10-30 |
| MONSTAT (Statistical Office), average wages release of 30 January 2026: 2025 average gross wage EUR 1,206 | https://www.monstat.org/cg/novosti.php?id=4638 | 2026-10-30 |

Not yet confirmed: the Ministry of Finance lump-sum scale and criteria under PIT Law art. 49(2), and so the actual 2026 lump-sum amounts (the old version's statement that the lump sum is one fixed monthly amount covering tax and contributions is not supported: the contribution base is set separately); the surtax rate each municipality has set for 2026; whether the surtax applies to the lump-sum tax; any statutory rule reclassifying a single-client sole trader as an employee (none found in the PIT or contributions law read); the date the EUR 30,000 threshold replaced an earlier EUR 18,000 threshold.

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
