---
name: ls-payroll-social
description: "PAYE, fringe benefits tax and contributions for employers in Lesotho. Covers Lesotho tax year 2026-27 (1 April 2026 to 31 March 2027), figures read from Revenue Services Lesotho and gazetted law on 1 November 2026. Use when someone asks about lesotho payroll and social contributions in Lesotho, what applies, what the rate or threshold is, when to file or pay, what a late filing costs, or how an amount is worked out. Not signed off by an accountant. It states which points could not be read at source so they are not relied on."
jurisdiction: LS
category: payroll
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
version: 0.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lesotho Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers paying employees in Lesotho. Employment income includes wages, salaries, bonuses, allowances, overtime, leave pay, commission, gratuity, fees and severance pay (s.18(1)).

Lesotho's tax year runs 1 April to 31 March. This skill covers 2026-27, from 1 April 2026.

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Lower band | 20% | Chargeable income up to M77,760 a year, residents | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Band limit | M77,760 a year (M6,480 a month) | In force 1 April 2026 | https://www.rsl.org.ls/sites/default/files/2026-09/INCOME%20TAX%20%28AMA%29%20REGULATIONS%20No.24%20of%20%202026.%20%281%29%20%281%29_0.pdf |
| Upper band | 30% | Chargeable income above M77,760 a year | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Personal tax credit | M12,240 a year (M1,020 a month) | Non-refundable; natural persons | https://www.rsl.org.ls/sites/default/files/2026-09/INCOME%20TAX%20%28AMA%29%20REGULATIONS%20No.24%20of%20%202026.%20%281%29%20%281%29_0.pdf |
| No tax below | M5,100 a month |  | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Fringe benefits tax | 40% | Employer pays on the taxable value | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Pension deduction cap | 20% of employment income | Contributions above this are a superannuation fringe benefit | https://www.rsl.org.ls/sites/default/files/2024-07/FBT%20Public%20Ruling.pdf |
| National social security | unverified | The older skill said no compulsory contributory scheme for private employees; not confirmed at source | unverified: not opened |
| Occupational pension contributions | unverified | Scheme rules set them; the older figure of about 5% each came from a secondary site | unverified: not opened |

## The base

Taxable pay is total earnings less allowable deductions such as approved pension contributions. Apply the monthly bands, then the M1,020 credit. Benefits in kind go through FBT, not PAYE. A low-interest loan is a benefit where the rate is under two thirds of the commercial lending rate (RSL FBT ruling).

## Deadlines and filing

- PAYE: pay RSL by the 15th of the month after deduction (RSL guide).
- FBT return: each quarter to 30 June, 30 September, 31 December, 31 March, within 14 days (s.152).
- Year end: tax certificates to employees within 28 days after the year ends, or within 7 days after employment ends; employer statement to RSL within 28 days.

## Penalties and interest

If tax was not withheld, the employer is liable and may recover it from the employee (RSL guide). Additional tax on tax not withheld runs at the specified rate, and RSL states 22% per twelve-month period for late filing and payment.

## Cross-border points

Foreign nationals working in Lesotho: residence under s.5 decides the bands; see the RSL guide on Taxation of Foreign Nationals. Services paid to a non-resident outside employment are in ls-corporate-income-tax.

## Two worked examples that recompute

Example 1 (RSL's own): M10,000 a month. M6,480 at 20% is M1,296; M3,520 at 30% is M1,056; less M1,020 gives M1,332.

```oa-check
name: PAYE M10,000 a month
inputs:
  pay: 10000
steps:
  - low: min(pay, 6480) * 0.20
  - high: max(pay - 6480, 0) * 0.30
  - paye: max(low + high - 1020, 0)
expected:
  paye: 1332.00
```

Example 2, a decision: is pay of M5,100 taxed? No. 20% is M1,020, which the credit clears.

```oa-check
name: PAYE M5,100 a month
inputs:
  pay: 5100
steps:
  - paye: max(min(pay, 6480) * 0.20 - 1020, 0)
expected:
  paye: 0.00
```

## Ask the client first

1. Gross monthly pay and allowances?
2. Benefits in kind: car, housing, loans?
3. Approved pension scheme, and contribution rates?
4. Any non-resident staff?
5. Leavers during the year?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment of Monetary Amounts) Regulations 2026, LN 24 of 2026; read in full (scan) | https://www.rsl.org.ls/sites/default/files/2026-09/INCOME%20TAX%20%28AMA%29%20REGULATIONS%20No.24%20of%20%202026.%20%281%29%20%281%29_0.pdf | 2026-11-01 |
| RSL Guide on Taxation of Employment Income 26-27; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf | 2026-11-01 |
| Income Tax Act 1993, RSL copy updated to 1 April 2012; read the sections cited; later amendments are not in this copy | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | 2026-11-01 |
| RSL FBT Public Ruling; read the rate and example parts | https://www.rsl.org.ls/sites/default/files/2024-07/FBT%20Public%20Ruling.pdf | 2026-11-01 |

Not yet confirmed: mandatory social security for private employers, the old-age pension statute, occupational pension rates, the annual reconciliation form name and any wage cap; the older skill's points on these are carried here unverified.

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
