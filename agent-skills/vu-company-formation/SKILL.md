---
name: vu-company-formation
description: "Vanuatu company formation, tax year 2026: incorporating a local company with the VFSC under the Companies Act 2012, the VT 35,000 registration and annual return fees, late-document penalties, business names, the allocated-month annual return and removal rule, accounting records, and the DCIR business licence (31 January renewal, 10% a month late)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vu-company-formation"
  jurisdiction: "VU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Vanuatu company formation and entity choice

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file without professional review.

## Who this applies to

Anyone setting up a local company in Vanuatu under the Companies Act No. 25 of 2012, registered by the Vanuatu Financial Services Commission (VFSC), and any business that needs a DCIR business licence. Overseas companies carrying on business in Vanuatu and international companies under the International Companies Act [Cap 222] have separate routes (VFSC entity guidance, https://www.vfsc.vu/learn-about-companies-other-entities/); their tax exemptions are in [corporate income tax](vu-corporate-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Register a company, s 6 | VT 35,000 online or offline | 2026 | https://www.vfsc.vu/companies-fees-and-penalties/ |
| Annual return, s 119 | VT 35,000 online or offline | 2026 | https://www.vfsc.vu/companies-fees-and-penalties/ |
| Document delivered late, within 25 working days after the time prescribed | VT 10,000 | 2026 | https://www.vfsc.vu/companies-fees-and-penalties/ |
| Document delivered more than 25 working days late | VT 25,000 | 2026 | https://www.vfsc.vu/companies-fees-and-penalties/ |
| Register a business name | VT 12,000; renewal VT 5,000 | 2026 | https://www.vfsc.vu/companies-fees-and-penalties/ |
| Business licence not renewed by 31 January | Penalty of 10% for every month the fee is overdue | 2026 | https://vanuatucustoms.gov.vu/taxes-and-licensing/licensing/business-licencing |

The original Companies Regulations Order No. 114 of 2015 listed VT 30,000 online and VT 35,000 offline; the VFSC schedule now shows VT 35,000 for both. The instrument behind the online increase was not found.

## The base

Not a tax. The registration application (s 6) names the company and its type (private, public or community), its rules, directors and their consents, shareholders and share allocations, registered office and postal address, any non-model rules, and the fee. From 5 January 2018 it must also give the nominators of any nominee shareholders and nominee directors (Companies Amendment Act No. 32 of 2017). The Registrar registers the company and issues the certificate when the application complies (ss 6 to 9).

## Deadlines and filing

1. Apply to the VFSC online with the s 6 details and VT 35,000.
2. Get a taxpayer identification number from DCIR.
3. Apply to DCIR for a business licence if the company carries on business for profit (unless exempt), with the TIN and VFSC certificate; a foreign-owned business also needs a valid Vanuatu Foreign Investment Promotion Authority certificate. A new licence runs from the start date to 31 December; renew on or before 31 January each year (a foreign investor renews the VFIPA certificate first).
4. Register for VAT if the VT 4 million test is met ([VAT](vu-vat-gst.md)).
5. File the annual return in the company's allocated month with the fee (s 119). The calendar year of incorporation is exempt; a subsidiary may use its holding company's month with written approval. From 5 January 2018 a company that has not filed within 6 months after the allocated date must be removed from the register, subject to s 142 (s 140(1)(a)).
6. Keep accounting records that explain transactions, show the financial position with reasonable accuracy and support financial statements (s 124); check the statement and audit rules in ss 125 to 129.

## Penalties and interest

Late documents: VT 10,000 or VT 25,000 (table). Late licence renewal: 10% a month. Missing the annual return by 6 months: removal from the register.

## Cross-border points

Foreign-owned businesses need a VFIPA certificate before the business licence. Overseas companies register under their own Part of the Companies Act and file their own annual return (s 161).

## Two worked examples that recompute

**1. New local company, registration and first-year business licence.** VFSC fee VT 35,000; no annual return in the year of incorporation; the next calendar year the annual return costs another VT 35,000, so VT 70,000 of VFSC fees over the first two years (derived).

```oa-check
name: Vanuatu company first two years VFSC fees
inputs:
  registration: 35000
  annual_return: 35000
steps:
  - two_years: registration + annual_return
expected:
  two_years: 70000
```

**2. Business licence fee VT 100,000 renewed two months late.** Penalty 10% for each of the two months, VT 20,000 (derived on a simple reading of "10% of every month"; DCIR does not say whether it compounds).

```oa-check
name: Vanuatu licence late two months
inputs:
  fee: 100000
  months: 2
steps:
  - penalty: fee * 0.10 * months
expected:
  penalty: 20000
```

## Ask the client first

- Local, overseas or international company? Private, public or community?
- Any nominee shareholders or directors?
- Foreign ownership (VFIPA certificate)?
- Business activity and expected turnover (licence category, VAT)?

## Sources

| Source | URL | Read on |
|---|---|---|
| VFSC, Companies fees and penalties (Read for the registration, annual return, penalty and business name fees) | https://www.vfsc.vu/companies-fees-and-penalties/ | 2026-11-14 |
| DCIR, Business licencing (Read for the licence period, renewal date and 10% penalty) | https://vanuatucustoms.gov.vu/taxes-and-licensing/licensing/business-licencing | 2026-11-14 |
| Companies Act No. 25 of 2012, official gazetted version, ss 6 to 9, 119, 124 to 129, 140, 161 (Read for the application and annual return) | https://www.vfsc.vu/wp-content/uploads/2025/06/Companies-Act-2012-Official-Gazetted-Version-1.pdf | 2026-11-14 |
| Companies Amendment Act No. 32 of 2017 (Read by Ryan Duguid for nominee disclosure and removal) | https://www.vfsc.vu/wp-content/uploads/2025/06/Companies-Amendment-Act-No.-32-of-2017-1.pdf | 2026-11-11 |

Not yet confirmed: the instrument that raised the online fee to VT 35,000; business licence fee bands by activity and turnover, and sector exemptions; whether the late-licence 10% compounds; overseas and international company reporting regimes. The old guide's capital-based fee scale (VT 30,000 to VT 250,000) and VT 10,000 business name fee are no longer on the VFSC schedule.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vu-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vu-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
