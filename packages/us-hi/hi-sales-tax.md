---
name: hi-sales-tax
description: Use this skill whenever asked about Hawaii General Excise Tax (GET). Trigger on phrases like "Hawaii GET", "General Excise Tax", "HI sales tax", "HRS §237". Hawaii has a GET on the SELLER, not a traditional sales tax. ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-HI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# HI Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Hawaii |
| Tax type | General Excise Tax (GET) -- NOT a traditional sales tax; tax on SELLER's gross income |
| Retail GET rate | 4.00% (4.50% on Oahu with county surcharge) |
| Wholesale rate | 0.50% |
| Services rate | 4.00% (4.50% Oahu) |
| Insurance commissions | 0.15% |
| Effective rate when passed to buyer | ~4.166% (to cover GET on the pass-through) |
| Tax base | Virtually ALL business activity including services, rentals, commissions |
| Sourcing | Destination-based |
| Economic nexus | $100,000 in gross proceeds or gross income |
| Tax authority | Hawaii Department of Taxation (DoTax) |
| Portal | https://tax.hawaii.gov |
| SST member | No |
| Skill version | 2.0 |

- **GET imposed on seller, applies broadly, and pyramids** — CRITICAL: GET is imposed on the SELLER, not the buyer. GET applies to virtually ALL transactions including services. GET pyramids (cascades) at every supply chain level.

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 4% (4.5% Oahu) | Retail rate |
| Clothing | TAXABLE | No exemption |
| Grocery food | TAXABLE | No food exemption -- GET applies to all |
| Prepared food | TAXABLE |  |
| ALL services (including professional) | TAXABLE | Hawaii taxes virtually ALL services |
| SaaS | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Wholesale sales | TAXABLE at 0.50% | Lower wholesale rate |
| Prescription drugs | EXEMPT |  |
| Manufacturing equipment | No specific exemption | GET applies broadly |
| Resale | 0.50% wholesale rate | Not fully exempt; taxed at wholesale rate |

## Section 5 -- Classification rules

### GET pyramiding

- **GET pyramiding across supply chain** — GET cascades at every level. Manufacturer pays 0.5% on wholesale sales. Wholesaler pays 0.5%. Retailer pays 4%. If passed to buyer, the pass-through amount is additional gross income subject to GET again.

### Tax on virtually everything

- **Broad tax base including professional services** — Hawaii has one of the broadest tax bases in the US. Legal, accounting, medical, consulting -- all subject to GET at 4%.

## Section 10 -- Prohibitions

- **Prohibition 1** — NEVER call Hawaii's tax a "sales tax" -- it is a General Excise Tax on the seller's gross income.
- **Prohibition 2** — NEVER assume food is exempt -- Hawaii taxes grocery food under GET.
- **Prohibition 3** — NEVER assume services are exempt -- Hawaii taxes virtually ALL services.
- **Prohibition 4** — NEVER forget the pyramiding effect -- GET cascades through the supply chain.
- **Prohibition 5** — NEVER forget the Oahu county surcharge (0.50% additional).
- **Never compute numbers** — NEVER compute any number.

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
