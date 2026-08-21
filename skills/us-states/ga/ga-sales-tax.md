---
name: ga-sales-tax
description: Use this skill whenever asked about Georgia sales and use tax. Trigger on phrases like "Georgia sales tax", "GA sales tax", "O.C.G.A. 48-8", "Georgia DOR". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-GA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# GA Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Georgia |
| State rate | 4.00% |
| Local rate range | 2% -- 4% (county) |
| Maximum combined rate | 8.00% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Georgia Department of Revenue |
| Portal | https://gtc.dor.ga.gov |
| SST member | No |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**  _(O.C.G.A. §48-8-3(57))_

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 4% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | O.C.G.A. §48-8-3(57) |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE | Georgia does not clearly tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Grocery food treatment** — NEVER treat grocery food as taxable -- it is exempt in Georgia.
- **SaaS treatment** — NEVER treat SaaS as clearly taxable -- Georgia has not enacted SaaS taxation.
- **Computation prohibition** — NEVER compute any number.

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
