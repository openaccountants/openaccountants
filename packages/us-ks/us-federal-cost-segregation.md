---
name: us-federal-cost-segregation
description: Cost segregation for US real property in tax year 2026. Splits a building's cost into 5-, 7- and 15-year property and the 27.5- or 39-year building, fixes the bonus depreciation rate from the binding contract date (100 percent for property acquired after 19 January 2025, 20 percent for older contracts placed in service in 2026), catches up a building already in service with Form 3115 (DCN 7) and a section 481(a) adjustment, tests whether the owner can use the loss (at-risk, passive activity, the USD 25,000 allowance, real estate professional, excess business loss) and models recapture on sale. Trigger on "cost segregation", "cost seg study", "look-back study", "accelerate depreciation on a building", "Form 3115 depreciation catch-up", "bonus on a rental property". Federal only.
version: "2.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US federal cost segregation for real property, tax year 2026

> **Source-cited draft.** Built from Public Law 119-21 section 70301, IRS Notice 2026-11, 26 U.S.C. 168, 465 and 469, Rev. Proc. 2025-32, Rev. Proc. 2025-23, Rev. Proc. 2015-13, the Cost Segregation Audit Techniques Guide (Pub. 5653) and Pubs. 544, 925 and 946 (2025 editions), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A cost segregation study moves parts of a building's cost out of the 27.5-year (residential rental) or 39-year (nonresidential) class into 5-, 7- and 15-year property. It changes the timing of depreciation, not the total. The early deduction comes mostly from bonus depreciation on those short-life parts: **100 percent** if the property was acquired (binding written contract date) after **January 19, 2025**, and **20 percent** if it was acquired before 20 January 2025 and placed in service in 2026. A building already in service is caught up with Form 3115 (automatic change DCN 7) and a section 481(a) adjustment, not by amending returns. Before promising a benefit, test whether the owner can use the loss: rentals are passive unless the owner is a real estate professional, and the USD 25,000 special allowance is gone at modified AGI of USD 150,000.

## Scope and who this is for

In scope: individuals, partnerships, S corporations and C corporations that own a building used in a business or held for rent, for tax year 2026: new construction, purchases, improvements, and look-back studies on buildings already in service. The result lands on Form 4562 (and Form 3115 for a catch-up), then Schedule E, Form 8825, Form 1065 or Form 1120 as the owner's return requires, with Forms 6198, 8582 and 461 for the loss limits and Form 4797 on sale.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Section 179 dollar limit and phase-out for 2026, bonus depreciation on equipment, vehicle caps | `us-section-179-and-bonus-depreciation` |
| State conformity to federal bonus and section 179 | `us-state-bonus-depreciation-conformity-matrix`, then the state's own rules |
| Rental income and expenses on Schedule E | `us-schedule-e-rental-income` |
| Real estate professional status and short-term rentals in depth | `us-real-estate-professional-and-short-term-rentals` |
| Like-kind exchange mechanics | `us-section-1031-like-kind-exchange` |
| Capital gains rates on a later sale | `us-capital-gains` |
| Net operating loss created by the deduction | `us-net-operating-loss-172` |
| Personal residences, dealer property, property used mainly abroad, housing and rehabilitation credits | not covered |

## Ask the client first

1. **Which tax year, which entity, which year-end.** Individual, partnership, S corporation or C corporation; calendar or fiscal year.
2. **The acquisition date.** For a purchase: the date the written contract was signed, whether it was binding (no clause limiting damages to a fixed amount), when any cancellation period or contingency ended, and the closing date. For construction: when physical work of a significant nature began, and when more than 10 percent of the total cost (excluding land and planning) was paid or incurred ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
3. **Placed-in-service dates and use.** The building and each later improvement; whether it is residential rental (80 percent or more of gross rental income from dwelling units), nonresidential, or short-term lodging ([Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf)).
4. **Cost records and past returns.** Purchase agreement, appraisal, assessment and closing statement, or construction contracts, change orders and invoices. How the property has been depreciated on returns already filed, and whether the owner ever elected out of bonus for any class. Whether the business is an electing real property trade or business (opted out of the business interest limit), which forces the building and qualified improvement property onto ADS.
5. **Who can use the loss.** Hours in real property trades or businesses, hours in all other work (including a W-2 job), the owner's and spouse's share of the rental (at least 10 percent?), modified AGI, and whether the financing is recourse or nonrecourse and from whom ([Pub. 925](https://www.irs.gov/pub/irs-pdf/p925.pdf)).
6. **Exit plans.** Any plan to sell, exchange or convert the property in the next few years: this drives recapture.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Bonus depreciation, property acquired after the start date | 100 percent | [Public Law 119-21, section 70301](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Start date: the 100 percent rule applies to property acquired after | January 19, 2025 | [Public Law 119-21, section 70301](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Election for the first tax year ending after 19 January 2025 (2025 for a calendar year): elect this rate instead of 100 percent | 40 percent | [Public Law 119-21, section 70301](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Bonus, property acquired before 20 January 2025 and placed in service in 2026 (pre-Act phase-down) | 20 percent | [26 U.S.C. 168(k)(6)(A)(v)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Bonus, property acquired before 20 January 2025 and placed in service in 2025 | 40 percent | [Notice 2026-11, section 2.01](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| Self-constructed property: safe harbor for when physical work begins (share of total cost paid or incurred, excluding land and preliminary work) | more than 10 percent | [Notice 2026-11, section 2.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| Residential rental property: share of gross rental income from dwelling units | 80 percent or more | [Pub. 946 (2025)](https://www.irs.gov/pub/irs-pdf/p946.pdf) |
| Mid-quarter convention applies if property placed in service in the last 3 months is more than this share of the year's depreciable bases | 40 percent | [Pub. 946 (2025)](https://www.irs.gov/pub/irs-pdf/p946.pdf) |
| 39-year nonresidential real property, first-year rate, placed in service in month 3 (Table A-7a) | 2.033% | [Pub. 946 (2025), Table A-7a](https://www.irs.gov/pub/irs-pdf/p946.pdf) |
| Positive section 481(a) adjustment taken in one year by election if less than | USD 50,000 | [Rev. Proc. 2015-13, section 7.03(3)(c)](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf) |
| Form 3115 automatic change number for impermissible to permissible depreciation | DCN 7 | [Rev. Proc. 2025-23, section 6.01](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf) |
| Passive loss special allowance for rental real estate (active participation) | USD 25,000 | [26 U.S.C. 469(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Allowance reduced by 50 percent of modified AGI above | USD 100,000 | [26 U.S.C. 469(i)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Allowance gone at modified AGI of | USD 150,000 | [Pub. 925 (2025)](https://www.irs.gov/pub/irs-pdf/p925.pdf) |
| Married filing separately, living apart all year: allowance | USD 12,500 | [26 U.S.C. 469(i)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Real estate professional: hours in real property trades or businesses | more than 750 hours | [26 U.S.C. 469(c)(7)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Real estate professional: share of all personal services in real property trades or businesses | more than one-half | [26 U.S.C. 469(c)(7)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm) |
| Excess business loss threshold, 2026 | USD 256,000 | [Rev. Proc. 2025-32, section 4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Excess business loss threshold, 2026, joint returns | USD 512,000 | [Rev. Proc. 2025-32, section 4.31](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Unrecaptured section 1250 gain, maximum rate | 25% | [26 U.S.C. 1(h)(1)(E)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm) |
| C corporations: extra ordinary income on section 1250 property under section 291 | 20% | [Pub. 544 (2025)](https://www.irs.gov/pub/irs-pdf/p544.pdf) |

The section 179 dollar limit and phase-out for 2026 are in `us-section-179-and-bonus-depreciation`; this skill covers only how section 179 applies to real property.

### Steps

1. **Fix the basis and take out the land.** Land is never depreciable. Allocate a lump-sum price between land and building in proportion to their fair market values at purchase; if the values are unclear, the property tax assessment ratio can be used ([Pub. 527](https://www.irs.gov/publications/p527); [Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf)).
2. **Get the study.** The IRS sets no required method. The Audit Techniques Guide says the detailed engineering approach from actual cost records is generally the most accurate, and that it is generally available only for new construction. For a purchase, the study must allocate the price using fair market values and appraisal methods ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
3. **Classify each component** as section 1245 property (personal property: 5- or 7-year) or section 1250 property (the building and its structural components: 27.5 or 39 years). Land improvements such as roads, fences and shrubbery are 15-year property. There is no bright-line test: the guide uses the six Whiteco factors on permanence and asks whether the item is a structural component ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf); [Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf)).
4. **Test each short-life component for bonus** (qualified property, not on ADS, used-property rules) and fix its acquisition date against January 19, 2025 ([Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
5. **Apply the bonus rate** from the table. Bonus is taken after any section 179 deduction and before regular MACRS ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
6. **Consider section 179** only where it is allowed on real property and adds something bonus does not (see "Section 179 on real property").
7. **Depreciate the rest under regular MACRS.** The building: straight line, mid-month convention. 5- and 7-year property: 200 percent declining balance; 15-year land improvements: 150 percent declining balance; both generally half-year convention, unless the 40 percent mid-quarter test is met ([Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf)).
8. **Test whether the loss can be used**: for partners and S corporation shareholders basis first, then at-risk, then passive activity, then (noncorporate taxpayers) excess business loss ([Pub. 925](https://www.irs.gov/pub/irs-pdf/p925.pdf)).
9. **For a building already in service, catch up with Form 3115** under DCN 7 and take the section 481(a) adjustment. Do not amend prior returns once a method has been adopted ([Rev. Proc. 2025-23, section 6.01](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf)).
10. **Model the exit** before the client relies on the deduction: section 1245 recapture on the short-life assets, section 1250 ordinary recapture where bonus was taken on section 1250 property, and unrecaptured section 1250 gain on the building ([Pub. 544](https://www.irs.gov/pub/irs-pdf/p544.pdf)).

### Recovery periods

Sources: [Pub. 946 (2025)](https://www.irs.gov/pub/irs-pdf/p946.pdf); [Pub. 527](https://www.irs.gov/publications/p527).

| Class | Typical cost segregation items | Method and convention |
| --- | --- | --- |
| 5-year | Appliances, carpets and furniture used in a residential rental activity; computers; office machinery | 200% DB, half-year (or mid-quarter) |
| 7-year | Office furniture and fixtures; property with no class life and not assigned to another class | 200% DB, half-year (or mid-quarter) |
| 15-year | Land improvements (shrubbery, fences, roads, sidewalks, bridges); qualified improvement property placed in service after 2017 | 150% DB for land improvements; straight line for qualified improvement property; half-year (or mid-quarter) |
| 27.5-year | Residential rental building and its structural components (furnace, water pipes, venting) | Straight line, mid-month |
| 39-year | Nonresidential building (office, store, warehouse) and its structural components | Straight line, mid-month |

- **Residential rental property** is a building where 80 percent or more of the gross rental income for the year is from dwelling units. A unit in a hotel or motel where more than half the units are used on a transient basis is not a dwelling unit ([Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf)).
- **Qualified improvement property** is "any improvement made by the taxpayer to an interior portion of a building which is nonresidential real property if such improvement is placed in service after the date such building was first placed in service" ([26 U.S.C. 168(e)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm)). Interior improvements already in a building when it is bought are not qualified improvement property in the buyer's hands. It excludes enlarging the building, elevators and escalators, and the internal structural framework. Improvements to a residential rental building are never qualified improvement property.

### Bonus depreciation: the acquisition date decides the rate

Sources: [Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf); [Public Law 119-21, section 70301](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [26 U.S.C. 168(k)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm).

| Property | Rate | Conditions |
| --- | --- | --- |
| Acquired after January 19, 2025, placed in service in 2026 | 100% | Permanent under the Act: no placed-in-service deadline and no further phase-down. The taxpayer may still elect out, class by class. [Public Law 119-21, section 70301](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Acquired after January 19, 2025, placed in service in the first tax year ending after that date (2025 for a calendar year) | 100%, or 40% if elected (60% for long production period property and certain aircraft) | The section 168(k)(10) election is made by statement on the timely filed return, including extensions, for that year ([Notice 2026-11, section 4.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)). |
| Acquired after September 27, 2017 and before January 20, 2025, placed in service in 2025 | 40% (60% for long production period property and certain aircraft) | Pre-Act phase-down. The 100% rate is not available. [Notice 2026-11, section 2.01](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| Acquired before January 20, 2025, placed in service in 2026 | 20% | Pre-Act section 168(k)(6)(A)(v). Long production period property and certain aircraft follow section 168(k)(6)(B); check the 2026 Form 4562 instructions when published. [26 U.S.C. 168(k)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |

- **"Acquired" means the binding contract date, not the closing date.** Property is not treated as acquired after the date a written binding contract for it is entered into (Act section 70301(c)). A binding contract is enforceable under state law and does not limit damages to a fixed amount. The acquisition date is the latest of the signing date, the date it becomes enforceable, the end of any cancellation period, and the date every contingency is met ([Notice 2026-11, sections 2.03 and 3.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Non-binding contract:** the acquisition date is when the taxpayer paid or incurred more than 10 percent of the total cost, excluding land and preliminary activities ([Notice 2026-11, section 2.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Self-constructed property** is acquired when physical work of a significant nature begins; under the safe harbor, when more than 10 percent of the total cost is paid or incurred, excluding land and preliminary work such as planning, design and financing. A component election can treat components acquired after January 19, 2025 as eligible even though the larger project began earlier ([Notice 2026-11, sections 2.03, 3.05 and 4](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Reliance:** Notice 2026-11 is interim guidance. A taxpayer who relies on it must follow sections 3 to 5 in full for all eligible property ([Notice 2026-11, section 6.02](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- **Not eligible:** the building itself (27.5 or 39 years is more than 20 years), land, and any property that must use ADS. ADS covers "nonresidential real property, residential rental property, and qualified improvement property held by an electing real property trade or business" ([26 U.S.C. 168(g)(8)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm)).
- **Used property** qualifies only if the taxpayer never used it before acquiring it, and the acquisition meets the section 179(d) purchase rules, which exclude property bought from a related party or received with a carryover basis ([26 U.S.C. 168(k)(2)(E)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm)).
- **Election out** is made class by class (for example all 5-year property) for everything in that class placed in service in the year, by statement on the timely filed return, including extensions. If the return was filed on time without it, it can still be made on an amended return filed within 6 months of the original due date (excluding extensions), marked "Filed pursuant to section 301.9100-2". It cannot be revoked without IRS consent ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
- **Qualified production property (section 168(n))** is a separate elective 100 percent allowance for the manufacturing part of a nonresidential building: construction must begin after January 19, 2025 and before January 1, 2029, and the property must be placed in service in the United States after July 4, 2025 and before January 1, 2031. Property a lessor leases out is not used by the lessor in a qualified production activity ([Public Law 119-21, section 70307](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm); [Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf)). Refer these cases.

### Section 179 on real property

The 2026 dollar limit and phase-out are in `us-section-179-and-bonus-depreciation`. On real property ([Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf); [Form 4562 instructions](https://www.irs.gov/instructions/i4562)):

- **Land and land improvements** (paved parking areas, fences, swimming pools, docks) are not section 179 property. Use bonus for 15-year land improvements instead.
- **Business income limit:** the deduction cannot exceed taxable income from the active conduct of a trade or business; the excess carries forward.
- **Trade or business use only:** property used only to produce income, such as rental property where renting is not a trade or business, does not qualify.
- **Lodging:** property used mainly to furnish lodging does not qualify, except as allowed by section 50(b)(2) (for example hotels). So section 179 generally does not reach the contents of an apartment building.
- **Noncorporate lessors** (individuals, partnerships, S corporations) generally cannot take section 179 on property they lease out. Two exceptions: property they manufacture, or property where the lease term (with renewals) is less than 50 percent of the class life and, for the first 12 months, business deductions on the property (other than rents and reimbursed amounts) exceed 15 percent of the rental income. Corporations are not subject to this rule.
- **Qualified real property election:** a taxpayer can elect to treat qualified improvement property, and roofs, HVAC, fire protection and alarm systems and security systems added to nonresidential real property after it was first placed in service, as section 179 property. Section 179 on real property is later recaptured under section 1245 ([Pub. 544](https://www.irs.gov/pub/irs-pdf/p544.pdf)).

### Catch-up on a building already in service: Form 3115

Sources: [Rev. Proc. 2025-23, section 6.01](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf); [Rev. Proc. 2015-13](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf); [Form 3115 instructions](https://www.irs.gov/instructions/i3115).

- **It is a method change.** Depreciating a component over too long a life is an impermissible method once used on 2 or more consecutively filed returns. The fix is the automatic change DCN 7 ("The designated automatic accounting method change number for a change under this section 6.01 is 7"). Once a method is adopted, it cannot be corrected by amending prior returns ([Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf); [Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)).
- **Only 1 return filed** (property placed in service in the year just before the year of change): use Form 3115, or amend the placed-in-service year's return, but only before filing the return for the next year (Rev. Proc. 2025-23, section 6.01(1)(b)).
- **Conditions of DCN 7:** the property must be owned at the beginning of the year of change. DCN 7 cannot make a late election or revoke one (a late bonus election-out or a late section 179 election needs a letter ruling), and cannot be used for a change in use or a change in placed-in-service date. Moving from not claiming bonus to claiming it is covered only if the taxpayer did not elect out for that class (Rev. Proc. 2025-23, section 6.01(1)(c)).
- **The catch-up amount:** the section 481(a) adjustment is the depreciation allowable under the proper method minus the depreciation actually taken, including bonus at the rate that applied in the placed-in-service year (unless the taxpayer elected out). A negative adjustment (a deduction) is taken in full in the year of change. A positive adjustment is spread over four taxable years, unless it is less than USD 50,000 and the taxpayer elects to take it in one year ([Rev. Proc. 2015-13, section 7.03](https://www.irs.gov/pub/irs-drop/rp-15-13.pdf)).
- **Required statements:** a detailed description of the old and new methods ("MACRS to MACRS" is not enough), the facts and law for the new classification, and each item's placed-in-service year. A taxpayer with average annual gross receipts of USD 10,000,000 or less for the 3 prior years may complete fewer Form 3115 lines (Rev. Proc. 2025-23, section 6.01(3) and (4)).
- **Filing:** attach the original Form 3115 to the timely filed return (including extensions) for the year of change, and file a signed copy with the IRS in Ogden no earlier than the first day of the year of change and no later than the date the original is filed. No user fee for an automatic change. The Form 3115 instructions (Rev. December 2022) still cite an older list of automatic changes; use Rev. Proc. 2025-23.

### Can the owner use the loss?

Sources: [Pub. 925 (2025)](https://www.irs.gov/pub/irs-pdf/p925.pdf); [26 U.S.C. 465](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec465.htm); [26 U.S.C. 469](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm).

- **Order:** partners and S corporation shareholders apply basis (partnership interest, or S corporation stock plus shareholder loans), then at-risk, then passive, then the excess business loss limit (Form 461).
- **At-risk (section 465):** in holding real property, the owner is at risk for qualified nonrecourse financing secured by that property. No one may be personally liable for it, it must not be convertible into an ownership interest, and it must come from (or be guaranteed by) a government, or come from a qualified person: one who actively and regularly lends money, such as a bank. The seller (or anyone related to the seller) and anyone who gets a fee from the investment (or anyone related to them) never qualify. A lender related to the owner qualifies only if the loan is commercially reasonable and on the same terms as loans to unrelated people (section 465(b)(6)).
- **Rentals are passive** even with material participation, unless the owner is a real estate professional. Exception: an average customer stay of seven days or less (or 30 days or less with significant personal services) is not a rental activity, so material participation decides. Detail in `us-real-estate-professional-and-short-term-rentals`.
- **USD 25,000 special allowance:** an individual who actively participates (approves tenants, sets rents) and owns, with the spouse, at least 10 percent by value of the activity for the whole year can deduct up to USD 25,000 of rental loss against other income. It is reduced by 50 percent of modified AGI above USD 100,000, so it is gone at USD 150,000. Married filing separately and living apart all year: USD 12,500, reduced from USD 50,000 of modified AGI and gone at USD 75,000. Married filing separately and living together at any time in the year: none. Limited partners are generally not treated as actively participating.
- **Real estate professional (section 469(c)(7)):** both tests for the year: more than one-half of all personal services in trades or businesses were in real property trades or businesses in which the individual materially participated, and more than 750 hours in them. On a joint return one spouse must meet both tests alone (the spouse's hours cannot be added for these tests, but do count for material participation). Employee work counts only if the individual owns more than 5 percent of the employer. A closely held C corporation qualifies if more than 50 percent of its gross receipts come from real property trades or businesses in which it materially participates.
- **Qualifying is not enough.** Each rental is a separate activity and the professional must materially participate in it (for example more than 500 hours), unless the owner elects to treat all interests in rental real estate as one activity, by statement with the original return (Treas. Reg. 1.469-9(g)).
- **Suspended passive losses** carry forward and are released when the owner disposes of the entire interest in a fully taxable transaction to an unrelated person (section 469(g)).
- **Excess business loss (section 461(l))**, for noncorporate taxpayers, applies after the passive rules, on Form 461: for 2026 the threshold is USD 256,000 (USD 512,000 joint).

### Recapture on sale

Sources: [Pub. 544 (2025)](https://www.irs.gov/pub/irs-pdf/p544.pdf); [26 U.S.C. 1(h)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm).

- **Section 1245 property** (the 5- and 7-year items, and any section 179 on real property): gain is ordinary income up to all depreciation allowed or allowable, including bonus and section 179. Gain above that is section 1231 gain.
- **Section 1250 property held more than 1 year:** gain is ordinary income only to the extent of additional depreciation (above straight line). A building on straight line has none, but **bonus taken on section 1250 property is additional depreciation**, for example on qualified improvement property. Land improvements can be section 1245 or section 1250 property depending on the asset ([Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf)), so classify each before modelling the sale.
- **Unrecaptured section 1250 gain:** the rest of the long-term gain on the building that comes from depreciation, taxed at a maximum of 25 percent, and not more than the net section 1231 gain for the year.
- **C corporations** (not S corporations) also treat 20 percent of the excess of the section 1245-style amount over the section 1250 amount as ordinary income under section 291.
- **Installment sales:** all section 1245 and 1250 recapture is taxed in the year of sale, even if no payment is received that year (see `us-installment-sale-6252`).
- **Allocate the sale price** to each asset and figure each gain separately; the allocation must be supportable.
- **Prior section 1231 losses:** a net section 1231 gain is ordinary income up to the unrecaptured net section 1231 losses of the previous 5 years.

### 2025 returns still open (extended to 15 October 2026)

- Split 2025 placements by acquisition date: acquired after January 19, 2025 gets 100 percent (or 40 percent, 60 percent for long production period property and certain aircraft, under the section 168(k)(10) election made by statement on the timely filed 2025 return, including extensions); acquired before January 20, 2025 gets 40 percent (60 percent for long production period property and certain aircraft) ([Form 4562 instructions (2025)](https://www.irs.gov/instructions/i4562); [Notice 2026-11, section 4.03](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)).
- Section 179 for tax years beginning in 2025: see `us-section-179-and-bonus-depreciation`.
- Form 3115 for a 2025 year of change goes with the timely filed 2025 return, including extensions (Rev. Proc. 2015-13, section 6.03(4)(a) may give an automatic 6-month extension). Excess business loss for 2025: USD 313,000 (USD 626,000 joint) ([Rev. Proc. 2024-40, section 2.32](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf)).
- Partnerships and S corporations have earlier due dates; check the entity's own deadline.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Contract signed before 20 January 2025, closing after | Acquired before 20 January 2025: no 100 percent rate. 40 percent if placed in service in 2025, 20 percent in 2026 | [Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf); [26 U.S.C. 168(k)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Contract with a clause limiting damages (liquidated damages) | May not be binding. Check the size of the clause under Treas. Reg. 1.168(k)-2(b)(5)(iii). If not binding, the acquisition date is when more than 10 percent of the cost is paid or incurred | [Notice 2026-11](https://www.irs.gov/pub/irs-drop/n-26-11.pdf) |
| Electing real property trade or business | Building and qualified improvement property must use ADS, so no bonus on qualified improvement property. 5-, 7- and 15-year personal property and land improvements are not listed in section 168(g)(8) | [26 U.S.C. 168(g)(8)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| Replacement property from a like-kind exchange | Bonus on carryover basis and excess basis if the property is new; if used, on the excess basis only | [Pub. 946](https://www.irs.gov/pub/irs-pdf/p946.pdf) |
| Look-back study where the owner elected out of bonus for that class | DCN 7 gives regular MACRS on the shorter lives only; bonus cannot be added without IRS consent | [Rev. Proc. 2025-23](https://www.irs.gov/pub/irs-drop/rp-25-23.pdf) |
| Rule-of-thumb percentage with no cost support | Not automatically rejected, but examined on its merits; documentation is typically weak | [Pub. 5653](https://www.irs.gov/pub/irs-pdf/p5653.pdf) |
| Interior improvements already in a bought building | Not qualified improvement property for the buyer; classify through the study | [26 U.S.C. 168(e)(6)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm) |
| State return | May add back bonus or section 179 | `us-state-bonus-depreciation-conformity-matrix` |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Binding contract date | Treat as before 20 January 2025 (the lower rate) until the contract is documented |
| Land value | No depreciation on the disputed part until an appraisal or the assessment ratio supports the split |
| Whether an election out was ever made | Ask for prior returns; do not claim bonus in a look-back until confirmed |
| Electing real property trade or business status | Ask; if unknown, do not take bonus on qualified improvement property |
| Real estate professional hours | Not a professional; apply the USD 25,000 allowance and its phase-out |
| Modified AGI | Ask; do not promise the special allowance |
| Exit plan | Assume a sale within 5 years and show the recapture |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Study priced as a percentage of the deduction, or built on a rule of thumb | Weak support on examination (Pub. 5653) |
| Owner has a full-time W-2 job but claims real estate professional status | The more-than-one-half test usually fails |
| Modified AGI over USD 150,000 and no professional status | The bonus loss is likely suspended |
| Sale or exchange planned soon after the study | Section 1245 recapture at ordinary rates can exceed the benefit |
| Form 3115 filed while under IRS examination | Audit protection depends on Rev. Proc. 2015-13 windows |
| Property bought from a related party | Used property fails the section 179(d) purchase rules: no bonus |

## Worked cases

Amounts in these cases are invented; rates come from the rates table.

**Case 1, a decision: is the study worth it on a 2026 office purchase?** A binding contract signed February 2026, closed and placed in service March 2026, price USD 3,000,000, land appraised at USD 600,000, so building basis USD 2,400,000. Without a study, the whole basis is 39-year property: first-year depreciation is USD 2,400,000 x 2.033% (Table A-7a, month 3) = USD 48,792. The study assigns 5-year USD 240,000, 7-year USD 60,000, 15-year land improvements USD 300,000 and 39-year building USD 1,800,000. Acquired after January 19, 2025, not ADS, no election out: 100 percent bonus on USD 600,000, plus USD 1,800,000 x 2.033% = USD 36,594 on the building, total USD 636,594. The study adds USD 587,802 of first-year deduction. Recommend the study if the owner can use the deduction this year (a C corporation, or an individual who is a real estate professional or has other passive income) and does not plan to sell soon; if the loss would only be suspended, the benefit is timing at best and the study fee may not pay back.

```oa-check
name: Cost segregation decision, 2026 office purchase
inputs:
  building_basis: 2400000
  short_life: 600000
  building_after_study: 1800000
  rate_39yr_month3: 0.02033
  bonus_rate: 1.00
steps:
  - without_study: building_basis * rate_39yr_month3
  - with_study: short_life * bonus_rate + building_after_study * rate_39yr_month3
  - extra_deduction: with_study - without_study
expected:
  without_study: 48792.00
  with_study: 636594.00
  extra_deduction: 587802.00
```

**Case 2, look-back study and the passive allowance.** A single owner bought a residential rental in 2019 and depreciated everything over 27.5 years on the 2019 to 2025 returns, never electing out of bonus. A 2026 study moves USD 200,000 into 5- and 15-year property. Bonus for property placed in service in 2019 was 100 percent ([Notice 2026-11, section 2.01](https://www.irs.gov/pub/irs-drop/n-26-11.pdf)); assuming the 2019 purchase met the used-property rules, the allowable depreciation on those parts is USD 200,000 and the 27.5-year depreciation claimed on them was USD 47,000. The section 481(a) adjustment is USD 153,000, negative, so it is deducted in full in 2026 under DCN 7, with Form 3115 attached to the 2026 return. The rental otherwise makes USD 20,000 net, so the 2026 rental loss is USD 133,000. The owner actively participates, is not a real estate professional and has modified AGI of USD 130,000: the allowance is USD 25,000 minus 50% x (USD 130,000 minus USD 100,000) = USD 10,000. USD 123,000 is suspended and carried forward.

```oa-check
name: Look-back 481(a) adjustment and the special allowance (2026)
inputs:
  allowable: 200000
  claimed: 47000
  rental_net_before: 20000
  magi: 130000
steps:
  - adjustment_481a: allowable - claimed
  - rental_loss: adjustment_481a - rental_net_before
  - allowance: max(25000 - max(magi - 100000, 0) * 0.5, 0)
  - allowed: min(allowance, rental_loss)
  - suspended: rental_loss - allowed
expected:
  adjustment_481a: 153000.00
  rental_loss: 133000.00
  allowance: 10000.00
  suspended: 123000.00
```

**Case 3, contract signed before the Act's date.** Binding contract December 2024, closing and placed in service February 2025. The study finds USD 500,000 of 5- and 15-year property. Acquired before 20 January 2025, so the 2025 rate is 40 percent: USD 200,000 bonus, and USD 300,000 to regular MACRS. Claiming 100 percent would be wrong. Had the same property been placed in service in 2026, the rate would be 20 percent.

**Case 4, real estate professional on a joint return.** Spouse A has a full-time W-2 job and 400 hours on the rentals; Spouse B has no other work and 900 hours on the rentals. B alone passes both tests (more than 750 hours, more than one-half of B's work), so the couple qualifies. A's hours cannot be added for these tests, but both spouses' hours count toward material participation in each rental (or in the single activity, if they elect to group).

**Case 5, sale after a study.** An individual sells a residential rental held more than 1 year. The 5-year items had USD 100,000 of bonus and now have zero basis; USD 10,000 of the price is supportably allocated to them, so section 1245 ordinary income is the lesser of depreciation (USD 100,000) or gain (USD 10,000): USD 10,000. The building had USD 180,000 of straight-line depreciation and a gain of USD 400,000, with no prior section 1231 losses. The whole USD 400,000 is section 1231 gain treated as long-term capital gain: USD 180,000 is unrecaptured section 1250 gain (maximum 25 percent) and USD 220,000 gets the regular long-term rates (see `us-capital-gains`).

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-CS-THUMB | Asked to put a percentage of basis into 5-, 7- or 15-year property from a rule of thumb or sales brochure | Refuse: get a study with cost support, or classify item by item from records (Pub. 5653) |
| R-CS-DATE | 100 percent bonus claimed without a documented binding contract or construction start after January 19, 2025 | Refuse until documented |
| R-CS-STUDY | The engineering study itself | Refer to a preparer who knows construction, cost estimating and the tax law |
| R-CS-REP | Real estate professional claim resting on thin or reconstructed time records | Refer |
| R-CS-SPECIAL | Qualified production property (section 168(n)), long production period property, the component election for projects begun before 20 January 2025, consolidated groups, public utility property | Refer |
| R-CS-EXAM | Form 3115 while the taxpayer is under IRS examination | Refer: audit protection and eligibility depend on Rev. Proc. 2015-13 timing windows |
| R-CS-1031 | Like-kind exchange where section 1245 property is given up and only section 1250 property is received | Refer: recapture can arise even without boot (Pub. 544) |
| R-CS-STATE | Any state's treatment | Do not state it; use `us-state-bonus-depreciation-conformity-matrix` and the state's rules |

## Filing and payment

- **Form 4562:** section 179 in Part I, bonus in Part II line 14, MACRS in Part III (mid-month "MM" for the building), attached to the return for the year the property is placed in service ([Form 4562 instructions](https://www.irs.gov/instructions/i4562)).
- **Elections by statement** (election out by class, the section 168(k)(10) election, the qualified production property designation) go on the timely filed return, including extensions.
- **Form 3115:** original attached to the return for the year of change; signed copy to the IRS in Ogden ([Form 3115 instructions](https://www.irs.gov/instructions/i3115)).
- **Losses:** Form 6198 (at-risk), Form 8582 (passive) and Form 461 (excess business loss) where they apply. A real estate professional reports on Schedule E line 43.
- **Sale:** Form 4797 for recapture and section 1231 gain; the Unrecaptured Section 1250 Gain Worksheet is in the Schedule D instructions.
- **Deadlines:** an individual's 2026 return and payment are due 15 April 2027; an extension moves filing (not payment) to 15 October 2027, and tax paid late accrues interest and any late-payment penalty from April ([IRS extensions page](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return)).

## Completion checklist

- Land allocated out at fair market value and excluded from every class.
- The study has a methodology narrative, cost support that reconciles to total cost, and a legal analysis of each section 1245 item (Pub. 5653).
- Binding contract or construction start date documented against January 19, 2025, and the matching bonus rate used (100, 40 or 20 percent).
- ADS status and any prior election out checked.
- Section 179 tested against the lessor, lodging and business income limits, with the figures from `us-section-179-and-bonus-depreciation`.
- For a building already in service: DCN 7 conditions met, section 481(a) adjustment and period computed.
- Basis, at-risk, passive, real estate professional and excess business loss limits applied in order; suspended amounts recorded.
- Recapture on a future sale modelled and explained.
- State treatment checked separately.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Law 119-21. Read for section 70301 (100 percent bonus, after January 19, 2025, the 40 percent election, binding contract rule) and section 70307 (qualified production property, construction before January 1, 2029, placed in service before January 1, 2031). | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |
| IRS Notice 2026-11. Read for section 2.01 (40 percent for 2025), 2.03 (binding contract, 10 percent safe harbor, non-binding contracts), 3 (interim guidance), 4.03 (168(k)(10) election) and 6.02 (reliance). | https://www.irs.gov/pub/irs-drop/n-26-11.pdf | 2026-11-13 |
| 26 U.S.C. 168 (govinfo, 2024 edition). Read for (e)(6) qualified improvement property, (g)(8) electing real property trade or business, (k)(2)(E) used property and (k)(6)(A)(v) 20 percent for 2026. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec168.htm | 2026-11-13 |
| 26 U.S.C. 465 (govinfo). Read for (b)(6) qualified nonrecourse financing. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec465.htm | 2026-11-13 |
| 26 U.S.C. 469 (govinfo). Read for (c)(7) real estate professional (more than one-half, more than 750 hours), (g) disposition and (i) the $25,000 allowance, $100,000 phase-out and $12,500 separate-return amount. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapE-partII-subpartC-sec469.htm | 2026-11-13 |
| 26 U.S.C. 1 (govinfo). Read for (h) the 25 percent rate on unrecaptured section 1250 gain. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partI-sec1.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.31 excess business loss threshold ($256,000, $512,000 joint). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Rev. Proc. 2024-40. Read for section 2.32, the 2025 excess business loss threshold. | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-13 |
| Rev. Proc. 2025-23. Read for section 6.01, DCN 7 and its conditions. | https://www.irs.gov/pub/irs-drop/rp-25-23.pdf | 2026-11-13 |
| Rev. Proc. 2015-13. Read for section 7.03: one year for a negative adjustment, four taxable years for a positive one, the less-than-$50,000 election. | https://www.irs.gov/pub/irs-drop/rp-15-13.pdf | 2026-11-13 |
| Cost Segregation Audit Techniques Guide (Pub. 5653). Read for study methods, Whiteco factors and rule-of-thumb studies. | https://www.irs.gov/pub/irs-pdf/p5653.pdf | 2026-11-13 |
| Pub. 946 (2025). Read for recovery classes, the 80 percent residential test, the 40 percent mid-quarter test, Table A-7a (2.033%), section 179 on real property and qualified production property. | https://www.irs.gov/pub/irs-pdf/p946.pdf | 2026-11-13 |
| Pub. 925 (2025). Read for the special allowance ($150,000, $12,500), active participation, the 5 percent owner-employee rule and the order of limits. | https://www.irs.gov/pub/irs-pdf/p925.pdf | 2026-11-13 |
| Pub. 544 (2025). Read for section 1245 and 1250 recapture, section 291 (20 percent), installment sales and section 1231 lookback. | https://www.irs.gov/pub/irs-pdf/p544.pdf | 2026-11-13 |
| Pub. 527. Read for land and building allocation. | https://www.irs.gov/publications/p527 | 2026-11-13 |
| Instructions for Form 4562 (2025). Read for the election out, the 301.9100-2 relief and line placement. | https://www.irs.gov/instructions/i4562 | 2026-11-13 |
| Instructions for Form 3115 (Rev. December 2022). Read for filing the original and the Ogden copy. | https://www.irs.gov/instructions/i3115 | 2026-11-13 |
| IRS extensions page. Read for the October extended due date. | https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-13 |

Not yet confirmed: the 2026 editions of Pub. 946, Pub. 925, Pub. 544 and the Form 4562 instructions were not published when read, so the 2026 bonus schedule for long production period property and certain aircraft acquired before 20 January 2025, and any 2026 line changes on Form 4562, are not stated; IRS proposed regulations under section 168(k) promised in Notice 2026-11 were not yet issued.
