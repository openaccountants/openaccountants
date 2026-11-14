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
  tax 9% / 12% / 15% plus 15% tax on dividends to individuals), the sole trader
  or d.o.o. decision worked both ways, and the red lines. Trigger phrases
  include reduce tax Montenegro, pausal, lump-sum tax Montenegro, preduzetnik
  or d.o.o., self-employed vs company Montenegro, Montenegro 9% tax, tax
  planning Montenegro. Rates must agree with montenegro-income-tax,
  me-corporate-income-tax and montenegro-social-contributions.
version: 1.0
jurisdiction: ME
tax_year: 2026
last_updated: 2026-11-14
category: tax-optimization
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax-optimization
type: decision
---

# Montenegro tax optimisation, tax year 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** For a small business, a sole trader (preduzetnik) on actual profit pays less income tax than a d.o.o. that pays out its profit: at EUR 20,000 profit, EUR 1,524 against EUR 4,530 before surtax and contributions. A company wins only when profit is large and stays in the company (at EUR 150,000 retained, EUR 15,000 corporate tax against EUR 21,024). The lump sum (pausal) can be cheaper still, but it is closed to professional, intellectual, trade and catering work and to VAT-registered taxpayers. The detailed computations live in [personal income tax](montenegro-income-tax.md), [corporate income tax](me-corporate-income-tax.md), [payroll](montenegro-payroll.md) and [social contributions](montenegro-social-contributions.md); figures here must agree with them.

The tax-law texts below are the Ministry of Finance consolidations on wapi.gov.me, which refused every connection on 2026-11-14; those rows keep their 2026-10-30 read date and were not reopened. The MONSTAT wage figure was re-read on 2026-11-14.

## Scope

This skill compares the ways a Montenegrin business owner can be taxed in 2026: as a sole trader taxed on actual profit, as a sole trader on the annual lump sum, or through a company (d.o.o.) paying corporate tax and then dividends or salary. It is for residents running a principal business. Out of scope: an employee's side income, non-residents, groups, and the 2027 corporate tax changes (Official Gazette 104/26 applies from 1 January 2027).

## Ask the client first

1. What exactly does the business do, for whom, and under what contracts (activity classification and single-client risk)?
2. What was last year's turnover, or what is planned turnover for a new business?
3. Is the business registered for VAT?
4. In which municipality does the business operate, and what is that municipality's surtax rate?
5. What profit does it make, and how does the owner want to take money out (drawings, salary or dividends), and how much can stay in the business?

## The method, step by step

1. **Classify the activity.** If it is on the art. 49(9) list, the lump sum is out (see step 3).
2. **Work out the sole trader tax on actual profit.** Principal business income: 0% up to EUR 8,400, 9% on the next EUR 3,600, 15% above EUR 12,000 (PIT Law art. 10(1)(2)). Supplementary business and occasional self-employment income: flat 15% (art. 10(1)(3)). Profit computation: [montenegro-income-tax](montenegro-income-tax.md).
3. **Test the lump sum.**
   - **Who can use it.** A taxpayer whose principal independent activity had turnover below EUR 30,000.01 in the previous year, or plans turnover below that when starting, can apply to pay income tax as an annual lump sum (art. 49(1)). It is never automatic: the tax authority grants it by ruling within 15 days of a well-founded application (art. 49(6)).
   - **What it replaces.** Only the personal income tax on that business income. The amount comes from the Ministry's scale (art. 49(2)), not from actual profit. Contributions are separate: for a lump-sum sole trader the contribution base is the taxable income set under the PIT rules (Contributions Law arts. 9(7), 11(5)).
   - **Excluded activities (art. 49(9)).** Lawyers, notaries, auditors, accountants, health services, consulting, design (projektantska), surveyors, public enforcement officers, other professional and intellectual occupations, hairdressers, billiard clubs, amusement games, retail and wholesale trade, catering, hotels, financial intermediation and real estate activities. IT, marketing and online services are not named: if the actual activity is consulting, design or another professional or intellectual occupation, the lump sum is not available. Classify the actual activity, not the label.
   - **Kiosks.** The tax authority can approve the lump sum for trade or catering from a kiosk, trailer or mobile unit (art. 49(10)), but only for a taxpayer who produces and sells exclusively its own products (art. 49(11)).
   - **VAT.** A VAT-registered taxpayer cannot pay income tax as a lump sum (art. 49(12)).
   - **Records.** Lump-sum taxpayers keep books of turnover (art. 49(5)). If circumstances justify it, the tax authority orders a change of method by ruling (art. 49(7)).
4. **Add the municipal surtax.** A municipality can charge a surtax on the tax on employment income, self-employment income, income from property and property rights, and capital income (Local Self-Government Financing Law art. 8). The ceiling is 13% of the tax, or 15% in Podgorica and Cetinje; use the rate set by the municipality's own decision (art. 9), never the ceiling as a guess.
5. **Add contributions.** The base for a sole trader on actual profit depends on yearly turnover (60%, 100% or 150% of the 2025 average monthly gross wage of EUR 1,206; see the table). Rates: [montenegro-social-contributions](montenegro-social-contributions.md).
6. **Work out the company route.** Corporate tax 9% on profit up to EUR 100,000, 12% on the next EUR 1,400,000 and 15% above EUR 1,500,000 (CPTL art. 28). A dividend to an individual is capital income taxed at 15% of the gross amount, withheld by the company when it pays; no costs are deductible (PIT Law arts. 37, 50); the surtax also applies to it (Local Self-Government Financing Law art. 8). On distributed profit in the first corporate band the burden before surtax is 9% + 15% x 91% = 22.65%. The company defers the 15% dividend tax while profit stays in it. A salary to the owner moves income into employment tax and contributions: [montenegro-payroll](montenegro-payroll.md).
7. **Compare** both routes on the same profit with surtax and contributions added, then route the decision to a licensed Montenegrin tax adviser.

### Rates, bands and thresholds

| Item | Amount (2026) | Source |
|---|---|---|
| Sole trader, principal business income | 0% up to EUR 8,400; 9% on EUR 8,400.01 to 12,000; 15% above EUR 12,000 (PIT Law art. 10(1)(2)) | PIT Law consolidation through 160/25: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 |
| Supplementary business and occasional self-employment income | 15% (art. 10(1)(3)) | same |
| Lump-sum regime, turnover test | Prior-year turnover (or planned turnover when starting) below EUR 30,000.01 (art. 49(1)) | same |
| Lump-sum application | By the end of January of the tax year; within 5 days of registration for a new business (art. 49(4)) | same |
| Lump-sum payment | 1/12 of the annual amount each month, by the end of the month for the previous month; seasonal business of up to 6 months pays by the 5th of the current month (art. 49(3), (8)) | same |
| Lump-sum amount | Annual amount from a scale set by the Ministry of Finance (art. 49(2)) | same |
| Undeclared income found from growth in assets | 80% tax (art. 10a) | same |
| Corporate profit tax | 9% up to EUR 100,000; EUR 9,000 + 12% up to EUR 1,500,000; EUR 177,000 + 15% above (CPTL art. 28) | Corporate Profit Tax Law consolidation through 88/24: https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 |
| Dividends paid to an individual | 15% of the gross dividend, withheld by the company (PIT Law arts. 37(1)(4), 37(3)-(4), 50) | PIT Law consolidation through 160/25: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 |
| Municipal surtax (prirez) | Up to 13% of the tax; up to 15% in Podgorica and Cetinje; each municipality sets its own rate (arts. 8, 9) | Local Self-Government Financing Law through 149/25: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 |
| Contribution base, sole trader on actual profit | By yearly turnover: up to EUR 9,000, 60% of the average monthly gross wage; up to EUR 15,000, 100%; over EUR 15,000, 150%; a higher pension base can be chosen (Contributions Law arts. 9(7), 11(5)) | Contributions Law through 160/25: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 |
| Contribution base, sole trader on the lump sum | The taxable income set under the PIT rules (arts. 9(7), 11(5)) | same |
| Average monthly gross wage used in 2026 (the 2025 average) | EUR 1,206 (Contributions Law art. 4(1)(23)), so monthly bases of EUR 723.60 / 1,206.00 / 1,809.00 | MONSTAT release, 30 January 2026: https://www.monstat.org/cg/novosti.php?id=4638 |

## Boundary and exception table

| Situation | Rule |
|---|---|
| Activity on the art. 49(9) list | No lump sum |
| Kiosk, trailer or mobile unit | Lump sum possible for trade or catering only if selling exclusively own products (art. 49(10)-(11)) |
| VAT-registered | No lump sum (art. 49(12)) |
| Turnover crosses EUR 30,000 | Lump sum test fails for the next year; also check VAT registration ([montenegro-vat](montenegro-vat.md)) |
| Undeclared income found from asset growth | 80% tax (art. 10a) |
| Single client under employer-like control | Reclassification rule not found in the laws read; treat as a risk, not as safe self-employment |

### Red lines (do not cross)

- **Lump sum for an excluded activity.** Never place consulting, design, accounting, legal or other professional or intellectual work, or trade or catering (outside the kiosk rule), in the lump sum (art. 49(9)-(11)).
- **Turnover suppression.** Never under-report turnover to stay below EUR 30,000.01. The tax authority can change the method by ruling (art. 49(7)), and undeclared income found from growth in assets is taxed at 80% (art. 10a).
- **VAT and the lump sum.** A VAT-registered taxpayer cannot use the lump sum (art. 49(12)).
- **Surtax.** Never leave out the municipal surtax when computing the burden of an individual.

## Worked cases

**Case 1 (decision): EUR 20,000 profit, sole trader or company paying out everything.** As a sole trader on actual profit (principal activity): 9% x 3,600 = 324 plus 15% x 8,000 = 1,200, total EUR 1,524. Through a company that pays out all its after-tax profit: corporate tax 9% x 20,000 = 1,800, dividend 18,200, dividend tax 15% x 18,200 = 2,730, total EUR 4,530. The sole trader route is EUR 3,006 cheaper. Both exclude the municipal surtax and social contributions, which must be added from the companion skills before deciding.

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
  - saving_sole_trader: company_route_tax - sole_trader_tax
expected:
  pit_band_9: 324
  pit_band_15: 1200
  sole_trader_tax: 1524
  corporate_tax: 1800
  dividend: 18200
  dividend_tax: 2730
  company_route_tax: 4530
  saving_sole_trader: 3006
```

**Case 2 (decision, the other way): EUR 150,000 profit kept in the business.** Sole trader: 324 + 15% x 138,000 = EUR 21,024. Company that retains the profit: 9% x 100,000 + 12% x 50,000 = EUR 15,000, so the company is EUR 6,024 cheaper while the money stays in. If the company then pays it all out, the 15% dividend tax on 135,000 (EUR 20,250) takes the company route to EUR 35,250, above the sole trader. The deciding figure is how much profit stays in the company.

```oa-check
name: Montenegro 2026 sole trader versus company on EUR 150,000 retained profit
inputs:
  profit: 150000
steps:
  - sole_trader_tax: max(0, min(profit, 12000) - 8400) * 0.09 + max(0, profit - 12000) * 0.15
  - corporate_tax: min(profit, 100000) * 0.09 + max(0, min(profit, 1500000) - 100000) * 0.12
  - saving_if_retained: sole_trader_tax - corporate_tax
  - company_if_distributed: corporate_tax + (profit - corporate_tax) * 0.15
expected:
  sole_trader_tax: 21024
  corporate_tax: 15000
  saving_if_retained: 6024
  company_if_distributed: 35250
```

## When to refuse or refer

- **Prohibition 1.** NEVER recommend the lump sum without the activity classification, the turnover evidence and the tax authority's ruling.
- **Prohibition 2.** NEVER present single-client work for one principal under employer-like control as safe self-employment; the reclassification rule is on the Not yet confirmed line below.
- **Prohibition 3.** NEVER omit the municipal surtax or social contributions when comparing routes.
- **Prohibition 4.** NEVER contradict the rates in montenegro-income-tax, me-corporate-income-tax or montenegro-social-contributions.
- **Prohibition 5.** NEVER present an item on the Not yet confirmed line as settled, or a planning comparison as definitive advice. Route the decision to a licensed Montenegrin tax adviser.

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Law, consolidated text through 160/25: read for arts. 10, 10a, 12, 37, 49, 50 (not reopened: wapi.gov.me refused connections on 2026-11-14) | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-30 |
| Law amending the Personal Income Tax Law, Official Gazette 160/25: read for arts. 14 and 21 (lump-sum wording; applies from 1 January 2026) (not reopened, as above) | https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0 | 2026-10-30 |
| Law amending the Personal Income Tax Law, Official Gazette 70/26: read for its two changes, art. 10(1)(4) (games of chance) and art. 50f | https://www.sluzbenilist.me/propisi/394390/download | 2026-11-14 |
| Corporate Profit Tax Law, consolidation through 88/24: read for art. 28 (not reopened, as above) | https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 | 2026-10-30 |
| Law amending the Corporate Profit Tax Law, Official Gazette 104/26: read for its application from 1 January 2027 and that art. 28 is unchanged (not reopened, as above) | https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0 | 2026-10-30 |
| Law on Financing Local Self-Government, consolidated through 149/25: read for arts. 8, 9 (not reopened, as above) | https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 | 2026-10-30 |
| Law on Compulsory Social Insurance Contributions, consolidated through 160/25: read for arts. 4(1)(23), 5(1)(12), 9(7), 11(5) (not reopened, as above) | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-30 |
| MONSTAT, average wages release of 30 January 2026: read for the 2025 average gross wage of EUR 1,206 ("prosječna bruto zarada iznosila je 1 206 eura") | https://www.monstat.org/cg/novosti.php?id=4638 | 2026-11-14 |

Not yet confirmed: every wapi.gov.me row was read on 2026-10-30 and could not be reopened on 2026-11-14, so re-read those texts in a browser before relying on them; the Ministry of Finance lump-sum scale and criteria under PIT Law art. 49(2), and so the actual 2026 lump-sum amounts (the old version's statement that the lump sum is one fixed monthly amount covering tax and contributions is not supported: the contribution base is set separately); the surtax rate each municipality has set for 2026; whether the surtax applies to the lump-sum tax; any statutory rule reclassifying a single-client sole trader as an employee (none found in the PIT or contributions law read); the date the EUR 30,000 threshold replaced an earlier EUR 18,000 threshold.
