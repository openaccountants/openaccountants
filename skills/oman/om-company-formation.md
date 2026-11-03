---
name: om-company-formation
description: "Company formation and entity choice for Oman, tax year 2026: entity forms, shareholders, capital minimums, foreign ownership, auditor triggers, tax card and notifications, from the Commercial Companies and Foreign Capital Investment Laws."
version: 1.2
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Company Formation & Entity Choice v1.2

> **General reference only.** This Guide is a draft for AI-assisted reference. It has not received independent closeout review or accountant attestation. Do not use it to file, pay or take a position without professional review.

## Who this applies to

Founders choosing a vehicle in Oman, Omani or foreign. Commercial companies must take a form in art. 4 of the Commercial Companies Law, or the company is void (art. 5).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Forms | General partnership, limited partnership, joint venture, joint stock (public or closed), holding, limited liability, one-person (art. 4) | 2026 | https://e.fsa.gov.om/Content/PDF/NewCommercialCompaniesLawEn.pdf |
| LLC members | Normally 2 to 50; ministerial increase permitted; State-only companies exempt; capital fully paid on registration (art. 234) | 2026 | same |
| Closed joint stock capital | At least OMR 500,000 (art. 91) | 2026 | same |
| Public joint stock capital | At least OMR 2,000,000; OMR 1,000,000 on conversion from another legal form (art. 91) | 2026 | same |
| Holding company capital | At least OMR 2,000,000, at least 51% of each subsidiary (arts 227, 230) | 2026 | same |
| LLC auditor triggers | More than 7 shareholders; capital above OMR 50,000; constitution requires it; holders of one fifth request it (art. 278) | 2026 | same |
| Foreign ownership | NONOPERATIVE HOLD: prior draft states full ownership or a share, through an establishment or company, in permitted activities (art. 6) | 2026 | https://qanoon.om/p/2019/rd2019050/ |
| Barred activities | NONOPERATIVE HOLD: prior draft identifies a minister's list (art. 14) | 2026 | same |

## The base

A one-person company is an LLC wholly owned by one natural or legal person. A natural person cannot establish more than one such company; a one-person company cannot itself establish another. Liability is normally limited to allocated capital, with personal exposure for bad-faith liquidation or mixing private and company business. Formation procedure is left to the Regulations; the LLC rules otherwise apply to the extent compatible with its nature (arts 291 to 297). Joint-stock companies require one or more licensed auditors appointed by the annual ordinary general meeting (art. 219).

NONOPERATIVE HOLD on the following Foreign Capital Investment Law summary: the prior draft read a private Arabic reproduction, but the current closeout has not recovered an official full instrument or current restrictions. Do not plan an incorporation from it. Foreign investment means direct foreign capital to set up, expand, finance, manage or own a project (art. 1). Foreign capital covers money, securities, machinery, intellectual property and reinvested profit (art. 4). Laws for GCC investors, Duqm, industrial estates and free zones stand apart (art. 2).

## Deadlines and filing

| Step | Rule | Official URL |
|---|---|---|
| Investor registration | NONOPERATIVE HOLD: the prior draft says the ministry's investment services centre registers the foreign investor and obtains approvals; silence past the regulation's period counts as acceptance (art. 5) | https://qanoon.om/p/2019/rd2019050/ |
| Tax card | Request when incorporating (art. 11) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Register data | Notify during commercial registration; other cases within 60 days (art. 11) | same |
| Income tax | All register holders register and file (https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, questions 1, 2) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| VAT | See [VAT](oman-vat.md) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Social contributions | See [payroll](om-payroll-social.md) | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ |

Annual checklist: keep accounts, file the income tax return, file quarterly VAT if registered and pay monthly contributions, subject to the sibling Guides’ conditions. NONOPERATIVE HOLD: the predecessor’s annual commercial-registration renewal cycle requires the current registration instrument or authenticated register confirmation; do not infer its due date here.

## Penalties and interest

See the sibling skills. Doing business without an art. 4 form makes the company void, and those who acted are jointly liable (art. 5).

## Cross-border points

NONOPERATIVE HOLD: the prior Foreign Capital Investment Law summary says foreign investors need a licensed establishment or company (art. 6), Omani courts hear disputes and arbitration is allowed (art. 17). These clauses and current restrictions require an official-source check before use. A branch is a permanent establishment for income tax (https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf, art. 2).

## Two worked examples that recompute

**1. Founders' capital check for a closed joint stock company.** With OMR 650,000 they clear the OMR 500,000 minimum by OMR 150,000.

```oa-check
name: Closed joint stock capital headroom
inputs:
  capital: 650000
  minimum: 500000
steps:
  - headroom: capital - minimum
expected:
  headroom: 150000
```

**2. Decision: LLC capital OMR 50,000 or OMR 60,000.** Art. 278 triggers an auditor above OMR 50,000. At OMR 60,000 the excess is OMR 10,000, so an auditor is required; at OMR 50,000 none is, on this test alone.

```oa-check
name: LLC auditor trigger excess
inputs:
  capital: 60000
  trigger: 50000
steps:
  - excess: max(capital - trigger, 0)
expected:
  excess: 10000
```

## Ask the client first

- Who owns it, and from which country?
- Activity, and is it on the barred list?
- Mainland, free zone or Duqm?
- Number of owners and intended capital?
- Bank, lender or regulator needing audited accounts?

## Sources

| Source | URL | Read on |
|---|---|---|
| Commercial Companies Law, RD 18/2019, official FSA English text (arts 4, 5, 91, 219, 227 to 234, 278 and 291 to 297 checked; FSA-hosted translation expressly says Arabic prevails; this is not a later-amendment completeness claim) | https://e.fsa.gov.om/Content/PDF/NewCommercialCompaniesLawEn.pdf | 2026-11-01 |
| Foreign Capital Investment Law, RD 50/2019, prior-draft private reproduction; official complete text not recovered for this closeout, all derived claims held | https://qanoon.om/p/2019/rd2019050/ | 2026-11-01 |
| Income Tax Law, RD 28/2009, authority-hosted English consolidation to RD 118/2020 (selected complete clauses: 1, 2, 11, 12, 40, 42 to 53, 69 to 72, 90, 112 to 116, 118, 124, 125, 150, 156, 157, 159bis and 159bis 4 to 6, 9 to 19, 160, 160bis, 179 to 181, 184; scope is recorded in the closeout ledger, not later-amendment closure) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf | 2026-11-01 |
| Tax Authority, Income Tax FAQs (all 16 read) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs | 2026-11-01 |
| VAT Law, RD 121/2020, Tax Authority English text (arts 28 to 57, 61, 71, 72, 99 to 101 read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 | 2026-11-01 |
| Social Protection Fund, contribution-rate FAQ answer checked in cached Fund FAQ HTML; conflicting commencement dates held | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ | 2026-11-01 |

Not yet confirmed: the ministry portal steps, fees, name reservation and timing (mocioman.gov.om and mcti.gov.om did not open, so the old 2 to 3 weeks and the old step list are not carried as fact: reserve name, notarise constitution, security clearance, commercial registration, municipality licence, tax and Fund registration); the old OMR 150,000 foreign LLC capital practice, which comes from a secondary source only; whether any LLC minimum exists (art. 234 states none); the current barred list; the one-person-company procedural Regulations and how art. 278 applies to its particular facts; joint-stock auditor appointment Regulations beyond art. 219.

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
