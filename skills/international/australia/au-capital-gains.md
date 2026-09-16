---
name: au-capital-gains
description: "Use this skill for any Australian capital gains tax question, for any entity type. Trigger on: \"CGT Australia\", \"capital gains Australia\", \"sell shares Australia\", \"50% CGT discount\", \"cost base Australia\", \"capital loss\", \"carry forward capital losses\", \"small business CGT concessions\", \"SBCGT\", \"active asset test\", \"15-year exemption\", \"retirement exemption CGT\", \"CGT rollover\", \"CGT event A1\", \"main residence exemption\", \"Australian CGT\", \"sell my Australian company\", \"dispose of property Australia\", \"CGT indexation from 2027\". Covers the calculation workflow from CGT event and cost base through losses, discounts and concessions, entity and residency differences, and the enacted 1 July 2027 changes. Routes to au-small-business-cgt, au-nonresident-cgt, au-rental-property and au-crypto-tax for their specialist rules."
version: 1.2
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027), with the enacted 1 July 2027 changes flagged"
last_updated: 2026-09-16
review_status: pending_review
depends_on:
  - au-individual-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Capital Gains

## Australia Capital Gains Tax v1.2

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

> **Enacted change from 1 July 2027.** The 50% CGT discount for individuals, trusts and
> partnerships is replaced by cost base indexation with a 30% minimum tax rate on capital gains.
> The change applies to gains that accrue after 1 July 2027. Separately, negative gearing for
> residential property investments is limited to new builds from 1 July 2027, with properties
> held at 7:30 pm AEST on 12 May 2026 exempt from that limit. Both measures are law. See
> Section 9 before advising on any disposal planned for 2027-28 or later.
> [ATO, Reforming negative gearing and capital gains tax](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax)

## Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Income year covered | 2026-27 (1 July 2026 to 30 June 2027) |
| CGT rate | No separate rate. The net capital gain is included in assessable income and taxed at the entity's rate |
| Effective top rate, individual, asset held over 12 months | 23.5% for 2026-27, being 47% (45% plus 2% Medicare levy) applied to half the gain |
| 50% general discount | Individuals and trusts, for assets held more than 12 months, until 30 June 2027 |
| Complying superannuation fund discount | 33.33% |
| Companies | No discount. The gain is taxed at the company rate |
| Annual tax-free amount | None. Australia has no annual CGT exemption |
| Primary legislation | ITAA 1997 Parts 3-1 and 3-3 |
| Tax authority | Australian Taxation Office |
| Where reported | Capital gains item in the return, with a CGT schedule where required |
| Reviewed by | Pending. Australian CPA or CA review required |

## Section 2 - The calculation workflow

Work through these steps in order. Each step can end the analysis.

**Step 1. Identify the CGT event and its date.**
A CGT event, not a payment, triggers CGT. For a disposal under a contract, the event happens at
the contract date, not settlement. This determines the income year, the 12-month holding test and
the residency position.

**Step 2. Check whether the asset or the gain is exempt.**
If an exemption applies in full, stop. Common exemptions: the main residence, a car or motorcycle,
a personal use asset acquired for $10,000 or less, an asset acquired before 20 September 1985,
certain compensation and gambling amounts, and depreciating assets used wholly for a taxable
purpose, which are dealt with under Division 40 instead.

**Step 3. Work out the cost base or reduced cost base.**
Use the cost base for a gain and the reduced cost base for a loss. See Section 4.

**Step 4. Calculate the gross gain or loss per asset.**
Capital proceeds less cost base gives a gain. Reduced cost base less capital proceeds gives a
loss. An amount that falls between the two produces neither.

**Step 5. Apply capital losses.**
Current year losses first, then losses carried forward from earlier years. Losses are applied
before any discount, which is what makes the order matter.

**Step 6. Apply the discount, if available.**
See Section 6 for the entity and residency tests.

**Step 7. Apply concessions.**
Small business CGT concessions, rollovers and any specific relief. See `au-small-business-cgt.md`.

**Step 8. Report the net capital gain.**
The net capital gain is included in assessable income for the year. A net capital loss cannot
reduce other income; it is carried forward indefinitely and used against future capital gains.

## Section 3 - What triggers CGT

**Common CGT events**

| Event | What it is |
| --- | --- |
| A1 | Disposal of a CGT asset by sale, gift or transfer |
| B1 | Use and enjoyment before title passes |
| C1 | Loss or destruction of an asset |
| C2 | Cancellation, surrender or expiry of a right or option |
| D1 | Creation of a contractual or other right |
| E4 | Capital payment from a trust exceeding the cost base of the interest |
| G1 | Return of capital on shares exceeding the cost base |
| I1 and I2 | Ceasing to be an Australian resident |
| K6 | Pre-CGT shares or trust interests where post-CGT property dominates |

More than one event can apply to the same transaction. Where that happens, the most specific event
generally prevails.

**CGT assets** include land and buildings, shares and units, goodwill, contractual rights,
options, crypto assets, foreign currency and leases.

**A gift is a disposal.** Where parties are not dealing at arm's length, or where no consideration
passes, the market value substitution rule replaces the actual proceeds with market value.

## Section 4 - Cost base and reduced cost base

**The five elements of the cost base**

| Element | Content |
| --- | --- |
| 1 | Money paid, or the market value of property given, to acquire the asset |
| 2 | Incidental costs of acquisition and disposal, such as stamp duty, legal fees, agent commission, valuation and brokerage |
| 3 | Non-capital costs of ownership, such as rates, land tax, insurance and interest, only for assets acquired after 20 August 1991 and only to the extent not deductible |
| 4 | Capital expenditure to increase or preserve the asset's value, or to install or move it |
| 5 | Capital expenditure to establish, preserve or defend title to the asset |

**The reduced cost base** is used to work out a capital loss. It contains elements 1, 2, 4 and 5
but not element 3, and it is reduced by amounts such as balancing adjustments and recouped
expenditure.

**Deductions reduce the cost base.** Amounts claimed as capital works deductions under Division 43
reduce the cost base, and element 3 excludes anything that was deductible. This is the most common
cost base error on a rental property disposal. See `au-rental-property.md`.

## Section 5 - Capital losses

- A capital loss can be applied only against capital gains, never against ordinary income.
- Current year capital losses are applied before prior year losses.
- Losses are applied before any CGT discount. Applying the discount first overstates the benefit
  of the loss.
- Where there is a choice, apply losses first against gains that do not qualify for the discount,
  because a discounted gain loses only half its value to a loss offset.
- Net capital losses carry forward indefinitely for individuals. Company and trust loss use is
  restricted by the continuity of ownership, business continuity and trust loss rules.
- A loss on a personal use asset or a collectable is quarantined. A collectable loss can only be
  used against collectable gains.
- Wash sale arrangements, where an asset is sold and substantially repurchased to crystallise a
  loss, attract Part IVA attention.

## Section 6 - The discount, and who gets it

**Entity treatment for assets held more than 12 months**

| Entity | Discount | Note |
| --- | --- | --- |
| Australian resident individual | 50% | Applies until 30 June 2027. See Section 9 |
| Australian trust | 50% | The discount flows through to beneficiaries, who must be able to use it in their own right |
| Complying superannuation fund | 33.33% | |
| Company | None | The full gain is taxed at the company rate |
| Foreign or temporary resident | Apportioned | No discount for the part of the gain accruing after 8 May 2012 while a foreign or temporary resident. A period of Australian residency during ownership can support an apportioned discount |

**The 12-month test.** The asset must be owned for at least 12 months before the CGT event,
excluding the day of acquisition and the day of the event. Previous ownership can count where the
asset was acquired through a deceased estate, through a relationship breakdown rollover, or as a
replacement asset under a rollover for a lost, destroyed or compulsorily acquired asset.

**Exclusions from the discount**

- A home first used for rental or business less than 12 months before disposal.
- Where the indexation method is chosen for an asset acquired before 21 September 1999.
- A CGT event that creates a new asset, such as granting a lease or a restrictive covenant,
  because the asset was not held for 12 months.
- Certain disposals of interests in companies and trusts with fewer than 300 members.
- An income asset converted into a capital asset to access the discount, under Part IVA.

An additional discount of up to 10% can apply to individuals who provide eligible affordable
rental housing.
[ATO, CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount)

## Section 7 - Small business CGT concessions

These sit on top of the discount and can reduce a gain to nil. Full rules are in
`au-small-business-cgt.md`. In outline:

**Basic conditions.** A CGT event happens to an asset that would otherwise produce a gain, the
taxpayer is a small business entity or satisfies the $6 million maximum net asset value test, and
the asset satisfies the active asset test. Additional conditions apply to shares and trust
interests.

**The four concessions**

| Concession | Effect | Core condition |
| --- | --- | --- |
| 15-year exemption | The whole gain is disregarded | Asset continuously held for at least 15 years, and the individual is 55 or over and retiring, or is permanently incapacitated |
| 50% active asset reduction | Halves the remaining gain | Basic conditions only |
| Retirement exemption | Exempts up to a $500,000 lifetime limit per individual | An amount must be paid into superannuation if the individual is under 55 |
| Rollover | Defers the gain | A replacement asset must be acquired, or capital improvement incurred, within the replacement asset period |

**Order of application.** Capital losses, then the general discount, then the 50% active asset
reduction, then the retirement exemption or rollover on what remains. Applied in that order the
effective rate on an eligible gain can approach nil, which is why the ATO scrutinises the active
asset test and the aggregation rules closely.

## Section 8 - Residency, foreign assets and withholding

- **Australian residents** are taxed on worldwide capital gains. A foreign income tax offset may
  be available for foreign tax paid on the same gain, limited to the Australian tax on that
  income. See `au-foreign-income.md`.
- **Foreign residents** are taxed only on taxable Australian property, principally Australian real
  property, an indirect interest in Australian real property, and assets used in an Australian
  permanent establishment. See `au-nonresident-cgt.md`.
- **Ceasing residency** triggers CGT events I1 and I2: a deemed disposal at market value of most
  CGT assets, with an election available to defer the gain until actual disposal, at the cost of
  remaining within the Australian CGT net. Taxable Australian property is excluded from the deemed
  disposal. See `leaving-australia-tax-residency-cgt.md`.
- **Main residence exemption for foreign residents.** A foreign resident at the time of disposal
  cannot claim the main residence exemption for property sold after 30 June 2020 unless the life
  events test is satisfied. There is no partial or apportioned exemption in that case, and the
  home first used to produce income rule is also unavailable. The life events test requires a
  continuous period of foreign residency of six years or less, plus a terminal medical condition
  of the taxpayer, spouse or child under 18, the death of a spouse or child under 18, or a CGT
  event arising from a formal relationship breakdown agreement.
  [ATO, Main residence exemption for foreign residents](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents)
- **Foreign resident capital gains withholding.** For contracts signed from 1 January 2025, the
  purchaser must withhold 15% of the sale price for all Australian real property, with no value
  threshold. An Australian resident vendor avoids withholding by giving the purchaser a clearance
  certificate before settlement. A foreign resident can apply for a variation. The withheld amount
  is credited against the vendor's assessment.
  [ATO, Foreign resident capital gains withholding](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding)
- **Foreign resident CGT regime changes from 1 October 2026.** The ATO states that enacted changes
  broaden the meaning of taxable Australian real property, apply the principal asset test over the
  365 days before a CGT event rather than only at the event, introduce a notification requirement
  for certain foreign resident vendor declarations, and provide a transitional 50% discount for
  eligible foreign residents disposing of certain Australian renewable energy assets. Confirm the
  amending Act before relying on the detail.
  [ATO, Strengthening the foreign resident CGT regime](https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime)

## Section 9 - The changes taking effect on 1 July 2027

**AUDIT FLASH POINT.** Advice on a disposal straddling 1 July 2027, and on timing a disposal to
sit either side of that date, will be examined closely. Part IVA applies to arrangements entered
into for the dominant purpose of obtaining a tax benefit.

On 12 May 2026, as part of the 2026-27 Federal Budget, the Government announced reforms to
negative gearing and capital gains tax. The ATO states the measures are now law, enacted by the
Treasury Laws Amendment (Tax Reform No. 1) Act 2026 and the Income Tax Rates Amendment
(Tax Reform No. 1) Act 2026, and that they apply from 1 July 2027:

- Negative gearing for residential property investments is limited to new builds. Properties held
  at 7:30 pm AEST on 12 May 2026 are exempt from the negative gearing change.
- The 50% CGT discount for individuals, trusts and partnerships is replaced by cost base
  indexation together with a 30% minimum tax rate on capital gains. The CGT reform applies only to
  gains that accrue after 1 July 2027.

**What this means in practice.** Until 30 June 2027 the existing 50% discount continues to apply
on the current tests. From 1 July 2027 the mechanism changes from a flat halving of the gain to an
inflation adjustment of the cost base, with a floor on the rate applied to the gain. The two
produce different answers: indexation helps a long-held asset in a high-inflation period and helps
much less over a short holding period, and the 30% floor removes the benefit of a low marginal
rate.

**Do not apply the new mechanism to a 2026-27 disposal**, and do not apply the 50% discount to a
gain accruing after 1 July 2027. The apportionment of a gain that accrues across the change date
is the detail to confirm against the enacted provisions and the ATO's guidance before advising.

This guide states the measures as the ATO summarised them on 29 June 2026. The detailed
transitional provisions, including how a gain is apportioned across 1 July 2027 and how the 30%
minimum rate interacts with the Medicare levy and with trust distributions, must be read in the
Acts before use.
[ATO, Reforming negative gearing and capital gains tax](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax);
[Treasury Laws Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00049/latest);
[Income Tax Rates Amendment (Tax Reform No. 1) Act 2026](https://www.legislation.gov.au/C2026A00050/latest)

## Section 10 - Worked example

**Facts.** Priya is an Australian resident individual for the whole of the 2026-27 income year.
All figures are synthetic.

| Item | Detail |
| --- | --- |
| Asset | Listed shares in one company |
| Acquired | 2 September 2022, for $28,000 plus $95 brokerage |
| Sold | Contract dated 14 March 2027, proceeds $46,000, brokerage on sale $110 |
| Other current year disposal | A second parcel sold at a capital loss of $1,500 |
| Carried forward | Net capital loss of $3,200 from 2024-25 |

**Step 1, CGT event and date.** CGT event A1 happens at the contract date, 14 March 2027, so the
gain falls in the 2026-27 income year.

**Step 2, exemptions.** None apply. Shares are not personal use assets.

**Step 3, cost base.**

```
Element 1  purchase price                        28,000
Element 2  brokerage on acquisition                  95
Element 2  brokerage on disposal                    110
Cost base                                        28,205
```

**Step 4, gross gain.**

```
Capital proceeds                                 46,000
Less cost base                                   28,205
Gross capital gain                               17,795
```

**Step 5, apply losses, current year first.**

```
Gross capital gain                               17,795
Less current year capital loss                    1,500
                                                 16,295
Less prior year net capital loss                  3,200
Gain remaining after losses                      13,095
```

**Step 6, discount.** Priya held the shares from 2 September 2022 to 14 March 2027, which is more
than 12 months, and she is an Australian resident. The disposal is before 1 July 2027, so the 50%
discount applies.

```
Gain after losses                                13,095
CGT discount at 50%                               6,547.50
Net capital gain included in assessable income    6,547.50
```

**Step 7, report.** $6,547.50 is included in Priya's assessable income for 2026-27 and taxed at
her marginal rate plus the Medicare levy.

**Why the order matters.** Applying the 50% discount before the losses would give
($17,795 x 50%) less $4,700, or $4,197.50, understating the net capital gain by $2,350. The losses
must come first.

## Section 11 - Common errors

- Using the settlement date instead of the contract date for a property or share disposal.
- Applying the discount before capital losses.
- Offsetting a capital loss against salary or business income.
- Including element 3 ownership costs in the reduced cost base, or including costs that were
  deductible.
- Failing to reduce the cost base by capital works deductions claimed on a rental property.
- Claiming the 50% discount for a company, or the full 50% for a complying super fund.
- Claiming the main residence exemption for a foreign resident vendor without testing the life
  events test.
- Assuming an Australian resident vendor is outside foreign resident capital gains withholding
  without obtaining a clearance certificate before settlement.
- Treating the 15-year exemption as available on age alone, without the 15 years of continuous
  ownership and the retirement or incapacity condition.
- Applying the 2027-28 rules to a 2026-27 disposal, or the reverse.

## Section 12 - Self-checks

- [ ] The CGT event and its date are identified, and the correct income year follows from them.
- [ ] Residency at the time of the CGT event is established, not assumed.
- [ ] Each element of the cost base is supported by a document.
- [ ] Capital works and capital allowance deductions have been removed from the cost base.
- [ ] Current year losses are applied before prior year losses, and both before any discount.
- [ ] The discount percentage matches the entity type.
- [ ] The 12-month test excludes the acquisition day and the event day.
- [ ] Small business concession conditions have been tested individually, not assumed as a set.
- [ ] Withholding and clearance certificate obligations are addressed before settlement.
- [ ] For a disposal in 2027-28 or later, Section 9 has been applied and the Acts have been read.

## Section 13 - Sources

- Income Tax Assessment Act 1997, Part 3-1 (CGT events, cost base, exemptions), Part 3-3 (CGT
  concessions), Division 115 (discount capital gains), Division 152 (small business concessions),
  Subdivision 118-B (main residence).
- Treasury Laws Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00049/latest
- Income Tax Rates Amendment (Tax Reform No. 1) Act 2026,
  https://www.legislation.gov.au/C2026A00050/latest
- ATO, CGT discount,
  https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount
- ATO, Main residence exemption for foreign residents,
  https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents
- ATO, Foreign resident capital gains withholding,
  https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding
- ATO, Reforming negative gearing and capital gains tax,
  https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax
- ATO, Strengthening the foreign resident CGT regime,
  https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime

Sources were checked on 16 September 2026.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this
> before lodging. Small business CGT eligibility requires detailed analysis of the active asset
> test, the aggregation rules and the maximum net asset value test.

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
