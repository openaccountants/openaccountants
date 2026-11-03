---
name: co-sales-tax
description: Use this skill whenever asked about Colorado sales and use tax, home-rule cities, CDOR filings. Trigger on phrases like "Colorado sales tax", "CO sales tax", "CDOR", "home-rule city Colorado", "retail delivery fee". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-CO
tax_year: 2025
last_updated: 2026-07-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# CO Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
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

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 2.9% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | EXEMPT from state | Local may still tax food |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE |  |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Home-rule cities prohibition** — NEVER ignore home-rule cities -- ~70+ cities self-administer with different rules.  _(Section 10 -- Prohibitions)_
- **SaaS taxability prohibition** — NEVER treat SaaS as taxable in Colorado.  _(Section 10 -- Prohibitions)_
- **Grocery food state exemption prohibition** — NEVER forget grocery food is exempt from STATE tax but local may still apply.  _(Section 10 -- Prohibitions)_
- **No computation prohibition** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
