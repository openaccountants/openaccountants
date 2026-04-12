---
name: nebraska-sales-tax
description: Use this skill whenever asked about Nebraska sales and use tax. Trigger on phrases like "Nebraska sales tax", "NE sales tax", "R.R.S. Neb. §77-2701", "Nebraska SST". ALWAYS load us-sales-tax first.
version: 2.0
---

# Nebraska Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
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

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 5.50% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | TAXABLE | Nebraska taxes SaaS and digital products |
| Canned software | TAXABLE | |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER treat SaaS as nontaxable in Nebraska.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
