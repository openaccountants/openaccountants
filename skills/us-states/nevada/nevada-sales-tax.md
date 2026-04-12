---
name: nevada-sales-tax
description: Use this skill whenever asked about Nevada sales and use tax. Trigger on phrases like "Nevada sales tax", "NV sales tax", "NRS 372". ALWAYS load us-sales-tax first.
version: 2.0
---

# Nevada Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Nevada |
| State rate | 6.85% |
| Local rate range | 0% -- ~1.525% |
| Maximum combined rate | ~8.375% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Nevada Department of Taxation |
| Portal | https://tax.nv.gov |
| SST member | Yes -- Full Member |
| No state income tax | Correct |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.85% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | Nevada has not enacted SaaS taxation |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER treat SaaS as taxable in Nevada.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
