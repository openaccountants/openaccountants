---
name: north-carolina-sales-tax
description: Use this skill whenever asked about North Carolina sales and use tax. Trigger on phrases like "North Carolina sales tax", "NC sales tax", "N.C.G.S. 105-164", "NC DOR". ALWAYS load us-sales-tax first.
version: 2.0
---

# North Carolina Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | North Carolina |
| State rate | 4.75% |
| Local rate range | 2.00% -- 2.75% |
| Maximum combined rate | 7.50% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | North Carolina Department of Revenue (NCDOR) |
| Portal | https://www.ncdor.gov |
| SST member | Yes (full member) |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 4.75% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT from state | Local 2% applies |
| Prepared food | TAXABLE at full rate | |
| SaaS | NOT TAXABLE | NC has not enacted clear SaaS taxation |
| Canned software (download) | TAXABLE | |
| Digital goods | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | Refund program |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER say grocery food is fully exempt -- state tax exempt but local 2% applies.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
