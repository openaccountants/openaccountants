---
name: ls-income-tax
description: "Personal income tax for residents and non-residents of Lesotho, including employees, sole traders and trustees. Covers Lesotho tax year 2026-27 (1 April 2026 to 31 March 2027), figures read from Revenue Services Lesotho and gazetted law on 1 November 2026. Use when someone asks about lesotho personal income tax in Lesotho, what applies, what the rate or threshold is, when to file or pay, what a late filing costs, or how an amount is worked out. Not signed off by an accountant. It states which points could not be read at source so they are not relied on."
jurisdiction: LS
category: international
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
version: 0.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lesotho Personal Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with Lesotho income: residents on worldwide income, non-residents on Lesotho-source income. An individual is resident if they have a normal place of abode in Lesotho and are present for part of the year, or are present on more than 182 days in any consecutive twelve months that includes part of the year, or are Lesotho Government officials posted overseas (Income Tax Act s.5).

Lesotho's tax year runs 1 April to 31 March. This skill covers 2026-27, from 1 April 2026.

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Lower band | 20% | Chargeable income up to M77,760 a year, residents | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Band limit | M77,760 a year (M6,480 a month) | In force 1 April 2026 | https://www.rsl.org.ls/sites/default/files/2026-09/INCOME%20TAX%20%28AMA%29%20REGULATIONS%20No.24%20of%20%202026.%20%281%29%20%281%29_0.pdf |
| Upper band | 30% | Chargeable income above M77,760 a year | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Personal tax credit | M12,240 a year (M1,020 a month) | Non-refundable; natural persons | https://www.rsl.org.ls/sites/default/files/2026-09/INCOME%20TAX%20%28AMA%29%20REGULATIONS%20No.24%20of%20%202026.%20%281%29%20%281%29_0.pdf |
| Tax-free employment income | M5,100 a month | Follows from the credit: 5,100 x 20% = 1,020 | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Non-resident rate | 25% | Standard rate, s.12(1). If the person lives permanently abroad but works or trades full-time in Lesotho, the 20% and 30% bands apply to that income, s.12(2) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Trustees, minors, electing non-residents | 40% | Fourth Schedule item 1 | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Commercial farming | 10% | Fourth Schedule item 2 | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Fringe benefits tax | 40% | Paid by the employer on the taxable value | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Interest paid to resident individuals | 10%, final | First M500 exempt | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf |

## The base

Chargeable income is gross income less allowed deductions. There is no separate capital gains tax: gains on business and investment assets go into chargeable income at ordinary rates under the Income Tax Act. Apply the bands, then take off the credit. The credit is non-refundable, so it cannot create a refund. Approved pension or retirement annuity contributions are allowable deductions (RSL employment guide). Business losses of an individual carry forward against later business income only (s.47).

## Deadlines and filing

- Return: by 30 June after the year ends (s.128; RSL filing page). File on the RSL e-filing platform or on paper with financial statements, withholding schedule and P16 tax certificates.
- Provisional tax: three instalments of 30% of last year's liability, due 30 September, 31 December and 31 March (s.150; RSL guide).
- Pay through RSL e-Payments, M-Pesa or the commercial banks named by RSL, and send proof to receipts@rsl.org.ls.

## Penalties and interest

The additional tax rate for late filing and late payment is 22% per twelve-month period as stated by RSL. It also applies to under-estimation and tax not withheld (Income Tax Act Part on additional tax, s.192 onward), where the specified rate is the rate RSL publishes. Poor records: additional tax equal to double the tax involved, as the Act words it.

## Cross-border points

Residents are taxed on worldwide income. Foreign tax relief and treaties: see ls-corporate-income-tax for the treaty list. Non-residents with Lesotho-source interest, dividends, royalties or service fees: see the withholding rows there.

## Two worked examples that recompute

Example 1: resident, chargeable income M120,000. First M77,760 at 20% is M15,552. Remaining M42,240 at 30% is M12,672. Total M28,224 less credit M12,240 is M15,984.

```oa-check
name: Resident M120,000, 2026-27
inputs:
  income: 120000
steps:
  - low: min(income, 77760) * 0.20
  - high: max(income - 77760, 0) * 0.30
  - tax: max(low + high - 12240, 0)
expected:
  tax: 15984.00
```

Example 2, a decision: should a person earning M60,000 expect to pay? No. M60,000 at 20% is M12,000, under the credit of M12,240, and the unused M240 is lost because the credit is non-refundable.

```oa-check
name: Resident M60,000, credit not refundable
inputs:
  income: 60000
steps:
  - low: min(income, 77760) * 0.20
  - tax: max(low - 12240, 0)
expected:
  tax: 0.00
```

## Ask the client first

1. Resident under s.5 for the year?
2. Employment, business, or both?
3. Total chargeable income for the year?
4. Approved pension contributions?
5. Provisional tax and withholding already paid?
6. Foreign income and foreign tax?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment of Monetary Amounts) Regulations 2026, LN 24 of 2026; read in full (scan) | https://www.rsl.org.ls/sites/default/files/2026-09/INCOME%20TAX%20%28AMA%29%20REGULATIONS%20No.24%20of%20%202026.%20%281%29%20%281%29_0.pdf | 2026-11-01 |
| RSL Guide on Taxation of Employment Income 26-27; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf | 2026-11-01 |
| Income Tax Act 1993, RSL copy updated to 1 April 2012; read the sections cited; later amendments are not in this copy | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | 2026-11-01 |
| RSL Withholding Tax Public Ruling; read the rate tables | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf | 2026-11-01 |
| RSL Tax Guide on Provisional Tax; read in full | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf | 2026-11-01 |
| RSL Corporate Income Tax Guide; read in full | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf | 2026-11-01 |
| RSL Filing of Tax Returns page; read in full | https://www.rsl.org.ls/filing-tax-returns | 2026-11-01 |

Not yet confirmed: amendments to the Income Tax Act after 1 April 2012 other than those restated by RSL guides and LN 24 of 2026; the current specified rate under s.192; the 22% rate rests on an undated RSL guide; the Income Tax Amendments and Tax Administration Bill announced for 2026-27 in the budget speech have not been traced as enacted.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
