---
name: ks-sales-tax
description: Use this skill whenever asked about Kansas sales and use tax. Trigger on phrases like "Kansas sales tax", "KS sales tax", "KDOR", "K.S.A. §79-3603", "Kansas grocery tax". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-KS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KS Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Kansas |
| State rate | 6.50% |
| Grocery food state rate | 0.00% (effective January 1, 2025 -- phased down from 6.5%) |
| Maximum combined rate | ~11.50% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross receipts |
| Tax authority | Kansas Department of Revenue (KDOR) |
| Portal | https://www.kdor.ks.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.50% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | 0% state (as of Jan 2025) | Local rates still apply; phased down from 6.5% |
| Prepared food | TAXABLE 6.50% |  |
| SaaS | NOT TAXABLE | Kansas has not clearly taxed SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Prohibition - grocery food state tax** — NEVER apply state tax to grocery food as of 2025 -- state rate is 0%. Local still applies.  _(Section 10 -- Prohibitions)_
- **Prohibition - phase-down history** — NEVER forget the phase-down history of grocery food taxation.  _(Section 10 -- Prohibitions)_
- **Prohibition - computation** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
