---
name: mn-sales-tax
description: "Use this skill whenever asked about Minnesota sales and use tax. Trigger on phrases like \"Minnesota sales tax\", \"MN sales tax\", \"M.S. 297A\", \"Minnesota DOR\". NOTE -- Minnesota EXEMPTS clothing. ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mn-sales-tax"
  jurisdiction: "US-MN"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# MN Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Minnesota |
| State rate | 6.875% |
| Local rate range | 0% -- ~2% |
| Maximum combined rate | ~8.875% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Minnesota Department of Revenue (MNDOR) |
| Portal | https://www.revenue.state.mn.us |
| SST member | Yes (full member) |
| Clothing exemption | Yes -- ALL clothing exempt |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.875% + local |  |
| Clothing and footwear | EXEMPT | Minnesota exempts ALL clothing |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE |  |
| Canned software (download) | TAXABLE |  |
| Digital goods | TAXABLE | Specified digital products |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT | Capital equipment refund program |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Clothing taxability prohibition** — NEVER treat clothing as taxable in Minnesota -- ALL clothing is exempt.
- **SaaS taxability prohibition** — NEVER treat SaaS as taxable.
- **No computation prohibition** — NEVER compute any number.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mn-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mn-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
