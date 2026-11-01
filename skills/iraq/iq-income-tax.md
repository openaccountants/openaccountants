---
name: iq-income-tax
version: 0.2
description: "Personal income tax for individuals in federal Iraq, tax year 2026: annual bands 3% to 15%, allowances, income report before 1 June, payment and penalties. Written for tax year 2026 from the Iraqi law and General Commission for Taxes pages. Use for questions about federal Iraq; the Kurdistan Region runs its own administration. Trigger phrases: Iraq tax, Iraqi dinar tax, General Commission for Taxes, GCT Baghdad."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Personal Income Tax

Tax year: 2026. Income earned in 2025 is assessed in assessment year 2026 (GCT guide: tax falls on income of the year before the assessment year).

## Who this applies to

Federal Iraq. Iraqi residents are taxed on income arising in or outside Iraq, and non-resident Iraqis are taxed at the same rates on Iraqi-source income (art. 13 as amended by CPA Order 49 of 2004). Non-resident non-Iraqis are in the art. 13(1)(b) scale, which has the same bands. A non-Iraqi resident gets allowances in proportion to full months in Iraq, except government-contracted teachers (art. 12(2)). The Kurdistan Region is out of scope.

## Rates, bands and thresholds

The bands are annual. GCT's 2019 circular confirms this: it gives these bands for an annual calculation and monthly equivalents of IQD 20,833, 41,666 and 83,333. The 2019 circular is the latest official scale we could open, and the 2026 guidelines do not restate it.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Band 1, annual taxable income to IQD 250,000 | 3% | 2026 | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf |
| Band 2, IQD 250,001 to 500,000 | 5% | 2026 | same |
| Band 3, IQD 500,001 to 1,000,000 | 10% | 2026 | same |
| Band 4, over IQD 1,000,000 | 15% | 2026 | same |
| Allowance, taxpayer (single, or wife's income taxed separately) | IQD 2,500,000 | 2026 | https://tax.mof.gov.iq/uploads/Najwan/thwabit/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%82%D8%B7%D8%A7%D8%B9%20%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B4%D8%B1.pdf |
| Allowance, married with housewife or merged income | IQD 4,500,000 in total | 2026 | same |
| Allowance, wife whose husband cannot work, certified by a medical committee | IQD 5,000,000 | 2026 | same |
| Allowance, widow or divorced woman | IQD 3,200,000 | 2026 | same |
| Allowance, over 63 | extra IQD 300,000 | 2026 | same |
| Allowance, each child, no limit on number | IQD 200,000 | 2026 | same |

GCT's guide also shows doubled figures for assessment years 2010, 2011 and 2013 only. They are not current.

A child counts while under 18, or at any age if unable to earn through disability, or while studying at secondary or higher level until the course ends or age 25, whichever is first (art. 12(3)).

## The base

Net income after expenses spent to earn it, backed by acceptable documents (GCT guide). Article 7 lists exemptions. Taxpayers outside the bookkeeping rules are assessed under GCT's annual guidelines; the 2026 guidelines state profits before allowances. A taxpayer with several income sources has only the smallest cut by 50%, and only for absolute-profit sources (2026 guidelines, seventh principle). Losses: see [corporate income tax](iq-corporate-income-tax.md), same art. 11.

Employees: tax is on salary and overtime; GCT's 2019 notes exclude allowances (mukhassasat) in the state-employee calculation, and take 10% of nominal salary off for permanent state staff pensions. A married woman gets the single allowance unless the couple file a merger request with her employer in January.

## Deadlines and filing

1. Tell your GCT branch you have started, with the lease and licence (GCT guide).
2. File the income report (taqrir dariba al-dakhl) at your branch before 1 June of the assessment year, registered or not (art. 27(2)). The authority can extend for a legitimate excuse (art. 27(3)).
3. GCT assesses and notifies you. Pay within 21 days of notice (art. 45). Instalments need a written request (art. 46).
4. Object within 21 days of notice, then appeal to the appeal committee within 21 days of rejection (GCT guide).

## Penalties and interest

- Late report: 10% of the tax, capped at IQD 500,000.
- Late payment: 5% added after 21 days, doubled after a further 21 days (art. 45), plus bank interest noted under that article.
- Concealing income: at least twice the tax (GCT guide).
- Bookkeeping breach: 10% to 25% of assessed income, minimum IQD 500.

## Cross-border points

Foreign-source income of Iraqi residents is in scope. Interest and annuities paid abroad: see [corporate income tax](iq-corporate-income-tax.md). Iraq's treaties in force per GCT: Yemen, Sudan, Tunisia, Hungary, UAE.

## Two worked examples that recompute

Single resident, annual income IQD 12,000,000. Allowance leaves 9,500,000. Tax IQD 1,345,000.

```oa-check
name: Single, IQD 12m
inputs:
  income: 12000000
  allowance: 2500000
steps:
  - taxable: income - allowance
  - b1: 250000 * 0.03
  - b2: 250000 * 0.05
  - b3: 500000 * 0.10
  - b4: (taxable - 1000000) * 0.15
  - tax: b1 + b2 + b3 + b4
expected:
  tax: 1345000
```

GCT's own contract-staff case: IQD 700,000 a month, married, housewife, no children. Monthly tax IQD 42,083.

```oa-check
name: GCT circular case, monthly 700,000
inputs:
  monthly: 700000
  allowance: 4500000
steps:
  - taxable: monthly * 12 - allowance
  - tax: 250000 * 0.03 + 250000 * 0.05 + 500000 * 0.10 + (taxable - 1000000) * 0.15
  - per_month: round(tax / 12)
expected:
  per_month: 42083
```

## Ask the client first

- Iraqi or not, and resident or not?
- Federal Iraq or Kurdistan Region?
- Employee, or business or profession?
- Marital status, spouse's income, children, age?
- Books kept under Regulation 2 of 1985, or assessed by guidelines?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 113 of 1982, GCT consolidated text: arts. 11, 12, 13, 15, 17, 19, 27, 45, 46, penalties | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |
| GCT circular on direct withholding, 2019, with worked notes (scan, read in full) | https://tax.mof.gov.iq/uploads/Najwan/thwabit/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%82%D8%B7%D8%A7%D8%B9%20%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B4%D8%B1.pdf | 2026-11-01 |
| GCT circular, allowances and rate scale, 2017 (scan, page 1 read) | https://tax.mof.gov.iq/uploads/Hiba/%D8%A7%D9%84%D8%B3%D9%85%D8%A7%D8%AD%D8%A7%D8%AA%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%D9%8A%D8%A9%20%D9%88%D9%85%D9%82%D9%8A%D8%A7%D8%B3%20%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9.pdf | 2026-11-01 |
| GCT income tax guide | https://tax.mof.gov.iq/%D8%AF%D9%84%D9%8A%D9%84-%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9-%D8%A7%D9%84%D8%AF%D8%AE%D9%84/ | 2026-11-01 |
| GCT 2026 assessment-year business profit guidelines (general principles and headings read) | https://tax.mof.gov.iq/wp-content/uploads/2026/05/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7-%D8%A7%D9%84%D8%B3%D9%86%D9%88%D9%8A%D9%87-%D9%84%D8%A7%D8%B1%D8%A8%D8%A7%D8%AD-%D8%A7%D9%84%D8%A7%D8%B9%D9%85%D8%A7%D9%84-%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D9%8A%D9%87-%D9%84%D9%84%D8%B3%D9%86%D9%87-%D9%A2%D9%A0%D9%A2%D9%A6-%D8%A7%D9%84%D8%AA%D9%82%D8%AF%D9%8A%D8%B1%D9%8A%D9%87.pdf | 2026-11-01 |

Not yet confirmed: Risk allowance exemption of 30% of basic salary and the rule treating undocumented taxpayers as unmarried: no official page opened. Employer remittance within 15 days: see the payroll skill. Whether a 2026 budget law changed bands or allowances: none found, but no 2026 budget text could be opened. Parts of GCT law text are the consolidated copy; amendments after it were not all read.

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
