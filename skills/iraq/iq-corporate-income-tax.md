---
name: iq-corporate-income-tax
version: 0.2
description: "Corporate income tax for companies in federal Iraq, tax year 2026: 15% standard, 35% oil, loss rules, withholding on payments abroad, the return filed by 31 May, line by line. Written for tax year 2026 from the Iraqi law and General Commission for Taxes pages. Use for questions about federal Iraq; the Kurdistan Region runs its own administration. Trigger phrases: Iraq tax, Iraqi dinar tax, General Commission for Taxes, GCT Baghdad."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Corporate Income Tax

Tax year: 2026.

## Who this applies to

Joint stock and limited companies, Iraqi or foreign, doing business with an office or place of control in Iraq. Foreign companies registered in Iraq or with a permanent establishment pay only on income arising in Iraq (art. 13(3); GCT return guide). A permanent establishment is a fixed site such as an office, branch, factory, construction site, store, mine or oil well. Kurdistan Region out of scope.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15% flat | 2026 | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf |
| Activities under Law 19 of 2010 (foreign oil contractors) | 35% | 2026 | https://tax.mof.gov.iq/uploads/Najwan/%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D9%84%D8%A6%20%D8%AA%D8%B5%D8%B1%D9%8A%D8%AD%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B4%D8%B1%D9%83%D8%A7%D8%AA.pdf |
| Foreign contractors, remuneration fee under licensing rounds | 35% of total remuneration fee | 2026 | https://tax.mof.gov.iq/uploads/Najwan/ta3ameem/%D8%B4%D8%B1%D9%83%D8%A9%20%D8%A7%D9%84%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9.pdf |
| Interest and annuities paid abroad, non-banks | 15% | 2026 | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf |
| Dividends paid from taxed profits | outside art. 19 | 2026 | same |
| Withholding on contractors, ceiling the authority can require | up to 10% | 2026 | same |

## The base

Start from accounting profit, adjust using return lines 11 to 24, and reach taxable income on line 25. Manager pay in a limited company has a statutory ceiling (line 22). Depreciation follows Regulation 9 of 1994.

Losses carry forward five consecutive years, up to half of each year's taxable income, against the same source only (art. 11). Tax falls on company income before distribution (art. 14), and dividends are relieved under art. 15. Accounts are accepted, subject to later audit under Cabinet Decision 23527 of 2023 (2026 guidelines).

## Deadlines and filing

1. Prepare Arabic accounts; pay in dinars (GCT return guide).
2. File the return (tasrih) with the accounts at the GCT Companies Department or a branch by 31 May of the year after the tax period.
3. Lines 25 to 27 reach taxable income; line 29 applies the rate; line 30 foreign tax credit, with official proof; line 31 withheld tax; line 33 tax due or refund.
4. GCT examines the return. Pay within 21 days of notice (art. 45).
5. Keep records for the bookkeeping regulation period.

## Penalties and interest

Late return 10% of tax, capped at IQD 500,000. Late payment 5%, doubled after 21 more days (art. 45). Bookkeeping breach 10% to 25% of assessed income.

## Cross-border points

Foreign tax credit is limited to Iraqi tax on that income. Non-bank interest paid abroad suffers 15%; banks are exempt (art. 19). Contracts between Iraqi and foreign parties follow Instructions 2 of 2008, with rates set yearly by GCT. Treaties in force per GCT: Yemen, Sudan, Tunisia, Hungary, UAE.

## Two worked examples that recompute

Loss cap: income IQD 100m, loss brought forward IQD 80m. Only 50m is usable; tax IQD 7.5m.

```oa-check
name: Loss cap
inputs:
  income: 100000000
  loss: 80000000
steps:
  - used: min(loss, income * 0.5)
  - tax: (income - used) * 0.15
expected:
  tax: 7500000
```

Decision: sole trader or LLC at profit IQD 100m, single owner. Individual pays 14,545,000; company pays 15,000,000. The individual route is IQD 455,000 cheaper at this level, before non-tax factors.

```oa-check
name: Individual against LLC
inputs:
  profit: 100000000
steps:
  - personal: 70000 + (profit - 2500000 - 1000000) * 0.15
  - company: profit * 0.15
  - gap: company - personal
expected:
  gap: 455000
```

## Ask the client first

- Iraqi or foreign company, with a branch or permanent establishment?
- Oil sector contract under Law 19 of 2010 or a licensing round?
- Federal Iraq or Kurdistan Region?
- Year end, and is it GCT-approved?
- Losses brought forward, by source?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 113 of 1982, GCT consolidated text: arts. 11, 12, 13, 15, 17, 19, 27, 45, 46, penalties | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |
| GCT guide to the company income tax return (scan, read in full by OCR) | https://tax.mof.gov.iq/uploads/Najwan/%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D9%84%D8%A6%20%D8%AA%D8%B5%D8%B1%D9%8A%D8%AD%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B4%D8%B1%D9%83%D8%A7%D8%AA.pdf | 2026-11-01 |
| GCT letter 16 May 2018, foreign contractors, remuneration fee (scan, page 1 read) | https://tax.mof.gov.iq/uploads/Najwan/ta3ameem/%D8%B4%D8%B1%D9%83%D8%A9%20%D8%A7%D9%84%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9.pdf | 2026-11-01 |
| GCT 2026 assessment-year business profit guidelines (general principles and headings read) | https://tax.mof.gov.iq/wp-content/uploads/2026/05/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7-%D8%A7%D9%84%D8%B3%D9%86%D9%88%D9%8A%D9%87-%D9%84%D8%A7%D8%B1%D8%A8%D8%A7%D8%AD-%D8%A7%D9%84%D8%A7%D8%B9%D9%85%D8%A7%D9%84-%D8%A7%D9%84%D8%AA%D8%AC%D8%A7%D8%B1%D9%8A%D9%87-%D9%84%D9%84%D8%B3%D9%86%D9%87-%D9%A2%D9%A0%D9%A2%D9%A6-%D8%A7%D9%84%D8%AA%D9%82%D8%AF%D9%8A%D8%B1%D9%8A%D9%87.pdf | 2026-11-01 |

Not yet confirmed: Resident-to-resident interest withholding 1.8% to 10%; KRI royalty 15% on a 75% base; non-upstream 3.3% or 7%; payment within 3 days of assessment; no advance payments; five-year limitation; mandatory inspection wording; current yearly contract withholding percentages: no official page opened.

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
