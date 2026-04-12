---
name: idaho-sales-tax
description: Use this skill whenever asked about Idaho sales and use tax. Trigger on phrases like "Idaho sales tax", "ID sales tax", "Idaho Code §63-3619", "Idaho SST". ALWAYS load us-sales-tax first.
version: 2.0
---

# Idaho Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Idaho |
| State rate | 6.00% |
| Local taxes | Resort city taxes up to 3% |
| Maximum combined rate | ~9.00% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in sales |
| Tax authority | Idaho State Tax Commission |
| Portal | https://tax.idaho.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | Idaho has not enacted SaaS taxation |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | Production exemption |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER forget resort city taxes (Sun Valley, McCall up to 3% additional).
- NEVER treat SaaS as taxable in Idaho.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
