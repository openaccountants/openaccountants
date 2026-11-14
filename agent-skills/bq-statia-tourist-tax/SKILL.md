---
name: bq-statia-tourist-tax
description: "Analyse 2026 Sint Eustatius tourist tax for accommodation providers, vessel operators and non-resident visitors. Use to distinguish paid land stays from vessel stays, identify the taxpayer and exemptions, calculate the statutory bases, and establish return and payment periods. Includes the current official ordinance, metadata, national enabling law and fictional component calculations. Preserves the separate ABB test and distinguishes filing extensions from automatic holiday adjustments. This source-cited draft holds actual forms, bundled-price allocation, disputed stay classification and unresolved operational cases. Load with the universal workflow base; professional review remains required before reliance."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bq-statia-tourist-tax"
  jurisdiction: "BQ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sint Eustatius: tourist tax in 2026

> **Built from the law. Not yet approved.** Written by Ryan Duguid and imported from his fork; conformed to the OpenAccountants standard by Claude. Not reviewed by an accountant. All outputs must be reviewed by a qualified tax professional before filing or payment. Tax year 2026. Currency: US dollars (USD).

## Scope

Establish the island, visitor's resident status, accommodation or vessel,
provider, dates, price and exemption before calculating tax. This ordinance
concerns Sint Eustatius. Do not use its rates or deadlines for Bonaire or Saba.
FinBES supplies the power to levy; the island ordinance supplies this charge.
[TOURISM]; [FIN, articles 40–41 and 53][FIN]

Load `workflow-base` and the applicable domain and BES companions. Preserve
source gates, confirmed profile, refusals, four universal outputs and all
domain outputs/checks. This Tier 2 reference supplies conditional components,
not a complete return, operational engagement or country pack. Unknown
mandatory conditions hold the complete financial output package.

## Ask the client first

1. **Is the stay on Sint Eustatius**: this ordinance does not apply on Bonaire or Saba.
2. **Land or water**: paid accommodation on land, or visitors on a vessel (with or without an overnight stay).
3. **Is the visitor a non-resident**, and does any exemption apply (homestay registration, short vessel stays under four hours, boats up to four metres)?
4. **The amount charged for the stay**, separated from breakfast and other additional services.
5. **Who is the provider or vessel operator** and which return period applies.

## The method, step by step

### Current instrument, taxpayer and chargeable stay

The official register records the Verordening toeristenbelasting Sint
Eustatius 2021 as current from 17 December 2020, with one version and source
AB 2020, no. 56. Article 12 separately starts the levy on **1 January 2021**
and repeals the 2019 ordinance for later events while saving earlier events.
Distinguish legal commencement, commencement of charging and the event date.
An older search result bearing 2013 or 2019 is not the current tariff.
[TOURISM, article 12][TOURISM]; [META]

Article 2 taxes stays by non-residents of the public body:

- **Land branch:** an overnight stay for monetary consideration.
- **Water branch:** a stay aboard a vessel for whose presence in the public
  body's waters port tax is paid. Establish this condition and the vessel
  classification rather than treating every arriving passenger as taxable.

The provider of the opportunity to stay is normally the taxpayer, with a
right to recover the tax from the visitor. Article 3 identifies the
self-operating property owner, property operator and specified vessel
captain/commander, manager or user. If no provider can be identified, the
visitor is the fallback taxpayer. Recovery through an invoice does not
automatically make the guest the primary filer. [TOURISM, articles 1–3][TOURISM]

The explanatory note says the non-resident category is not limited to leisure
tourists and discusses monetary consideration for time-share stays. A
business trip or unusual payment structure therefore needs classification,
not an assumed exemption. A resident owner's own stay is not automatically
a paid non-resident overnight stay. Actual resident status, consideration
and any mixed property/operator arrangements remain fact-dependent. [TOURISM]

### Exemptions and separate bases

| Branch | Article 4 exemptions to establish | Source of the figure |
|---|---|---|
| Land | Specified visiting aircraft crew; the visitor also staying aboard a vessel for which water tourist tax is due; or a dwelling registered with the named tourism foundation as a homestay. | https://lokaleregelgeving.overheid.nl/CVDR743003/1 |
| Water | Stay shorter than four hours; specified care vessels; canoes, rowing boats and tenders; motor/sailing boats no longer than four metres; or a vessel present under government order. | https://lokaleregelgeving.overheid.nl/CVDR743003/1 |

[TOURISM]

A homestay is not just a booking-platform label: article 1 describes a home
with no more than five guest rooms, registration, interaction with the
resident and access to shared living space. Establish the actual statutory
category and registration. No exemption is inferred solely from being a
small property, day visitor or non-profit operator. [TOURISM]

Article 4(2)(a)'s operative wording is **shorter than four hours**. A stay
of exactly four hours does not satisfy that particular exemption. The
explanatory note's looser phrase about a stay up to four hours does not
change the operative threshold. Other exemptions and the underlying charge
must still be checked. [TOURISM]

| Branch | Base and tariff under articles 5–6 | Source of the figure |
|---|---|---|
| Land | **7%** of the amount charged for the stay, excluding taxes and charges for additional services. | https://lokaleregelgeving.overheid.nl/CVDR743003/1 |
| Water with overnight stay | **USD 3 per person per etmaal**, including a part of an etmaal. | https://lokaleregelgeving.overheid.nl/CVDR743003/1 |
| Water without overnight stay | **USD 2 per person per etmaal**, including a part of an etmaal. | https://lokaleregelgeving.overheid.nl/CVDR743003/1 |

[TOURISM]; [MONEY, articles 1–2][MONEY]

Article 1 defines an **etmaal** as a continuous 24-hour period beginning
at **21:00**, or part of it. It is not automatically a midnight-to-midnight
calendar day or each completed 24 hours after arrival. Establish the
actual counted units and overnight status. A month in the land-tax period
rule is a calendar month under article 7; do not replace it with the
ordinance's separately defined 30-etmaal term. [TOURISM]

The land base excludes additional services, with breakfast given as an
example in the note. Allocate a bundled room/meal/other-service price using
established facts and a supportable method; do not invent a universal
allocation percentage or deduct every business cost. Actual all-inclusive,
refund, cancellation, time-share valuation and fractional-cent cases remain
held pending their complete method. [TOURISM]

## Worked cases

### Fictional tax components

These cases stipulate non-resident visitors, the relevant taxable branch,
established USD amounts or counted units, the required vessel/port-tax
conditions and no other exemption except where stated. They do not establish
a live registration, final return or an ABB result. [TOURISM]

| Stipulated facts | Component result |
|---|---|
| Paid overnight accommodation charge 1,000; separately established breakfast/additional services 150 | Land base 1,000; tax 70. The separately identified 150 is excluded. |
| Four taxable vessel visitors, each with two established etmalen and overnight stays | 4 × 2 × 3 = 24 water tax. |
| Three taxable vessel visitors, one established etmaal each without an overnight stay | 3 × 1 × 2 = 6 water tax. |
| Vessel stay of three hours, otherwise within the charge | Exempt under the shorter-than-four-hours condition. |
| Vessel stay of exactly four hours | The short-stay exemption fails; determine all other conditions and the actual units before calculating tax. |
| Qualifying motor/sailing boat exactly four metres long | The no-longer-than-four-metres exemption applies. |
| A qualifying homestay registration and all other category conditions are stipulated | The land exemption applies; an ABB exemption is not thereby established. |

### Recomputed cases

**Case 1, paid land stay.** A guest pays USD 1,000 for the room and USD 150 for separately identified breakfast. The base is USD 1,000 and the tax at 7% is USD 70.

```oa-check
name: Sint Eustatius land tourist tax (2026)
inputs:
  room_charge: 1000
  extras: 150
steps:
  - tax: room_charge * 0.07
  - wrong_if_extras_included: (room_charge + extras) * 0.07
expected:
  tax: 70
  wrong_if_extras_included: 80.50
```

**Case 2, a decision for a vessel: overnight or day visitors?** Four visitors each staying two etmalen with overnight stays pay 4 x 2 x USD 3 = USD 24. Three day visitors for one etmaal without an overnight stay pay 3 x 1 x USD 2 = USD 6.

```oa-check
name: Sint Eustatius water tourist tax, overnight and day (2026)
inputs:
  overnight_visitors: 4
  overnight_etmalen: 2
  day_visitors: 3
steps:
  - overnight_tax: overnight_visitors * overnight_etmalen * 3
  - day_tax: day_visitors * 1 * 2
expected:
  overnight_tax: 24
  day_tax: 6
```

## When to refuse or refer

| Code | Situation | Action |
|---|---|---|
| R-BQ-TOUR-ISLAND | Tourist tax on Bonaire or Saba | Refer: a separate island ordinance applies; this skill covers Sint Eustatius only |
| R-BQ-TOUR-BUNDLE | Bundled price where the stay cannot be separated from other services | Refer: allocation is not settled here |
| R-BQ-TOUR-ABB | ABB on the same accommodation | Refer to `bq-abb`; the tourist tax result does not settle ABB |

## Filing and payment

### Filing, payment and ABB

Land tax uses a calendar-month period. Water tax uses the vessel's continuous
period in the public body's waters, with notification at the start of the
stay. Article 9 makes water tax due at the start. Article 8 uses payment on
return and requires an issued return to be delivered within **fifteen days
after the land period ends**, or **six hours after the water stay begins**.
The named assessing officer may shorten the stated filing term. Keep the
actual notice, issued return and any shorter term. [TOURISM, articles 7–9][TOURISM]

Article 10 requires land payment within **fifteen days after the period**.
Water payment is due within **six hours after the stay begins or before
departure to sea, if earlier**. A short visit can therefore have a payment
deadline earlier than the ordinary six-hour filing limit. An authorised
filing extension extends the specified payment term by the same duration.
No extension is inferred merely from a request. [TOURISM]

Article 10(4) excludes the Algemene termijnenwet from these **payment**
terms. The note explains that a weekend or public holiday does not move
them automatically to the next working day. Do not silently extend that
statement to every filing or objection term. Article 11 excludes remission
in collection. Other procedure, records, penalties and remedies require
FinBES's adaptations and the applicable general law; use `bq-tax-compliance`
with that local-law check. [TOURISM]; [FIN, articles 67, 74–75][FIN]

Belastingwet BES article 6.11(1)(m) conditionally exempts hotel-room and
apartment rentals from ABB when the specified island tourist tax is due on
those services under an ordinance, subject to implementing conditions and
limits. A tourist-tax exemption does not prove this condition. Nor does
charging a tourist-tax line prove the actual service qualifies. Apply
`bq-abb` separately; do not automatically charge both taxes or infer that
all accommodation and additional services are ABB-exempt. Actual exemption
eligibility and implementing/form mapping remain held. [B1]

Keep separate stay-price, excluded-service, visitor/unit, exemption and tax
schedules; reconcile tax recovered, tax payable, returns and payments.
The responsible practitioner retains identities, registrations, tax numbers
and bank details outside the agent. No booking, licensing, filing, payment
or private-document submission is authorised by this reference.

## Completion checklist

### Verification and limits

Check current instrument/event date; actual resident status; land versus
water; provider versus fallback visitor; port-tax condition; each exemption;
strict four-hour versus inclusive four-metre boundaries; established etmalen;
additional services; distinct filing/payment clocks; authorised extensions;
and the conditional ABB interaction. Preserve all workflow outputs, holds
and professional review.

Read on 17 October 2026: the complete current ordinance, articles 1–13 and
explanatory note; its complete metadata; FinBES articles 40–41, 53, 67 and
74–75; and Belastingwet BES article 6.11. The note has an apparent copied
waste-charge heading and describes charging commencement as commencement;
the operative provisions and metadata remain distinct. The original AB PDF,
actual forms, registration evidence, port-tax instruments, bundled-price
methods and live operational cases were not reviewed. No complete island
tax pack, engagement workbook or practitioner sign-off is claimed.

## Sources

| Source | URL | Read on |
|---|---|---|
| TOURISM. Read for the provisions this skill cites as [TOURISM]. | https://lokaleregelgeving.overheid.nl/CVDR743003/1 | 2026-10-17 |
| META. Read for the provisions this skill cites as [META]. | https://lokaleregelgeving.overheid.nl/CVDR743003?show-wti=true | 2026-10-17 |
| FIN. Read for the provisions this skill cites as [FIN]. | https://wetten.overheid.nl/BWBR0028151/2023-01-01 | 2026-10-17 |
| B1. Read for the provisions this skill cites as [B1]. | https://wetten.overheid.nl/BWBR0029244/2026-04-11 | 2026-10-17 |
| MONEY. Read for the provisions this skill cites as [MONEY]. | https://wetten.overheid.nl/BWBR0028551/2012-07-01 | 2026-10-17 |

[TOURISM]: https://lokaleregelgeving.overheid.nl/CVDR743003/1
[META]: https://lokaleregelgeving.overheid.nl/CVDR743003?show-wti=true
[FIN]: https://wetten.overheid.nl/BWBR0028151/2023-01-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[MONEY]: https://wetten.overheid.nl/BWBR0028551/2012-07-01

Not yet confirmed: the return and payment forms; allocation of a bundled price; disputed classification of stays; holiday adjustments to due dates. Sources were read by Ryan Duguid on 2026-10-17 and not re-opened on import.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bq-statia-tourist-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bq-statia-tourist-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
