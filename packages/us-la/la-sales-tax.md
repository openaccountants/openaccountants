---
name: la-sales-tax
description: Use this skill whenever asked about Louisiana sales and use tax. Trigger on phrases like "Louisiana sales tax", "LA sales tax", "R.S. 47:301", "parish sales tax", "Sales Tax Commission". CRITICAL -- among highest combined rates in the US (~11.45%). ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-LA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# LA Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Louisiana |
| State rate | 4.45% |
| Local rate range | 0% -- 7% (parish + city) |
| Maximum combined rate | ~11.45% (among highest in US) |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| State authority | Louisiana Department of Revenue (LDR) |
| Remote seller portal | Louisiana Sales Tax Commission -- https://www.lstc.la.gov |
| State portal | https://revenue.louisiana.gov |
| SST member | No |
| Parish self-administration | Parishes administer their own local taxes (similar to AL) |
| Skill version | 2.0 |

**CRITICAL: Louisiana parishes self-administer local sales taxes. The Louisiana Sales Tax Commission handles remote seller compliance centrally.**

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 4.45% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | EXEMPT from state | Some parishes may still tax food |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE | Louisiana has not clearly taxed SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Parish self-administration** — NEVER ignore parish-level self-administration -- local compliance is separate from state.
- **Highest combined rates** — NEVER forget Louisiana has among the highest combined rates in the US.
- **SaaS taxability** — NEVER treat SaaS as clearly taxable in Louisiana.
- **No computation** — NEVER compute any number.

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
