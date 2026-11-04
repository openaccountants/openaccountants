---
name: ne-sales-tax
description: Use this skill whenever asked about Nebraska sales and use tax. Trigger on phrases like "Nebraska sales tax", "NE sales tax", "R.R.S. Neb. §77-2701", "Nebraska SST". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-NE
tax_year: 2025
last_updated: 2026-07-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# NE Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Nebraska |
| State rate | 5.50% |
| Local rate | Up to 2.00% (city) |
| Maximum combined rate | ~7.50% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Nebraska Department of Revenue |
| Portal | https://revenue.nebraska.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 5.50% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | TAXABLE | Nebraska taxes SaaS and digital products |
| Canned software | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Never treat SaaS as nontaxable** — NEVER treat SaaS as nontaxable in Nebraska.
- **Never compute any number** — NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
