---
name: om-company-formation
description: "Company formation and entity choice for Oman, tax year 2026: entity forms, shareholders, capital minimums, foreign ownership, auditor triggers, tax card and notifications, from the Commercial Companies and Foreign Capital Investment Laws."
version: 1.1
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Company Formation & Entity Choice

## Who this applies to

Founders choosing a vehicle in Oman, Omani or foreign. Commercial companies must take a form in art. 4 of the Commercial Companies Law, or the company is void (art. 5).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Forms | General partnership, limited partnership, joint venture, joint stock (public or closed), holding, limited liability, one-person (art. 4) | 2026 | https://decree.om/2019/rd20190018/ |
| LLC members | 2 to 50, capital fully paid on registration (art. 234) | 2026 | same |
| Closed joint stock capital | At least OMR 500,000 (art. 91) | 2026 | same |
| Public joint stock capital | At least OMR 2,000,000 (art. 91) | 2026 | same |
| Holding company capital | At least OMR 2,000,000, 51% of subsidiaries (arts 228, 230) | 2026 | same |
| LLC auditor triggers | More than 7 shareholders; capital above OMR 50,000; constitution requires it; holders of one fifth request it (art. 278) | 2026 | same |
| Foreign ownership | Full ownership or a share, through an establishment or company, in permitted activities (art. 6) | 2026 | https://qanoon.om/p/2019/rd2019050/ |
| Barred activities | A minister's list (art. 14) | 2026 | same |

## The base

Foreign investment means direct foreign capital to set up, expand, finance, manage or own a project (art. 1). Foreign capital covers money, securities, machinery, intellectual property and reinvested profit (art. 4). Laws for GCC investors, Duqm, industrial estates and free zones stand apart (art. 2).

## Deadlines and filing

| Step | Rule | Official URL |
|---|---|---|
| Investor registration | The ministry's investment services centre registers the foreign investor and obtains approvals; silence past the regulation's period counts as acceptance (art. 5) | https://qanoon.om/p/2019/rd2019050/ |
| Tax card | Request when incorporating (art. 11) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Register data | Notify during commercial registration; other cases within 60 days (art. 11) | same |
| Income tax | All register holders register and file (https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, questions 1, 2) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| VAT | See [VAT](oman-vat.md) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Social contributions | See [payroll](om-payroll-social.md) | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ |

Annual run: renew the commercial registration, keep accounts, file the income tax return, file quarterly VAT if registered, pay monthly contributions.

## Penalties and interest

See the sibling skills. Doing business without an art. 4 form makes the company void, and those who acted are jointly liable (art. 5).

## Cross-border points

Foreign investors must use an establishment or company with a licence from the centre (art. 6). Oman's courts hear disputes and arbitration is allowed (art. 17). A branch is a permanent establishment for income tax (https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf, art. 2).

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
| Commercial Companies Law, RD 18/2019, Decree.om translation, a private publisher (arts 4, 91, 219, 229, 230, 234, 278 read) | https://decree.om/2019/rd20190018/ | 2026-11-01 |
| Foreign Capital Investment Law, RD 50/2019, Arabic text on Qanoon.om, a private publisher (arts 1 to 17 read) | https://qanoon.om/p/2019/rd2019050/ | 2026-11-01 |
| Income Tax Law, RD 28/2009, consolidated to RD 118/2020, Tax Authority English text (arts 2, 11, 12, 50, 52, 53, 69 to 73, 90, 112 to 118, 124, 125, 156, 159bis 11 to 19, 179 to 184 read) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf | 2026-11-01 |
| Tax Authority, Income Tax FAQs (all 16 read) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs | 2026-11-01 |
| VAT Law, RD 121/2020, Tax Authority English text (arts 28 to 57, 61, 71, 72, 99 to 101 read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 | 2026-11-01 |
| Social Protection Fund, FAQ on contribution rates (whole page read) | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ | 2026-11-01 |

Not yet confirmed: the ministry portal steps, fees, name reservation and timing (mocioman.gov.om and mcti.gov.om did not open, so the old 2 to 3 weeks and the old step list are not carried as fact: reserve name, notarise constitution, security clearance, commercial registration, municipality licence, tax and Fund registration); the old OMR 150,000 foreign LLC capital practice, which comes from a secondary source only; whether any LLC minimum exists (art. 234 states none); the current barred list; the one-person company rules; the audit rule for one-person and joint stock companies beyond art. 219.

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
