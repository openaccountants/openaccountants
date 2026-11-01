---
name: lb-income-tax
description: "Personal income tax in Lebanon for tax year 2026: salary tax, business income, family allowances, filing. Sources and unverified rows are marked per row."
version: 1.1
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lebanon Personal Income Tax

## Who this applies to

Employees, sole traders, partners and self-employed professionals with income from activity in Lebanon. Lebanon taxes by schedule, not on a single total.



## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Advance at customs, taxpayers with no income tax or VAT declarations in the previous 3 years | 1.5% of import value, credited against tax due, penalties still apply | 2026 | https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf |
| Payroll tax bracket rescaling context | Employment income is taxed under a dedicated payroll tax with progressive brackets, withheld at source by the employer. Brackets have been repeatedly re-scaled to track currency depreciation; the figures below reflect the 2024-2025 budget-law updates and should be confirmed against the latest circular. | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened |
| Progressive payroll tax rate range | 2% to 25% | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959 |
| Annual payroll bracket range (2025) | LL 360 million up to LL 13.5 billion (approx : confirm against 2025 MoF circular) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; 2024 Budget Law |
| Family exemption : single individual | LL 450,000,000 per year | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; 2024 Budget Law |
| Additional exemption : married with unemployed spouse | LL 225,000,000 added to the single exemption | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; 2024 Budget Law |
| Additional exemption : per legitimate child | LL 45,000,000 per child (Subject to maximum number of children per the law) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; 2024 Budget Law |
| Rate reduction for pensions | Payroll rates halved for retirement pensions and similar benefits | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959 |
| Business/professional income tax basis | Income of sole proprietorships, general partnerships and self-employed professionals is taxed on a separate progressive schedule under Chapter 1. | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened |
| Progressive business income tax rate range | 4% to 25% | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959 |
| Annual business-income bracket range | LL 540 million up to LL 13.5 billion (approx : confirm 2025 indexation) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; 2024 Budget Law |
| Residence and territorial taxation context | Salary tax is withheld and remitted by employers; resident individuals are taxed on Lebanon-source employment and business income under the territorial principle. | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened |
| When salary is taxable in Lebanon | If the beneficiary is resident in Lebanon, OR the service is performed in/benefits a Lebanese company, OR the funding source is in Lebanon | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959 |
| Payroll tax collection mechanism | Withheld at source by the employer and remitted to the tax authority | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959 |
| Non-resident tax payment frequency | Quarterly, within 15 days of the end of each quarter | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; 2022 Budget Law |
| Annual employer payroll declaration deadline | By 28 February of the following year (Form R10) (approx : confirm exact form and date with MoF) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959 |

## The base

Salary, business and movable-capital income are taxed separately. Family allowances are deducted before the salary bands. Band tables: unverified, so do not compute band tax from this skill until the Ministry text is opened.

## Deadlines and filing

Employers withhold and remit salary tax. Business income returns use the Ministry's e-services (eservices.finance.gov.lb): IDAL describes the steps as open E-services, supply the required information and documents, receive an E-pin by email, then file the form online ([IDAL](https://www.investinlebanon.gov.lb/en/doing_business/tax_system)). Form R10 and 28 February: unverified.

## Penalties and interest

Late declarations and incorrect information carry financial penalties, multiplied on repeat violations (Budget 2026 art. 18, [Citizen Budget](https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf)). Amounts: unverified. An exceptional 85% reduction of penalties owed to public entities applied if paid within three months of the law's publication, with a reduced penalty of at least LBP 200,000 or USD 5; that window has passed unless extended (art. 43).

## Cross-border points

Non-resident salary tax payment frequency is in the table (unverified). Offshore company staff: see [corporate income tax](lb-corporate-income-tax.md).

## Two worked examples that recompute

### Example 1: family allowance total (unverified allowance amounts)

Married, non-working spouse, two children: 450,000,000 + 225,000,000 + 2 x 45,000,000 = LL 765,000,000.

```oa-check
name: Family allowance, married, two children
inputs:
  single: 450000000
  spouse: 225000000
  child: 45000000
  children: 2
steps:
  - total: single + spouse + child * children
expected:
  total: 765000000
```

### Example 2: import advance, decision to file overdue declarations first

Goods worth LL 2,000,000,000, no declarations for 3 years. Unfiled: 1.5% advance is LL 30,000,000 at customs. Filed: no advance under art. 27. The advance is credited, so the cost is cash timing, and penalties remain either way.

```oa-check
name: Article 27 advance
inputs:
  value: 2000000000
steps:
  - advance: value * 0.015
expected:
  advance: 30000000
```

## Ask the client first

- Employee, sole trader, partner or professional?
- Marital status, spouse working, number of children.
- Currency of pay and the rate used.
- Resident, and where the work is done.
- Declarations filed for the last 3 years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ministry of Finance Citizen Budget 2026, measures list, all pages (hosted by Institut des Finances, a Ministry body) | https://institutdesfinances.gov.lb/sites/default/files/2026-04/Pamphlet-Citizen%20Budget%202026-Apr26-En-final.pdf | 2026-11-01 |
| IDAL, Doing Business, Tax System (whole page) | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |
| Ministry of Finance, finance.gov.lb tax pages | unverified: CAPTCHA, not read | not read |

Not yet confirmed: every row marked unverified. finance.gov.lb returned a CAPTCHA during this refresh, which we did not solve; only archive indexes of it were read, and the text of 2026 Budget Law No. 40 of 10 Feb 2026 was not opened (the law number comes from a search summary, not an official page). Citizen Budget wording covers measures only, so anything else in that law is unread.

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
