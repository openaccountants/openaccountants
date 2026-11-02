---
name: tn-income-tax
description: "Tunisia personal income tax (IRPP) for tax year 2026: residence test, eight-band scale, family deductions, employee expenses, minimum tax, optional flat tax from the 2026 finance law, return deadlines by income type and advance payments. Use for any question on how much income tax an individual, employee, trader or professional pays in Tunisia, IRPP, baremes, declaration annuelle, forfait, or when a Tunisian return is due. Figures come from the DGI texts; items that could not be opened are marked unverified."
version: 1.1
jurisdiction: TN
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia Personal Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals with a habitual residence in Tunisia, taxed on all income of the previous year: a main home in Tunisia, or 183 days or more of stay in the calendar year, continuous or not, or State agents posted abroad who are not taxed on all their income there (Code IRPP-IS art. 2). Non-residents are taxed only on Tunisian-source income and the capital gain in art. 27(2) (art. 3). Tax year: calendar 2026, return filed in 2027 for 2026 income.

Excluded: companies (see [corporate income tax](tn-corporate-income-tax.md)). The method note by another author sits in [IRPP calculation](irpp-calculation.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Band 0 to TND 5,000 | 0% | 2026 | Annual net income; fraction of a dinar counts as one dinar. Art. 44 I. LF 2026 did not change the scale | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Above 5,000 to 10,000 | 15% | 2026 | same | same |
| Above 10,000 to 20,000 | 25% | 2026 | same | same |
| Above 20,000 to 30,000 | 30% | 2026 | same | same |
| Above 30,000 to 40,000 | 33% | 2026 | same | same |
| Above 40,000 to 50,000 | 36% | 2026 | same | same |
| Above 50,000 to 70,000 | 38% | 2026 | same | same |
| Above 70,000 | 40% | 2026 | same | same |
| Employee flat expenses | 10%, cap TND 2,000 a year | 2026 | On pay after compulsory pension and social deductions. Art. 26 I | same |
| Pension allowance | 25% of gross | 2026 | 30% from 1 Jan 2027, 40% from 2028, 50% from 2029. LF 2026 art. 56 | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf |
| Head of household deduction | TND 300 | 2026 | Art. 40 I | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Child deduction | TND 100 each | 2026 | First four dependent children under 20 on 1 January, no separate income. Art. 40 II | same |
| Student child | TND 1,000 | 2026 | Higher studies, no grant, under 25 on 1 January. Art. 40 III | same |
| Disabled child | TND 2,000 | 2026 | Any age or rank. Art. 40 III | same |
| Dependent parent | 5% of taxable net income, cap TND 450 a parent | 2026 | Parent files a return; parent income plus deduction at most twice the SMIG; split between children. Art. 40 IV | same |
| Minimum tax, commercial and non-commercial | 0.2% of turnover, floor TND 300 | 2026 | Due even with no turnover. Art. 44 II | same |
| Reduced minimum tax | 0.1%, floor TND 200 | 2026 | Income with two-thirds deduction, or price-controlled goods with gross margin up to 6%. Art. 44 II | same |
| Optional flat tax, turnover up to TND 50,000 | TND 4,000 a year | 2026 | Half in rural zones and villages; see conditions below. LF 2026 art. 91 | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf |
| Optional flat tax, TND 50,001 to 100,000 | TND 5,000 a year | 2026 | same | same |
| Basic flat tax, turnover up to TND 10,000 | TND 400 a year | 2026 | Half outside pre-2015 communal zones. Art. 44 ter | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Basic flat tax, turnover TND 10,000 to 100,000 | 3% of turnover | 2026 | +50% if filed over 30 days late. Art. 44 ter | same |
| Social Solidarity Contribution | unverified: 0.5% in the old file | 2026 | LF 2026 art. 87 keeps the exceptional rule for income whose return falls due in 2023 to 2026. The rate sits in LF 2018 art. 53, not opened | unverified |
| Non-resident short-stay employees | unverified: 20% on gross in the old file | 2026 | Stays up to 6 months; article not traced | unverified |

## The base

Net income is computed by category, then added. From pay deduct compulsory pension and social contributions, then flat expenses (art. 26 I). From the total deduct family allowances (art. 40). Benefits in kind count at real value; a company car used privately is taxed by the art. 26 III method. From 2026 the value of work transport provided to workers is outside tax (LF 2026 art. 22). Cash donations to the bodies listed in art. 39 I(6) are deductible with a detailed list and proof of payment (LF 2026 art. 38). Income tax itself is not deductible (art. 41).

Optional flat tax (LF 2026 art. 91, Code art. 44 ter): turnover at most TND 100,000, no imports, no wholesale, no non-commercial or brokerage activity, not moved to the real regime by an audit. It also covers listed declassed activities such as cafes and car mechanics. It discharges tax on spontaneously declared turnover if deemed profit is at most 25% of it, and bars ordinary audit for six years, with exceptions.

## Deadlines and filing

| Filer | Annual return due |
|---|---|
| Capital, property or foreign income other than pay | 25 February |
| Traders | 25 April |
| Services, industry, professions, or more than one category | 25 May |
| Artisans | 25 July |
| Farming or fishing | 25 August |
| Employees and pensioners | 5 December |

Source: art. 60 I. The old file's single 25 June date is not in art. 60. Optional flat tax: two equal parts by 25 April and 25 October (LF 2026 art. 91).

From the second year of activity, three advance payments (acomptes), each 30% of the prior year's tax, are due in the first 25 days of the sixth, ninth and twelfth months after year end for individuals in business or a profession; not farmers, fishers or basic flat-tax payers; artisans skip the first (art. 51). Withholding is credited against them.

Steps for online filing (DGI): 1. Fill in the adhesion form and lodge it at your tax control office. 2. Buy an electronic certificate from ANCE, DIGIGO or USB token. 3. Log in to the online filing service on jibaya.tn and complete the return. Box numbers and post-filing steps: see Not yet confirmed.

## Penalties and interest

The flat tax rises 50% if the return is over 30 days late (art. 44 ter). Minimum tax rises 50% if paid over a month late (art. 44 II). General late-payment rates sit in the Tax Procedures Code, which could not be opened.

## Cross-border points

Residents declare foreign income; foreign income other than pay is due 25 February, foreign pay 5 December (art. 60). Withholding on non-residents: [cross-border](tn-cross-border.md).

## Two worked examples that recompute

Simple: net taxable income TND 30,000. 5,000 at 0%, 5,000 at 15%, 10,000 at 25%, 10,000 at 30%. Tax TND 6,250, matching the 20.83% effective rate in art. 44.

```oa-check
name: IRPP on TND 30000
inputs:
  income: 30000
steps:
  - b15: (min(income, 10000) - 5000) * 0.15
  - b25: (min(income, 20000) - 10000) * 0.25
  - b30: (min(income, 30000) - 20000) * 0.30
  - tax: b15 + b25 + b30
expected:
  tax: 6250.00
```

Decision: trader with turnover TND 80,000 and profit TND 20,000, single, in a town. Optional flat tax is TND 5,000. On the real regime the scale gives 750 + 2,500 = TND 3,250, against a minimum tax of TND 300 (0.2% × 80,000 is 160, below the floor). At this profit the real regime is cheaper by TND 1,750, before bookkeeping cost and the six-year audit protection.

```oa-check
name: Flat tax against real regime
inputs:
  profit: 20000
  turnover: 80000
  flat: 5000
steps:
  - scale: (min(profit, 10000) - 5000) * 0.15 + (profit - 10000) * 0.25
  - minimum: max(turnover * 0.002, 300)
  - real: max(scale, minimum)
  - saving: flat - real
expected:
  real: 3250.00
  saving: 1750.00
```

## Ask the client first

1. Where is your main home, and how many days in Tunisia in 2026?
2. Which income categories do you have?
3. Family status and dependants on 1 January?
4. If in business: activity, turnover, imports, wholesale?
5. What tax was withheld, and do you hold the certificates?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code IRPP-IS, French text updated to LF 2025, archived copy of the DGI file; articles cited in this skill read. The 2026 edition page exists but its PDF could not be opened | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf | 2026-11-01 |
| Loi n° 2025-17 du 12 decembre 2025, loi de finances 2026, JORT n° 148, archived copy of the DGI file; tax articles read | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf | 2026-11-01 |
| DGI page on online filing, archived April 2025; steps read | https://web.archive.org/web/20250419084126/https://jibaya.tn/blog/la-tele-declaration-fiscale/ | 2026-11-01 |

Not yet confirmed: Social Solidarity Contribution rate and 5,000 exemption (LF 2018 art. 53; Note commune 1 of 2026 PDF not opened). Non-resident short-stay 20% rate from the old file. Employer monthly remittance from the old file (form exists; rule not re-read). The old 9.68% employee CNSS figure (see payroll skill). Return form boxes. Any change to the code by LF 2026 not named here: LF 2026 was searched for references to the code, the 2026 consolidated edition was not read.

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
