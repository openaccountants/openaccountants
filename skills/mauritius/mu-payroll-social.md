---
name: mu-payroll-social
description: >
  Mauritius payroll and social contributions for 2026. Covers PAYE under the cumulative system, Contribution Sociale Generalisee (CSG), National Savings Fund, training levy, the Portable Retirement Gratuity Fund, end of year bonus, directors fees, car benefit, the joint monthly return, the Return of Employees, self-employed contributions, penalties and interest. Use for running a Mauritius payroll, employer on-costs, PAYE or CSG questions, or MRA employer returns.
jurisdiction: MU
category: payroll
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Employers of staff in Mauritius, and self-employed people paying social contribution. Income tax bands are in [Income tax](mu-income-tax.md). Daily-paid workers paid after each day's work are outside PAYE ([MRA PAYE page](https://www.mra.mu/employers/paye)).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| CSG employee | 1.5% | Monthly remuneration up to Rs 50,000 | 2026/27 | https://www.mra.mu/download/SocialContributionAndSocialBenefitsAct2021.pdf |
| CSG employer | 3% | Same | 2026/27 | same |
| CSG employee, higher | 3% | Above Rs 50,000 | 2026/27 | same |
| CSG employer, higher | 6% | Same | 2026/27 | same |
| CSG domestic employee | Nil employee, 3% employer | Up to Rs 3,000 in aggregate | 2026/27 | same |
| CSG self-employed, low | Rs 150 a month | Net income up to Rs 10,000 a month | 2026/27 | same |
| CSG self-employed, middle | 1.5% of 90% of net income, or Rs 150 if higher | Up to Rs 50,000 a month | 2026/27 | same |
| CSG self-employed, high | 3% of 90% of net income | Above Rs 50,000 a month | 2026/27 | same |
| NSF employee | 1% of basic wage | Between the limits below | 2026/27 | https://www.mra.mu/employers/npf-nsf-contributions |
| NSF employer | 2.5% of basic wage | Same | 2026/27 | same |
| NSF maximum wage | Rs 29,710 a month | From 1 July 2026 | 2026/27 | same |
| NSF minimum wage | Rs 4,580 a month; Rs 2,910 private household | From 1 July 2026 | 2026/27 | same |
| Training levy | 1.5% of total basic wage | No ceiling; excludes household workers, overtime, bonus, allowances | 2026/27 | https://www.mra.mu/download/TheHumanResourceDevelopmentAct2003.pdf |
| PAYE no-withholding point | Monthly emoluments up to Rs 38,462 | Not directors' fees | 2026/27 | https://www.mra.mu/employers/paye |
| Directors' and board fees | 15%, or 20% at their request | s.96 | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Car benefit, up to Rs 3 million | Rs 12,000, 13,500, 15,000 a month by engine; electric Rs 13,500 | Up to 1,600cc, 1,601 to 2,000cc, above 2,000cc | 2026/27 | https://www.mra.mu/download/PayrollTaxes.pdf |
| Car benefit, above Rs 3 million | Rs 25,000 to Rs 5m, Rs 35,000 to Rs 8m, Rs 50,000 above | From 1 October 2025 | 2026/27 | same |

No NSF is due for an employee under 18 or past final retirement age of 70, or for a non-citizen employee of an export manufacturer in the first 2 years ([MRA guide](https://www.mra.mu/employers/npf-nsf-contributions)).

## The base

CSG runs on remuneration; end of year bonus prescribed by law is computed separately on the basic pay part ([MRA CSG page](https://www.mra.mu/business/csg)). NSF and levy run on basic wage, excluding bonus and allowances. A special allowance or similar item follows its own communique.

PAYE is cumulative: take chargeable income from July to date, deduct 1/13 of the reliefs on the Employee Declaration Form (EDF) for each month, apply the bands, deduct tax already withheld, round down to the rupee. The month the statutory bonus is paid counts as the 13th month. An employee files one EDF with one employer, online. A non-citizen resident files one too. A non-resident gets no reliefs. For a top earner the 35% band applies above Rs 12 million from July 2026.

**AUDIT FLASH POINT** MRA's PAYE page still shows three bands and the individual Fair Share Contribution through June 2028. The Act cut both for income from 1 July 2026: see [Income tax](mu-income-tax.md). Check payroll software for the update.

## Deadlines and filing

1. Register as employer and get the Employer Registration Number (ERN) and password.
2. Each month log in at [MRA e-Services](https://www.mra.mu/index.php/e-services) with the ERN.
3. Choose the Joint PAYE and CSG/NSF return, by screen input or CSV in the MRA format.
4. Include ALL employees. Show basic wage, wage relativity adjustment, and the total on separate items.
5. Download new EDFs monthly and update reliefs.
6. Submit and pay electronically by the end of the following month (ITA s.100(1B); SC Act s.6(2)). May and November are due 2 days before the end of June and December, excluding Saturdays and public holidays (s.100(1C)).
7. Training levy goes with the same cycle: end of the following month if electronic (HRD Act s.18(3)).
8. PRGF: employers with no private pension scheme pay monthly (Workers' Rights Act s.94). The Act says the 20th of the next month; the [MRA calendar](https://www.mra.mu/important-dates) lists the PRGF return with the end-of-month items. Use the earlier date.
9. By 15 August: Statement of Emoluments to staff, and the Return of Employees for the prior income year ([PAYE Guide](https://www.mra.mu/download/PAYEGuide.pdf)).
10. Self-employed may elect an annual return, paid in advance by 15 October ([SC Act](https://www.mra.mu/download/SocialContributionAndSocialBenefitsAct2021.pdf) s.6(2)(c)).

## Penalties and interest

| Item | Figure | Conditions | Source |
|---|---|---|---|
| PAYE late | 10% of unpaid tax | s.101 | https://www.mra.mu/download/ITAConsolidated.pdf |
| PAYE interest | 0.5% per month or part | s.122D(1)(a) | same |
| Not joining e-filing | Rs 5,000 per month, cap Rs 50,000 | s.101A | same |
| CSG late | 10% plus 1% per month | SC Act s.10 | https://www.mra.mu/download/SocialContributionAndSocialBenefitsAct2021.pdf |
| NSF late | 5% surcharge per month or part | NSF Act s.16 | https://www.mra.mu/download/TheNationalSavingsFundAct1995.pdf |
| PRGF late | 10% surcharge plus 1% per month | Workers' Rights Act | https://www.mra.mu/download/WorkersRightsAct2019.pdf |

## Cross-border points

A non-resident's emoluments have no reliefs: gross pay for the period is chargeable. Duties performed wholly or mainly in Mauritius are Mauritius-source wherever paid (s.74). Fees to directors of a resident company are Mauritius-source wherever the work is done.

## Two worked examples that recompute

**Example 1.** Basic pay Rs 60,000 a month, private employer. Employee CSG Rs 1,800, NSF Rs 297.10. Employer CSG Rs 3,600, NSF Rs 742.75, levy Rs 900. Employer on-cost Rs 5,242.75.

```oa-check
name: Rs 60,000 basic, 2026/27 ceilings
inputs:
  basic: 60000
  nsfmax: 29710
steps:
  - ee_csg: basic * 0.03
  - ee_nsf: min(basic, nsfmax) * 0.01
  - er_csg: basic * 0.06
  - er_nsf: min(basic, nsfmax) * 0.025
  - levy: basic * 0.015
  - oncost: er_csg + er_nsf + levy
expected:
  ee_nsf: 297.10
  oncost: 5242.75
```

**Example 2. Decision: raise basic pay to Rs 51,000, or keep Rs 50,000 and pay Rs 1,000 as allowance?** The rate switches on the whole amount. At Rs 51,000 employee CSG is Rs 1,530 and employer CSG Rs 3,060. At Rs 50,000 it is Rs 750 and Rs 1,500. A real allowance can change the base only where the law's remuneration definition leaves it out, so check first: disguised pay is a risk.

```oa-check
name: CSG jump at Rs 50,000
inputs:
  low: 50000
  high: 51000
steps:
  - low_total: low * 0.015 + low * 0.03
  - high_total: high * 0.03 + high * 0.06
  - extra: high_total - low_total
expected:
  extra: 2340.00
```

## Ask the client first

1. Private or public sector, and any private pension scheme?
2. Basic pay, allowances and bonus by employee?
3. Citizen, non-citizen resident, or non-resident?
4. EDF on file?
5. Directors paid fees?
6. Company cars, with cost and engine size?

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Contribution and Social Benefits Act 2021: ss.4, 6, 10, First Schedule | https://www.mra.mu/download/SocialContributionAndSocialBenefitsAct2021.pdf | 2026-11-01 |
| Income Tax Act consolidated: ss.93 to 101A, 122D, s.74 | https://www.mra.mu/download/ITAConsolidated.pdf | 2026-11-01 |
| NSF Act: definition of basic wage, s.16 | https://www.mra.mu/download/TheNationalSavingsFundAct1995.pdf | 2026-11-01 |
| HRD Act: s.18, First Schedule | https://www.mra.mu/download/TheHumanResourceDevelopmentAct2003.pdf | 2026-11-01 |
| Workers' Rights Act: Part VIII s.94 and surcharge | https://www.mra.mu/download/WorkersRightsAct2019.pdf | 2026-11-01 |
| MRA NPF/NSF guide page, read for the 1 July 2026 limits | https://www.mra.mu/employers/npf-nsf-contributions | 2026-11-01 |
| MRA CSG page, read in full | https://www.mra.mu/business/csg | 2026-11-01 |
| MRA PAYE page, read, out of date on bands | https://www.mra.mu/employers/paye | 2026-11-01 |
| MRA letter of 6 October 2025, read in full | https://www.mra.mu/download/PayrollTaxes.pdf | 2026-11-01 |
| PAYE Guide, sections 13 and 14 and EDF parts read | https://www.mra.mu/download/PAYEGuide.pdf | 2026-11-01 |
| MRA tax calendar and e-Services menu read | https://www.mra.mu/important-dates | 2026-11-01 |

Not yet confirmed: the prescribed PRGF contribution rate; the 2026/27 monthly PAYE bracket table, because no MRA letter for the 35% band was found; the National Minimum Wage; the remuneration definition for allowances under CSG. The old version's CSG employer rates of 4.5% and 9% apply only to some public-sector cases shown on the MRA page before their salary review.

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
