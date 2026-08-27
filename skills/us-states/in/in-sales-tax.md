---
name: in-sales-tax
description: Use this skill whenever asked about Indiana sales and use tax. Trigger on phrases like "Indiana sales tax", "IN sales tax", "IC 6-2.5", "Indiana DOR". Indiana has one of the SIMPLEST structures -- 7% flat with no local sales taxes. ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-IN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IN Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Indiana |
| State rate | 7.00% (flat -- no local sales tax) |
| Local taxes | None |
| Maximum combined rate | 7.00% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Indiana Department of Revenue |
| Portal | https://intime.dor.in.gov |
| SST member | Yes (full member) |
| Skill version | 2.0 |

**One of the simplest sales tax states -- 7% flat rate statewide, no local add-ons.**

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 7% | Uniform statewide |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE | Indiana does not tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT | IC 6-2.5-5-3 |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Never add local tax** — NEVER add local tax -- Indiana has no local sales taxes.
- **Never treat SaaS as taxable** — NEVER treat SaaS as taxable in Indiana.
- **Never compute any number** — NEVER compute any number.

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
