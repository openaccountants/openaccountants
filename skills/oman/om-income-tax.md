---
name: om-income-tax
description: "Personal income tax for Oman: none in tax year 2026, and the rules of the 5% tax that starts on 1 January 2028 under Royal Decree 56/2025, read from the law text and the Tax Authority FAQs."
version: 1.1
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Personal Income Tax

## Who this applies to

For tax year 2026 no personal income tax applies in Oman. The Personal Income Tax Law (RD 56/2025, published 30 June 2025) takes effect on 1 January 2028 (decree art. 4). From then it covers natural persons, resident and non-resident. A tax resident is a person in Oman for more than 183 days, continuous or not, in the calendar tax year (art. 1). Residents are taxed on income in or outside Oman; non-residents on income arising in Oman (art. 6).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Tax in 2026 | None; the law starts 1 January 2028 | 2026 | https://qanoon.om/p/2025/rd2025056/ |
| Rate | 5% of taxable income (art. 8) | 2028 on | same |
| Threshold | Net income is what exceeds OMR 42,000 of gross income (art. 1) | 2028 on | same |
| Flat costs, self-employment and rental | 15% of that income, or actual costs (arts 11, 13); the choice holds for 3 years (art. 29) | 2028 on | same |
| Withholding by payers on other income | 20% of the tax due where the income exceeds OMR 20,000; full tax for a non-resident (art. 44) | 2028 on | same |
| Zakat and donations relief | Capped at 5% of gross income (art. 25) | 2028 on | same |
| Late payment | 1% a month (art. 45) | 2028 on | same |

## The base

Gross income has eleven sources (art. 7): salaries and wages; self-employment not entered in the commercial register (art. 10); rental; royalties; interest; dividends and gains on shares and sukuk; gains on real estate; pensions and end-of-service pay; prizes; grants and gifts; membership fees.

Exempt or deductible (art. 25): diplomats' salaries, on reciprocity; the living allowance for Omani staff at missions; a new resident's foreign income for 18 months, once; an Omani resident's pay for work abroad; contributions to up to two pension schemes; education and healthcare costs for the family; gains on the main home after 2 years from notifying the Tax Authority; a second home once in a lifetime; zakat and donations to named bodies; income on Omani government sukuk, bills and bonds; compensation other than for pay; inheritance, wills and gifts between spouses or first-degree relatives; interest on a loan for the main home, once in a lifetime; income from registered industrial property for 5 years.

Losses on self-employment, rental, real estate and securities carry forward within the same source to the fifth following year (arts 26, 27). Foreign tax is creditable up to the tax due, with no carry forward (art. 32). The Tax Authority says the foreign tax must relate to income taxable in Oman (https://tms.taxoman.gov.om/portal/web/taxportal/personal-income-tax-faqs, question 7).

Worked points from the Tax Authority: pensions and Shura and State Council fees count; residential rent is taxable although exempt from VAT; royalty costs are not deductible; improvement costs count only on disposal (https://tms.taxoman.gov.om/portal/web/taxportal/personal-income-tax-faqs, questions 2, 3, 17, 18, 19).

## Deadlines and filing

| Step | Rule | Official URL |
|---|---|---|
| Who files | A person whose gross income exceeds OMR 42,000 (art. 33) | https://qanoon.om/p/2025/rd2025056/ |
| When | Electronically, within 6 months of the year end; the first return covers 2028 | same |
| Salary only, one employer | The employer files on the person's request (art. 33) | same |
| Payment | By the return date (art. 42); employers remit periodically (art. 43) | same |
| Correction | Within 30 days of finding the error, inside 3 years, unless an audit has started (art. 35) | same |
| Leaving Oman | Return at least 60 days before residence ends (art. 37) | same |
| Death | Executor files within 180 days (art. 36) | same |
| Records | 5 years from filing (art. 51) | same |
| Objection | 45 days from notice; the Tax Authority decides in 90 days (art. 59) | same |

The form, portal screens and box numbers do not exist yet in any source we opened, so no filing how-to is given here.

## Penalties and interest

Late payment 1% a month, which the Chairman may waive (art. 45). The Tax Authority may assess within 3 years of filing, or 5 years for fraud (art. 41). Collection lapses after 7 years from the last assessment (art. 50). The fine articles after art. 61 are on the Not yet confirmed line.

## Cross-border points

International agreements prevail (art. 2). RD 56/2025 art. 3 repeals item 1 of art. 18 bis of the Income Tax Law from 2028. The Tax Authority says a non-resident consultant paid by a government body then bears 5%, not 10% (https://tms.taxoman.gov.om/portal/web/taxportal/personal-income-tax-faqs, question 20). Residents and non-residents can get a tax residence certificate on request (art. 3).

## Two worked examples that recompute

**1. Salary OMR 60,000 in 2028, no exemptions.** OMR 18,000 exceeds the threshold, so tax is OMR 900.

```oa-check
name: Salary 60000 in 2028
inputs:
  gross: 60000
steps:
  - net: gross - 42000
  - tax: net * 0.05
expected:
  net: 18000
  tax: 900
```

**2. Decision: flat 15% or actual costs, freelancer earning OMR 80,000 with OMR 20,000 of real costs.** Actual costs win: OMR 900 against OMR 1,300. This follows arts 1 and 28, which take costs from net income; the regulation has not confirmed the order.

```oa-check
name: Freelancer flat costs against actual costs
inputs:
  gross: 80000
  actual: 20000
steps:
  - net: gross - 42000
  - flat_costs: gross * 0.15
  - tax_flat: (net - flat_costs) * 0.05
  - tax_actual: (net - actual) * 0.05
expected:
  tax_flat: 1300
  tax_actual: 900
```

## Ask the client first

- Which tax year is the question about? Before 2028 the answer is nil.
- Days in Oman in the year?
- Omani or not, and is any pay earned abroad?
- Which of the eleven income sources, and how much of each?
- Is any activity in the commercial register? If so, the Income Tax Law applies instead (art. 10).
- Which exemptions apply (pension, education, health, home loan)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Law, RD 56/2025, Arabic gazette text (issue 1602) on Qanoon.om, a private publisher (arts 1 to 61 read). The Tax Authority page for the law text was not found | https://qanoon.om/p/2025/rd2025056/ | 2026-11-01 |
| Tax Authority, PIT FAQs (all 20 read) | https://tms.taxoman.gov.om/portal/web/taxportal/personal-income-tax-faqs | 2026-11-01 |

Not yet confirmed: the Executive Regulations of RD 56/2025, due within a year of publication (decree art. 2), which we did not find on the Tax Authority site or in the portal page list, so costs order, return form, employer remittance dates and exemption controls are open; the penalty articles after art. 61; capital gains for individuals before 2028 (no tax on the same reasoning, no separate source opened); whether non-resident individuals have any Oman tax on pay in 2026 other than art. 18 bis withholding on services.

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
