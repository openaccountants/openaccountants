---
name: mississippi-sales-tax
description: Use this skill whenever asked about Mississippi sales and use tax. Trigger on phrases like "Mississippi sales tax", "MS sales tax", "Miss. Code §27-65". ALWAYS load us-sales-tax first.
version: 2.0
---

# Mississippi Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Mississippi |
| State rate | 7.00% |
| Local taxes | Very limited (up to 0.25% in some areas) |
| Maximum combined rate | ~7.25% |
| Sourcing | Origin-based |
| Economic nexus | $250,000 in sales |
| Tax authority | Mississippi Department of Revenue |
| Portal | https://www.dor.ms.gov |
| SST member | No |
| Skill version | 2.0 |

**Mississippi taxes MOST services broadly and taxes grocery food at a reduced rate.**

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 7% | |
| Clothing | TAXABLE | No exemption |
| Grocery food | TAXABLE at 5% | Reduced rate (not exempt) |
| Prepared food | TAXABLE 7% | |
| SaaS | NOT TAXABLE | Not clearly taxed |
| Canned software | TAXABLE | |
| Most services | TAXABLE | Mississippi taxes services broadly |
| Professional services | Varies | Many professional services taxable |
| Manufacturing equipment | REDUCED RATE | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER say grocery food is exempt -- Mississippi taxes it at 5%.
- NEVER assume services are exempt -- Mississippi taxes most services.
- NEVER forget origin-based sourcing.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
