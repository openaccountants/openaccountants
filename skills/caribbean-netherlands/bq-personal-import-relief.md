---
name: bq-personal-import-relief
description: >
  Analyse 2026 BES import relief for moving households, inherited personal
  goods, students, low-value post, private gifts and travellers' baggage.
  Use to select the relevant permission, person, goods, value, age, quantity
  and time conditions before computing import taxes. Separates duty, ABB and
  excise, normal residence from income-tax residence, and oral declarations
  from exemptions. Includes primary legislation, authority guidance and
  fictional boundary cases. This source-cited draft holds actual valuation,
  classifications, disputed eligibility, forms and other relief regimes.
  Load with the universal workflow base and BES companions; professional
  review remains required before reliance.
jurisdiction: BQ
category: international
tax_year: 2026
tax_year_notes: "Selected personal-import relief checked on 17 October 2026; actual event, island, goods and operative conditions required"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
  - bq-tax-system
  - bq-customs-clearance
  - bq-customs-valuation
  - bq-customs-debt-remedies
  - bq-excise
---

# Bonaire, Sint Eustatius and Saba: personal-import relief

Identify the importing island, person, goods, purpose, route, relevant
residence, event dates, value basis, quantities and permissions. An import
duty nil rate, oral declaration or customs permission does not independently
establish an ABB/excise exemption. Use `bq-customs-valuation`, `bq-abb` and
`bq-excise` for the separate charges and `bq-customs-clearance` for procedure.

Load `workflow-base` and applicable domain/BES references. Preserve source
gates, confirmed profile, refusals, four universal outputs and all domain
outputs/checks. This Tier 2 reference covers selected personal-import
reliefs. Unknown mandatory conditions hold the complete financial output
package; no country pack or complete engagement is certified.

## Legal route, territory and permission

B1 article 6.20(1)(b) delegates ABB relief for imports entitled to duty
relief. Regulation 3.15 applies chapter-III duty exemptions correspondingly,
with its express exceptions. Regulation 3.14 instead lists the provisions
applying to excise, including 3.32–3.38 and 3.41–3.47; its list does **not**
include the student provisions 3.39–3.40. Do not infer excise relief merely
because an ABB/duty branch applies. Excise's island/goods scope remains
separate in `bq-excise`. [B1]; [RULES]

Regulation 3.15(1)(a) describes an exclusion from ABB relief where goods exported from an
island's free circulation are re-imported into that same island after the
specified zero-rated export treatment. Distilled spirits imported by
travellers under eighteen have the separate 3.14/3.15 exclusion. The other
motor-vehicle, fish and packaging exceptions in 3.15 concern their named
branches, rather than a general override of every personal exemption.
[RULES]

Its numerical export pointer needs verification: regulation 3.15(1)(a)
still names B1 6.10(2)(c), while the current Act places its specified
producer/export/HDE goods zero-rate branch in (d) and uses (c) for the
specified cars/vans without CO2 emissions. Tax regulation 6.6(1) also retains the (c)
goods pointer. Hold actual same-island re-import/zero-rate application
until the mapping is verified; do not silently rewrite either rule.
Use `bq-warehouses-hde` for the related source comparison. [B1]; [RULES]; [TAX-RULES]

DAB 3.25 defines personal goods by personal/household use and defines
foreign territory for this title as everything outside the importing
public body. Its passenger-vehicle definition excludes sport/hobby vehicles
and has its own public-road and non-business conditions. Establish those
definitions; a vehicle's marketing name or the shared BQ catalogue label
does not settle its relief or tax classification. [DAB]

Article 3.26's normal residence generally uses at least 183 days per
calendar year with personal/professional ties. It has specific rules for
separated ties and fixed-duration assignments; studying abroad does not
alone move normal residence. Proof and requested supplements are required.
This is the customs-title test, not a replacement for `bq-income-tax`'s
tax residence or an entity's place of establishment. [DAB]

Under 3.27, a permit is required unless expressly excepted. Obtain it before
the import declaration or relevant preceding export, subject to the stated
on-declaration route. A timely electronic/written request, necessary proof
and reasoned written decision matter. Report later facts affecting the
permit and identify the goods on request. A refusal of a permit-free relief
can be put in writing on request. Articles 3.28–3.31 add identity, goods
accounts/security, permitted changes/destruction, withdrawal and compliance
conditions. A permit application alone does not establish relief. [DAB]

## Moving a household

Article 3.32 concerns natural persons transferring normal residence to a
BES island. Ordinary personal goods must have been possessed for at least
six months before the former normal residence was given up and, for
non-consumables, used there. They must be intended for the same purpose in
the new normal residence. Supply a signed goods list and declare within
six months after establishing normal residence on the island. Partial
shipments must fit that term. [DAB]; [G-MOVE]

Passenger vehicles have a different condition: demonstrable uninterrupted
possession **and use for at least one year before embarkation in the origin
country**, with relief limited to one passenger vehicle per family/household.
The inspector may require security. Article 3.33 allows specified special-case
departures from the import/vehicle time conditions; retain the actual grant.
Do not apply the ordinary six-month possession rule to a car. [DAB]

Article 3.32(6) excludes alcohol/tobacco beyond normal household stock and
transport means other than qualifying passenger vehicles. The public page
uses broader wording for tobacco and describes moving from outside BES;
the statutory title defines foreign territory per importing public body.
Use the statutory definitions and obtain case-specific confirmation for
inter-island moves and disputed stock/vehicle categories rather than
silently resolving those differences from the summary page. [DAB]; [G-MOVE]

Under 3.35, within twelve months **from acceptance of the import declaration**,
the relieved personal goods cannot be lent, pledged, hired or transferred
for consideration or free of charge without prior inspector permission.
This clock does not start from the move, vessel departure or a later sale.
Use `bq-customs-debt-remedies` for failed conditions and evidence/remedy
controls. [DAB]

## Inherited goods and students

Article 3.36 covers personal goods inherited by a natural person normally
resident on the islands, and goods inherited **by testament** by an
island-established non-profit entity. Alcohol, tobacco and business vehicles
are excluded. The required evidence includes a declaration by a notary or
comparable export-country official proving inheritance, a signed list and
import declaration within one year after the goods were placed in the
beneficiary's possession. The clock is not simply the date of death.
Partial shipments fit the term; special circumstances can support an
inspector-granted extension under 3.37. Article 3.38's permitted generic
description does not cover motor vehicles. [DAB]

This goods-import relief is separate from succession/gift taxation and
foreign inheritance connections in `bq-inheritance-gifts`. It does not
establish relief for a purchased item or prove an overseas estate's tax.

Article 3.39 covers specified pupils/students moving to an island to study
and those moving there after completing study abroad. Its enrolment test
requires a regular university student or the stated full-time higher or
secondary vocational education. Covered goods are used normal student-room
furnishings, linen/clothing new or used, and normal study equipment.
Provide enrolment proof and a signed list; article 3.35's restrictions
apply correspondingly. The permit/goods conditions remain necessary and
the excise list does not automatically adopt this student branch.
[DAB]; [RULES]

## Post and unpaid private gifts

| Branch | Value and substantive conditions |
|---|---|
| Negligible-value post, 3.41–3.42 | Direct letter-post or postal-package consignments to a person on an island, total goods value no more than **USD 28**. Alcohol and tobacco are excluded. No relief permit is required. Do not turn the postal route into a general exemption for every courier or commercial shipment. |
| Private-to-private gift, 3.43–3.44 | Occasional consignment containing only personal goods, sent without any payment by the recipient, total value no more than **USD 70**, including the listed alcohol/tobacco value. No relief permit is required. A purchase, reimbursement or routine commercial supply does not meet the unpaid/occasional conditions merely because the sender writes “gift”. |

[DAB]

The authority's gift guidance includes freight/postage in the USD 70 value
and discusses post/courier gifts. Reconcile the applicable value basis,
goods identity and carriage evidence with `bq-customs-valuation`; a genuine
gift is not automatically a zero-value transaction. Do not assume the
USD 28 postal test excludes transport costs or that every charge on a
courier invoice is government tax. Actual disputed value/method is held.
[G-GIFT]; [DAB]

Article 3.43's gift quantities are separate from traveller allowances:

- Tobacco: 50 cigarettes **or** 25 cigarillos of at most 3 grams each **or**
  10 cigars **or** 50 grams smoking tobacco, or a proportional assortment.
- Alcohol: one litre of the specified over-22%-volume spirits/alcohol
  group **or** one litre of the specified at-most-22%/sparkling/fortified
  group, or a proportional assortment; separately two litres still wine.

The total USD 70 condition still includes those goods. A quantity limit
does not independently exempt a higher-value consignment; the gift rule
does not create the traveller's separate beer allowance. [DAB]

## Travellers' baggage

Articles 3.45–3.47 require occasional personal goods in baggage presented
on arrival, or later presented baggage registered as accompanying baggage
with the transport provider at departure. They do not exempt commercial
goods. New-looking, special or expensive goods have 3.45(5)'s proof
condition concerning prior export from free circulation. Test new foreign
acquisitions separately under 3.46 below. [DAB]

For foreign-acquired goods other than the specified alcohol/tobacco group,
3.46 gives a total **USD 500 per traveller**, reduced to **USD 150 for those
under fifteen**. If the total exceeds the limit, only whole goods fitting
within the available allowance can qualify; the value of an individual
good cannot be split. Do not deduct USD 500 from every expensive item or
pool portions of travellers' allowances to split one item. [DAB]; [G-TRAVEL]

| Article 3.45(2) group | Traveller quantity, subject to all conditions |
|---|---|
| Tobacco alternatives | 200 cigarettes, 50 cigarillos of at most 3 grams, 25 cigars, or 125 grams smoking tobacco; alternatively a proportional assortment. These are alternatives, not cumulative full allowances. |
| Spirits/other specified alcohol alternatives | One litre of the specified over-22%-volume spirits/alcohol group, or one litre of the specified at-most-22%/sparkling/fortified group, or a proportional assortment. |
| Additional specified drinks | Two litres still wine and eight litres beer. |

[DAB]

International-transport crew receive **half** those alcohol/tobacco
quantities. DAB 3.45(4) excludes alcohol/tobacco for travellers under
seventeen; the ABB/excise rules separately exclude distilled spirits for
travellers under eighteen. Keep those ages and tax branches distinct.
The authority confirms tobacco from seventeen and the stated distilled
drink group from eighteen. An exemption does not establish compliance with
other import, health or restricted-goods law. [DAB]; [RULES]; [G-TRAVEL]

No relief permit is required under 3.47 and the import declaration may be
oral. That does not turn the separate oral-declaration form threshold in
`bq-customs-clearance` into a tax allowance. Preserve declaration and
inspection obligations where the relief conditions are not met. [DAB]

## Fictional boundary checks

These cases stipulate verified legal value bases, ordinary qualifying
goods, route and remaining conditions unless a missing condition is the
point being tested. They determine components, not an actual tax bill:

| Stipulated facts | Component result |
|---|---|
| Eligible postal consignment at 28 versus 28.01 | 28 meets the inclusive value ceiling; 28.01 fails that branch's value condition. Goods exclusions and route still matter. |
| Unpaid occasional private gift at 70 versus 70.01, including relevant carriage | 70 meets that ceiling; 70.01 does not. Do not infer a partial USD 70 allowance. |
| “Gift” label on a paid purchase | The label does not establish 3.43's no-payment condition. |
| Traveller age fourteen versus fifteen | The former uses the under-fifteen USD 150 ceiling; the latter is not in that age restriction. All other conditions remain necessary. |
| One foreign-acquired indivisible camera worth 520 | No USD 500 portion of that item is relieved under 3.46. Determine tax on the applicable complete base separately. |
| Separate eligible items at 300 and 250 for an adult traveller | Do not treat only the arithmetic excess of 50 as outside relief. One cannot split the 250 item to fill the remaining 200 after selecting the 300 item. |
| 100 cigarettes plus 25 cigarillos in an eligible adult traveller's baggage | Each uses half its alternative tobacco allowance: **100 ÷ 200 + 25 ÷ 50 = 1**. This tests the proportional quantity component, not age, value, health or other eligibility. |
| Eligible international crew member | The cigarette quantity component is **200 ÷ 2 = 100**; do not apply the full passenger quantity. Other product groups retain their own half limits. |
| Seventeen-year-old carrying distilled spirits | Do not apply ABB/excise traveller relief; their separate under-eighteen exclusion applies. |
| Household vehicle possessed/used only six months before embarkation | The ordinary goods rule does not satisfy the vehicle's one-year condition. No departure is inferred without a grant. |
| Two otherwise qualifying passenger vehicles for one household | The one-per-household limit is not multiplied by the number of adult movers. |
| Inherited goods received later than the death date | Establish the possession event for 3.36's one-year declaration term; do not start it from death alone. |
| Student goods with no enrolment proof | Hold the student route; do not infer the required institution/course or excise relief. |

## Verification and limits

Check charge and relief branch, importing island, normal residence,
person/use, age, value method, indivisible items, quantity alternatives,
actual event dates, permit/exception and later-disposal conditions. Retain
sanitised evidence references, source differences, Needs Input/holds,
all workflow outputs and professional-review questions. The practitioner
keeps identities, authorities, tax identifiers and bank details outside
the agent.

Read on 17 October 2026: DAB 3.25–3.47, customs regulation 3.14–3.15,
B1 6.20 and all three authority pages below. Earlier clearance, value,
excise and debt sources remain with their respective companions. The
public moving summary's territory/tobacco wording is not silently
substituted for the statutory text.

Actual disputed value/carriage/classification, inter-island moving,
special household stock, permit conditions, restricted goods, temporary
visitor imports, business/institutional/diplomatic relief, external form
annexes, live code/portal cases and tax computations are not completed.
No PDF/OCR, private taxpayer records, identity/tax identifier or bank
submission, application, import declaration, payment, engagement workbook
or practitioner sign-off was used. No comprehensive-area credit is claimed.

[DAB]: https://wetten.overheid.nl/BWBR0029236/2025-01-01
[RULES]: https://wetten.overheid.nl/BWBR0029309/2025-01-01
[B1]: https://wetten.overheid.nl/BWBR0029244/2026-04-11
[TAX-RULES]: https://wetten.overheid.nl/BWBR0029332/2025-01-01
[G-TRAVEL]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-particulieren/reizigersbagage/reizigersvrijstelling
[G-MOVE]: https://www.belastingdienst-cn.nl/onderwerpen/douanezaken-particulieren/verhuizen/verhuizen-naar-caribisch-nederland
[G-GIFT]: https://www.belastingdienst-cn.nl/onderwerpen/belastingzaken-particulieren/abb-algemene-bestedingsbelasting-particulieren/familielid-kennis-heeft-goederen-toegezonden

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
