---
name: nm-sales-tax
description: "Use this skill whenever asked about New Mexico Gross Receipts Tax (GRT). Trigger on phrases like \"New Mexico GRT\", \"Gross Receipts Tax\", \"NM sales tax\", \"NMSA §7-9\". NM has a GRT, not a traditional sales tax. ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nm-sales-tax"
  jurisdiction: "US-NM"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# NM Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | New Mexico |
| Tax type | Gross Receipts Tax (GRT) -- NOT a traditional sales tax; tax on the SELLER |
| State GRT rate | 5.125% |
| Local add-on range | 0% -- ~4.1875% |
| Maximum combined rate | ~9.3125% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 in taxable gross receipts |
| Tax authority | New Mexico Taxation and Revenue Department (TRD) |
| Portal | https://tap.state.nm.us |
| SST member | No |
| Skill version | 2.0 |

**CRITICAL: NM GRT taxes virtually ALL services and most transactions. One of the broadest tax bases in the US (similar to Hawaii GET). Tax is on the seller, not the buyer.**

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | Deductible from gross receipts |
| Prepared food | TAXABLE |  |
| ALL services (including professional) | TAXABLE | NM taxes virtually all services |
| SaaS | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Healthcare services | DEDUCTIBLE | Specific healthcare deductions available |
| Manufacturing equipment | DEDUCTIBLE | Deduction from gross receipts |
| Prescription drugs | EXEMPT |  |
| Resale | DEDUCTIBLE |  |

## Section 10 -- Prohibitions

- **Prohibition -- terminology** — NEVER call NM's tax a "sales tax" without noting it is a GRT on the seller.
- **Prohibition -- services exemption assumption** — NEVER assume services are exempt -- NM taxes virtually ALL services.
- **Prohibition -- deduction vs exemption** — NEVER confuse "deduction" with "exemption" -- NM uses deductions from gross receipts.
- **Prohibition -- computation** — NEVER compute any number.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nm-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nm-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
