---
name: li-company-formation
description: >
  Prepare a 2026 Liechtenstein entity-formation workpaper under the Persons and
  Companies Act (PGR), centred on the GmbH, with the AG, Anstalt and foundation
  capital rules. Covers minimum capital (GmbH CHF 10,000, AG CHF 50,000, Anstalt
  CHF 30,000 (CHF 50,000 if in shares), foundation CHF 30,000, or the same amounts in EUR or USD), payment and
  contributions in kind, the standard and simplified GmbH formation routes,
  registration with the Office of Justice, qualified management and
  disqualification rules, size classes (micro, small, medium, large), statutory
  audit or review and the micro-company review waiver, filing annual accounts
  within 12 months, and the link to the CHF 1,800 minimum tax. Trigger on:
  Liechtenstein company formation, GmbH gründen Liechtenstein, AG Liechtenstein,
  Handelsregister, Mindestkapital. Out of scope: trusts, full foundation law,
  regulated licences, registry fees and incorporation timetables.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
version: 0.3
---

# Liechtenstein company formation and entity screening v0.3

## Scope and first decision

This skill prepares the 2026 GmbH formation route and flags the capital rules of other legal forms (AG, Anstalt, foundation; trusts are out of scope). It follows the [PGR consolidated 1 September 2026][law] and the [Office of Justice GmbH fact sheet dated July 2025][factsheet]. Companies are entered in the commercial register (Handelsregister) kept by the Office of Justice (Amt für Justiz) and acquire legal personality on registration. Every formed legal entity then enters the tax system: test the CHF 1,800 minimum tax and its exception in [li-corporate-income-tax](li-corporate-income-tax.md).

Retain business/purpose and regulated-activity facts, founders/beneficiaries, ownership/control, intended country of work and management, capital currency and funding, registered office/service address, governance, licensing, expected accounts/size and beneficial-owner evidence. Tax residence and trade/sector permission are separate determinations; registration alone does not settle them.

## Capital is not a fee or tax

| Form/screen | Statutory minimum in selected nominal currency | Source and limitation |
|---|---|---|
| GmbH | CHF 10,000, or EUR 10,000, or USD 10,000 | PGR article 122; each member's contribution rules in article 391 |
| AG, or an Anstalt or other legal entity whose capital is divided into shares | CHF 50,000, or EUR 50,000, or USD 50,000 | Article 122; AG formation/payment rules remain separately applicable |
| Anstalt or other legal entity whose capital is not divided into shares | CHF 30,000, or EUR 30,000, or USD 30,000 | Article 122; determine actual legal form before applying |
| Foundation | CHF 30,000, or EUR 30,000, or USD 30,000 | PGR article 552 section 13; no full foundation method supplied |

These are statutory nominal-currency alternatives, not amounts translated at a current exchange rate. Article 122(2) requires the statutory minimum capital/assets to be fully contributed. It does **not** mean every AG's entire higher subscribed capital must always be paid in full: article 284 separately addresses full subscription and at least 25% on each share, with any higher statutory/articles requirement and the overall minimum retained. Contributions in kind require their own evidence/procedure. The AG arithmetic below is only a funding screen. [PGR, articles 122 and 284][law]

For GmbH members, article 391 requires at least CHF 50 per member contribution, its stated multiples/quotas, and full payment or contribution in kind at formation. The fact sheet identifies expert valuation for in-kind contributions and capital at the company's free disposal on registration. These matters are not proved by a bank-balance total alone. [PGR, article 391][law]; [fact sheet, sections 7–8][factsheet]

## Ordinary GmbH preparation method

1. Decide the actual form/purpose and applicable regulated/trade permissions. An asset-holding purpose is not automatically an ordinary commercial business or a PVS tax classification.
2. Choose the normal publicly authenticated articles or the article 390(5) simplified route. The latter requires at most three shareholders, one manager, the authority model and no departures from the law; shareholder signatures still require authentication. It is not a universal online/self-service exemption from formalities. [PGR, article 390][law]
3. Reconcile articles, owners/contributions, manager/representation powers, seat, financial year and other required particulars. Article 394 addresses the register application and supporting information. The GmbH acquires legal personality through registration, not when the owners merely sign a draft. [PGR, articles 390 and 394][law]
4. Assess qualified-management and disqualification rules. Article 180a has a qualified-member rule with express exceptions; article 180b has exclusions. The fact sheet distinguishes ordinary/trade-supervised cases and noncommercial GmbHs. Do not replace these with a blanket “one local resident director” statement. Representation/service-address duties are separate from tax actual management. [PGR, article 180a][law]; [fact sheet, section 3][factsheet]
5. Obtain contribution evidence, required valuation/authentication, signed corporate/organ documents and current authority forms; reconcile the intended register particulars to all documents. Preserve the actual registration decision and register extract. This skill does not establish present portal acceptance, registry fees, beneficial-owner filing particulars or a guaranteed duration.
6. Start separate tax, VAT, payroll/insurance and accounts workstreams using the topic skills. The corporate minimum-tax exception and source/management facts must be tested, rather than assuming every formed entity owes the same minimum tax.

### Management evidence is not a residence shortcut

PGR 180a(1)–(2) specifies the qualified management/representation member and licence/equivalence routes;180a(3)–(4) contains express supervised/trade/association exceptions, including the stated foundation caveat. Keep the actual qualification/licence or exemption evidence. Article 180b separately bars the specified incapable/convicted representatives, including corresponding EEA exclusions, requires a no-exclusion declaration at registration and addresses later resignation/removal of representation. Its specified conviction exclusion lasts five years from the final judgment. A postal address alone proves none of these conditions. [PGR 180a–180b][law]

## Accounts, review and disclosure

PGR article 1064 provides the size criteria and separate first-application/two-period rules. Article 1058a allows the stated commercial micro-companies to waive a review, with exclusions, a unanimous decision, signed declaration/supporting evidence and continuing rights to demand a review. It is not an automatic exemption because one year's turnover is small. Audit/review, the choice of reviewer and an accounting-period change need their own current classification. [PGR, articles 1058a and 1064][law]

### Ordinary size and assurance workpaper

For the article 1063 entities, establish the exact legal form, financial year, accounting currency and any special article 1057/public-interest/disclosure regime before the ordinary tests below. The current Swiss-franc thresholds in PGR 1064 are:

| Size class | Balance sheet | Net turnover | Average employees | Test |
|---|---:|---:|---:|---|
| Micro | CHF 580,000 | CHF 1,160,000 | 10 | At least two of three not exceeded |
| Small | CHF 9.2 million | CHF 18.5 million | 50 | At least two of three not exceeded |
| Medium | CHF 32.4 million | CHF 64.8 million | 250 | At least two small limits exceeded and at least two medium limits not exceeded |
| Large | Above the medium class under the statutory test | As specified | As specified | At least two medium limits exceeded |

These are current PGR 1064(1)–(3) figures, with the monetary amendments first applicable to financial years beginning on/after 1 January 2024, as specified in the consolidation's notes 1952–1959. Equality is “not exceeded”; it is not a requirement that all three limits be met. Article 1064(4) ordinarily requires the conditions at two consecutive balance-sheet dates, with its first-application rule at the first balance-sheet date. Keep the two-year record or the actual first-application basis. Article 1064(5) requires prescribed thresholds for non-CHF accounts, not an invented exchange-rate conversion. [PGR 1063–1064 and application notes][law]

Article 1058 distinguishes statutory audit from review. Under the ordinary route, a small company outside the stated special-disclosure exception has a review rather than an automatic audit exemption with no assurance. A qualifying **commercial micro-company** can waive that review only through1058a's actual procedure; segmented entities and bearer-share AGs are excluded. Obtain the unanimous governing-body decision, signed management declaration and minutes/current supporting accounts, retain the filing/registration, and adjust the articles where necessary. Members can demand a review later, and the authority can require renewed evidence. Do not infer a waiver from size alone or describe an unsigned intention as a registered waiver. This is an assurance screen, not a full consolidated-accounts/sustainability method. [PGR 1058–1058a][law]

Under article 1122(1), the covered company's approved annual accounts and required report must be filed with the Office of Justice **before expiry of the twelfth month after the balance-sheet date**, subject to an actual granted extension and the provision's scope. A valid review waiver affects the required report, not the underlying disclosure obligation. Tax filing and corporate approvals have separate clocks. Article 1122(6) requires electronic submission of the paragraph 1 documents. Preserve the actual electronic receipt and extension decision; a review waiver does not cancel accounts filing. The fact sheet corroborates the GmbH reporting route; it is not a complete annual-accounts or sustainability skill. [PGR, article 1122][law]; [fact sheet, sections 10–11][factsheet]

Registry fees, late-filing penalties and business-permission procedures are not covered here; take them from the Office of Justice for the case.

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

Establish purpose/licensing, actual founders/beneficiaries/control, intended residence/management, capital currency and contributions, governance/service address, representation and accounts/size. Refer trusts, foundations, Anstalt control/benefits, segmented entities, noncash contributions, foreign owners/management, regulated activities, disqualification, review waivers and all disputed formation/tax cases.

## Sources

| Source | URL | Read on |
|---|---|---|
| Personen- und Gesellschaftsrecht (PGR), LR 216.0, consolidated 1 September 2026, articles 122, 180a-180b, 261, 284, 390-391, 394, 552 section 13, 1057-1058a, 1063-1064, 1122 | https://www.gesetze.li/konso/pdf/1926004000 | 2026-10-30 |
| Amt für Justiz, fact sheet on the GmbH (July 2025) | https://www.llv.li/serviceportal2/amtsstellen/amt-fuer-justiz/handelsregister/merkblaetter/007_merkblatt_zur_gmbh.pdf | 2026-10-30 |
| Amt für Justiz, registering a GmbH | https://www.llv.li/de/privatpersonen/beruf-und-arbeitsplatz/handelsregister/eintragungen/gesellschaft-mit-beschraenkter-haftung | 2026-10-30 |

Not yet confirmed: registry fees; incorporation timetable; late-filing penalties for annual accounts; trusts and the full foundation regime; thresholds for accounts in a currency other than CHF; beneficial-owner filing particulars.

[law]: https://www.gesetze.li/konso/pdf/1926004000
[factsheet]: https://www.llv.li/serviceportal2/amtsstellen/amt-fuer-justiz/handelsregister/merkblaetter/007_merkblatt_zur_gmbh.pdf
[registration]: https://www.llv.li/de/privatpersonen/beruf-und-arbeitsplatz/handelsregister/eintragungen/gesellschaft-mit-beschraenkter-haftung

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
