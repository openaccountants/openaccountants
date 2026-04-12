---
name: colorado-sales-tax
description: Use this skill whenever asked about Colorado sales and use tax, home-rule cities, CDOR filings. Trigger on phrases like "Colorado sales tax", "CO sales tax", "CDOR", "home-rule city Colorado", "retail delivery fee". ALWAYS load us-sales-tax first.
version: 2.0
---

# Colorado Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Colorado |
| State rate | 2.90% (lowest in the US) |
| Maximum combined rate | ~11.2% (with home-rule city taxes) |
| Sourcing | Destination-based (state); home-rule cities may differ |
| Economic nexus | $100,000 in retail sales |
| Tax authority | Colorado Department of Revenue (CDOR) |
| Portal | https://www.colorado.gov/revenueonline |
| SST member | Yes (associate) |
| Home-rule cities | ~70+ self-administer their own sales tax |
| Skill version | 2.0 |

**CRITICAL: ~70+ home-rule cities self-administer with different rates, rules, and exemptions. Denver, Aurora, Colorado Springs, Boulder are all home-rule.**

## Section 3 -- Transaction pattern library

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE 2.9% + local | |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | EXEMPT from state | Local may still tax food |
| Prepared food | TAXABLE | |
| SaaS | NOT TAXABLE | |
| Canned software (download) | TAXABLE | |
| Professional services | NOT TAXABLE | |
| Manufacturing equipment | EXEMPT | |
| Prescription drugs | EXEMPT | |
| OTC drugs | EXEMPT | |
| Resale | EXEMPT | |

## Section 10 -- Prohibitions

- NEVER ignore home-rule cities -- ~70+ cities self-administer with different rules.
- NEVER treat SaaS as taxable in Colorado.
- NEVER forget grocery food is exempt from STATE tax but local may still apply.
- NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.
