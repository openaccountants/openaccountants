---
name: ag-medical-benefits
description: Prepare separate Medical Benefits Scheme calculations for ordinary employees, age categories and low earnings without importing social-security ceilings.
version: 0.1
jurisdiction: AG
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Antigua and Barbuda Medical Benefits Scheme contributions

**Source-cited draft; independent review pending.** Sources accessed 22 October 2026. This Guide covers the stated topic only, not comprehensive country coverage.

## Separate contribution schedule

The MBS publishes these categories:

| Category | Employee | Employer |
|---|---:|---:|
| Employed, over 16 and under 60 | 3.5% of wages | 3.5% of wages |
| Employed, 60 to under 70 | 2.5% | 0% |
| Employed, 70 or over | 0% | 0% |
| Employed, under EC$400 monthly or EC$100 weekly | 0% | 7% |

Self-employed rates are 5% from age 16 to under 60, 2.5% from 60 to under 70, and zero from 70. [MBS contribution-rate table](https://www.mbs.gov.ag/v2/contribution-rates/).

The published table does not resolve priority where the age and low-earnings categories overlap. It also says “over 16” for employees but “aged 16” for self-employment. **Exact age-16 employee treatment and overlapping categories remain unverified.** Do not encode an assumed answer. The table does not establish that the social-security earnings ceiling also applies to MBS.

## Bounded worked examples

Assume verified MBS wages, age 35 and no exemption:

- Monthly EC$4,000: employee **EC$140**, employer **EC$140**, total **EC$280**.
- Monthly EC$350: employee **EC$0**, employer **EC$24.50** under the published low-earnings category.
- Weekly EC$90: employee **EC$0**, employer **EC$6.30** under the weekly category.

For an employee aged 62 with monthly wages of EC$4,000, the published age category gives employee **EC$100**, employer **EC$0**. These examples avoid the unresolved category intersections. They are not a complete net-pay calculation.

## Working-paper preparation

Record date of birth, employment classification, pay frequency, actual wages, wage-component evidence and any exemption document. Keep separate columns for social security and MBS. Reconcile each scheme to its own return and payment; a combined payroll deduction total is not sufficient evidence that both agencies were paid.

MBS's Business Account Services page identifies **R3A** submissions and contribution-payment channels. Use the current agency form and retain payment allocation evidence. [MBS Business Account Services](https://www.mbs.gov.ag/v2/services/business-account-services/).

## Release gaps

The operative legislation for the rate table, wage definition, exceptions, contribution ceiling or absence of one, deadlines, penalties and birthday-period treatment remains to be reconciled. The undated agency table supports these limited category calculations, not a claim that every 2026 payroll condition has been checked. No deadline from social security has been copied to this scheme.

## Review output

Retain the calculation, source versions and factual classification. A qualified local reviewer must check current amendments and the actual case before anyone files, pays or relies on the result. No professional attestation is claimed.

> Contributed by Ryan Duguid.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
