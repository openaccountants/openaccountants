---
name: sc-tax-overview
description: "Seychelles tax overview for tax year 2026: authority, currency, tax year, the main taxes and where each is covered, deadlines, tourism levies and immovable property tax. Use as the starting point for any Seychelles tax question, including what taxes apply to a business, a property owner or a tourism operator. Source-based; no accountant has signed it."
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

# Seychelles Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone with a business, employment, property or tourism activity in Seychelles. The authority is the Seychelles Revenue Commission (SRC), the currency the Seychelles Rupee (SCR), the tax year the calendar year.

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| Income tax | Monthly bands; see sc-personal-income-tax | 2026 | https://src.gov.sc/income-and-non-monetary-benefits-tax/ |
| Business tax | See sc-corporate-income-tax | 2026 | https://src.gov.sc/wp-content/uploads/2022/12/SI-108-of-2021-Business-Tax-Amendment-of-Schedules-Regulations-2021.pdf |
| VAT | See sc-vat-gst | 2026 | https://src.gov.sc/seychelles-tax-system/ |
| Pension Fund | See sc-payroll-social | 2026 | https://pensionfund.sc/mandatory-contribution/ |
| Immovable Property Tax, non-Seychellois, residential | 0.50% of market value, by 31 December | 2026 | https://src.gov.sc/seychelles-tax-system/ |
| Immovable property: failure to apply to register | SCR 50,000 commercial, industrial, multi-purpose and villas; SCR 10,000 others | 2026 | same |
| Tourism Environmental Sustainability Levy, per person per night | Medium 24 to 50 rooms SCR 75; large 51 rooms on SCR 100; yachts and island resorts SCR 100 | 2026 | same |
| Small establishments, 1 to 24 rooms | Levy no longer applies from 1 Jan 2026 (S.I. 90 of 2025). Earlier rate SCR 25 | 2026 | same |

Commercial and industrial property, and a residence owned by a taxpayer married to a Seychellois, pay no Immovable Property Tax. A first-time residential owner can apply for one year's exemption. The levy excludes citizens, residents, airline and yacht crew and children of 12 or under.

## The base

Each tax has its own base, in its own skill. Seychelles has historically been territorial.

## Deadlines and filing

Monthly returns and payments: 21st in person, 23rd by portal or, for payment, bank transfer ([Act 27 of 2023](https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf)). Annual business return: 31 March. Portal: [tms.src.gov.sc](https://tms.src.gov.sc/). Tourism levy and accommodation turnover tax: 21st ([SRC](https://src.gov.sc/seychelles-tax-system/)), on their own forms.

## Penalties and interest

See [Corporate income tax](sc-corporate-income-tax.md).

## Cross-border points

Treaties and TIEAs are on the [Agreements page](https://src.gov.sc/agreements/). SRC's voluntary disclosure programme began in 2026; read its guide for terms. No cross-border skill exists in this pack yet.

## Two worked examples that recompute

A non-Seychellois owns a residence valued at SCR 4,000,000: tax SCR 20,000.

```oa-check
name: Immovable Property Tax
inputs:
  value: 4000000
steps:
  - tax: value * 0.005
expected:
  tax: 20000
```

Decision: a 30-room guest house or a 20-room one in 2026, two guests for ten nights. The 30-room one collects SCR 1,500 from guests; the 20-room one nothing.

```oa-check
name: Tourism levy, medium
inputs:
  guests: 2
  nights: 10
steps:
  - levy: guests * nights * 75
expected:
  levy: 1500
```

## Ask the client first

- Business, employment, property or tourism?
- Citizen or non-citizen?
- Turnover?
- Rooms, if accommodation?

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the figures cited: SRC Tax System page, whole page read | https://src.gov.sc/seychelles-tax-system/ | 2026-11-01 |
| Read for the figures cited: SRC Income and Non-Monetary Benefits Tax page, whole page | https://src.gov.sc/income-and-non-monetary-benefits-tax/ | 2026-11-01 |
| Read for the figures cited: S.I. 108 of 2021, reg 2, First Schedule item 1 | https://src.gov.sc/wp-content/uploads/2022/12/SI-108-of-2021-Business-Tax-Amendment-of-Schedules-Regulations-2021.pdf | 2026-11-01 |
| Read for the figures cited: Seychelles Pension Fund, Mandatory Contribution page | https://pensionfund.sc/mandatory-contribution/ | 2026-11-01 |
| Read for the figures cited: Revenue Law (Amendment) Act 2023 (Act 27 of 2023), ss 3, 4, 7 | https://src.gov.sc/wp-content/uploads/2024/12/Act-27-2023-Revenue-Law-Amendment-Act-2023.pdf | 2026-11-01 |
| Read for the figures cited: SRC Agreements page, treaty lists | https://src.gov.sc/agreements/ | 2026-11-01 |

Not yet confirmed: room band overlap at 24 rooms on the SRC page, which puts 24 in both small and medium; capital gains and inheritance taxes, not covered by pages read.

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
