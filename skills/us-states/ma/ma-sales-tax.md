---
name: ma-sales-tax
description: Use this skill whenever asked about Massachusetts sales and use tax. Trigger on phrases like "Massachusetts sales tax", "MA sales tax", "MA DOR", "ST-9", "Massachusetts clothing exemption". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MA Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Massachusetts |
| State rate | 6.25% |
| Local taxes | None |
| Maximum combined rate | 6.25% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 in sales |
| Tax authority | Massachusetts Department of Revenue (DOR) |
| Portal | https://www.mass.gov/orgs/massachusetts-department-of-revenue |
| SST member | No |
| Clothing exemption | Yes -- under $175/item |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.25% |  |
| Clothing under $175/item | EXEMPT | Per-item threshold |
| Clothing $175+ per item | TAXABLE on amount over $175 | Only excess over $175 is taxed |
| Grocery food | EXEMPT |  |
| Prepared food (meals) | TAXABLE at 6.25% | Local option meals tax up to 0.75% additional |
| SaaS | TAXABLE | Massachusetts taxes SaaS |
| Canned software | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Clothing under $175 taxation prohibition** — NEVER apply full tax to clothing under $175 -- only the excess over $175 is taxable.  _(Section 10 -- Prohibitions)_
- **Local option meals tax prohibition** — NEVER forget the local option meals tax (up to 0.75% additional on prepared food).  _(Section 10 -- Prohibitions)_
- **No computation prohibition** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

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
