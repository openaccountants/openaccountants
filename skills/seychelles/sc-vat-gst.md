---
name: sc-vat-gst
description: "Seychelles Value Added Tax for tax year 2026: the 15% standard rate, zero rating and exemptions, SCR 2,000,000 compulsory and SCR 100,000 voluntary thresholds, the 2025 refusal and cancellation rules, input tax limits, the SCR 50,000 input tax credit form, VAT on imports, returns and refunds. Use for Seychelles VAT rate, register for VAT in Seychelles, voluntary VAT registration, VAT return due date, or VAT on imports. Source-based; no accountant has signed it."
jurisdiction: SC
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Seychelles VAT v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons making taxable supplies in Seychelles in an enterprise, and all importers. A business making only exempt supplies should not register.

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15% | 2026 | https://src.gov.sc/seychelles-tax-system/ |
| Zero rate | 0% on exports and Second Schedule items | 2026 | same |
| Exempt | First Schedule, including pharmaceuticals, infant formula, basic necessities, education, health, financial services | 2026 | same |
| Compulsory registration | Taxable supplies made or expected of SCR 2,000,000 or more | 2026 | https://src.gov.sc/wp-content/uploads/2024/12/SI-97-2024-Value-Added-Tax-Amendment-of-Fourth-Schedule-Regulations-2024.pdf |
| Voluntary registration | Taxable supplies of SCR 100,000 or more, from 1 Jan 2025 | 2026 | same |
| Input tax credit form | Needed when input tax is SCR 50,000 or more per transaction, local purchases only | 2026 | https://src.gov.sc/wp-content/uploads/2025/10/Act-16-2024-Value-Added-Tax-Amendment-Act-2024.pdf |

The pack's old 2025 figures are unchanged. No 2026 amendment to this rate was found on the SRC legislation list read on 1 Nov 2026, so 2026 rests on the instruments below staying in force.

## The base

Output tax less input tax. Excess input is a credit, usually carried forward; exporters and zero-rated suppliers can have it refunded ([brochure](https://src.gov.sc/wp-content/uploads/2022/12/VAT-Credit-Refund-Brochure.pdf)). No input credit for taxable supplies used to make exempt supplies, nor, unless used for making taxable supplies specific to the business, for passenger vehicles and their parts and repairs, petroleum, entertainment, accommodation, or club memberships (VAT Act s 25, [SRC](https://src.gov.sc/seychelles-tax-system/)).

Imports are taxed on CIF value plus customs duties and excise, collected by Customs at the point of entry. Levies are excluded from 1 January 2025 (Act 16 of 2024 s 8).

Registration tests: section 7 looks at the start of any 12 months or the end of any 12 months or less; apply within 14 days of becoming required (quoted in [Public Ruling 2025-2](https://src.gov.sc/wp-content/uploads/2025/04/VAT-Threshold-Public-Ruling.pdf)). Capital asset sales and sale of the business are ignored, and SRC can add an associate's supplies. For voluntary registration SRC visits the premises first and checks trading, a fixed place, records and cash register licensing. It may refuse or defer a person with no bank account, a bad record or fraud concerns (Act 16 of 2024 ss 4, 5). Cancellation periods moved from twelve to twenty-four months in s 12(4), and SRC may refuse to cancel to protect revenue (s 6).

## Deadlines and filing

Compulsory registrants file monthly, voluntary registrants quarterly ([FAQ](https://src.gov.sc/faq/)). A return is due by the 21st in person, or the 23rd through the Tax Portal; payment by the 21st in person, or the 23rd by portal or bank transfer ([Act 27 of 2023](https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf)). Large businesses and payments of SCR 50,000 or more use the portal.

Steps: download the VAT return from the [SRC download page](https://src.gov.sc/download/) or use [tms.src.gov.sc](https://tms.src.gov.sc/); enter output and input tax; attach the [input tax credit form](https://src.gov.sc/wp-content/uploads/2025/01/Vat-Schedule-Guide.pdf) for each qualifying local purchase; lodge; pay to the SRC Collection Account. New registrants use the VAT Registration Form and receive a certificate and sticker to display. Return box numbers were not read.

SRC is building e-invoicing, with no start date published as of [16 September 2026](https://src.gov.sc/src-completes-market-survey-as-part-of-e-invoicing-project/).

## Penalties and interest

Late filing and payment amounts are in [Corporate income tax](sc-corporate-income-tax.md).

## Cross-border points

Exports are zero rated. The old pack's reverse charge on imported services could not be confirmed from the Act: see below.

## Two worked examples that recompute

Import: CIF SCR 2,000 plus SCR 600 duty gives a base of SCR 2,600 and VAT of SCR 390 (SRC's FAQ example).

```oa-check
name: Import VAT
inputs:
  cif: 2000
  duty: 600
steps:
  - vat: (cif + duty) * 0.15
expected:
  vat: 390
```

Decision: register voluntarily at SCR 500,000 of net sales with SCR 200,000 of net purchases? Registered, it charges SCR 75,000, recovers SCR 30,000 and remits SCR 45,000. Unregistered, the SCR 30,000 is a cost. It pays off when customers can recover the VAT.

```oa-check
name: Voluntary registration at SCR 500,000
inputs:
  sales: 500000
  purchases: 200000
steps:
  - output: sales * 0.15
  - input: purchases * 0.15
  - remit: output - input
expected:
  remit: 45000
```

## Ask the client first

- Taxable supplies in the last 12 months and expected next 12?
- Any exempt supplies, so input tax may be blocked?
- Compulsory or voluntary registration?
- Imports or exports?
- Bank account and compliance record?

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the figures cited: SRC Tax System page, whole page read | https://src.gov.sc/seychelles-tax-system/ | 2026-11-01 |
| Read for the figures cited: S.I. 97 of 2024, Fourth Schedule | https://src.gov.sc/wp-content/uploads/2024/12/SI-97-2024-Value-Added-Tax-Amendment-of-Fourth-Schedule-Regulations-2024.pdf | 2026-11-01 |
| Read for the figures cited: VAT (Amendment) Act 2024 (Act 16 of 2024), whole Act | https://src.gov.sc/wp-content/uploads/2025/10/Act-16-2024-Value-Added-Tax-Amendment-Act-2024.pdf | 2026-11-01 |
| Read for the figures cited: Revenue Law (Amendment) Act 2023 (Act 27 of 2023), ss 3, 4, 7 | https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf | 2026-11-01 |
| Read for the figures cited: SRC FAQ, domestic section | https://src.gov.sc/faq/ | 2026-11-01 |
| Read for the figures cited: SRC Public Ruling 2025-2, read by OCR | https://src.gov.sc/wp-content/uploads/2025/04/VAT-Threshold-Public-Ruling.pdf | 2026-11-01 |
| Read for the figures cited: SRC VAT Input Tax Credit Form guide | https://src.gov.sc/wp-content/uploads/2025/01/Vat-Schedule-Guide.pdf | 2026-11-01 |
| Read for the figures cited: SRC VAT refund brochure | https://src.gov.sc/wp-content/uploads/2022/12/VAT-Credit-Refund-Brochure.pdf | 2026-11-01 |
| Read for the figures cited: SRC e-invoicing notice, 16 Sep 2026 | https://src.gov.sc/src-completes-market-survey-as-part-of-e-invoicing-project/ | 2026-11-01 |

Not yet confirmed: reverse charge on imported services, from the old pack; the VAT Act 2010 PDF on the SRC site is an image that OCR could not read, so its sections are cited only through SRC pages, the 2024 Amendment Act and Public Ruling 2025-2; VAT penalties specific to the Act; full schedule item lists.

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
