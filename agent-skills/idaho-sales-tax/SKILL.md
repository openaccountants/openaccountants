---
name: idaho-sales-tax
description: "Use this skill whenever asked about Idaho sales and use tax. Trigger on phrases like \"Idaho sales tax\", \"ID sales tax\", \"Idaho Code §63-3619\", \"Idaho SST\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/idaho-sales-tax"
  jurisdiction: "US-ID"
  tax_year: "2025"
  last_updated: "2026-07-13"
---

# Idaho Sales Tax

## Section 1 -- Quick reference

**Section 1 -- Quick reference**

| Field | Value |
| --- | --- |
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

**Section 3 -- Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6% |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE | Idaho has not enacted SaaS taxation |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT | Production exemption |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Resort city taxes** — NEVER forget resort city taxes (Sun Valley, McCall up to 3% additional).
- **SaaS taxability** — NEVER treat SaaS as taxable in Idaho.
- **No computation** — NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `idaho-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/idaho-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
