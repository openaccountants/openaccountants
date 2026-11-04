---
name: ms-sales-tax
description: "Use this skill whenever asked about Mississippi sales and use tax. Trigger on phrases like \"Mississippi sales tax\", \"MS sales tax\", \"Miss. Code §27-65\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-sales-tax"
  jurisdiction: "US-MS"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# MS Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Mississippi |
| State rate | 7.00% |
| Local taxes | Very limited (up to 0.25% in some areas) |
| Maximum combined rate | ~7.25% |
| Sourcing | Origin-based |
| Economic nexus | $250,000 in sales |
| Tax authority | Mississippi Department of Revenue |
| Portal | https://www.dor.ms.gov |
| SST member | No |
| Skill version | 2.0 |

**Mississippi taxes MOST services broadly and taxes grocery food at a reduced rate.**

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 7% |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | TAXABLE at 5% | Reduced rate (not exempt) |
| Prepared food | TAXABLE 7% |  |
| SaaS | NOT TAXABLE | Not clearly taxed |
| Canned software | TAXABLE |  |
| Most services | TAXABLE | Mississippi taxes services broadly |
| Professional services | Varies | Many professional services taxable |
| Manufacturing equipment | REDUCED RATE |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Prohibition: grocery food exemption claim** — NEVER say grocery food is exempt -- Mississippi taxes it at 5%.
- **Prohibition: services exemption assumption** — NEVER assume services are exempt -- Mississippi taxes most services.
- **Prohibition: sourcing rule** — NEVER forget origin-based sourcing.
- **Prohibition: computing numbers** — NEVER compute any number.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
