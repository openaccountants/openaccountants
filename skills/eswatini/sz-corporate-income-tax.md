---
name: sz-corporate-income-tax
description: "Eswatini Corporate Income Tax for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about corporate income tax in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
jurisdiction: SZ
category: international
tax_year: 2026
tax_year_notes: "Year of assessment to 30 June 2026"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eswatini Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies with income from a source within or deemed within Eswatini, branches of non-resident companies, and payers of withholding tax. Tax year: the year of assessment 1 July 2025 to 30 June 2026. The latest amending law found is the Income Tax (Amendment) Act 2023. ERS says those amendments took effect on 1 July 2024. No 2026 amending law was found on the ERS site, and that absence is not proof that none exists.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Company rate | 25%. The ERS rates page still says 27.5%; the Third Schedule and the 2025 ERS notice say 25% | 2026 | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf |
| Presumptive tax, company turnover to E50,000 | 0%. Excludes professionals and investment income | 2026 | https://www.ers.org.sz/IncomeTax/PresumptiveTax |
| Presumptive tax, turnover above E50,000 and below E500,000 | 1.75% of total turnover | 2026 | https://www.ers.org.sz/IncomeTax/PresumptiveTax |
| Interest deduction cap | Net interest above 30% of tax EBITDA denied, for group companies other than banks and insurers. Carry forward 3 years (s 65sep) | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Non-resident shareholders tax | 15%; 12.5% for a company registered in Botswana, Lesotho, Namibia or South Africa that is not a subsidiary or branch of a company from elsewhere (s 21) | 2026 | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf |
| South Africa treaty dividends | 10% for a company holding at least 25%; otherwise 15% (art. 10) | 2026 | https://www.ers.org.sz/documents/SouthAfrica.pdf |
| Non-resident interest | 10% . The ERS rates page shows 15% for outside SACU; ERS Withholding page and the Order say 10% | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Royalties and management fees to non-residents | 15% of gross, final | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Non-resident contractors, construction | 15%, excluding direct cost of materials | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Non-resident service payments | 15% of gross on Eswatini-source service contracts | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Entertainers and sportspersons | 15% of gross | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Branch profits tax | 15%; 12.5% for a qualifying neighbouring-country company (s 32E) | 2026 | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf |
| Resident interest and dividends paid | 10% | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Rent paid to a non-company lessor by a non-natural person | 10% | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |
| Trust distributions to vested beneficiaries | 33% | 2026 | https://www.ers.org.sz/IncomeTax/Withholding |

## The base

Source basis, regardless of residence. The 2023 Act added Division X (gains on business assets; the cost base is value at commencement for older assets), a permanent establishment definition and arm's length rules (ss 65quat onward). Controlled transactions use an approved transfer pricing method and need documents under s 35bis. The domestic exemption threshold is set by Gazette notice.

## Deadlines and filing

For the year ended 30 June 2025 all non-individual entities filed and paid by 31 October 2025. Approved other year-ends: within 4 months after year-end. Draft financial statements were accepted, with signed audited ones to follow. Withholding is due by the 15th of the following month.

Provisional tax: first payment within 6 months of the start of the year, second by year-end, third by the return date. Presumptive taxpayers: 25%, 50%, 75% and 100% cumulative by 30 September, 31 December, 31 March and 30 June.

### How to file
1. Appoint a Public Officer: board resolution, signed acceptance, certified ID, and work permit for a non-citizen.
2. Log in to TaxEase at https://taxease.ers.org.sz/ and complete the return. Attach the financial statements.
3. Dormant registered companies also file, and tell the Commissioner General in writing why they are not operating.
4. Pay by EFT, speed point, MoMo Pay or bank deposit, quoting the reference. Cash is not accepted.

## Penalties and interest

Late return: 20% of tax payable, or E20 a day on a loss. Late payment: 18% a year. Failure to withhold: payer is liable plus 20%. Withheld but not remitted: 10% under 30 days late, 15% from 30 days, 20% from 90 days, 25% from 180 days. Under-estimating provisional tax below 90% of actual: 20% of the shortfall as defined. Records: 5 years.

## Cross-border points

A foreign service paid by a business usually triggers 15% withholding and may also trigger [VAT reverse charge](sz-vat-gst.md). A treaty rate needs the treaty text read for that country.

## Two worked examples that recompute

Company profit E800,000 at 25%.

```oa-check
name: Company tax on E800,000
inputs:
  profit: 800000
steps:
  - tax: profit * 0.25
expected:
  tax: 200000
```

Decision: a retail company with turnover E400,000 and profit E40,000 pays E7,000 presumptive against E10,000 normal. If profit were under E28,000, normal tax would be lower, and the company must weigh leaving presumptive tax, which it can do only after two years.

```oa-check
name: Presumptive or normal, company turnover E400,000
inputs:
  turnover: 400000
  profit: 40000
steps:
  - presumptive: turnover * 0.0175
  - normal: profit * 0.25
  - breakeven: presumptive / 0.25
expected:
  presumptive: 7000
  normal: 10000
  breakeven: 28000
```

## Ask the client first

1. What is the year-end, and is it approved?
2. What is turnover, and is the business professional or does it have investment income?
3. Is it in a group, with related-party transactions or interest?
4. Who are the non-resident payees, and where are they resident?
5. Is it a branch of a foreign company?

## Sources

| Source | URL | Read on |
|---|---|---|
| ERS, Public Notice, returns for tax year end 2025 (scanned, OCR); cited sections read | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf | 2026-11-01 |
| Income Tax (Amendment) Act 2023 (Act 20 of 2023); scanned, read by OCR, Third Schedule pages checked by eye; cited sections read | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | 2026-11-01 |
| ERS, Rates and Thresholds; whole page read | https://www.ers.org.sz/IncomeTax/RatesandThres | 2026-11-01 |
| ERS, Withholding Taxes; whole page read | https://www.ers.org.sz/IncomeTax/Withholding | 2026-11-01 |
| ERS, Presumptive Tax; whole page read | https://www.ers.org.sz/IncomeTax/PresumptiveTax | 2026-11-01 |
| Income Tax Order 1975, ERS consolidated copy to the 2013 amendments; sections cited were read; cited sections read | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf | 2026-11-01 |
| Eswatini and South Africa tax treaty, art. 10; cited sections read | https://www.ers.org.sz/documents/SouthAfrica.pdf | 2026-11-01 |
| ERS, Self Assessment; whole page read | https://www.ers.org.sz/IncomeTax/SelfAssessment | 2026-11-01 |
| ERS, Step-by-Step Guide for New Businesses; whole page read | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf | 2026-11-01 |
| ERS, Income Tax Returns; whole page read | https://www.ers.org.sz/IncomeTax/IncomeTaxReturn | 2026-11-01 |

Not yet confirmed: The commencement notice for the 2023 Act was not opened; 1 July 2024 rests on the ERS Presumptive Tax page. The ERS notice for returns for the year ended 30 June 2026 was not found, so 2025 dates are given as the latest published. Development Approval Order rate of 10% from the old pack: not found in an official source. The old pack's 5% royalty refund under a treaty and the four-year audit practice: no official source found. The old 120-day rule appears in the ERS guide, but the 2025 notice gives 4 months and 31 October. The transfer pricing threshold, regulations and the intangibles cap percentage were not found.

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
