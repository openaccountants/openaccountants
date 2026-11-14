---
name: jm-tax-overview
description: "Overview of the Jamaican tax system for 2026, to route a question to the right skill. Tax Administration Jamaica (TAJ) collects income tax, General Consumption Tax and payroll contributions; the year of assessment is the calendar year. Headline figures for 2026: personal threshold J$1,876,614 effective, 25% and 30% on statutory income with the break at J$6,000,000, company tax 25% unregulated and 33 1/3% regulated, GCT 15% standard with a J$15,000,000 registration threshold, returns due 15 March. Trigger on Jamaica tax overview, how is tax in Jamaica, TAJ, Jamaica tax system. Not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jm-tax-overview"
  jurisdiction: "JM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Jamaica Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone who needs the shape of Jamaican tax for 2026 before loading a detailed skill. Tax Administration Jamaica (TAJ) administers income tax, GCT and the payroll contributions; the currency is the Jamaican dollar (J$). Residents are taxed on income from all sources; non-residents on Jamaica-source income.

| Question | Skill |
|---|---|
| Individual or self-employed income tax, S04 | `jm-income-tax` |
| Company income tax, IT02 | `jm-corporate-income-tax` |
| GCT, Form 4A | `jamaica-gct` |
| Employer PAYE, NIS, NHT, Education Tax, HEART | `jm-payroll-social` |
| Forming a company or business name | `jm-company-formation` |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Year of assessment | Calendar year | Individuals and companies | TAJ, rates, threshold and exemptions 2013 to 2028: https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 |
| Personal threshold, effective 2026 | J$1,876,614 | Residents only; PAYE uses a higher annual rate from 1 April 2026 (see `jm-payroll-social`) | same |
| Personal rates | 25% above the threshold to J$6M of statutory income, 30% above J$6M | Statutory income | same |
| Non-resident individual | 25%, no threshold | Unless a treaty sets a rate | TAJ, non-residents and income tax: https://www.jamaicatax.gov.jm/documents/10194/20399532/1-Non-residents+and+Income+Tax+Final+Document.pdf/d8ccd3fa-4a99-e798-1a4b-841e952d82ba |
| Company rate, unregulated | 25% | From 1 January 2013 | Jamaica Information Service: https://jis.gov.jm/new-threshold-and-corporate-income-tax-rate-january-1/ |
| Company rate, regulated | 33 1/3% | Regulated by the BOJ, FSC, OUR or Ministry of Finance | same |
| GCT standard rate | 15% | From April 2020; 25% on telephone services | TAJ, General Consumption Tax guide: https://www.jamaicatax.gov.jm/general-consumption-tax1 |
| GCT registration threshold | J$15,000,000 over 12 months | From 1 April 2025 | same |
| Individual and company annual returns | 15 March of the following year | S04 and IT02, with estimates | TAJ, self-employed guide (updated November 2026): https://www.jamaicatax.gov.jm/documents/10194/20399532/4-Income+Tax+and+Self+Employed+Individuals++%28+Updated+Nov.+2026+%29.pdf/c4f3878c-7a44-0a3b-d4a2-4a8cbef3f9ef |
| Quarterly estimates | 15 March, 15 June, 15 September, 15 December | Self-employed | same |
| Employee contributions | NIS 3% to J$5,000,000, NHT 2%, Education Tax 2.25% | Employer: NIS 3%, NHT 3%, Education Tax 3.5%, HEART 3% | TAJ, payroll taxes and statutory contributions (April 2025 edition): https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 |

## The base

- Income tax is charged on statutory income: total income less exemptions (pension and age relief) and deductions (NIS, approved pension schemes, business expenses, capital allowances).
- GCT is a value added tax on supplies of goods and services, including imported services, with zero-rated exports and exempt supplies.
- Payroll contributions are charged on gross emoluments (NIS, NHT, HEART) or statutory income (Education Tax).
- Capital gains, transfer tax and stamp duty on property and shares are not covered here (see Not yet confirmed).

## Deadlines and filing

All income tax returns are filed online on the TAJ portal; GCT Form 4A is due by the last day of the month after the period; employer S01 by the 14th; S02 by 31 March. Details are in each skill.

## Penalties and interest

Each skill carries its own penalties. PAYE paid late is increased at 50% a year (Income Tax Act s. 41(2)(a), TAJ employer's guide); failure to register for GCT costs J$5,000 (individual) or J$10,000 (company) plus 2.5% a month.

## Cross-border points

Residents: worldwide income. Non-residents: Jamaica-source income at 25% for individuals, with treaty rates for listed countries (see `jm-income-tax`). Imported services are self-assessed for GCT.

## Two worked examples that recompute

### Example 1: Resident with statutory income J$8,000,000 in 2026

Income tax = 25% x (J$6,000,000 - J$1,876,614) + 30% x J$2,000,000 = J$1,030,846.50 + J$600,000 = J$1,630,846.50.

```oa-check
name: JM 2026 overview, resident statutory income 8m
inputs:
  si: 8000000
  threshold: 1876614
steps:
  - tax: max(min(si, 6000000) - threshold, 0) * 0.25 + max(si - 6000000, 0) * 0.30
expected:
  tax: 1630846.50
```

### Example 2: Must a trader with J$14,400,000 or J$16,800,000 of supplies register for GCT?

The threshold is J$15,000,000 over 12 months. J$14,400,000 is J$600,000 under it (no duty to register, voluntary registration possible); J$16,800,000 is J$1,800,000 over it (must register). The monthly averages are J$1,200,000 and J$1,400,000 against J$1,250,000.

```oa-check
name: JM 2026 GCT threshold test both ways
inputs:
  threshold: 15000000
  supplies_a: 14400000
  supplies_b: 16800000
steps:
  - gap_a: threshold - supplies_a
  - excess_b: supplies_b - threshold
  - monthly_a: supplies_a / 12
  - monthly_b: supplies_b / 12
expected:
  gap_a: 600000
  excess_b: 1800000
  monthly_a: 1200000
  monthly_b: 1400000
```

## Ask the client first

1. Individual, self-employed, employer or company?
2. Resident in Jamaica for the year?
3. Turnover in the last 12 months (GCT)?
4. Any employees?
5. Any income or customers outside Jamaica?

## Sources

| Source | URL | Read on |
|---|---|---|
| TAJ, individual income tax rates, threshold and exemptions 2013 to 2028: read for the 2026 threshold, rates and break | https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 | 2026-11-14 |
| TAJ, non-residents and income tax: read for the non-resident rate and treaty table | https://www.jamaicatax.gov.jm/documents/10194/20399532/1-Non-residents+and+Income+Tax+Final+Document.pdf/d8ccd3fa-4a99-e798-1a4b-841e952d82ba | 2026-11-14 |
| Jamaica Information Service, corporate income tax rate: read for the 25% and 33 1/3% company rates | https://jis.gov.jm/new-threshold-and-corporate-income-tax-rate-january-1/ | 2026-11-14 |
| TAJ, General Consumption Tax guide: read for the 15% and 25% rates and the J$15,000,000 threshold | https://www.jamaicatax.gov.jm/general-consumption-tax1 | 2026-11-14 |
| TAJ, self-employed guide (updated November 2026): read for the 15 March deadline and quarterly estimates | https://www.jamaicatax.gov.jm/documents/10194/20399532/4-Income+Tax+and+Self+Employed+Individuals++%28+Updated+Nov.+2026+%29.pdf/c4f3878c-7a44-0a3b-d4a2-4a8cbef3f9ef | 2026-11-14 |
| TAJ, payroll taxes and statutory contributions (April 2025 edition): read for the contribution rates | https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 | 2026-11-14 |

Not yet confirmed: the absence of a capital gains tax on individuals; transfer tax and stamp duty rates on property and shares (the earlier income tax skill cited 1.5% and 15% without a source); the late-filing penalty and interest for income tax returns.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jm-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jm-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
