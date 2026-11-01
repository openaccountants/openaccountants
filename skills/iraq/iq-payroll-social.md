---
name: iq-payroll-social
version: 0.2
description: "Payroll in federal Iraq, tax year 2026: employer income tax withholding with monthly bands, worked cases from GCT, and social security marked unverified. Written for tax year 2026 from the Iraqi law and General Commission for Taxes pages. Use for questions about federal Iraq; the Kurdistan Region runs its own administration. Trigger phrases: Iraq tax, Iraqi dinar tax, General Commission for Taxes, GCT Baghdad."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Payroll & Social Contributions

Tax year: 2026.

## Who this applies to

Employers in federal Iraq withholding income tax on staff pay, and social security for private-sector workers. Kurdistan Region out of scope.

## Rates, bands and thresholds

Income tax bands and allowances: see [income tax](iq-income-tax.md). Monthly bands below come from GCT.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Monthly band to IQD 20,833 | 3% | 2026 | https://tax.mof.gov.iq/uploads/Najwan/thwabit/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%82%D8%B7%D8%A7%D8%B9%20%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B4%D8%B1.pdf |
| IQD 20,834 to 41,666 | 5% | 2026 | same |
| IQD 41,667 to 83,333 | 10% | 2026 | same |
| Over IQD 83,334 | 15% | 2026 | same |
| Pension deduction, permanent state staff | 10% of nominal salary | 2026 | same |
| unverified: employer social security | 12% (25% for oil-class employers) | 2026 | unverified |
| unverified: employee social security | 5% | 2026 | unverified |

## The base

The employer withholds on cash and in-kind pay and pensions (art. 17(1)). Contract staff: salary less allowances, then the scale. Permanent state staff: also deduct the 10%. Over- or under-withholding can be settled before the financial year ends.

## Deadlines and filing

Withhold from the start of the assessment year in the manner the Minister sets (art. 17(1)). Report staff names, addresses and pay when the authority asks (art. 18). The employer must hand over the tax even if it failed to deduct it (art. 17(3)). GCT publishes a withholding return (tasrih) and four tables by marital status.

## Penalties and interest

If tax is not delivered within 21 days of the dates the Minister sets, the art. 45 additions apply (art. 17(4)): 5%, doubled after 21 more days.

## Cross-border points

A non-Iraqi resident gets allowances pro rata by full months in Iraq (art. 12(2)).

## Two worked examples that recompute

GCT's contract case: IQD 700,000 a month, housewife, no children.

```oa-check
name: Contract staff
inputs:
  pay: 700000
steps:
  - taxable: pay - 375000
  - tax: round((taxable - 83333) * 0.15 + 5833)
expected:
  tax: 42083
```

Permanent state employee, same case with 10% pension deduction of a IQD 700,000 nominal salary.

```oa-check
name: Permanent state staff
inputs:
  pay: 700000
steps:
  - taxable: pay - pay * 0.10 - 375000
  - tax: round((taxable - 83333) * 0.15 + 5833)
expected:
  tax: 31583
```

## Ask the client first

- Private, state or contract employee?
- Marital status, children, age?
- Nominal salary and allowances?
- Federal Iraq or Kurdistan Region?

## Sources

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law 113 of 1982, GCT consolidated text: arts. 11, 12, 13, 15, 17, 19, 27, 45, 46, penalties | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |
| GCT circular on direct withholding, 2019, with worked notes (scan, read in full) | https://tax.mof.gov.iq/uploads/Najwan/thwabit/%D8%B6%D9%88%D8%A7%D8%A8%D8%B7%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%82%D8%B7%D8%A7%D8%B9%20%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B4%D8%B1.pdf | 2026-11-01 |

Not yet confirmed: All social security figures, base, ceiling and registration: Law 39 of 1971 cited in the old skill appears replaced by Law 18 of 2023, but neither text could be opened (molsa.gov.iq refused). Employer remittance within 15 days: not found in what was read. GCT tables are for 2019 and were not restated later.

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
