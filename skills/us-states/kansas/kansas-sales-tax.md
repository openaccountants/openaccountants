---
name: kansas-sales-tax
description: Use this skill whenever asked about Kansas sales and use tax. Trigger on phrases like "Kansas sales tax", "KS sales tax", "KDOR", "K.S.A. §79-3603", "Kansas grocery tax". ALWAYS load us-sales-tax first.
version: 2.0
---

# Kansas Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Kansas |
| State rate | 6.50% |
| Grocery food state rate | 0.00% (effective January 1, 2025 -- phased down from 6.5%) |
| Maximum combined rate | ~11.50% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross receipts |
| Tax authority | Kansas Department of Revenue (KDOR) |
| Portal | https://www.kdor.ks.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.50% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | 0% state (as of Jan 2025) | Local rates still apply; phased down from 6.5% |
| Prepared food | TAXABLE 6.50% | |
| SaaS | NOT TAXABLE | Kansas has not clearly taxed SaaS |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER apply state tax to grocery food as of 2025 -- state rate is 0%. Local still applies.
- NEVER forget the phase-down history of grocery food taxation.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
