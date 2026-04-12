---
name: arkansas-sales-tax
description: Use this skill whenever asked about Arkansas sales and use tax. Trigger on phrases like "Arkansas sales tax", "AR sales tax", "DFA", "A.C.A. §26-52", "Arkansas grocery tax", "Arkansas SST". ALWAYS load us-sales-tax first.
version: 2.0
---

# Arkansas Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Arkansas |
| State rate | 6.50% |
| Grocery food state rate | 0.125% (reduced; local rates still apply at full rate) |
| Maximum combined rate | ~11.625% |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Arkansas Dept. of Finance and Administration |
| Portal | https://atap.arkansas.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 6.50% | |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | 0.125% state + full local | Reduced, not exempt |
| Prepared food | TAXABLE 6.50% | |
| SaaS | NOT TAXABLE | Not clearly taxed |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER say grocery food is exempt -- it is taxed at 0.125% state plus full local.
- NEVER forget SST certificates are accepted.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
