---
name: au-capital-gains
description: "Use this skill for any Australian capital gains tax question, for any entity type. Trigger on: \"CGT Australia\", \"capital gains Australia\", \"sell shares Australia\", \"50% CGT discount\", \"cost base Australia\", \"capital loss\", \"carry forward capital losses\", \"small business CGT concessions\", \"SBCGT\", \"active asset test\", \"15-year exemption\", \"retirement exemption CGT\", \"CGT rollover\", \"CGT event A1\", \"main residence exemption\", \"Australian CGT\", \"sell my Australian company\", \"dispose of property Australia\", \"CGT indexation from 2027\". Covers the calculation workflow from CGT event and cost base through losses, discounts and concessions, entity and residency differences, and the enacted 1 July 2027 changes. Routes to au-small-business-cgt, au-nonresident-cgt, au-rental-property and au-crypto-tax for their specialist rules."
version: 1.7
jurisdiction: AU
tax_year: 2026
last_updated: 2026-11-22
depends_on:
  - au-individual-return
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# AU Capital Gains

## AU Capital Gains

## AU Capital Gains

## Australia Capital Gains Tax v1.7

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

> **Enacted changes from 1 July 2027.** Cost base indexation generally replaces the 50% CGT
> discount for gains accruing from that date. Discounts remain available for qualifying new
> residential dwellings and affordable housing. A 30% minimum tax applies to defined gains
> of resident individuals, with exceptions. Separate rules restrict deductions for some
> residential property losses. See Section 9 for the transition and exceptions.
> [ATO, Reforming negative gearing and capital gains tax](https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax)

## Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Income year covered | 2026-27 (1 July 2026 to 30 June 2027) |
| CGT rate | No separate rate. The net capital gain is included in assessable income and taxed at the entity's rate |
| Effective rate at the top individual income tax bracket with full Medicare levy | 23.5% for a gain eligible for the 50% discount in 2026-27, calculated as (45% + 2%) × 50% |
| 50% general discount | Eligible individuals and trusts meeting the 12-month test. See Section 9 for events from 1 July 2027 |
| Complying superannuation fund discount | 33⅓% |
| Companies | No general CGT discount. See Section 8 for the transitional foreign renewable energy rule |
| Annual tax-free amount | None. Australia has no annual CGT exemption |
| Primary legislation | ITAA 1997 Parts 3-1 and 3-3 |
| Tax authority | Australian Taxation Office |
| Where reported | Capital gains item in the return, with a CGT schedule where required |
| Reviewed by | Pending. Australian CPA or CA review required |

## Section 2 - The calculation workflow

Work through these steps in order. Each step can end the analysis.

**Step 1. Identify the CGT event and its date.**
Identify the statutory trigger for the event. For an A1 disposal under a contract, the event
happens when the contract is entered into. That date determines the income year and is used
for the 12-month holding test and the relevant residency tests.

**Step 2. Check whether the asset or the gain is exempt.**
If an exemption applies in full, stop. Common exemptions: the main residence, a car or motorcycle,
a personal use asset whose first cost base element is $10,000 or less, an asset acquired before 20 September 1985,
certain compensation and gambling amounts, and depreciating assets used wholly for a taxable
purpose, which are dealt with under Division 40 instead. Disregard any gain that qualifies for
the small business 15-year exemption before working through the remaining steps.

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
| E4 | Qualifying trust payment with a non-assessable part. The adjusted amount reduces the cost bases up to the applicable amounts. The excess over the cost base produces a gain |
| G1 | Qualifying capital payment for a share. The non-assessable part reduces the cost bases up to the applicable amounts. The excess over the cost base produces a gain |
| I1 and I2 | Ceasing to be an Australian resident |
| K6 | Certain events involving pre-CGT shares or trust interests when qualifying post-CGT property meets the 75% net value test in section 104-230 |

- **Multiple events** — More than one event can apply to the same transaction. Where that happens, the most specific event generally prevails.
- **CGT assets** — CGT assets include land and buildings, shares and units, goodwill, contractual rights, options, crypto assets, foreign currency and leases.
- **A gift is a disposal** — A gift is a disposal. Where parties are not dealing at arm's length, or where no consideration passes, the market value substitution rule replaces the actual proceeds with market value.
- **Capital versus revenue** — Establish whether the profit is on capital or revenue account before applying CGT. A trading business or an isolated profit-making transaction produces ordinary income, and section 118-20 reduces a capital gain to the extent the amount is otherwise assessable, so the same profit is not taxed twice. Holding an asset for more than a year does not by itself make it a capital investment.  _([ITAA 1997 (Cth) s 118-20](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-20))_
- **Main residence conditions** — The main residence exemption depends on the dwelling being the taxpayer's home, land of two hectares or less, the extent of any income-producing use, the absence rule and residency at the CGT event. A property bought as an investment is not exempt because the owner later moves in: the exemption is apportioned to the days it was the main residence. Check occupation, absences and use before applying it.  _([ITAA 1997 (Cth) s 118-110](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-110); [s 118-185](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/118-185))_

## Section 4 - Cost base and reduced cost base

**The five elements of the cost base**

| Element | Content |
| --- | --- |
| 1 | Money paid, or the market value of property given, to acquire the asset |
| 2 | Incidental costs of acquisition and disposal, such as stamp duty, legal fees, agent commission, valuation and brokerage |
| 3 | Non-capital costs of ownership, such as rates, land tax, insurance and interest, only for assets acquired after 20 August 1991 and only to the extent not deductible |
| 4 | Capital expenditure to increase or preserve the asset's value, or to install or move it |
| 5 | Capital expenditure to establish, preserve or defend title to the asset |

- **The reduced cost base** — The reduced cost base is used to work out a capital loss and has five elements. Elements 1, 2, 4 and 5 match the cost base. Its third element replaces ownership costs with the assessable balancing-adjustment amounts specified in section 110-55(3), including its statutory relief cases. Apply the section's exclusions separately: subsection (4) excludes deductible amounts, including deductible balancing adjustments, and subsection (6) excludes recouped expenditure unless the recoupment is assessable. Do not subtract an assessable balancing adjustment merely because a deductible balancing adjustment is excluded.  _([ITAA 1997 (Cth) s 110-55](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-55))_
- **Capital works deductions** — Exclude Division 43 deductions claimed or still claimable for assets acquired after 7:30 pm ACT time on 13 May 1997. For land or buildings acquired at or before that time, this treatment applies to fourth-element expenditure incurred after 30 June 1999. See section 110-45 and `au-rental-property.md`.
- **Selling costs belong in the cost base, not the proceeds** — Capital proceeds are the money and the market value of property received for the event. Agent commission, legal fees and other disposal costs are second-element cost base amounts. Reconcile proceeds to the contract before adding selling costs to the cost base, otherwise they are counted twice.  _([ITAA 1997 (Cth) s 116-20](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/116-20); [s 110-25](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/110-25))_

## Section 5 - Capital losses

- **Capital loss applied only against capital gains** — A capital loss can be applied only against capital gains, never against ordinary income.
- **Order of losses** — Current year capital losses are applied before prior year losses.
- **Losses before discount** — Losses are applied before any CGT discount. Applying the discount first overstates the benefit of the loss.
- **Choice of which gains to offset** — Where there is a choice, apply losses first against gains that do not qualify for the discount, because a discounted gain loses only half its value to a loss offset.
- **Carry forward of net capital losses** — Net capital losses carry forward indefinitely for individuals. Companies must check their continuity of ownership and business continuity rules. Schedule 2F trust loss tests apply to tax losses and certain debt deductions. A trust generally uses its capital losses against its own capital gains.
- **Personal use asset losses** — Disregard losses on personal use assets. They cannot offset capital gains or carry forward.  _([ITAA 1997 (Cth) s 108-20(1)](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-20))_
- **Collectable losses** — A collectable loss can offset only collectable gains. Carry any unused amount forward for future collectable gains, subject to the collectable exemption rules.  _([ITAA 1997 (Cth) s 108-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/108-10))_
- **Wash sales** — Wash sale arrangements, where an asset is sold and substantially repurchased to crystallise a loss, attract Part IVA attention.

## Section 6 - The discount, and who gets it

**Entity treatment for assets held more than 12 months**

| Entity | Discount | Note |
| --- | --- | --- |
| Australian resident individual | 50% | For pre-1 July 2027 events. See Section 9 for the transition and later exceptions |
| Australian trust | 50% | The discount flows through to beneficiaries, who must be able to use it in their own right |
| Complying superannuation fund | 33⅓% |  |
| Company | No general discount | See Section 8 for the foreign renewable energy exception |
| Foreign or temporary resident | Apportioned | No discount for the part of the gain accruing after 8 May 2012 while a foreign or temporary resident. A period of Australian residency during ownership can support an apportioned discount |

- **The 12-month test** — The asset must be owned for at least 12 months before the CGT event, excluding the day of acquisition and the day of the event. Previous ownership can count where the asset was acquired through a deceased estate, through a relationship breakdown rollover, or as a replacement asset under a rollover for a lost, destroyed or compulsorily acquired asset.
- **Exclusions from the discount** — If section 118-192 treats a dwelling as acquired when it was first used to produce income, measure the 12 months from that date. The rule generally requires first income-producing use after 7:30 pm ACT time on 20 August 1996, a partial exemption at disposal and eligibility for a full exemption immediately before that first use. The discount is unavailable where the old indexation method is used for an eligible asset acquired at or before 11:45 am ACT time on 21 September 1999, or for excluded CGT events such as granting a lease or a restrictive covenant. Sections 115-45 and 115-50 can also deny a discount on certain shares and trust interests. Part IVA can apply to schemes converting income assets into capital assets to obtain the discount.
- **Additional affordable housing discount** — An additional discount of up to 10% can apply to individuals who provide eligible affordable rental housing. _([ATO, CGT discount](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/cgt-discount))_
- **Trust capital gains in a beneficiary's hands** — A beneficiary specifically entitled to a trust capital gain grosses up any discounted or reduced amount under Subdivision 115-C, then applies their own capital losses, discount percentage and concessions. The trust's discount does not settle the beneficiary's net capital gain. See `au-trust-distributions.md`.  _([ITAA 1997 (Cth) s 115-215](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/115-215))_

## Section 7 - Small business CGT concessions

- **Overview and basic conditions** — The 15-year exemption takes priority over losses and the CGT discount. The other concessions can reduce the gain after losses and any discount. A qualifying CGT event must otherwise produce a gain, the asset must pass the active asset test and at least one of the gateways below must apply. See `au-small-business-cgt.md` for the detailed rules.

**The four concessions**

| Concession | Effect | Core condition |
| --- | --- | --- |
| 15-year exemption | The whole gain is disregarded | Continuous ownership for at least 15 years. At the event, the relevant individual must be at least 55 and the event connected with their retirement, or they must be permanently incapacitated. Check the significant-individual conditions for companies, trusts, shares and trust interests |
| 50% active asset reduction | Halves the remaining gain | Basic conditions only |
| Retirement exemption | Exempts up to a $500,000 lifetime limit per individual | An amount must be paid into superannuation if the individual is under 55 |
| Rollover | Defers all or part of the gain | A replacement asset or qualifying improvement is needed by the end of the replacement asset period to maintain the deferral. Events J5 and J6 can crystallise a gain |

- **Order of application** — Disregard gains eligible for the 15-year exemption first. For the remaining gains, apply capital losses, the general discount if eligible, the 50% active asset reduction if used, then the retirement exemption or rollover if eligible.
- **Gateways and the active asset test period** — The basic conditions are met through a CGT small business entity with aggregated turnover below $2 million, the $6 million maximum net asset value test, or the partnership and passively held asset pathways, counting connected entities and affiliates. The asset must be active for at least half the test period, or 7.5 years where it was owned for more than 15 years. Shares and trust interests carry additional conditions.  _([ITAA 1997 (Cth) s 152-10](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/152-10); [s 152-35](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/152-35))_

## Section 8 - Residency, foreign assets and withholding

- **Australian residents** — Australian residents generally include capital gains from assets worldwide. Temporary residents generally disregard gains and losses to the extent a foreign resident would disregard them under Division 855. For eligible foreign tax paid on an amount included in assessable income, the foreign income tax offset limit is the greater of $1,000 and the tax difference calculated under section 770-75. See `au-foreign-income.md`.
- **Foreign residents** — Foreign residents are taxed only on taxable Australian property, principally Australian real property, an indirect interest in Australian real property, and assets used in an Australian permanent establishment. See `au-nonresident-cgt.md`.
- **Ceasing residency** — CGT event I1 generally brings unrealised gains and losses to account at market value when an individual or company ceases Australian residency. Section 104-160(3) excludes taxable Australian real property, Australian permanent-establishment assets, and options or rights over those latter two categories (section 855-15 items 1 and 3). Section 104-160(5) separately disregards gains and losses on assets acquired before 20 September 1985. The event does not exclude all taxable Australian property: indirect Australian real-property interests can remain within I1. An individual may choose under section 104-165 to disregard all I1 gains and losses, with affected assets remaining in the Australian CGT net. Event I2 concerns a trust ceasing to be a resident trust. See ITAA 1997 sections 104-160 to 104-175 and `leaving-australia-tax-residency-cgt.md`.  _([ITAA 1997 sections 104-160 to 104-175](https://www.ato.gov.au/law/view/document?docid=PAC/19970038/104-160))_
- **Main residence exemption for foreign residents** — A foreign resident at the time of disposal cannot claim the main residence exemption for property sold after 30 June 2020 unless the life events test is satisfied. There is no partial or apportioned exemption in that case, and the home first used to produce income rule is also unavailable. The life events test requires a continuous period of foreign residency of six years or less, plus a terminal medical condition of the taxpayer, spouse or child under 18, the death of a spouse or child under 18, or a CGT event arising from a formal relationship breakdown agreement.  _([ATO, Main residence exemption for foreign residents](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents))_
- **Foreign resident capital gains withholding** — For contracts entered into from 1 January 2025, acquisitions of taxable Australian real property generally attract 15% withholding with no property-value threshold. For an ordinary arm's length sale, use the price. Check Schedule 1 to the Taxation Administration Act 1953, sections 14-200 and 14-215, for the calculation and excluded transactions. An Australian resident vendor can provide a valid clearance certificate by settlement. A foreign resident can apply for a variation. The vendor can claim a credit for the withheld amount. _([ATO, Foreign resident capital gains withholding overview](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview))_
- **Foreign resident CGT regime changes from 1 October 2026** — The law broadens taxable Australian real property and generally tests principal assets at the relevant time or at any time in the preceding 365 days. Certain foreign vendor declarations trigger notification requirements. For CGT events before 1 July 2040, an eligible foreign entity other than an individual, or a trustee of a foreign trust for CGT purposes, can get a transitional 50% discount on qualifying Australian renewable energy assets or eligible indirect interests. Check Schedules 2 and 3 of the [amending Act](https://www.legislation.gov.au/C2026A00086/latest).

## Section 9 - The changes taking effect on 1 July 2027

- **Discount and indexation.** Use the pre-reform rules for a disposal in 2026-27. For CGT events from 1 July 2027, check the deemed sale and reacquisition rules in sections 112-155 to 112-175 for existing assets. They can preserve the previous treatment for the gain accrued through 30 June 2027. Use the new cost base indexation rules where eligible for gains accruing from 1 July 2027. Eligible new residential dwellings can qualify for the 50% discount under section 115-102, with an option to use indexation where available. Section 115-125 preserves a discount for qualifying affordable housing. Check eligibility at beneficiary or partner level where relevant.
- **Minimum income tax.** Division 119 calculates a top-up using 30% of a resident individual's statutory minimum tax capital gain, before tax offsets. The base uses eligible post-reform gains remaining after losses, discounts, concessions and specified deductions. It excludes gains to which the new dwelling and affordable housing discount provisions apply. Recipients of payments listed in section 119-15 are exempt from the top-up. The Medicare levy is calculated separately.
- **Residential property losses.** From 2027-28, section 26-155 generally quarantines the excess of deductions over income from affected residential accommodation. The excess may reduce qualifying gains, and any remainder carries forward. The rules except eligible new dwellings and interests last acquired before 7:30 pm ACT time on 12 May 2026. For a contractual acquisition, use the time the contract was entered into. Other statutory exceptions also apply.
- **Timing and evidence.** Check the event date, transition rules and required valuations before calculating a gain across 1 July 2027. Part IVA may apply if its tax benefit and dominant purpose tests are met.

## Section 10 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Asset | Listed shares in one company |
| Acquired | 2 September 2022, for $28,000 plus $95 brokerage |
| Sold | Contract dated 14 March 2027, proceeds $46,000, brokerage on sale $110 |
| Other current year disposal | A second parcel sold at a capital loss of $1,500 |
| Carried forward | Net capital loss of $3,200 from 2024-25 |

**Facts.** The shareholder is an Australian resident individual for the whole of the 2026-27 income year. All figures are synthetic.

**Step 1, CGT event and date.** CGT event A1 happens at the contract date, 14 March 2027, so the gain falls in the 2026-27 income year.

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

**Step 6, discount.** The shareholder held the shares from 2 September 2022 to 14 March 2027, satisfying the 12-month test. The resident individual qualifies for the 50% discount on this disposal before 1 July 2027.

```
Gain after losses                                13,095
CGT discount at 50%                               6,547.50
Net capital gain included in assessable income    6,547.50
```

**Step 7, report.** Include $6,547.50 in assessable income for 2026-27. The income tax and any Medicare levy depend on the shareholder's complete return.

**Why the order matters.** Applying the 50% discount before the losses would give ($17,795 x 50%) less $4,700, or $4,197.50, understating the net capital gain by $2,350. The losses must come first.

## Section 11 - Common errors

- Using the settlement date instead of the contract date for a property or share disposal.
- Applying the discount before capital losses.
- Offsetting a capital loss against salary or business income.
- Including element 3 ownership costs in the reduced cost base, or including costs that were deductible.
- Failing to account for capital works deductions claimed or still claimable for a rental property.
- Claiming the 50% discount for a company, or the full 50% for a complying super fund.
- Claiming the main residence exemption for a foreign resident vendor without testing the life events test.
- Assuming an Australian resident vendor is outside foreign resident capital gains withholding without obtaining a clearance certificate before settlement.
- Treating the 15-year exemption as available on age alone, without the 15 years of continuous ownership and the retirement or incapacity condition.
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
- [ ] The workpapers hold the event date, proceeds, each cost base element, the loss and discount calculations, valuations, and any concession choice or rollover election.

## Section 13 - Sources

- Income Tax Assessment Act 1997, Part 3-1 (CGT events, cost base, exemptions), Part 3-3 (CGT concessions), Division 115 (discount capital gains), Division 152 (small business concessions), Subdivision 118-B (main residence).
- Treasury Laws Amendment (Tax Reform No. 1) Act 2026, https://www.legislation.gov.au/C2026A00049/latest
- Income Tax Rates Amendment (Tax Reform No. 1) Act 2026, https://www.legislation.gov.au/C2026A00050/latest
- ATO, CGT discount, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount
- ATO, Main residence exemption for foreign residents, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/main-residence-exemption-for-foreign-residents
- ATO, Foreign resident capital gains withholding, https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding
- ATO, Reforming negative gearing and capital gains tax, https://www.ato.gov.au/about-ato/new-legislation/in-detail/individuals/tax-reform-boosting-home-ownership-reforming-negative-gearing-and-capital-gains-tax
- ATO, Strengthening the foreign resident CGT regime, https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/strengthening-the-foreign-resident-cgt-regime

Sources were checked on 22 November 2026.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before lodging. Small business CGT eligibility requires detailed analysis of the active asset test, the aggregation rules and the maximum net asset value test.
