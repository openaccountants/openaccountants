---
name: sc-company-formation
description: "Seychelles company formation and entity choice for 2026: domestic companies under the Companies Act 1972, International Business Companies under the 2016 Act, sole traders, partnerships and special licence companies; registered agent and director rules; the 2026 IBC amendments; SRC business registration, TIN and accounting record duties. Use for form a company in Seychelles, IBC rules, or IBC TIN. Source-based; no accountant has signed it."
jurisdiction: SC
category: formation
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Seychelles Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Local trading through a Companies Act 1972 company, a partnership or a sole trader, against an International Business Company (IBC) under the International Business Companies Act 2016. The Financial Services Authority regulates IBCs. The Registrar handles domestic companies; the registry site refused access, so domestic detail is limited.

## Rates, bands and thresholds

| Item | Amount or rule | Tax year | Official URL |
|---|---|---|---|
| IBC members | One or more at all times, s 99 | 2026 | https://fsaseychelles.sc/component/edocman/consolidated-international-business-companies-act-2016-to-11th-july-2025/download?Itemid=0 |
| IBC director | At least one at all times, s 130 | 2026 | same |
| IBC first director appointment | Within 30 days from incorporation, s 134(1), changed from nine months by Act 13 of 2026 s 2 | 2026 | https://src.gov.sc/wp-content/uploads/2026/10/Act-13-2026-International-Business-Companies-Amendment-Act-2026.pdf |
| IBC registered agent | In Seychelles at all times, s 164 | 2026 | https://fsaseychelles.sc/component/edocman/consolidated-international-business-companies-act-2016-to-11th-july-2025/download?Itemid=0 |
| IBC annual return, s 171 | Repealed | 2026 | same |
| IBC financial summary | A company outside s 175(1A) keeps an annual financial summary at its registered office within 6 months of year end, and lodges records held abroad at least twice a year. A non-large holding company lodges records at least twice a year | 2026 | same |
| IBC nominee directors | Register must show nominee status and the nominator by 31 Dec 2026 | 2026 | https://src.gov.sc/wp-content/uploads/2026/10/Act-13-2026-International-Business-Companies-Amendment-Act-2026.pdf |
| IBC directors on the public side | Name and appointment date of current directors, from 1 Jan 2027 (ss 346, 352) | 2026 | same |
| IBC TIN | Issued only to IBCs with Seychelles-sourced income or in a multinational group; TRCs continue | 2026 | https://src.gov.sc/suspension-of-tin-for-ibcs-applying-for-bank-purpose-only/ |
| Business registration at SRC | Within 28 days of starting | 2026 | https://src.gov.sc/wp-content/uploads/2023/01/SI-138-2022-Revenue-Administration-Business-Registration-and-Declaration-of-Operation-Regulations-2022-1.pdf |


## The base

Section 5 bars an IBC from banking anywhere and from insurance, securities, fund, gambling and corporate services business in Seychelles unless licensed where the section allows. An IBC working in Seychelles registers the business with SRC and pays business tax; one without Seychelles income has no return ([brochure](https://src.gov.sc/wp-content/uploads/2022/12/Frequently-Asked-Questions-for-IBC-Brochure.pdf)). The brochure says 14 days to register; S.I. 138 of 2022 says 28 and the law wins. An IBC cancels its TIN within 30 days of being struck off.

## Deadlines and filing

1. Choose the entity. IBCs go through a licensed registered agent.
2. Obtain any licence.
3. Complete the SRC registration form (General, Presumptive or Residential Rent) within 28 days, with ID, licence and company certificate, and tax agent details ([FAQ](https://src.gov.sc/faq/)).
4. Register employees within 7 days.
5. Notify changes within 28 days; suspension 14 days ahead; cessation within 28 days ([S.I. 138](https://src.gov.sc/wp-content/uploads/2023/01/SI-138-2022-Revenue-Administration-Business-Registration-and-Declaration-of-Operation-Regulations-2022-1.pdf)).

## Penalties and interest

SRC registration offences are in [Corporate income tax](sc-corporate-income-tax.md). IBC Act penalties were not read.

## Cross-border points

An IBC can request a Tax Residency Certificate in writing, for a fee ([brochure](https://src.gov.sc/wp-content/uploads/2022/12/Frequently-Asked-Questions-for-IBC-Brochure.pdf)).

## Two worked examples that recompute

Decision on rate only, for SCR 1,500,000 of Seychelles profit: see [Corporate income tax](sc-corporate-income-tax.md). Company tax is SCR 275,000.

```oa-check
name: Company tax on SCR 1,500,000
inputs:
  profit: 1500000
steps:
  - tax: 1000000 * 0.15 + (profit - 1000000) * 0.25
expected:
  tax: 275000
```

The same profit as a sole trader is SCR 259,600.10, so the entity choice moves SCR 15,399.90 before any other cost.

```oa-check
name: Sole trader tax on SCR 1,500,000
inputs:
  profit: 1500000
steps:
  - tax: (1000000 - 102666) * 0.15 + (profit - 1000000) * 0.25
expected:
  tax: 259600.10
```

## Ask the client first

- Will it trade with Seychelles customers or own local property?
- Any licensed activity?
- Group member?
- Who are the owners and nominees?

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for the figures cited: FSA consolidated IBC Act 2016, listed as to 24 August 2026, read ss 5, 99, 130, 134, 164, 171, 175 | https://fsaseychelles.sc/component/edocman/consolidated-international-business-companies-act-2016-to-11th-july-2025/download?Itemid=0 | 2026-11-01 |
| Read for the figures cited: IBC (Amendment) Act 2026 (Act 13 of 2026), whole Act | https://src.gov.sc/wp-content/uploads/2026/10/Act-13-2026-International-Business-Companies-Amendment-Act-2026.pdf | 2026-11-01 |
| Read for the figures cited: SRC notice, Suspension of TIN for IBCs, 21 Aug 2026 | https://src.gov.sc/suspension-of-tin-for-ibcs-applying-for-bank-purpose-only/ | 2026-11-01 |
| Read for the figures cited: SRC FAQ brochure for IBCs | https://src.gov.sc/wp-content/uploads/2022/12/Frequently-Asked-Questions-for-IBC-Brochure.pdf | 2026-11-01 |
| Read for the figures cited: S.I. 138 of 2022, registration regs | https://src.gov.sc/wp-content/uploads/2023/01/SI-138-2022-Revenue-Administration-Business-Registration-and-Declaration-of-Operation-Regulations-2022-1.pdf | 2026-11-01 |
| Read for the figures cited: SRC FAQ, domestic section | https://src.gov.sc/faq/ | 2026-11-01 |

Not yet confirmed: minimum share capital for either company type; the old claim that an IBC cannot trade with residents or own local real estate; IBC incorporation time and government fees; Companies Act 1972 annual filings; Companies (Special Licences) Act rules; the register of beneficial owners rules. The registry site returned 403 and these rest on third-party pages in the old pack, which were removed as citations.

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
