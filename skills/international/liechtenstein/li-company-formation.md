---
name: li-company-formation
description: >
  Prepare a 2026 Liechtenstein entity-formation workpaper, centred on an ordinary
  GmbH and selected AG, establishment and foundation capital distinctions. Use for
  statutory capital, permitted nominal currency, contributions, standard versus
  simplified GmbH formation, register evidence and the separate accounting/review
  workstream. It corrects the earlier approximate GmbH capital range and blanket
  capital-payment claim. Establish purpose, owners, management, licensing and
  reporting duties before choosing a form. This draft does not supply an authority
  fee quote, incorporation timetable, universal resident-director rule, full trust or
  foundation method, every audit exemption or approved filing. Named local legal
  and accountant review remain separate requirements.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
version: 0.2
---

# Liechtenstein company formation and entity screening v0.2

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

## Scope and first decision

This source-cited 2026 draft prepares the ordinary GmbH route and flags selected other legal forms. The [PGR consolidated 1 September 2026][law] and [Office of Justice GmbH fact sheet dated July 2025][factsheet] replace the earlier secondary-source approximations. They do not establish a fixed incorporation time, all-in cost, tax exemption or suitability for a particular owner.

Retain business/purpose and regulated-activity facts, founders/beneficiaries, ownership/control, intended country of work and management, capital currency and funding, registered office/service address, governance, licensing, expected accounts/size and beneficial-owner evidence. Tax residence and trade/sector permission are separate determinations; registration alone does not settle them.

## Capital is not a fee or tax

| Form/screen | Statutory minimum in selected nominal currency | Source and limitation |
|---|---|---|
| GmbH | CHF 10,000, or EUR 10,000, or USD 10,000 | PGR article 122; each member's contribution rules in article 391 |
| AG / stated share-divided entity rule | CHF 50,000, or EUR 50,000, or USD 50,000 | Article 122; AG formation/payment rules remain separately applicable |
| Stated non-share-divided entity rule | CHF 30,000, or EUR 30,000, or USD 30,000 | Article 122; determine actual legal form before applying |
| Foundation | CHF 30,000, or EUR 30,000, or USD 30,000 | PGR article 552 section 13; no full foundation method supplied |

These are statutory nominal-currency alternatives, not amounts translated at a current exchange rate. Article 122(2) requires the statutory minimum capital/assets to be fully contributed. It does **not** mean every AG's entire higher subscribed capital must always be paid in full: article 284 separately addresses full subscription and at least 25% on each share, with any higher statutory/articles requirement and the overall minimum retained. Contributions in kind require their own evidence/procedure. The AG arithmetic below is only a funding screen. [PGR, articles 122 and 284][law]

For GmbH members, article 391 requires at least CHF 50 per member contribution, its stated multiples/quotas, and full payment or contribution in kind at formation. The fact sheet identifies expert valuation for in-kind contributions and capital at the company's free disposal on registration. These matters are not proved by a bank-balance total alone. [PGR, article 391][law]; [fact sheet, sections 7–8][factsheet]

## Ordinary GmbH preparation method

1. Decide the actual form/purpose and applicable regulated/trade permissions. An asset-holding purpose is not automatically an ordinary commercial business or a PVS tax classification.
2. Choose the normal publicly authenticated articles or the article 390(5) simplified route. The latter requires at most three shareholders, one manager, the authority model and no departures from the law; shareholder signatures still require authentication. It is not a universal online/self-service exemption from formalities. [PGR, article 390][law]
3. Reconcile articles, owners/contributions, manager/representation powers, seat, financial year and other required particulars. Article 394 addresses the register application and supporting information. The GmbH acquires legal personality through registration, not when the owners merely sign a draft. [PGR, articles 390 and 394][law]
4. Assess qualified-management and disqualification rules. Article 180a has a qualified-member rule with express exceptions; article 180b has exclusions. The fact sheet distinguishes ordinary/trade-supervised cases and noncommercial GmbHs. Do not replace these with a blanket “one local resident director” statement. Representation/service-address duties are separate from tax actual management. [PGR, article 180a][law]; [fact sheet, section 3][factsheet]
5. Obtain contribution evidence, required valuation/authentication, signed corporate/organ documents and current authority forms; reconcile the intended register particulars to all documents. Preserve the actual registration decision and register extract. This draft does not establish present portal acceptance, registry fees, beneficial-owner filing particulars or a guaranteed duration.
6. Start separate tax, VAT, payroll/insurance and accounts workstreams using the topic Guides. The corporate minimum-tax exception and source/management facts must be tested, rather than assuming every formed entity owes the same minimum tax.

## Accounts, review and disclosure

PGR article 1064 provides the size criteria and separate first-application/two-period rules. Article 1058a allows the stated commercial micro-companies to waive a review, with exclusions, a unanimous decision, signed declaration/supporting evidence and continuing rights to demand a review. It is not an automatic exemption because one year's turnover is small. Audit/review, the choice of reviewer and an accounting-period change need their own current classification. [PGR, articles 1058a and 1064][law]

Under article 1122(1), the covered company's approved annual accounts and required report must be filed with the Office of Justice **before expiry of the twelfth month after the balance-sheet date**, subject to an actual granted extension and the provision's scope. A valid review waiver affects the required report, not the underlying disclosure obligation. Tax filing and corporate approvals have separate clocks. The fact sheet corroborates the GmbH reporting route; it is not a complete annual-accounts or sustainability Guide. [PGR, article 1122][law]; [fact sheet, sections 10–11][factsheet]

No current authority fee tariff, late-filing penalty amount, full filing form, every board/supervision exception or business-permission procedure has been established by this draft. Preserve any notice and obtain the applicable procedure before filing or quoting an outcome.

## Worked controls

### Three-founder GmbH capital reconciliation

Assume the chosen CHF minimum and three proposed fully paid cash contributions CHF 4,000, CHF 3,000 and CHF 3,000. They total CHF 10,000 and leave no shortfall against the statutory capital screen. This does not establish simplified-route eligibility, authenticated documents, licensing, costs or registration.

```oa-check
name: Liechtenstein assumed GmbH contribution total
inputs:
  first_contribution: 4000
  second_contribution: 3000
  third_contribution: 3000
  statutory_chf_minimum: 10000
steps:
  total_capital: first_contribution + second_contribution + third_contribution
  capital_shortfall: max(0, statutory_chf_minimum - total_capital)
expected:
  total_capital: 10000
  capital_shortfall: 0
```

### AG minimum versus subscribed amount

Assume CHF 100,000 subscribed share capital, uniform contributions, no higher articles requirement, ordinary article 284 conditions and the CHF 50,000 minimum. A 25% amount would be CHF 25,000, so the overall statutory minimum requires at least CHF 50,000. This leaves CHF 50,000 unpaid subscribed capital in this assumed screen, not a conclusion that an actual filing satisfies every share/contribution requirement.

```oa-check
name: Liechtenstein assumed AG contribution and statutory minimum
inputs:
  assumed_subscribed_capital: 100000
  ordinary_per_share_fraction: 0.25
  statutory_chf_minimum: 50000
steps:
  assumed_fractional_payment: assumed_subscribed_capital * ordinary_per_share_fraction
  required_funding_screen: max(assumed_fractional_payment, statutory_chf_minimum)
  assumed_unpaid_subscribed_amount: assumed_subscribed_capital - required_funding_screen
expected:
  assumed_fractional_payment: 25000
  required_funding_screen: 50000
  assumed_unpaid_subscribed_amount: 50000
```

## Ask and refer

Establish purpose/licensing, actual founders/beneficiaries/control, intended residence/management, capital currency and contributions, governance/service address, representation and accounts/size. Refer trusts, foundations, Anstalt control/benefits, segmented entities, noncash contributions, foreign owners/management, regulated activities, disqualification, review waivers and all disputed formation/tax cases. Full formation/annual-reporting scope and named local professional review remain open. This secondary topic does not make any core tax domain complete.

## Sources

Read 24 October 2026:

- [Current PGR, 1 September 2026 consolidation][law], selected articles 122, 180a, 261, 284, 390–391, 394, 552 section 13, 1058a, 1064 and 1122. Whole PDF retrieval is not whole PGR verification.
- [Office of Justice GmbH fact sheet, July 2025][factsheet], selected organisation, capital and reporting provisions compared with the current PGR.
- [Official GmbH registration page][registration], current models/forms entry point; no live application was exercised.

[law]: https://www.gesetze.li/konso/pdf/1926004000
[factsheet]: https://www.llv.li/serviceportal2/amtsstellen/amt-fuer-justiz/handelsregister/merkblaetter/007_merkblatt_zur_gmbh.pdf
[registration]: https://www.llv.li/de/privatpersonen/beruf-und-arbeitsplatz/handelsregister/eintragungen/gesellschaft-mit-beschraenkter-haftung

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
