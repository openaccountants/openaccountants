---
name: north-dakota-sales-tax
description: Use this skill whenever asked about North Dakota sales and use tax. Trigger on phrases like "North Dakota sales tax", "ND sales tax", "NDCC §57-39.2", "ND SST". ALWAYS load us-sales-tax first.
version: 2.0
---

# North Dakota Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | North Dakota |
| State rate | 5.00% |
| Local rate range | 0% -- 3.50% (city) |
| Maximum combined rate | ~8.50% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross sales |
| Tax authority | North Dakota Office of State Tax Commissioner |
| Portal | https://www.tax.nd.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 5% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | TAXABLE | ND taxes SaaS and specified digital products |
| Canned software | TAXABLE | |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER treat SaaS as nontaxable in North Dakota.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
