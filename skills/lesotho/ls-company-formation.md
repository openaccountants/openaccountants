---
name: ls-company-formation
description: "Forming a company in Lesotho: entity types, registration steps, fees, licences and first tax registrations. Covers Lesotho tax year 2026-27 (1 April 2026 to 31 March 2027), figures read from Revenue Services Lesotho and gazetted law on 1 November 2026. Use when someone asks about lesotho company formation and entity choice in Lesotho, what applies, what the rate or threshold is, when to file or pay, what a late filing costs, or how an amount is worked out. Not signed off by an accountant. It states which points could not be read at source so they are not relied on."
jurisdiction: LS
category: formation
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
version: 0.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lesotho Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders and foreign companies setting up in Lesotho. Companies register under the Companies Act No. 18 of 2011 at the One-Stop Business Facilitation Centre (OBFC). Types: public, private and non-profit companies, plus external companies. A sole trader is taxed in the owner's hands.

Lesotho's tax year runs 1 April to 31 March. This skill covers 2026-27, from 1 April 2026.

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Name reservation | M30 | Internal or external company | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ |
| Internal company application | M500 |  | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ |
| External company application | M1,000 | The page labels this row oddly; confirm on filing | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ |
| Trading licence | M500 to M50,000 (MSME); M1,500 to M150,000 (large) | Risk-based; for negative-listed activities; annual renewal | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ |
| Manufacturing licence | M150 small; M3,500 medium to large | M1,000 late renewal | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ |
| Business ID | Renewed every 3 years |  | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ |
| VAT registration | M2,000,000 a year | See ls-vat-gst | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Registration%20For%20Value%20Added%20Tax%20Purposes%20%20-%20VAT%20101%20%281%29.pdf |
| Minimum share capital | unverified | Older skill: none. Companies Act not read | unverified: not opened |
| Minimum shareholders and directors | unverified | Older skill: one of each. Companies Act not read | unverified: not opened |

## The base

Steps: (1) create an account on the companies registry; (2) get authority to file (directors, or an authorised agent); (3) search and reserve the name; (4) choose the company type; (5) submit online with articles, director consents, application form, shareholder list and certified IDs (external companies also a foreign certificate of incorporation); (6) pay by EFT and send proof to the OBFC; (7) RSL and the OBFC assess the application jointly. Then register for tax and, if needed, VAT, and get any licence. A private company restricts share transfers and a public company may offer shares to the public, per the older skill (Companies Act not read).

## Deadlines and filing

- Annual return to the Registrar: required per the older skill; date and fee unverified.
- Trading licence: renew yearly and display at the premises.
- Manufacturing licence: renew yearly under 50 employees; above 50, it expires 31 December.
- Accounting records and annual financial statements: required per the older skill; audit thresholds unverified.
- Incorporation time: the LNDC page gives none, and the older skill's estimate of days to weeks is unverified.

## Penalties and interest

Not stated on the page read. See ls-income-tax and ls-vat-gst for tax penalties.

## Cross-border points

A foreign company registers as an external company with its foreign certificate of incorporation. A Lesotho branch pays 25% on repatriated income as well as income tax (see ls-corporate-income-tax).

## Two worked examples that recompute

Example 1: internal company fees M30 plus M500 is M530, before any licence.

```oa-check
name: Internal company fees
inputs:
  name: 30
  application: 500
steps:
  - total: name + application
expected:
  total: 530.00
```

Example 2, a decision: an external company costs M500 more in fees than a local one: M1,030 against M530. Weigh this with branch tax on repatriated income.

```oa-check
name: External against internal
inputs:
  internal: 530
  external: 1030
steps:
  - extra: external - internal
expected:
  extra: 500.00
```

## Ask the client first

1. Local company, external company or sole trader?
2. Activity: is it negative-listed or manufacturing?
3. Who are the directors and shareholders?
4. Expected taxable turnover?
5. Staff numbers?

## Sources

| Source | URL | Read on |
|---|---|---|
| LNDC Business Registration and Licensing page; read in full | https://lndc.org.ls/knowledge-base/business-registration-and-licensing/ | 2026-11-01 |
| RSL Guide on Registration for VAT, VAT 101; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Registration%20For%20Value%20Added%20Tax%20Purposes%20%20-%20VAT%20101%20%281%29.pdf | 2026-11-01 |

Not yet confirmed: everything resting on the Companies Act 2011 and Companies Regulations 2012 (share capital, member and director minimums, annual return, audit, business names): msm.org.ls failed its security certificate and lesotholii.org showed a security check, so neither was read; OBFC site did not load.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
