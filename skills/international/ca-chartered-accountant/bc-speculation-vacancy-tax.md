---
name: bc-speculation-vacancy-tax
description: Use this skill for BC Speculation and Vacancy Tax on residential properties in designated areas. Triggers "BC SVT", "BC speculation tax", "vacant home tax BC", "0.5% SVT BC", "2% SVT foreign", "speculation tax declaration BC". DIFFERENT from federal Underused Housing Tax (UHT) which also applies.
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BC Speculation Vacancy Tax

## British Columbia — Speculation and Vacancy Tax (SVT) — Skill v1.0

The BC Speculation and Vacancy Tax (SVT) is an annual provincial tax on residential property owners in designated taxable areas of British Columbia. It is administered by the BC Ministry of Finance under the Speculation and Vacancy Tax Act, SBC 2018, c. 46. The SVT is distinct from the federal Underused Housing Tax (UHT) and the City of Vancouver Empty Homes Tax (EHT) — these three regimes can stack on the same property.

This skill covers tax year 2025 (declarations due by March 31, 2026, based on 2025 ownership and use).

## 1. Quick reference

**Quick reference table**

| Item | Detail |
| --- | --- |
| Tax type | Annual provincial property tax on residential property |
| Authority | BC Ministry of Finance |
| Statute | Speculation and Vacancy Tax Act, SBC 2018, c. 46 |
| Tax base | BC Assessment value of residential property as of July 1 of prior year |
| Rate — Canadian citizen/PR who is a BC resident for tax purposes | 0.5% |
| Rate — Foreign owner, satellite family, or untaxed worldwide income | 2.0% |
| Declaration deadline | March 31 each year (covers prior calendar year) |
| Payment deadline | First business day of July |
| Filing | Mandatory annual declaration for ALL owners of residential property in designated areas, even if exempt |
| Filing channel | BC SVT online portal (gov.bc.ca/SVT) using Declaration Code and Letter ID mailed each January |

- **Owner-based tax** — The SVT is owner-based, not property-based: where a residential property has multiple owners, each owner files a separate declaration and each is assessed separately on their proportional interest.

## 2. Required inputs and refusal catalogue

### Required inputs

- **Required inputs list** — To compute or review a BC SVT position, the following inputs are required: - Civic address and folio number of every BC residential property the owner holds an interest in - Confirmation each property is in a designated taxable area (see Section 4) - BC Assessment value as of July 1 of the prior year (e.g., July 1, 2024 for the 2025 declaration) - Ownership percentage for each co-owner - Owner's tax residency status: Canadian citizen or permanent resident, foreign national, or other - Owner's BC tax residency: did the owner file a BC T1 (resident at Dec 31) for the year? - Worldwide income for the year and the share reported on a Canadian T1 (to test the satellite family / untaxed worldwide income rule) - Occupancy facts for the property: principal residence days, rental days, rental tenant details (arm's-length or not), vacancy days - Any exemption circumstances: hardship event, death, separation/divorce, recent purchase date, building permit / construction status, strata rental restriction predating Oct 2018, medical absence, etc. - Declaration Code and Letter ID from the SVT letter (needed to file the declaration)

### Refusal catalogue (out of scope for this skill)

- **R-BC-SVT-1** — Property held by a corporation, partnership, or trust (corporate interest holders use a different declaration path with beneficial owner attribution rules under Part 4 of the Act).  _(Part 4 of the Act)_
- **R-BC-SVT-2** — Mixed-use property, stratified hotel units, or commercial-with-residential where Class 1 vs. Class 6 BC Assessment treatment is unclear.
- **R-BC-SVT-3** — First Nations land or property on a reserve subject to the Indian Act.  _(Indian Act)_
- **R-BC-SVT-4** — Bare trust, alter ego trust, joint partner trust, or other beneficial ownership arrangement.
- **R-BC-SVT-5** — Appeal of an SVT assessment, notice of objection, or judicial review under Part 7.  _(Part 7)_
- **R-BC-SVT-6** — Strata corporation seeking the strata-rental-restriction exemption — fact-specific review of bylaws.
- **R-BC-SVT-7** — Property used in a short-term rental business (the rental-period exemption requires tenancies of at least one month).
- **R-BC-SVT-8** — Death of the registered owner during the calendar year with estate-administration timing questions.
- **R-BC-SVT-9** — Properties outside the designated areas where the user nevertheless received a letter (resolve via BC SVT office; do not file on assumption).
- **R-BC-SVT-10** — Interaction with the federal Prohibition on the Purchase of Residential Property by Non-Canadians Act (different regime, different definitions).  _(Prohibition on the Purchase of Residential Property by Non-Canadians Act)_
- **Refusal handling** — For everything in the refusal catalogue, do not attempt the calculation — produce a brief that lists the issue, the relevant statutory section, and a referral to a BC-credentialed adviser.

## 3. Rates

**SVT rates by owner category**

| Owner category | Rate |
| --- | --- |
| Canadian citizen or permanent resident who is a BC resident for income tax purposes | 0.5% |
| Other Canadian citizen or permanent resident (e.g., resident in another province) | 0.5% |
| Foreign owner | 2.0% |
| Member of a satellite family | 2.0% |
| Owner with untaxed worldwide income (more than half of worldwide income not reported on a Canadian T1) | 2.0% |

- **Rate determination timing** — The SVT rate for a calendar year depends on the owner's status on December 31 of that year.

### Definitions

- **Foreign owner** — An individual who is neither a Canadian citizen nor a permanent resident of Canada under the Immigration and Refugee Protection Act.  _(Immigration and Refugee Protection Act)_
- **Satellite family** — An owner (and their spouse) whose unreported worldwide income for the year exceeds the income they reported on Canadian T1 returns. Tested at the household level.
- **Untaxed worldwide income** — Worldwide income not reported on a Canadian T1 return. Includes foreign-source income exempt from Canadian tax.

### Tax credits available

- **BC resident credit** — Up to $2,000 per owner per year (i.e., shelters up to $400,000 of the 0.5% base), available only to BC residents who are not foreign owners or members of a satellite family.
- **Other resident of Canada credit** — Based on BC-source income; available to Canadian citizens/PRs who are not BC residents.
- **Foreign owner / satellite family credit** — Based on BC-source income reported on Canadian T1; allows the owner to shelter the portion attributable to BC-taxed earnings.
- **Credit transferability** — Credits are not transferable between properties or between owners.

## 4. Designated taxable areas

- **Scope of application** — The SVT applies only inside designated taxable areas. It is NOT a province-wide tax. Properties outside these areas are not subject to SVT and their owners do not need to declare.

### Original designated areas (2018 onward)

- **Original designated areas list** — - Municipalities within the Metro Vancouver Regional District (excluding Bowen Island and the Village of Lions Bay initially, plus Electoral Area A excluding UBC/UEL) - Municipalities within the Capital Regional District (excluding Salt Spring Island, Juan de Fuca Electoral Area, and the Southern Gulf Islands) - City of Abbotsford - District of Mission - City of Chilliwack - City of Kelowna - City of West Kelowna - City of Nanaimo - District of Lantzville

### 2023 expansion (declarations starting 2024 for 2023 tax year)

- **2023 expansion list** — Added by Order in Council under section 132 of the Act: - District of Squamish - Village of Lions Bay - Bowen Island Municipality - District of Lake Country - District of Peachland  _(section 132 of the Act)_

### 2024 expansion (declarations starting 2025 for 2024 tax year)

- **2024 expansion list** — Added in the second wave of expansion: - City of Vernon - District of Coldstream - City of Penticton - District of Summerland - City of Courtenay - Town of Comox - Village of Cumberland - City of Parksville - Town of Qualicum Beach - City of Salmon Arm - City of Kamloops

### How to verify

- **Verification method** — A property's designation is determined by its civic address falling inside the boundaries of a listed municipality or regional district subdivision. Reserve land, treaty land, and certain electoral areas inside an otherwise-designated regional district are excluded. Do not rely on the postal code — use the property's legal description and the BC SVT area lookup tool on gov.bc.ca/SVT.

## 5. Annual declaration

- **Annual declaration requirement** — A declaration is required every year by **March 31** from **every owner** of residential property in a designated taxable area, regardless of whether SVT is ultimately owed. This includes owners claiming a 100% exemption (principal residence, long-term rental, hardship, etc.).

### Mechanics

- **Declaration mechanics** — - In mid-January each year the BC SVT office mails a Declaration letter to each registered owner of designated-area residential property. The letter contains: - The Declaration Code (property-specific) - The Letter ID (owner-specific) - The Folio number - The owner files online at gov.bc.ca/SVT using their BC Services Card login, or by phone on 1-833-554-2323. - Where there are multiple registered owners, each must file separately. One owner's declaration does not satisfy another's obligation. - Spouses generally each declare even where only one is on title, where the property is the principal residence of the non-owner spouse — but in most cases declaration is by registered owner only.

### What is reported

- **Reported items** — - Whether the property was the owner's principal residence - Whether the property was rented (and to whom — arm's-length tenant, related tenant who is a BC resident, etc.) - Number of qualifying rental months and tenant details - Exemption claimed (if any) with the statutory category - Worldwide income facts where 2% rate is possible - Co-owner allocation

### Notice of Assessment

- **Notice of Assessment process** — After the declaration is processed, the SVT office issues a Notice of Assessment showing tax payable, credits applied, and balance due. Payment is due the first business day of July (commonly July 2 or July 3).

## 6. Exemptions

- **Exemptions overview** — The Act and Regulations provide a long list of exemptions, codified in Part 3 and the Regulation. The most common exemptions encountered in freelance / individual-owner work are listed below.  _(Part 3 of the Act; the Regulation)_

### Principal residence

- **Principal residence exemption** — - Property is the owner's principal residence (the place where they live, eat, and sleep more than at any other place) for the year. - An individual can have only one principal residence at a time. Spouses can have only one principal residence between them, subject to limited separation exceptions.

### Tenanted property (long-term rental)

- **Long-term rental exemption** — - Property is rented to an arm's-length tenant for at least **6 months** in the year, in periods of at least **one month** each. - Short-term rental days (less than one month per tenancy) do NOT count toward the 6-month threshold. - Where the tenant is not arm's-length, the tenant must be a BC resident for income tax purposes AND the tenant's BC-earned income for the year must equal at least three times the annual fair-market rent for the unit.

### Other common exemptions

- **Other exemptions list** — - **Recent purchase** — property acquired during the calendar year (one-year buffer). - **Under construction / major renovation** — building permit exempting the year, plus continuing reasonable progress. - **Death of the owner** — the year of death and the year following are typically exempt for the deceased and the executor. - **Separation or divorce** — exemption while the property is on the market and the parties are separated. - **Medical absence** — owner in residential care or hospitalized; specific certification required. - **Court order** — property subject to a court order preventing occupancy or sale. - **Hazardous or uninhabitable** — fire, flood, contamination making the unit unsafe (limited duration). - **Strata rental restriction predating October 16, 2018** — covered under transitional rules; this exemption is now substantially narrowed because the Strata Property Amendment Act, 2022 (Bill 44) eliminated most strata rental restrictions. - **Hardship** — discretionary; case-by-case relief under section 87. Every exemption requires correct factual documentation. The declaration is signed under penalty of perjury — an unsupported exemption claim risks a reassessment plus penalties (section 96).  _(section 87; section 96; Strata Property Amendment Act, 2022 (Bill 44))_

## 7. Interaction with federal Underused Housing Tax (UHT)

- **UHT overview** — The federal Underused Housing Tax came into force January 1, 2022, under the Underused Housing Tax Act (S.C. 2022, c. 5, s. 10). It is a separate 1% annual federal tax that can apply on top of the SVT.  _(Underused Housing Tax Act (S.C. 2022, c. 5, s. 10))_

**BC SVT vs Federal UHT comparison**

| Feature | BC SVT | Federal UHT |
| --- | --- | --- |
| Authority | BC Ministry of Finance | Canada Revenue Agency |
| Geographic scope | BC designated areas only | All of Canada |
| Who pays | Owners (any status) at the relevant rate | Non-resident, non-Canadian owners primarily; certain Canadian "affected owners" must also file |
| Rate | 0.5% or 2.0% | 1% |
| Base | BC Assessment value (July 1 prior year) | Greater of taxable value (assessed value × 1) and most recent sale price, with election available |
| Filing deadline | March 31 | April 30 (return form UHT-2900) |
| Excluded owners | None — all designated-area owners declare | "Excluded owners" (Canadian citizens, PRs, public bodies, etc.) do not file; "affected owners" must file even when no tax |

- **2023 UHT amendments** — Important: 2023 amendments to the UHT (Bill C-69, Royal Assent June 20, 2024) narrowed the "affected owner" definition so that more Canadian individuals are now "excluded owners." Specifically, Canadian citizens and PRs holding through partnerships or trustees of certain trusts are now excluded for the 2023 and later calendar years. The 1% UHT rate continues to apply only to "non-excluded owners" — primarily non-resident non-Canadians, certain corporations, and partnerships.  _(Bill C-69, Royal Assent June 20, 2024)_
- **Stacking rule** — A single property can be subject to both SVT and UHT simultaneously. They are not coordinated. A non-resident foreign individual owning a vacant Vancouver condo files: 1. A federal UHT return (Form UHT-2900) by April 30 — 1% federal tax. 2. A BC SVT declaration by March 31 — 2% provincial tax. Each is computed on its own base, with its own exemptions, and paid to its own administering authority.

## 8. Interaction with City of Vancouver Empty Homes Tax (EHT)

- **EHT overview** — The City of Vancouver's Empty Homes Tax (Vacancy Tax By-law No. 11674) is a municipal tax applying only to properties in the City of Vancouver. It does not apply elsewhere in Metro Vancouver.  _(Vacancy Tax By-law No. 11674)_

**BC SVT vs Vancouver EHT comparison**

| Feature | BC SVT | Vancouver EHT |
| --- | --- | --- |
| Authority | BC Ministry of Finance | City of Vancouver |
| Geographic scope | BC designated areas including Vancouver | City of Vancouver only |
| Rate | 0.5% or 2.0% | 3% (rate confirmed at 3% for 2024 onward, up from 1% originally and 1.25% then 3%) |
| Base | BC Assessment value | BC Assessment value (taxable assessed value) |
| Declaration deadline | March 31 | First Friday in February (city portal) |
| Stacking | Both apply on the same Vancouver property |  |

- **Three-layer stacking** — A vacant Vancouver condo owned by a non-resident foreign individual potentially attracts ALL THREE layers: - Vancouver EHT — 3% municipal - BC SVT — 2% provincial (foreign owner rate) - Federal UHT — 1% federal Stacked effective rate on assessed value: 6% per year.

## 9. Worked example

Mr. K is a citizen and tax resident of Singapore. He owns 100% of a strata condo at 999 West Cordova St, Vancouver. The condo is in the City of Vancouver (Metro Vancouver designated area). BC Assessment value as of July 1, 2024 is **$1,250,000**. In calendar year 2025 the unit was vacant for 11 months while Mr. K listed it informally with a realtor; for one month his adult niece (Canadian citizen, BC resident, university student with $9,000 of BC employment income) stayed in the unit rent-free. Mr. K has no Canadian-source income and files no Canadian T1.

### Step 1 — Determine SVT rate

Mr. K is not a Canadian citizen and not a permanent resident. He is a foreign owner. **SVT rate = 2.0%.**

### Step 2 — Test SVT exemptions

- Principal residence? No — Mr. K lives in Singapore.
- Long-term rental? The niece occupied the unit for one month. To qualify for the rental exemption when the tenant is non-arm's-length, the tenant must be a BC resident AND have BC-earned income at least 3× annual fair market rent for the year. Even assuming the niece is BC resident, her $9,000 BC income would need to be at least 3× the annual FMV rent for a West Cordova condo (realistically $48,000+ rent → $144,000+ income test). She does not meet the income test. The non-arm's-length rental exemption fails.
- Additionally, the 6-month threshold is not met — only one month of occupancy.
- No other exemption applies.

**SVT before credit:** $1,250,000 × 2.0% = **$25,000**.

### Step 3 — SVT credits

The BC resident credit and the Other Resident of Canada credit are not available to foreign owners. The foreign-owner credit is based on BC-source income reported on a Canadian T1. Mr. K has none. **Credit: $0.**

**BC SVT payable: $25,000.**

### Step 4 — Federal UHT (Form UHT-2900)

Mr. K is a non-resident, non-Canadian individual — a non-excluded "affected owner" who must file UHT-2900. Exemptions to consider:

- Primary place of residence — No.
- Qualifying occupancy (at least 180 days in qualifying occupancy periods of at least one month) — One month of niece occupancy. Fails the 180-day threshold.
- Vacation property in eligible area — Downtown Vancouver is not a UHT-eligible vacation area.
- Newly constructed / not suitable for year-round use / seasonal access — No.

No UHT exemption applies. UHT base is the greater of taxable value and most recent sale price (unless the owner elects fair-market-value supported by appraisal). Assuming taxable value of $1,250,000 governs:

**Federal UHT payable: $1,250,000 × 1% = $12,500.**

### Step 5 — Vancouver Empty Homes Tax (EHT)

The unit was unoccupied or under-occupied for more than 180 days in the year (occupied only one month, ~30 days). EHT applies.

**Vancouver EHT payable: $1,250,000 × 3% = $37,500.**

### Step 6 — Combined annual exposure

**Combined annual exposure table**

| Layer | Authority | Amount |
| --- | --- | --- |
| BC SVT (2.0% foreign owner) | BC Ministry of Finance | $25,000 |
| Federal UHT (1% non-resident) | CRA | $12,500 |
| City of Vancouver EHT (3%) | City of Vancouver | $37,500 |
| **Total** |  | **$75,000** |

Effective combined annual rate on $1,250,000 assessed value: **6.0%**.

### Step 7 — Filing obligations and deadlines

- Vancouver EHT — first Friday in February 2026 (City portal)
- BC SVT declaration — March 31, 2026 (BC portal)
- Federal UHT-2900 — April 30, 2026 (CRA)
- BC SVT payment — first business day of July 2026
- Vancouver EHT payment — first business day of April 2026 (per City schedule)
- Federal UHT payment — April 30, 2026

All three authorities act independently. Late filing of any one of them triggers a separate penalty regime.

## 10. Penalties

- **Penalties section intro** — 

### Failure to declare — automatic 2% assessment

- **Failure to declare penalty** — If an owner does not file an SVT declaration by March 31, the BC SVT office issues an assessment at the **maximum 2.0% rate** on the full BC Assessment value, regardless of the owner's actual residency status or any exemption that might otherwise apply. The owner can apply to file a late declaration to remove or reduce the tax, but the burden is on the owner and interest may apply.

### Other penalties under Part 9

- **False or misleading declaration** — Penalty up to the amount of tax that would have been payable if the property were fully taxable, plus possible prosecution.  _(Part 9)_
- **Tax avoidance arrangement** — General anti-avoidance rule in section 92.  _(section 92)_
- **Failure to provide records on demand** — Penalty up to $25,000 per day.  _(Part 9)_
- **Late payment of assessed tax** — Interest at the rate prescribed under the Financial Administration Act, compounded monthly.  _(Financial Administration Act)_

### Audit window

- **Reassessment period** — The Administrator may reassess up to **six years** after the original Notice of Assessment, or any time in the case of fraud or misrepresentation attributable to neglect, carelessness, or wilful default (section 78).  _(section 78)_

## 11. Conservative defaults

- **Default 1 — Assume the higher rate** — If the owner's residency status is unclear, assume 2.0% until the 0.5% rate is documented (BC tax residency + Canadian citizen/PR status confirmed).
- **Default 2 — Assume no exemption** — Every exemption requires documented facts. If documentation is missing, present the SVT as fully payable and flag the exemption opportunity for owner sign-off.
- **Default 3 — Assume the declaration is mandatory** — If the property is in any of the listed designated areas, the declaration is mandatory regardless of exemption. Do not advise skipping the declaration on the theory that "nothing is owed."
- **Default 4 — Stack, do not net** — Treat SVT, UHT, and Vancouver EHT as independent regimes. Compute each separately. Do not attempt to credit one against another — they do not interact.
- **Default 5 — Use BC Assessment value** — Use BC Assessment value as of July 1 of the prior year as the base unless the owner has obtained a successful appeal under the Assessment Act for the relevant roll year.  _(Assessment Act)_
- **Default 6 — Multiple-owner properties** — For multiple-owner properties, each owner files independently. Do not attempt to combine declarations.
- **Default 7 — Refer corporate/partnership/trust holdings** — Refer all corporate, partnership, and trust holdings to the refusal catalogue. This skill is for individual registered owners only.
- **Default 8 — Escalate designated area questions** — Escalate any question about whether a property is in a designated area — use the official BC SVT area lookup; do not infer from postal code or city name alone.
- **Default 9 — Check UHT and EHT for non-resident owners** — For non-resident owners, always check federal UHT and any applicable municipal EHT in addition to SVT. Failing to flag UHT is a material omission.
- **Default 10 — Reviewer brief only** — The skill produces a reviewer brief, not a filed declaration. A BC-credentialed adviser (CPA-BC or BC-licensed lawyer) must sign off before filing.

## 12. Sources

### Primary legislation

- **Primary legislation list** — - **Speculation and Vacancy Tax Act**, SBC 2018, c. 46 — full text on BC Laws. - **Speculation and Vacancy Tax Regulation**, B.C. Reg. 275/2018 — exemption details and prescribed amounts. - **Underused Housing Tax Act**, S.C. 2022, c. 5, s. 10 — federal companion regime; as amended by Bill C-69 (Royal Assent June 20, 2024). - **City of Vancouver Vacancy Tax By-law No. 11674** — Empty Homes Tax. - **Strata Property Amendment Act, 2022** (Bill 44) — eliminated most strata rental restrictions, narrowing the SVT strata-rental-restriction exemption.

### Government guidance

- **Government guidance list** — - BC Ministry of Finance — Speculation and Vacancy Tax homepage and technical guides at gov.bc.ca/SVT. - BC SVT designated areas reference list and area-lookup tool at gov.bc.ca/SVT. - CRA Underused Housing Tax — guidance, Form UHT-2900, and notices UHTN1 through UHTN16. - City of Vancouver Empty Homes Tax declaration portal and bylaw guidance.

### Order in Council expansion authority

- **OIC list** — - OIC making the 2023 expansion (Squamish, Lions Bay, Bowen Island, Lake Country, Peachland). - OIC making the 2024 expansion (Vernon, Coldstream, Penticton, Summerland, Courtenay, Comox, Cumberland, Parksville, Qualicum Beach, Salmon Arm, Kamloops).

### Cross-references inside this package

- **Cross references** — - See `bc-individual-return.md` for the BC personal income tax determination of "BC resident" that drives the 0.5% vs. 2.0% SVT rate. - For corporations, partnerships, and trusts holding BC residential property, refer to a BC-credentialed adviser — outside the scope of this individual-owner skill.

## End of skill v1.0

*End of skill v1.0. Verification status: pending. Do not file an SVT declaration based solely on this skill without sign-off from a BC-credentialed adviser (CPA-BC or BC-licensed lawyer).*

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
