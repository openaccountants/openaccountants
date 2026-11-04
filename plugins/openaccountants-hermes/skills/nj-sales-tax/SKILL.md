---
name: nj-sales-tax
description: "Use this skill whenever asked about New Jersey sales and use tax. Trigger on phrases like \"New Jersey sales tax\", \"NJ sales tax\", \"NJ Division of Taxation\", \"UEZ\", \"NJ clothing exemption\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nj-sales-tax"
  jurisdiction: "US-NJ"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# NJ Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | New Jersey |
| State rate | 6.625% |
| Local taxes | None (except Urban Enterprise Zones at 3.3125%) |
| Maximum combined rate | 6.625% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | NJ Division of Taxation |
| Portal | https://www.nj.gov/treasury/taxation/ |
| SST member | No |
| Clothing exemption | Yes -- ALL clothing and footwear exempt |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.625% |  |
| Clothing and footwear | EXEMPT | NJ exempts ALL clothing and footwear |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | TAXABLE | NJ taxes SaaS and digital products |
| Canned software | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |
| Urban Enterprise Zone (UEZ) sales | TAXABLE at 50% rate (3.3125%) | Qualifying retailers in UEZs |

## Section 10 -- Prohibitions

- **Clothing taxability prohibition** — NEVER treat clothing as taxable in NJ -- ALL clothing and footwear is exempt.  _(Section 10 -- Prohibitions)_
- **UEZ reduced rate reminder** — NEVER forget the UEZ reduced rate program (3.3125%).  _(Section 10 -- Prohibitions)_
- **No computation rule** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nj-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nj-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
