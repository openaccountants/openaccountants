---
name: us-federal-cost-segregation
description: "Cost segregation studies for US real property: reclassifiable basis, bonus rate, Form 3115 look-back, passive-loss usability."
jurisdiction: US
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US federal cost segregation for real property: 2026 method, with 2025 return notes

Figures are for tax year 2026 unless a line says 2025. The bonus depreciation rules come from P.L. 119-21 (the One Big Beautiful Bill Act, "OBBBA") as explained in IRS Notice 2026-11 and Publication 946 (2025). The 2026 section 179 limits come from Rev. Proc. 2025-32. A separate section covers 2025 returns, which are due by October 15, 2026 if the taxpayer got an extension.

## Scope and who this is for

- **Covers:** individuals, partnerships, S corporations and C corporations that own a building used in a business or held for rent: new construction, purchases, improvements, and "look-back" studies on buildings already in service.
- **What cost segregation does:** it splits the cost of a building project into components with shorter recovery periods (5-, 7- and 15-year property) and the building itself (27.5 or 39 years). It changes the *timing* of depreciation, not the total. Most of the early deduction usually comes from then taking bonus depreciation on the short-life components.
- **Does not cover:** personal residences, dealer property, property used mainly abroad, housing and rehabilitation credits, and like-kind exchange mechanics (see the `us-section-1031-like-kind-exchange` Guide).
- **State tax is separate.** Many states do not follow federal bonus depreciation, or follow it only in part. This Guide gives the federal answer only. For each state, use the `us-state-bonus-depreciation-conformity-matrix` Guide and then check the state's own rules.

## Ask the client first

- Which tax year are we working on (2025 or 2026), what type of entity owns the building, and what is its tax year-end?
- For a purchase: the date the written contract was signed, whether it was binding (no clause limiting damages to a fixed amount), the date any cancellation periods or contingencies ended, and the closing date. For construction: the date physical work of a significant nature began, and when more than 10% of the total cost (excluding land and planning) was paid or incurred ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- The placed-in-service date of the building and of each later improvement.
- Is the building residential rental property (80% or more of gross rental income from dwelling units), nonresidential (office, retail, warehouse, industrial), or short-term lodging ([Pub. 946](https://www.irs.gov/publications/p946))?
- Cost records: purchase agreement, appraisal, tax assessment and closing statement, or for construction the contracts, change orders and invoices.
- How has the property been depreciated on returns already filed, and did the owner ever elect *out* of bonus for any class?
- Is the business an "electing real property trade or business" (opted out of the business interest limit)? That forces the building and qualified improvement property onto the Alternative Depreciation System (ADS).
- Who is the owner for the passive rules? Hours spent in real property trades or businesses, hours spent in all other work (including a W-2 job), and whether the owner and spouse own at least 10% of the rental activity ([Pub. 925](https://www.irs.gov/publications/p925)).
- Financing: recourse or nonrecourse, and who is the lender (for the at-risk rules).
- Any plan to sell, exchange or convert the property in the next few years (this drives recapture).

## The method, step by step

1. **Fix the basis and take out the land.** Land is never depreciable. Allocate a lump-sum purchase price between land and building in proportion to their fair market values at purchase. If the values are unclear, the property tax assessment ratio can be used ([Pub. 527](https://www.irs.gov/publications/p527); [Pub. 946](https://www.irs.gov/publications/p946)).
2. **Get the study.** The IRS has not set any required method for cost segregation studies. The Audit Techniques Guide says the detailed engineering approach from actual cost records is generally the most accurate, and that it is generally available only for new construction. For a purchase, the study must allocate the price using fair market values and appraisal methods ([Cost Segregation ATG, Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
3. **Classify each component** as §1245 property (personal property, which gets a 5- or 7-year life) or §1250 property (the building and its structural components, 27.5 or 39 years). Land improvements such as roads, fences and shrubbery are 15-year property. There is no bright-line test: the ATG uses the six Whiteco factors on permanence and asks whether the item is a structural component of the building ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf); [Pub. 946](https://www.irs.gov/publications/p946)).
4. **Test each short-life component for bonus depreciation** (qualified property, not ADS, used-property rules) and fix its acquisition date against January 19, 2025. See the bonus section below ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
5. **Apply the right bonus rate** from the table below (100% for property acquired after January 19, 2025, unless an election applies). Bonus is taken after any §179 deduction and before regular MACRS ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
6. **Consider §179** only where it is allowed and adds something bonus does not (see the §179 section). It is an election, subject to a dollar limit, a phase-out and a business income limit.
7. **Depreciate the rest under regular MACRS.** The building uses straight-line and the mid-month convention. 5- and 7-year property uses 200% declining balance, and 15-year land improvements use 150% declining balance, generally with the half-year convention. Check the mid-quarter test: it applies if more than 40% of the year's non-real-property basis was placed in service in the last 3 months ([Pub. 946](https://www.irs.gov/publications/p946)).
8. **Test whether the loss can be used.** For partners and S corporation shareholders, start with basis. Then apply the at-risk rules, then the passive activity rules, and then, for noncorporate taxpayers, the excess business loss limit ([Pub. 925](https://www.irs.gov/publications/p925)).
9. **For a building already in service, catch up with Form 3115.** Use automatic change DCN 7 and take the §481(a) adjustment. Do not amend prior returns once a method has been adopted ([Rev. Proc. 2025-23 §6.01](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf)).
10. **Model the exit before the client relies on the deduction.** Work out §1245 recapture on the short-life assets, §1250 ordinary recapture where bonus was taken on §1250 property, and unrecaptured §1250 gain on the building ([Pub. 544](https://www.irs.gov/publications/p544)).

## Recovery periods ([Pub. 946](https://www.irs.gov/publications/p946); [Pub. 527 Table 2-1](https://www.irs.gov/publications/p527))

| Class | Typical cost segregation items | Method and convention |
| --- | --- | --- |
| 5-year | Appliances, carpets and furniture used in a residential rental activity; computers; office machinery | 200% DB, half-year (or mid-quarter) |
| 7-year | Office furniture and fixtures; property with no class life and not assigned to another class | 200% DB, half-year (or mid-quarter) |
| 15-year | Land improvements (shrubbery, fences, roads, sidewalks, bridges); qualified improvement property placed in service after 2017 | 150% DB for land improvements; straight-line for qualified improvement property; half-year (or mid-quarter) |
| 27.5-year | Residential rental building and its structural components (furnace, water pipes, venting) | Straight-line, mid-month |
| 39-year | Nonresidential building (office, store, warehouse) and its structural components | Straight-line, mid-month |

- **Residential rental property** means a building where 80% or more of the gross rental income for the tax year is from dwelling units. A unit in a hotel or motel where more than half the units are used on a transient basis is not a dwelling unit ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Qualified improvement property** is an improvement *made by the taxpayer* to the interior of a nonresidential building, placed in service after the building was first placed in service. Interior improvements already in a building when it is bought are not qualified improvement property in the buyer's hands. It excludes the cost of enlarging the building, elevators and escalators, and the internal structural framework ([26 U.S.C. §168(e)(6)](https://www.law.cornell.edu/uscode/text/26/168)). Improvements to a residential rental building are never qualified improvement property.

## Bonus depreciation rates by acquisition date ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf); [Pub. 946](https://www.irs.gov/publications/p946))

| Property | Rate | Conditions |
| --- | --- | --- |
| Acquired after January 19, 2025, and placed in service after January 19, 2025 | 100% | Permanent under OBBBA: there is no placed-in-service deadline and no further phase-down. The taxpayer may still elect out, class by class. |
| Same property, placed in service in the first tax year ending after January 19, 2025 (the 2025 calendar year for a calendar-year taxpayer) | 40% if elected (60% for long production period property and certain aircraft) | Only if the §168(k)(10) election is made by statement on the timely filed return, including extensions, for that year. |
| Acquired after September 27, 2017, and before January 20, 2025, and placed in service in 2025 | 40% (60% for long production period property and certain aircraft) | Pre-OBBBA phase-down still applies. The 100% rate is not available. |
| Acquired before January 20, 2025, and placed in service in 2026 | 20% | The pre-OBBBA rate has phased down by 20 percentage points a year and is 40% for 2025 ([Notice 2026-11 §2.01](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)). Confirm against the 2026 Form 4562 instructions when they are published. Long production period property and aircraft have a different schedule, so check the 2026 Form 4562 instructions. |

- **"Acquired" means the binding contract date, not the closing date.** Property is not treated as acquired after the date a written binding contract for it is entered into (OBBBA §70301(c)(4)). A binding contract is one that is enforceable under state law and does not limit damages to a fixed amount. The acquisition date is the latest of: the date the contract is signed, the date it becomes enforceable, the end of any cancellation period, and the date every contingency is met ([Notice 2026-11 §§2.02, 2.03 and 3.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Self-constructed property** is acquired when physical work of a significant nature begins. Under a safe harbor, that is when more than 10% of the total cost is paid or incurred, excluding land and preliminary work such as planning, design and financing. A component election can treat components acquired after January 19, 2025 as eligible even though the larger project began earlier ([Notice 2026-11 §§2.03 and 3.05](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Reliance:** Notice 2026-11 is interim guidance. A taxpayer who relies on it must follow sections 3 to 5 in full for all eligible property ([Notice 2026-11 §6.02](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Not eligible:** the building itself (27.5 or 39 years is more than 20 years), land, and any property that must use ADS. ADS covers nonresidential real property, residential rental property and qualified improvement property held by an electing real property trade or business ([Pub. 946](https://www.irs.gov/publications/p946); [26 U.S.C. §168(g)(8)](https://www.law.cornell.edu/uscode/text/26/168)).
- **Used property** qualifies only if the taxpayer never used it before acquiring it, and the acquisition meets the §179(d) purchase rules, which exclude property bought from a related party or received with a carryover basis ([26 U.S.C. §168(k)(2)(E)](https://www.law.cornell.edu/uscode/text/26/168)).
- **Election out** is made class by class (for example, all 5-year property) for everything in that class placed in service in the year. Attach a statement to the timely filed return, including extensions. If the return was filed on time without it, the election can still be made on an amended return filed within 6 months of the original due date (excluding extensions), marked "Filed pursuant to section 301.9100-2". The election cannot be revoked without IRS consent ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
- **Qualified production property (§168(n))** is a separate, elective 100% allowance for the manufacturing part of a nonresidential building. Construction must begin after January 19, 2025 and before January 1, 2029, and the building must be placed in service in the United States after July 4, 2025 and before January 1, 2031. Lessors generally do not qualify ([Pub. 946](https://www.irs.gov/publications/p946)). Refer these cases.

## Section 179 on real property ([Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Pub. 946](https://www.irs.gov/publications/p946))

| Tax years beginning in | Maximum §179 deduction | Reduced dollar for dollar when §179 property placed in service exceeds |
| --- | --- | --- |
| 2026 | $2,560,000 | $4,090,000 |
| 2025 | $2,500,000 | $4,000,000 |

- **The 2025 amounts** are set by OBBBA §70306 for property placed in service in tax years beginning after December 31, 2024. They replace the lower 2025 amounts in Rev. Proc. 2024-40 ([Rev. Proc. 2025-32 §§2.10 and 3.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)).
- **Land and land improvements** (for example paved parking areas, fences, swimming pools, docks) are not §179 property. Use bonus for 15-year land improvements instead ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Business income limit:** the deduction cannot exceed taxable income from the active conduct of a trade or business. The excess carries forward ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Trade or business use only:** property used only to produce income, such as rental property where renting is not a trade or business, does not qualify ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Lodging:** property used mainly to furnish lodging does not qualify, except as allowed by §50(b)(2), for example for hotels. So §179 generally does not reach the contents of an apartment building ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Noncorporate lessors:** an individual, partnership or S corporation that leases property to others generally cannot take §179 on it. Two exceptions: property it manufactures, or property it buys where the lease term (including renewal options) is less than 50% of the class life *and*, for the first 12 months, its business deductions on the property (other than rents and reimbursed amounts) are more than 15% of the rental income. Corporations are not subject to this rule ([Pub. 946](https://www.irs.gov/publications/p946)).
- **Qualified real property election:** a taxpayer can elect to treat certain property as §179 property. That covers qualified improvement property, and roofs, HVAC, fire protection and alarm systems, and security systems added to nonresidential real property after it was first placed in service ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)). The §179 amount on real property is later recaptured under §1245 ([Pub. 544](https://www.irs.gov/publications/p544)).

## Catch-up on a building already in service: Form 3115 ([Rev. Proc. 2025-23 §6.01](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf); [Rev. Proc. 2015-13](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf))

- **When the change is a method change:** depreciating a component over too long a life is an impermissible method once it has been used on 2 or more consecutively filed returns. The fix is an automatic change under DCN 7 in Rev. Proc. 2025-23 §6.01. Once a method is adopted, it cannot be corrected by amending prior returns ([Pub. 946](https://www.irs.gov/publications/p946); [Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
- **Only 1 return filed** (property placed in service in the year just before the year of change): the owner can use Form 3115, or amend the placed-in-service year's return, but only before filing the return for the next year ([Rev. Proc. 2025-23 §6.01(1)(b)](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf)).
- **Conditions of DCN 7:** the property must be owned at the beginning of the year of change. DCN 7 cannot be used to make a late election or revoke an election, including a late bonus election-out or a late §179 election (that needs a letter ruling). It also cannot be used for a change in use or a change in placed-in-service date. A change from not claiming bonus to claiming it is covered only if the taxpayer did *not* elect out for that class ([Rev. Proc. 2025-23 §6.01(1)(c)](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf); [Pub. 946](https://www.irs.gov/publications/p946)).
- **The catch-up amount:** the §481(a) adjustment is the difference between the depreciation actually taken and the depreciation *allowable* under the proper method. That includes bonus at the rate that applied in the placed-in-service year, unless the taxpayer elected out. A negative adjustment (a deduction) is taken in full in the year of change. A positive adjustment is spread over 4 years, unless it is less than $50,000 and the taxpayer makes the de minimis election to take it in 1 year ([Rev. Proc. 2015-13 §7.03](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf)).
- **Required statements:** a detailed description of the old and new methods ("MACRS to MACRS" is not enough), the facts and law for the new classification, and each item's placed-in-service year. A taxpayer with average annual gross receipts of $10,000,000 or less for the 3 prior years may complete fewer Form 3115 lines ([Rev. Proc. 2025-23 §6.01(3) and (4)](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf)).
- **Filing:** attach the original Form 3115 to the timely filed return (including extensions) for the year of change. File a signed copy with the IRS in Ogden no earlier than the first day of the year of change and no later than the date the original is filed. There is no user fee for an automatic change ([Form 3115 instructions](https://www.irs.gov/instructions/i3115)). The Form 3115 instructions still cite an older list of automatic changes; use Rev. Proc. 2025-23.

## Recapture on sale ([Pub. 544](https://www.irs.gov/publications/p544); [26 U.S.C. §1(h)(6)](https://www.law.cornell.edu/uscode/text/26/1))

- **§1245 property (the 5- and 7-year items, and any §179 on real property):** gain is ordinary income up to all the depreciation allowed or allowable, including bonus and §179. Any gain above that is §1231 gain.
- **§1250 property held more than 1 year:** gain is ordinary income only to the extent of "additional depreciation", meaning depreciation above straight-line. A building on straight-line has none. But **bonus taken on §1250 property is additional depreciation**, for example on qualified improvement property. Pub. 544 shows this for qualified improvement property. The applicable percentage is 100% for residential and nonresidential property ([Pub. 544](https://www.irs.gov/publications/p544)). Land improvements can be §1245 or §1250 property depending on the asset ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)), so classify each one before you model the sale.
- **Unrecaptured §1250 gain:** the rest of the long-term gain on the building that comes from depreciation. It is taxed at a maximum of 25%, and it cannot exceed the net §1231 gain for the year ([Pub. 544](https://www.irs.gov/publications/p544); [26 U.S.C. §1(h)(6)](https://www.law.cornell.edu/uscode/text/26/1)).
- **C corporations** (not S corporations) also treat 20% of the excess of the §1245-style amount over the §1250 amount as ordinary income under §291 ([Pub. 544](https://www.irs.gov/publications/p544)).
- **Installment sales:** all §1245 and §1250 recapture is taxed in the year of sale, even if no payment is received that year ([Pub. 544](https://www.irs.gov/publications/p544)).
- **Allocate the sale price** to each asset and figure each gain separately; the allocation must be supportable ([Pub. 544](https://www.irs.gov/publications/p544)).
- **Prior §1231 losses:** a net §1231 gain is ordinary income up to the net §1231 losses of the previous 5 years that have not yet been recaptured ([Pub. 544](https://www.irs.gov/publications/p544)).

## Can the owner use the loss? At-risk, passive and excess business loss limits ([Pub. 925](https://www.irs.gov/publications/p925); [26 U.S.C. §469](https://www.law.cornell.edu/uscode/text/26/469))

- **At-risk (§465):** in the activity of holding real property, the owner is at risk for qualified nonrecourse financing secured by that real property. No one may be personally liable for it, it must not be convertible into an ownership interest, and it must come from, or be guaranteed by, a government, or come from a qualified person. A qualified person actively and regularly lends money, such as a bank. The seller (or anyone related to the seller) and anyone who gets a fee from the investment (or anyone related to them) never qualify. A lender related to the owner qualifies only if the loan is commercially reasonable and on the same terms as loans to unrelated people ([26 U.S.C. §465(b)(6)](https://www.law.cornell.edu/uscode/text/26/465); [Pub. 925](https://www.irs.gov/publications/p925)).
- **Rentals are passive** even with material participation, unless the owner is a real estate professional. Exception: an average customer stay of 7 days or less (or 30 days or less with significant personal services) is not a rental activity, so material participation decides ([Pub. 925](https://www.irs.gov/publications/p925)).
- **$25,000 special allowance:** an individual who *actively* participates (for example, approves tenants and sets rents) and owns, with the spouse, at least 10% by value of the activity for the whole year, can deduct up to $25,000 of rental loss against other income ([Pub. 925](https://www.irs.gov/publications/p925)).
  - The allowance is reduced by 50% of modified adjusted gross income above $100,000, so it is gone at $150,000 ([Pub. 925](https://www.irs.gov/publications/p925)).
  - Married filing separately and living apart all year: the limit is $12,500, reduced from $50,000 of MAGI and gone at $75,000. Married filing separately and living together at any time in the year: no allowance ([Pub. 925](https://www.irs.gov/publications/p925)).
  - Limited partners are generally not treated as actively participating.
- **Real estate professional (§469(c)(7)).** The individual must meet *both* tests for the year ([26 U.S.C. §469(c)(7)](https://www.law.cornell.edu/uscode/text/26/469)):
  - more than half of all personal services in all trades or businesses were in real property trades or businesses in which the individual materially participated; and
  - more than 750 hours in those real property trades or businesses.
- **Rules for the professional tests** ([26 U.S.C. §469(c)(7)](https://www.law.cornell.edu/uscode/text/26/469); [Pub. 925](https://www.irs.gov/publications/p925)):
  - On a joint return, one spouse must meet both tests alone. The spouse's hours cannot be added. The spouse's participation *does* count for material participation.
  - Work as an employee counts only if the individual owns more than 5% of the employer ([Pub. 925](https://www.irs.gov/publications/p925)).
  - A closely held C corporation qualifies if more than 50% of its gross receipts come from real property trades or businesses in which it materially participates ([26 U.S.C. §469(c)(7)](https://www.law.cornell.edu/uscode/text/26/469)).
- **Qualifying is not enough.** Each rental is a separate activity, and the professional must materially participate in it (for example, more than 500 hours). The alternative is the election to treat all interests in rental real estate as one activity, made by statement with the original return ([Pub. 925](https://www.irs.gov/publications/p925); Treas. Reg. §1.469-9(g)).
- **Suspended passive losses** carry forward. They are released when the owner disposes of the entire interest in a fully taxable transaction to an unrelated person ([26 U.S.C. §469(g)](https://www.law.cornell.edu/uscode/text/26/469)).
- **Excess business loss (§461(l))**, for noncorporate taxpayers, applies after the passive rules and is figured on Form 461. For tax years beginning in 2026, the threshold is $256,000 ($512,000 for joint returns) ([Rev. Proc. 2025-32 §4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)). For 2025 it is $313,000 ($626,000 joint) ([Rev. Proc. 2024-40 §2.32](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf)).
- **Partners and S corporation shareholders** apply the limits in this order: basis in the partnership interest (or S corporation stock plus shareholder loans), then at-risk, then passive, then the excess business loss limit (Form 461) ([Pub. 925](https://www.irs.gov/publications/p925)).

## Boundaries and exceptions

| Situation | Treatment | Source |
| --- | --- | --- |
| Contract signed before January 20, 2025, closing after | Acquired before January 20, 2025: no 100% rate. Use 40% for 2025 placement and the phase-down after that | [Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| Contract with a clause limiting damages (for example liquidated damages) | May not be a binding contract. Check the size of the clause under Treas. Reg. §1.168(k)-2(b)(5)(iii) before choosing the acquisition date. If it is not binding, apply the non-binding contract rule: the acquisition date is when more than 10% of the cost is paid or incurred | [Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| Electing real property trade or business (opted out of the §163(j) interest limit) | Building and qualified improvement property must use ADS, so no bonus on qualified improvement property. 5-, 7- and 15-year personal property and land improvements are not listed in §168(g)(8) | [Pub. 946](https://www.irs.gov/publications/p946) |
| Replacement property from a like-kind exchange | Bonus on carryover basis and excess basis if the property is new. If it is used, bonus on the excess basis only | [Pub. 946](https://www.irs.gov/publications/p946) |
| Look-back study where the owner elected out of bonus for that class | DCN 7 catch-up gives regular MACRS on the shorter lives only. Bonus cannot be added without IRS consent | [Rev. Proc. 2025-23](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf) |
| Rule-of-thumb percentage with no cost support | Not automatically rejected, but examined on its own merits. The documentation is typically weak | [Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf) |
| State return | May add back bonus or §179 | Use the `us-state-bonus-depreciation-conformity-matrix` Guide |

## Worked cases

Amounts marked "assumed" are illustrations, not official figures.

### Case 1: 2026 purchase of an office building, full bonus ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf); [Pub. 946](https://www.irs.gov/publications/p946))

- Contract signed and binding February 2026, closed March 2026. Price $3,000,000 (assumed). Land appraised at $600,000 (assumed), so the depreciable basis is $2,400,000.
- The study assigns: 5-year $240,000, 7-year $60,000, 15-year land improvements $300,000, and 39-year building $1,800,000 (all assumed). Check: 240,000 + 60,000 + 300,000 + 1,800,000 = 2,400,000.
- Acquired after January 19, 2025, not ADS, no election out. Bonus at 100% on 240,000 + 60,000 + 300,000 = $600,000.
- The $1,800,000 building uses 39-year straight-line, mid-month from March 2026.

### Case 2: contract signed before the OBBBA date ([Pub. 946](https://www.irs.gov/publications/p946); [Form 4562 instructions](https://www.irs.gov/instructions/i4562))

- Binding contract signed December 2024, closing February 2025, placed in service February 2025. The study finds $500,000 (assumed) of 5- and 15-year property.
- The property was acquired before January 20, 2025, so the 2025 rate is 40%: $500,000 × 40% = $200,000 bonus. The other 500,000 − 200,000 = $300,000 goes to regular MACRS. Claiming 100% here would be wrong.

### Case 3: look-back study, residential rental bought in 2019 ([Rev. Proc. 2025-23](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf); [Rev. Proc. 2015-13](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf))

- The owner depreciated everything over 27.5 years on the 2019 to 2025 returns and never elected out of bonus. A 2026 study moves $200,000 (assumed) into 5- and 15-year property.
- Bonus for property placed in service in 2019 was 100% ([Notice 2026-11 §2.01](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)). Assuming the 2019 purchase met the used-property rules (not bought from a related party and not previously used by the owner), the allowable depreciation on those components is $200,000. The 27.5-year depreciation actually claimed on them is $47,000 (assumed).
- The §481(a) adjustment is 200,000 − 47,000 = $153,000, negative, so it is deducted in full in 2026 under DCN 7. File Form 3115 with the 2026 return.
- Test whether the owner can use that deduction under the passive rules (see Case 5) before promising a benefit.

### Case 4: 2026 §179 phase-out ([Rev. Proc. 2025-32 §4.24](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf))

- A corporation places $4,200,000 (assumed) of §179 property in service in 2026.
- The limit is $2,560,000 − ($4,200,000 − $4,090,000) = $2,450,000, still subject to the business income limit.

### Case 5: special allowance phase-out ([Pub. 925](https://www.irs.gov/publications/p925))

- A single owner who actively participates has MAGI of $130,000 (assumed) and a $40,000 (assumed) rental loss driven by bonus. There is no other passive income.
- Reduction: 50% × ($130,000 − $100,000) = $15,000. Allowance: $25,000 − $15,000 = $10,000. The other $30,000 is suspended and carried forward.

### Case 6: real estate professional on a joint return ([26 U.S.C. §469(c)(7)](https://www.law.cornell.edu/uscode/text/26/469))

- Spouse A has a full-time W-2 job and 400 hours (assumed) on the rentals. Spouse B has no other work and 900 hours (assumed) on the rentals.
- B alone passes both tests (more than 750 hours, more than half of B's work), so the couple qualifies. A's hours cannot be added for these tests, but both spouses' hours count toward material participation in each rental (or in the single activity, if they elect to group).

### Case 7: sale after a cost segregation study ([Pub. 544](https://www.irs.gov/publications/p544))

- An individual sells a residential rental held for more than 1 year. The 5-year items had $100,000 (assumed) of bonus and now have an adjusted basis of zero. $10,000 (assumed) of the price is supportably allocated to them.
- §1245 ordinary income is the lesser of depreciation ($100,000) or gain ($10,000), so $10,000.
- The building had $180,000 (assumed) of straight-line depreciation and a gain of $400,000 (assumed), and there are no prior §1231 losses. The whole $400,000 is §1231 gain, treated as long-term capital gain. Of it, $180,000 is unrecaptured §1250 gain (maximum rate 25%, within the $400,000 net §1231 gain), and the other 400,000 − 180,000 = $220,000 gets the regular long-term capital gain rates.

## 2025 returns: tax year 2025, extended deadline October 15, 2026 ([Form 4562 instructions (2025)](https://www.irs.gov/instructions/i4562); [IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return))

- **Split 2025 placements by acquisition date.** Property acquired after January 19, 2025 gets 100%. Property acquired before January 20, 2025 gets 40% (60% for long production period property and certain aircraft) ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
- **The 40%/60% §168(k)(10) election** is for property acquired after January 19, 2025 and placed in service in the tax year that includes January 20, 2025. It is made by statement on the timely filed 2025 return, including extensions ([Notice 2026-11 §4.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **§179 for tax years beginning in 2025:** $2,500,000, reduced by the excess over $4,000,000 of §179 property placed in service ([Rev. Proc. 2025-32 §3.02](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf)).
- **Form 3115 for a 2025 year of change** goes with the timely filed 2025 return, including extensions (Rev. Proc. 2015-13 §6.03(4)(a) may give an automatic 6-month extension) ([Form 3115 instructions](https://www.irs.gov/instructions/i3115)).
- **Partnerships and S corporations** have earlier due dates; check the entity's own deadline.

## When to refuse or refer

- **Refuse** to put a percentage of basis into 5-, 7- or 15-year property from a rule of thumb or a sales brochure. Get a study with cost support, or classify item by item from records ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
- **Refuse** to claim 100% bonus until the binding contract date (or construction start date) is documented as after January 19, 2025 ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Refer** the study itself to a preparer who knows construction, cost estimating and the tax law ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
- **Refer** real estate professional claims that rest on thin or reconstructed time records.
- **Refer** qualified production property (§168(n)), long production period property, the component election for projects begun before January 20, 2025, consolidated groups, and public utility property.
- **Refer** a Form 3115 filed while the taxpayer is under IRS examination. Audit protection and eligibility depend on the timing windows in Rev. Proc. 2015-13 ([Rev. Proc. 2015-13](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf)).
- **Refer** sales inside a like-kind exchange where §1245 property is given up and only §1250 property is received, because recapture can arise even without boot ([Pub. 544](https://www.irs.gov/publications/p544)).
- **Do not state** any state's treatment. Point to the `us-state-bonus-depreciation-conformity-matrix` Guide and the state's own rules.

## Filing and payment

- **Form 4562:** §179 in Part I, bonus in Part II line 14, and MACRS in Part III (mid-month "MM" for the building). Attach it to the return for the year the property is placed in service ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
- **Elections by statement** (election out by class, the §168(k)(10) election, the qualified production property designation) go on the timely filed return, including extensions ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
- **Form 3115:** attach the original to the return for the year of change, and send a signed copy to the IRS in Ogden ([Form 3115 instructions](https://www.irs.gov/instructions/i3115)).
- **Losses:** Form 6198 (at-risk) and Form 8582 (passive loss) where they apply ([Pub. 925](https://www.irs.gov/publications/p925)). A real estate professional reports on Schedule E line 43.
- **Sale:** Form 4797 for recapture and §1231 gain. The Unrecaptured Section 1250 Gain Worksheet is in the Schedule D instructions ([Pub. 544](https://www.irs.gov/publications/p544)).
- **Deadlines:** an individual's return and payment are due by the April filing date. An extension moves only the filing date, to October 15, and tax paid late accrues interest and any late-payment penalty from April ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).

## Completion checklist

- Land is allocated out at fair market value and excluded from every class.
- The study has a methodology narrative, cost support that reconciles to total cost, and a legal analysis of each §1245 item ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
- The binding contract or construction start date is documented against January 19, 2025, and the matching bonus rate is used.
- ADS status and any prior election out are checked.
- §179 is tested against the lessor, lodging and business income limits, using the right year's figures.
- For a building already in service, DCN 7 conditions are met and the §481(a) adjustment and period are computed.
- Basis, at-risk, passive, real estate professional and excess business loss limits are applied in order, and suspended amounts are recorded.
- Recapture on a future sale is modelled and explained to the client.
- State treatment is checked separately.

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
