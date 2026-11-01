---
name: sc-payroll-social
description: "Seychelles payroll for tax year 2026: Seychelles Pension Fund contributions of 5% employee and 5% employer, employer income tax withholding, non-monetary benefits tax at 15% and its values, the payroll withholding statements under the 2024 regulations, the 21st and 23rd deadlines, and penalties. Use for Seychelles employer contributions, SPF rate, payroll filing, payroll XML, or non-monetary benefits tax. Source-based; no accountant has signed it."
jurisdiction: SC
category: payroll
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Seychelles Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Every employer in Seychelles, including employers of domestic workers. Register employees within 7 days of employment ([SRC](https://src.gov.sc/seychelles-tax-system/)). Tax bands are in [Income tax](sc-personal-income-tax.md).

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| SPF employee | 5% of gross monthly salary, from 1 Jan 2023 | 2026 | https://pensionfund.sc/mandatory-contribution/ |
| SPF employer | 5% matched; total 10% | 2026 | same |
| SPF long-term plan | 2017 plan: rise to 10.5% by 2035, one percent every five years. A plan, not a rate in force | 2026 | https://pensionfund.sc/increase-in-mandatory-contribution-rate/ |
| Non-monetary benefits tax, paid by employer | 15% of taxable value, from 1 Jan 2023 | 2026 | https://src.gov.sc/income-and-non-monetary-benefits-tax/ |
| Accommodation value | Monthly: onsite shelter SCR 300; dormitory 600; bedrooms one 2,500, two 3,000, three 4,000, four 5,000 | 2026 | same |
| Accommodation exemption | Business stay of three months or less; construction and tourism staff | 2026 | same |
| Utilities | Actual cost; exempt for tourism staff | 2026 | same |
| In-house benefit | Exempt if the month total is within 20% of basic salary | 2026 | same |
| Meals, uniforms | Exempt | 2026 | same |
| Motor vehicle | Actual fuel and rental cost; employer-owned vehicle SCR 600 a day | 2026 | same |

No 2026 amendment to this rate was found on the SRC legislation list read on 1 Nov 2026, so 2026 rests on the instruments below staying in force.

## The base

SPF runs on gross monthly salary. No ceiling appears on the SPF page read. The benefit value falls to the extent the benefit is used for work or the employee pays for it.

## Deadlines and filing

SPF: by the 21st of the following month ([SPF](https://pensionfund.sc/mandatory-contribution/)). Tax and statements: by the 21st in person, the 23rd through the Tax Portal; payment by the 21st in person, the 23rd by portal or bank transfer ([Act 27 of 2023](https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf)).

Steps under [S.I. 19 of 2024](https://src.gov.sc/wp-content/uploads/2025/05/SI-19-2024-Income-and-Non-Monetary-Benefits-Tax-Payroll-Regulations-2024.pdf) and the [Payroll Guide](https://src.gov.sc/wp-content/uploads/2025/01/Payroll-Guide-2024-updated.pdf):

1. Pick the form: Payroll Withholding Statement; Simplified statement for fewer than 10 employees paying no exempt emoluments other than 13th month pay and overtime, plus non-monetary benefits; Domestic Worker statement; 13th Month statement.
2. Header: employer name, NIN for a sole trader, business registration number, year, month.
3. Section 1 employee details including 11-digit NIN or GOP, SPF number, TIN, dates, citizenship, rate. Section 2 emoluments. Section 3 tax. Section 4 non-monetary benefits. Section 5 total to remit.
4. Submit in XML to pit@src.gov.sc with TIN, month and year in the message, until the portal takes it. Employers with fewer than 10 employees or one domestic worker can file in person.
5. Pay, with the statement, and give employees payslips.

The guide predates any portal go-live; confirm the live route at [tms.src.gov.sc](https://tms.src.gov.sc/).

## Penalties and interest

Section 42 Revenue Administration Act additional tax applies to late statements ([guide](https://src.gov.sc/wp-content/uploads/2025/01/Payroll-Guide-2024-updated.pdf)). Amounts are in [Corporate income tax](sc-corporate-income-tax.md). An employer who fails to withhold or pay is personally liable.

## Cross-border points

Non-citizens need the [Income tax](sc-personal-income-tax.md) rate check. Whether a non-citizen pays SPF was not confirmed.

## Two worked examples that recompute

Citizen on SCR 20,000: SPF SCR 1,000 from each side, income tax SCR 2,216.68 on the gross, assuming no SPF relief (see below).

```oa-check
name: Citizen, SCR 20,000
inputs:
  pay: 20000
steps:
  - spf_ee: pay * 0.05
  - spf_er: pay * 0.05
  - tax: (10000 - 8555.5) * 0.15 + (pay - 10000) * 0.20
  - cost: pay + spf_er
expected:
  cost: 21000
```

Decision: pay SCR 40,000 as a scheme bonus or extra salary in one month, for basic of SCR 20,000 a month. Scheme bonus: SCR 20,000 exempt, SCR 20,000 at 15%, SCR 3,000. As salary the month's tax rises by SCR 8,000. The scheme saves SCR 5,000.

```oa-check
name: Bonus scheme against salary
inputs:
  basic: 20000
  extra: 40000
steps:
  - bonus_tax: (extra - basic) * 0.15
  - salary_tax: extra * 0.20
  - saving: salary_tax - bonus_tax
expected:
  saving: 5000
```

## Ask the client first

- Headcount, and any domestic workers?
- Citizens or non-citizens?
- Gross pay and any exempt emoluments?
- Benefits in kind, and the sector?
- Bonus scheme or 13th month pay?

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the figures cited: Seychelles Pension Fund, Mandatory Contribution page | https://pensionfund.sc/mandatory-contribution/ | 2026-11-01 |
| Read for the figures cited: Seychelles Pension Fund, Increase in mandatory contribution rate (2017 notice) | https://pensionfund.sc/increase-in-mandatory-contribution-rate/ | 2026-11-01 |
| Read for the figures cited: SRC Income and Non-Monetary Benefits Tax page, whole page | https://src.gov.sc/income-and-non-monetary-benefits-tax/ | 2026-11-01 |
| Read for the figures cited: S.I. 19 of 2024, regs 1 to 3 | https://src.gov.sc/wp-content/uploads/2025/05/SI-19-2024-Income-and-Non-Monetary-Benefits-Tax-Payroll-Regulations-2024.pdf | 2026-11-01 |
| Read for the figures cited: SRC Payroll Guide v3 January 2025, read by OCR | https://src.gov.sc/wp-content/uploads/2025/01/Payroll-Guide-2024-updated.pdf | 2026-11-01 |
| Read for the figures cited: Revenue Law (Amendment) Act 2023 (Act 27 of 2023), ss 3, 4, 7 | https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf | 2026-11-01 |
| Read for the figures cited: SRC Tax System page, whole page read | https://src.gov.sc/seychelles-tax-system/ | 2026-11-01 |

Not yet confirmed: SPF wage ceiling; SPF treatment of non-citizens; SPF late payment penalty; whether SPF contributions reduce taxable pay; employee status form date under the 2024 regulations; employer social security beyond SPF.

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
