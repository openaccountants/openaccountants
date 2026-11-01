---
name: ye-company-formation-and-renewal
description: >
  Yemen limited-liability company formation and renewal research draft scoped to the Sana'a ministry's published service requirements. Covers documents, capital conditions and renewal evidence with two conditional examples. Current nationwide legal requirements, foreign ownership and full reporting obligations remain unresolved.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://moit.gov.ye/commercial-companies-Limit"
    title: "Sana'a ministry: limited-liability company formation service"
    as_of: "2026-10-22"
  - url: "https://moit.gov.ye/node/209"
    title: "Sana'a ministry: limited-liability company renewal service"
    as_of: "2026-10-22"
  - url: "https://www.yemen-nic.info/db/laws_ye/detail.php?ID=11607"
    title: "Law 15/1999 amending Companies Law article 245"
    as_of: "2026-10-22"
---

# Yemen: limited-liability company formation and renewal

## Scope

This Guide records the published service requirements of the ministry headquartered in Sana'a. It does not establish nationwide application, an Aden procedure, foreign-investment permission or a complete Companies Law consolidation. The 2026 metadata records research, not legal certification. Confirm the responsible registry and permitted activity before preparing an application.

## Formation application

The ministry service requires an accepted reserved name, an application by a partner/legal representative, signed authenticated constitutional documents conforming to ministry templates, **2–30 adult partners**, and capital of **YER2 million for one activity plus YER1 million per additional activity**. Minimum unit value is **YER5,000**; cash capital must be deposited fully with an approved bank after authentication.

Collect identity documents, bank evidence, management and accountant appointment minutes, the accountant's practising licence, authorisations, and a corporate partner's registration and participation resolution. [Ministry formation requirements](https://moit.gov.ye/commercial-companies-Limit).

The fetched 1999 amendment to article 245(b)–(c) requires the founders' licence application with the formation contract and draft articles. Signatures are authenticated before the controller, a person authorised in writing, the provincial ministry director or the competent court. This historical amendment alone does not establish today's complete law. [Law 15/1999](https://www.yemen-nic.info/db/laws_ye/detail.php?ID=11607).

## Renewal and financial reporting evidence

The renewal service requires a ministry-approved company account, formation/amendment authorisation, registered name and commercial registration. The general meeting must approve the latest completed year's accounts, with minutes authenticated by the ministry representative assigned to attend.

Its document list includes the latest constitutional documents and relevant extraordinary-meeting minutes, commercial registration with latest renewal, partner/manager identities, latest ordinary-meeting approval of financial statements and profit/loss account, renewed tax and zakat cards, chamber membership and the contract with the licensed accountant. [Ministry renewal requirements](https://moit.gov.ye/node/209).

The page does not establish a complete statutory annual filing calendar or audit thresholds. This Guide does not convert the service's documentary requirements into a claim that all reporting duties have been discharged. Obtain the entity's actual licence, financial year and filing notices before setting deadlines. No processing-time promise or fee estimate is made.

## Example 1: one activity

Assume the ministry's stated conditions apply. YER2 million capital divided into YER5,000 units yields 400 units. This establishes arithmetic only, not registration acceptance.

```oa-check
name: Yemen one activity capital units
inputs:
  capital: 2000000
  unit_value: 5000
steps:
  - units: capital / unit_value
expected:
  units: 400
```

## Example 2: three activities

Under the same assumption, three activities require YER4 million: YER2 million plus two additions of YER1 million. At YER5,000 per unit, that is 800 units. Activity approval remains separate.

```oa-check
name: Yemen additional activity capital
inputs:
  initial_capital: 2000000
  additional_activities: 2
  increment: 1000000
  unit_value: 5000
steps:
  - required_capital: initial_capital + additional_activities * increment
  - units: required_capital / unit_value
expected:
  required_capital: 4000000
  units: 800
```

## Intake and unresolved requirements

Collect proposed activities, operating location, partner identities/nationalities, ownership chain, legal representatives, proposed management and financing. Reconcile these against the competent registry's current requirements. No application or account has been created by this research.

Outstanding work includes the complete amended Companies Law, current capital instrument, foreign ownership and sector restrictions, beneficial-ownership reporting, non-cash contributions, statutory accounts/audit and filing deadlines, licence renewal periods, fees, sanctions, liquidation and territorial differences. The full original Companies Law page timed out during this pass; no unexamined provision is treated as verified. This is initial formation/renewal coverage only.

## Sources

- [Ministry formation service](https://moit.gov.ye/commercial-companies-Limit).
- [Ministry renewal service](https://moit.gov.ye/node/209).
- [Law 15/1999, article 245 amendment](https://www.yemen-nic.info/db/laws_ye/detail.php?ID=11607).

## Disclaimer

Source-cited research draft. Verify the applicable administration, law and entity facts before submission. No professional attestation.
