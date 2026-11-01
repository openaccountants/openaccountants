---
name: na-corporate-income-tax
description: >
  Namibia corporate income tax, 2026: 30% rate, mining rates, assessed loss limit, provisional tax, the 7-month return, withholding and penalties. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: NA
category: international
tax_year: 2026
tax_year_notes: "Individuals: year of assessment 1 March 2026 to 28 February 2027. Companies: financial year."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia Corporate Income Tax v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

The annotated Income Tax Act read runs to Income Tax Amendment Act 4 of 2024. The 2025 and 2026 gazette indexes list no Income Tax or VAT amendment act.

## Who this applies to

Companies and close corporations with Namibian-source or deemed-source income ([NamRA](https://www.namra.org.na/business-tax/page/companies-amp-close-corporations/)). A company in Namibia appoints a public officer. NamRA's pages still say 32%; that rate is out of date, and Schedule 4 para 3 governs.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Non-mining company, years from 1 January 2025 | 30% | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (Schedule 4 para 3(1)(a)) |
| Prior: years from 1 January 2024 | 31% | 2024 | same |
| Mining other than diamonds | 37.5% | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (para 3(1)(b)) |
| Diamond mining | 50% plus 10% surcharge on the tax: 55% in effect | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (para 3(1)(c)) |
| Petroleum operations | 35% | 2018/19 table | https://www.namra.org.na/tax-types/page/income-tax/ |
| Long-term insurers | 40% of gross investment income taxed at the company rate; page shows 12.8% at the old 32% | 2018/19 table | https://www.namra.org.na/tax-types/page/income-tax/ |
| Assessed loss set-off | Limit: greater of N$1 million or 80% of taxable income before set-off | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.21(1)) |
| Non-resident shareholders tax, company holding 25%+ | 10% | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.45) |
| Non-resident shareholders tax, other | 20% | 2026 | same |
| Interest, royalties, management and consultancy fees to non-residents | 10%: see cross-border skill | 2026 | https://www.namra.org.na/tax-types/page/withholding-tax-30120/ |

## The base

Income less expenditure incurred to produce it, not capital (s.17). Capital items such as vehicles and machinery: one third a year for three years. Buildings: 20% in the first year, 4% for each of the next 20 years ([NamRA](https://www.namra.org.na/business-tax/page/companies-amp-close-corporations/)). Not deductible: private expenses, costs not producing income, land tax, recoverable insured losses (s.24). Youth internship allowance: s.17E formula (A/B) x C - C, A = 50% of C, B = the corporate rate, C = actual cost or N$50,000 if less, for a registered internship, 36 months at most. Export and manufacturer incentives: ss.17A, 17B, 17D ran only to the end of the 2025 tax year and s.17C was repealed from 31 December 2025. Net interest cap: [transfer pricing skill](na-transfer-pricing.md).

## Deadlines and filing

Return and tax: last day of the 7th month after year end (s.56(1A)(b)). Provisional: within 6 months of the start of the year, half of estimated tax; by the last day of the year, the full estimate less the first payment (Sch 2 para 24), with an estimate each time (para 19). The old 40% and 80% tests: the Act's test is an estimate below 80% of final income, for each period (para 20). NamRA's page still words it as 40% and 80% of tax.

Steps: ITAS registration ([NamRA brochure](https://www.namra.org.na/documents/cms/uploaded/information-brochure--how-to-register-on-itas-ce02d8af03.pdf)): 1. Go to https://itas.namra.org.na and choose to register. 2. Create a username and password and give a valid email. 3. Activate through the emailed link. 4. Log in and link your taxpayer account. 5. Complete the mandatory fields and submit. Payment ([NamRA](https://www.namra.org.na/documents/cms/uploaded/information-brochure--tax-payments-325a997127.pdf)): EFT, direct deposit, cash or point of sale. The reference is payment type, registration office, taxpayer number, tax type and tax period. Tax type 11 is income tax; its period is the year plus a 2-digit value, "00" for final income tax. Box numbers for the company return are not on pages opened.

## Penalties and interest

Late payment: interest 20% a year from the day after the due date (s.79(2), https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf). Failure to render a return: additional tax up to twice the tax chargeable, less amounts paid (s.66(1)(a)). Omission or incorrect statement: twice the shortfall (s.66(1)(b), (c)). The Minister may remit (s.66(2)), but not where there was intent to evade unless circumstances were extenuating. Late provisional tax: penalty 10% per month or part, capped at the unpaid tax (Sch 2 para 28) plus interest 20% (s.80(2), interest capped at the original tax by s.80(5)). Missing provisional estimate: N$100 per day (Sch 2 para 21). Under-estimate below 80% of final taxable income: additional tax up to 100% of the shortfall (Sch 2 para 20). The tax amnesty extension ran to 31 October 2026 (https://www.namra.org.na/tax-amnesty); it is over unless NamRA extends it again.

## Cross-border points

See the [cross-border skill](na-cross-border.md) and [transfer pricing skill](na-transfer-pricing.md).

## Two worked examples that recompute

Example 1. Taxable income N$1,000,000 at 30% gives N$300,000.

```oa-check
name: Company 30%
inputs:
  ti: 1000000
steps:
  - tax: ti * 0.30
expected:
  tax: 300000.00
```

Example 2. A decision: how much loss to use. Income before set-off N$5,000,000, balance of loss N$6,000,000. Limit is the greater of N$1m and N$4m, so N$4m is set off. Taxable N$1,000,000, tax N$300,000; N$2,000,000 of loss carries on.

```oa-check
name: Loss limit
inputs:
  i: 5000000
  loss: 6000000
steps:
  - lim: max(1000000, i * 0.8)
  - used: min(loss, lim)
  - tax: (i - used) * 0.30
  - left: loss - used
expected:
  tax: 300000.00
  left: 2000000.00
```

## Ask the client first

1. Year end?
2. Mining, petroleum, insurance or other trade?
3. Loss balance brought forward?
4. Payments to non-residents or connected parties?
5. Was it a registered manufacturer or EPZ enterprise?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 24 of 1981, annotated to Act 4 of 2024 (read: Schedule 4 para 3, ss.17, 17E, 21, 45, 56, 66, 79, 80, Schedule 2 paras 19, 20, 24, 28) | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf | 2026-11-01 |
| NamRA companies page (read: whole page, 32% is stale) | https://www.namra.org.na/business-tax/page/companies-amp-close-corporations/ | 2026-11-01 |
| NamRA income tax page (read: company table 2018/19) | https://www.namra.org.na/tax-types/page/income-tax/ | 2026-11-01 |
| NamRA withholding page (read: whole page) | https://www.namra.org.na/tax-types/page/withholding-tax-30120/ | 2026-11-01 |
| NamRA ITAS brochure (read: whole) | https://www.namra.org.na/documents/cms/uploaded/information-brochure--how-to-register-on-itas-ce02d8af03.pdf | 2026-11-01 |
| NamRA tax payments brochure (read: whole) | https://www.namra.org.na/documents/cms/uploaded/information-brochure--tax-payments-325a997127.pdf | 2026-11-01 |

Not yet confirmed: Whether the 18% registered manufacturer rate in para 3(2) still applies, since Act 5 of 2021 deleted the continued application of s.5A while para 3(2) remains in the text; current petroleum and long-term insurer rates (only the 2018/19 page was read; the Petroleum (Taxation) Act was not opened); Budget 2026/27 proposals; company return boxes.

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
