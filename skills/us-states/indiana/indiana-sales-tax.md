---
name: indiana-sales-tax
description: Use this skill whenever asked about Indiana sales and use tax. Trigger on phrases like "Indiana sales tax", "IN sales tax", "IC 6-2.5", "Indiana DOR". Indiana has one of the SIMPLEST structures -- 7% flat with no local sales taxes. ALWAYS load us-sales-tax first.
version: 2.0
---

# Indiana Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Indiana |
| State rate | 7.00% (flat -- no local sales tax) |
| Local taxes | None |
| Maximum combined rate | 7.00% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Indiana Department of Revenue |
| Portal | https://intime.dor.in.gov |
| SST member | Yes (full member) |
| Skill version | 2.0 |

**One of the simplest sales tax states -- 7% flat rate statewide, no local add-ons.**

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 7% | Uniform statewide |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | Indiana does not tax SaaS |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | IC 6-2.5-5-3 |
| Prescription drugs | EXEMPT | |
| OTC drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER add local tax -- Indiana has no local sales taxes.
- NEVER treat SaaS as taxable in Indiana.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
