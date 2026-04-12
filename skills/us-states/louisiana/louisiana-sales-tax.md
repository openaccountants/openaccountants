---
name: louisiana-sales-tax
description: Use this skill whenever asked about Louisiana sales and use tax. Trigger on phrases like "Louisiana sales tax", "LA sales tax", "R.S. 47:301", "parish sales tax", "Sales Tax Commission". CRITICAL -- among highest combined rates in the US (~11.45%). ALWAYS load us-sales-tax first.
version: 2.0
---

# Louisiana Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Louisiana |
| State rate | 4.45% |
| Local rate range | 0% -- 7% (parish + city) |
| Maximum combined rate | ~11.45% (among highest in US) |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| State authority | Louisiana Department of Revenue (LDR) |
| Remote seller portal | Louisiana Sales Tax Commission -- https://www.lstc.la.gov |
| State portal | https://revenue.louisiana.gov |
| SST member | No |
| Parish self-administration | Parishes administer their own local taxes (similar to AL) |
| Skill version | 2.0 |

**CRITICAL: Louisiana parishes self-administer local sales taxes. The Louisiana Sales Tax Commission handles remote seller compliance centrally.**

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 4.45% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | EXEMPT from state | Some parishes may still tax food |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | Louisiana has not clearly taxed SaaS |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER ignore parish-level self-administration -- local compliance is separate from state.
- NEVER forget Louisiana has among the highest combined rates in the US.
- NEVER treat SaaS as clearly taxable in Louisiana.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
