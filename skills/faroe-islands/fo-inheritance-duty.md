---
name: fo-inheritance-duty
description: >
  Calculate Faroese inheritance and succession duty for 2026 estates,
  legacies, death benefits, inheritance advances and retained-use gifts.
  Classifies the recipient's relationship, applies the whole-share rate
  table, aggregates receipts from the same deceased and distinguishes
  estate-wide exemptions from individual allowances. Covers net-benefit
  valuation, undivided estates, usufructs, cross-border assets and payment
  liability. Supplies the actual probate inventory fields, original-paper
  submission route, assessment, filing and payment clocks, late interest
  and penalties. Trigger on Faroe Islands inheritance tax, arvaavgjald,
  succession duty, inherited property, life insurance on death and an
  inheritance declaration. Estate income tax and the deceased's final
  income-tax assessment use the separate estate-tax Guide.
jurisdiction: FO
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-31
version: 0.2
---

# Faroe Islands inheritance and succession duty v0.2

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this Guide for a dutiable inheritance, legacy or death gift, including
specified succession to family settlements and income rights. Inheritance
advances and advances to descendants that reduce their eventual inheritance
are included; duty on those advances ordinarily arises on the giver's death,
not automatically when the advance was paid. Ordinary inheritance and the
specified death-linked acquisitions become chargeable at death; settlement
succession and a missing person's estate follow the distinct succession or
judgment triggers. [Order 468/1921 §§4, 10][duty]

Include insurance and other death-contract proceeds funded by the deceased,
less consideration actually reimbursed by the recipient. The Act excludes
contracts made to fulfil a legal or administrative obligation. Insurance
for a surviving spouse is chargeable only where its aggregate amount,
capitalising annuities under §20, exceeds DKK 3,000. A gift with income or use
retained for life, or for an unexpired term at death, and a disposition to
avoid this duty are also within §5. A payment outside probate is not thereby
outside duty. Obtain the policy and beneficiary details. [Order §5][duty];
[court, insurance section][court]

An undivided estate retained by a surviving spouse has no duty on the assets
remaining undivided. At eventual division use the then-taking heirs and
their relationship to the spouses. Earlier settlements with first-deceased
heirs, legacies and §§4–5 dispositions are brought into account. If other
estate erosion exceeds half its original wealth, §14 also brings relevant
gifts/advances back, capped at half the original estate; its special
calculation permits rounding the estate and those advances down to DKK 100.
This is a deferral with add-back rules, not an unlimited gift exemption.
[Order §14][duty]

## Rates, bands and thresholds

First establish the recipient's class. **A:** spouse, descendants and adopted
children. **B:** parents and their descendants, excluding A. **C:** grandparents
and their descendants, excluding A/B. **D:** everyone more remote or unrelated.
A separated spouse uses actual kinship under §6. Community-property spouses,
reciprocal wills and testamentary appointment powers require the relationship
rules in §7, rather than an assumed single relationship. [Order §§2, 6–7][duty]

The selected percentage applies to the **whole individual aggregated share**,
not just the excess in that band. Round the chargeable share down to a multiple
of DKK 50 under §3; retain its unrounded amount and check the court's rate
classification, especially at a boundary. [Order §§2–3, 21][duty]

| Aggregated share in DKK | Class A | Class B | Class C | Class D | Official source |
|---|---:|---:|---:|---:|---|
| Up to 1,000 | 1% | 4% | 7% | 10% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 1,000 to 2,000 | 1.25% | 4.25% | 7.25% | 10.25% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 2,000 to 3,000 | 1.5% | 4.5% | 7.5% | 10.5% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 3,000 to 5,000 | 1.75% | 4.75% | 7.75% | 10.75% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 5,000 to 10,000 | 2% | 5% | 8% | 11% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 10,000 to 20,000 | 2.25% | 5.25% | 8.25% | 11.25% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 20,000 to 50,000 | 2.5% | 5.5% | 8.5% | 11.5% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 50,000 to 100,000 | 2.75% | 5.75% | 8.75% | 11.75% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |
| Over 100,000 | 3% | 6% | 9% | 12% | [Order §2](https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa) |

State bodies, churches, municipalities, associations, companies, institutions,
foundations and endowment funds pay a flat 10%, except the specified §4(c) family
settlements, which use the kinship rules. A public-benefit purpose is not an
automatic zero rate: §3 permits an approved reduction to 4%, and specified
public-interest objects or consumed advances can receive discretionary
exemption. A family preference beyond two generations prevents the stated
charitable classification. Keep the actual approval. [Order §§2–3, 6][duty]

There is no duty if the **whole net estate is below DKK 200**. The spouse and
children under 18 are exempt where the **part of the estate falling in
inheritance does not exceed DKK 500**; that is not a DKK 500 deduction from
every heir's share. These two exemptions do not cover §4(e)/§5 acquisitions.
A recipient who lived in the deceased's home or was demonstrably financially
dependent for the preceding five years uses class A for a share up to
DKK 2,000. Prove both the period and amount. [Order §3][duty]

## The base

1. List everything the same person receives from the same deceased, including
   prior dutiable advances and legacies. Compute duty on the combined share,
   then deduct inheritance duty already paid on those earlier acquisitions.
   The specified community-property spouses count as one giver/one receipt
   unless the testamentary separate-property exception applies. An excess
   liability above an heir's current distribution is that heir's personal
   debt, not a burden on the other heirs. [Order §21][duty]
2. Start with the actual net benefit. Deduct genuine debts, burdens and
   acquisition expenses. If only specified assets/a limited fund are liable,
   deduct only obligations burdening or arising from acquiring those assets.
   A purported debt to the deceased's spouse, children, or the children's
   descendants or spouses without an actual loan or other performance is not
   deductible; include it in that payee's inheritance or legacy instead.
   This inheritance duty itself is not deductible. Foreign inheritance duty can reduce the
   base where it has not instead been relieved under §9. [Order §16][duty]
3. Value at the public estate's final accounting date or, for private
   administration, the inheritance declaration date. Earlier completed
   advances use receipt-date value, advance distributions their distribution
   date, and income rights their commencement conditions. Keep these
   inheritance-duty values distinct from the death-date D03 inventory and
   income-tax carrying values. [Order §17][duty]; [D03 pp 2–6][opening]
4. Use market value. Real property uses local open-market value unless a
   special valuation is obtained; Copenhagen-quoted securities use their
   quotation, other securities face value unless their actual value differs;
   irrecoverable receivables are excluded; ships and chattels use sale value.
   The specified perpetual property rights use 25 times net annual value,
   ascertainable disposal consideration or the redeemable amount, as §18
   directs. Document the valuation, not the insurance sum. [Order §18][duty]
5. For a bequest stated free of duty, apply §21's express method: calculate
   ordinary duty on the named bequest, add that duty to the bequest, then
   calculate the payable duty on that enlarged amount. Do not substitute an
   algebraic infinite gross-up. [Order §21][duty]
6. A full income/use right for someone other than the eventual capital heir
   initially bears duty on its capitalised value; capital duty waits until
   that right ends. A partial income obligation creates the separate
   income-right and net-capital computations in §15(2). Later succession and
   an income-holder who ultimately takes the capital have the additional
   charge/credit rules in §15. Ownership powers and family settlements are
   classified under §19. [Order §§15, 19][duty]
7. For income rights, use 25 times annual value for a perpetual right, ten
   times for indefinite duration unless the fixed/life-term rule applies;
   an unascertainable capital yield is 4% annually. Fixed-term/life rights
   require §20's specified actuarial basis, excluding administration and
   acquisition costs. Its current operative tables/provider were not verified:
   do not substitute a guessed life expectancy or the ten-times method.
   Suspensive conditions defer payment; a resolutive condition needs approved
   actual-benefit adjustment. Death of the first recipient before payment
   and partly paid succession cases follow §12, rather than automatically
   charging two full duties. [Order §§12–13, 20][duty]

## Deadlines and filing

**Open the case and establish authority.** Notify the probate court of the death
with the medical/death certificate. Its letter to the initial contact permits
obtaining bank records. The court says assets cannot be sold or transferred
without its approval. Choose the actual probate method; the ordinary private
route requires all heirs' agreement, age 18 or above, no guardianship and
solvency, and makes them jointly responsible for known and unknown debts and
guarantees. The court's application deadline is as soon as possible and no
later than **3½ months after death**; all heirs sign personally or by original
probate power. Obtain the court's approval rather than treating an application
as permission to distribute. [Court, opening/private-administration sections][court]

**Prepare both inventories.** Use the court-linked [D03 §14 opening form][opening].
Identify deceased, spouse, earlier-deceased spouse, responsible contact and
actual property regime; separate community and separate property statements
where both are divided. Fill the death-date assets (cash, claims, vehicles,
boats, contents, deposits, copyright, refunds, foreign/local banks, property,
shares, receivables, insurance and business assets), debts with documents,
net assets in box 32, outside-estate benefits in box 33 and gifts/advances in
box 34. The form distinguishes death-date inventory from subsequent events;
retain a separate income-tax carrying-value/death-year income schedule under
[the estate-tax Guide](fo-estate-income-tax.md). [D03, all six pages][opening]

Use the [four-page closing inventory][closing], with the case number,
identity/property regime and chosen closing date. Box 1 brings opening net
assets from D03 box 32; boxes 2–4 record later income/value increases;
boxes 5–8 record funeral, administration and other supported costs/losses;
box 9 reconciles net inheritance. Box 10 separates the surviving spouse's
community-property share from inheritance. Box 11 discloses other chargeable
gifts, advances and insurance; box 12 lists every heir/legatee, address, birth
date, relationship and amount; box 13 must reconcile to box 9 c or 10 b.
Record early property withdrawal dates and explanations in box 14 and retain
valuation evidence. Every heir signs box 15 or supplies the original probate
power. Both PDFs require a date and **blue-ink original sent to Skiftirættin,
C. Pløyensgøta 1, PO Box 28, 110 Tórshavn; not email**. The opening D03 form is
signed by the responsible person. This Guide sends no document.
[D03 pp 1, 6][opening]; [closing inventory, all four pages][closing]

**Keep the clocks separate.** The D03/death-year information is due within
**six months after death**; where administration is decided later than four
months after death, Tax Act §14(3) instead allows two months after that
decision. The court's closing inventory/declaration is due within **one year
after death**; the court limits the selected closing date to death through
that anniversary. For a different statutory duty trigger or no Faroese
probate, §26 uses **one year from the duty trigger**. Public-to-private
transfer starts §29's one-year period at transfer; later knowledge starts it
at knowledge, explained in the declaration. Apply before the deadline for
an extension: the probate authority can grant up to six months, further
extension requires the approval named in §29. Do not replace the one-year
duty filing clock with income tax's 15-month test.
[Tax Act §14(3)][tax]; [Order §§26–29][duty]; [court, inventories][court]

**Check, approve and pay.** The court checks the inventories and sends them to
TAKS for tax approval; it and the contact receive that approval, then the
contact receives the duty invoice. Reconcile every class, aggregate share,
value, relief and credit to the workpaper and retain the assessment and
receipt. Private heirs/spouse are jointly liable, subject to §21's personal
excess-liability exception; payment before distribution is the court's
recommendation. Public administrators arrange duty at closing; extraordinary
administrators unable to close within two years report the reason and repeat
annually. [Order §§23–25, 31, 34][duty]; [court, approval/invoice][court]

Section 32 gives **three months from assessment notification** (including
notification to the appointed representative) for its stated administrative
challenge and **three months from notification of that decision** to request
the stated judicial proceedings. Its operative text names Justitsministeriet;
the current receiving office/routing has not been established here. Preserve
the notification and immediately obtain the correct routing from the existing
case's appeal instructions; do not let that uncertainty erase the statutory
clock. Unchallenged assessments become binding under §32. Section 33 then
sets payment **six weeks after the assessment becomes binding**, with a
holiday moved to the next working day, and proof of payment to the probate
authority **within three weeks after the payment deadline**. This is not six
weeks after death or automatically six weeks after the invoice's issue date.
Use the actual assessment/invoice instructions and investigate any differing
date before the earlier deadline. [Order §§32–34][duty]

Section 11 permits annual instalments for its listed income/succession rights
when the rate is at least 2%, with as many instalments as whole percentage
points and an up-front 2% increase for each year over which payment is spread.
Faroese property needs the specific approval and ordinarily mortgage security.
Do not assume an automatic general property instalment election. Later
instalments fall on successive anniversaries with the statutory holiday
adjustment. [Order §§11, 33][duty]

## Penalties and interest

A late or materially unusable declaration increases affected filers' duty by
**one third**; missing signatures similarly affect those who did not sign.
The Act permits daily fines to compel a proper declaration and discretionary
waiver of the increase. Intentional concealment falling outside §38 produces
double duty unless settled with the stated approval; knowingly false or
incomplete information under §38 produces a fine of **five times the duty
evaded or attempted**, and each knowing joint declarant faces the full fine.
These are separate statutory cases, not cumulative automatic additions to
every late return. [Order §§30, 37–38][duty]

Late payment bears **one sixth per mille per day**, namely the duty divided
by 6,000 for each late day. Missing payment proof after the three-week period
leads to collection. Preserve actual dates and receipts; the 0.7% monthly
income-tax rate is not this duty's daily rate. Banks, institutions and probate
administrators also have information and neglect sanctions under §§35–40;
those are not a fixed general taxpayer late-filing fine. [Order §§33–40][duty]

## Cross-border points

A deceased domiciled in the Faroes is within the worldwide-assets rule.
Foreign real property and foreign family-settlement income can receive the
specified discretionary relief if taxed abroad; there is no automatic
unlimited foreign-duty credit. Determine domicile when the duty arises.
For a deceased domiciled outside the Faroes, §8 ordinarily reaches Faroese
real property, its specified rights and Faroese family settlements; an estate of a Danish person who died abroad, formally referred to Faroese
probate under the provision named in §8, has the separate wider rule.
[Order §§8–9][duty]

Faroese representatives of foreign heirs can be liable. A direct payer to an
overseas recipient without a Faroese intermediary must deduct the duty and
is responsible for its payment; the statutory property-security rule also
applies to specified nonresident-to-nonresident transfers. These rules must
be checked before remitting a foreign heir's gross share. They do not supply
income-tax treaty relief or remove capital-gains tax on a distribution.
[Order §34][duty]; [estate-tax Guide](fo-estate-income-tax.md)

## Two worked examples that recompute

### 1. Ordinary sibling inheritance and relationship control

Fictional private estate: after proved debts/costs, one sibling receives
DKK 60,149, no earlier acquisition or exemption. Round to DKK 60,100. Class B's
whole-share rate is 5.75%, producing DKK 3,455.75. Treating the same sibling
as a descendant would produce DKK 1,652.75 and understate duty by
DKK 1,803. This checks both the actual relationship and whole-share method;
it is not a marginal-band computation. [Order §§2–3, 16, 21][duty]

```oa-check
name: Faroese sibling class and whole-share duty
inputs:
  net_share: 60149
  rounding_unit: 50
  sibling_rate: 0.0575
  descendant_rate: 0.0275
steps:
  chargeable_share: floor(net_share / rounding_unit) * rounding_unit
  sibling_duty: chargeable_share * sibling_rate
  wrong_descendant_duty: chargeable_share * descendant_rate
  understatement: sibling_duty - wrong_descendant_duty
expected:
  chargeable_share: 60100
  sibling_duty: 3455.75
  wrong_descendant_duty: 1652.75
  understatement: 1803
```

### 2. Outside-estate insurance changes the band

Fictional unrelated beneficiary receives DKK 96,000 net inheritance plus
DKK 6,000 life-insurance proceeds outside the estate. The deceased paid all
premiums, the beneficiary reimbursed nothing, no statutory obligation or
undivided-estate exception applies, and there was no prior duty payment.
Aggregate DKK 102,000, class D at 12%: DKK 12,240. Omitting the policy gives
DKK 11,280 (96,000 × 11.75%), understating duty by DKK 960. If the correctly
assessed DKK 12,240 is paid ten days late, §33 daily interest is DKK 20.40.
The scenario's classifications are facts to prove, not an insurance safe
harbour. [Order §§2, 5(a), 21, 33][duty]

```oa-check
name: Faroese insurance inclusion changes whole-share band
inputs:
  net_inheritance: 96000
  chargeable_outside_insurance: 6000
  aggregated_class_d_rate: 0.12
  omitted_policy_class_d_rate: 0.1175
  late_days: 10
steps:
  aggregate_share: net_inheritance + chargeable_outside_insurance
  correct_duty: aggregate_share * aggregated_class_d_rate
  omitted_policy_duty: net_inheritance * omitted_policy_class_d_rate
  understatement: correct_duty - omitted_policy_duty
  daily_interest: correct_duty / 6000 * late_days
expected:
  aggregate_share: 102000
  correct_duty: 12240
  omitted_policy_duty: 11280
  understatement: 960
  daily_interest: 20.4
```

## Ask the client first

- What are the death date, domicile, probate approval/method and property regime,
  and was either spouse already in an undivided estate?
- Who receives each share, what proves the relationship, and is there a will,
  adoption, separation, guardianship or five-year dependency/household claim?
- What assets, debts, valuation evidence, funeral/administration costs and early
  distributions exist, including foreign property and uncollectible claims?
- What gifts, advances, retained-use transfers, insurance, pensions and family
  rights exist, who funded them, and what duty/foreign duty was already paid?
- Who is the appointed contact, and what signed applications, powers, inventory
  receipts, approvals, assessment notifications, appeal instructions and payment
  receipts exist?

## Sources

| Official source | URL | Read on |
|---|---|---|
| Inheritance Duty Order 468/1921, current through Act 209/2025 effective 1 January 2026; §§1–44 | https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa | 2026-10-31 |
| Current Tax Act 109/2023, §14 opening/death-year information | https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt | 2026-10-31 |
| Føroya Rættur, probate procedures, inventories, insurance and duty; official publisher-hosted copy | https://domstoldk.euwest01.umbraco.io/fo/faeroeerne/brug-retten/ | 2026-10-31 |
| Current court-linked D03, all six pages | https://domstoldk.euwest01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf | 2026-10-31 |
| Current court-linked closing inventory, all four pages | https://domstoldk.euwest01.umbraco.io/media/1ndp1gcb/b%C3%BAuppger%C3%B0-14-uppger%C3%B0.pdf | 2026-10-31 |

Not yet confirmed: current receiving-office routing for the administrative appeal/approvals still named Justitsministeriet in the operative Order; the current actuarial tables/provider for fixed-term/life rights; current implementation of rare historic family-settlement/successive-death instalment cases and the exact near-band-boundary rate ordering where the unrounded share crosses a band. Those branches require case-specific support and are not treated as exemptions. This Guide remains a source-cited tier-2 draft pending independent review and professional attestation. The canonical court URL returned 403 and the normal in-app browser was unavailable; the linked official publisher-hosted pages/forms were read through web retrieval. No authority was contacted.

[duty]: https://logir.fo/Anordning/468-af-08-11-1921-hvorved-lov-om-arveafgift-af-27051908-saettes-i-kraft-pa
[tax]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[court]: https://domstoldk.euwest01.umbraco.io/fo/faeroeerne/brug-retten/
[opening]: https://domstoldk.euwest01.umbraco.io/media/tfjl4r3d/d03-uppger%C3%B0-yvir-ogn-og-skuld-vi%C3%B0-dey%C3%B0a-sambaert-14-%C3%AD-skattal%C3%B3gini-241023.pdf
[closing]: https://domstoldk.euwest01.umbraco.io/media/1ndp1gcb/b%C3%BAuppger%C3%B0-14-uppger%C3%B0.pdf
