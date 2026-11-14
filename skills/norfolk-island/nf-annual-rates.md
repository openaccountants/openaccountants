---
name: nf-annual-rates
description: >
  Establish selected Norfolk Island ordinary rates and annual waste charges
  for 2026-27 using the adopted council resolution and applied legislation.
  Use for residential, farmland, accommodation and business property,
  valuation, vacant-land discounts, instalments, pensioner concessions or
  rating objections. Includes category boundaries, amount-in-dollar tables,
  fictional calculations, separate review clocks and source checks. Separates
  the importer waste levy, approved service fees and historical absentee
  levy from annual property charges. Preserves actual assessment, current
  amendments, interest authority, relief and procedure gates, together with
  universal workflow outputs. This source-cited reference does not complete
  the property or country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "2026-27 annual rates adopted 30 June 2026; sources checked 18 October 2026; actual notices, later amendments and other charges require separate verification"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - nf-tax-system
---

# Norfolk Island: ordinary rates and annual waste charges

Confirm the rating year, liable person, parcel, Council category and
subcategory, area, dominant use, valuation in force, notice and service
dates, charge basis and claimed relief. Do not query ownership records or
collect private identity, pension, bank or client documents through this
reference. Record reviewer-held evidence readiness instead.

Load `workflow-base` and `nf-tax-system`, plus the relevant domain bases for
the engagement. Preserve the confirmed profile, source and period gates,
refusals, four universal outputs and applicable domain outputs and checks.
Missing facts remain Needs Input and unresolved law remains held. This
reference supplies selected parameters, not an actual assessment, a filing
instruction or a complete country companion.

## Establish the legal and annual source chain

Norfolk Island Act sections 5 and 18A apply the prescribed jurisdiction's
laws from time to time, subject to modifications, suspension and priority
rules. The Applied Laws Ordinance's Schedule 1 excludes the NSW Local
Government Act 1993 and legislation made under it from the general
suspension. Read the current NSW text **with** Norfolk modifications;
an old applied-law compilation alone does not establish the current rule.
Section 18B also changes who exercises specified State powers. [NI];
[APPLIED, sections 4–8 and Schedule 1][APPLIED]

The **30 June 2026 carried Council resolution**, item 13.1, adopts the
2026–27 operational plan/budget and fees and makes the ordinary rates
under sections 534, 535 and 537. The tables below reproduce that resolution,
not a forecast or an individual rates notice. The resolution's base amounts
produce **45% of each category's aggregate ordinary-rate yield**; this is
not a 45% charge or discount on each property's value. [JUNE]

The September operational-plan report proposes changes to water-assurance
Business Accommodation E and two fire-callout fees. It recommends **28
days' public exhibition followed by final Council consideration**. A report,
proposal or future rating-model review is not proof of a carried amendment.
The selected July and August financial motions do not make new ordinary
rates. Before an actual calculation, obtain the applicable notice and any
later carried amendments; the selected records do not establish that every
fee or charge remained unchanged. [SEPT]; [JULY]; [AUGUST]

## Classify the land and valuation

Council declares each rateable parcel as farmland, residential, mining or
business before making its ordinary rate. Farmland requires the statutory
dominant commercial farming use, including the relevant significance,
continuity and profit-purpose conditions; rural residential land is
excluded. Residential categorisation has its own dominant-use and vacant
land rules. Mining has its statutory use test; business is the residual
category. Area alone does not decide the primary category. Mixed,
strata/company-title, vacant and changed-use cases require their particular
rules and the Council declaration. [LGA, sections 514–521][LGA]

The current General Regulation separately addresses caravan/manufactured
home estates and retirement villages, serviced apartments and time-share
accommodation. Read those conditions with the actual use and Council
subcategory; do not classify from a property's advertising label alone.
Norfolk modifications allow subcategories by parcel size and, for business,
kind of business. [REG, sections 120–122][REG];
[APPLIED, Schedule 4 items 36–37][APPLIED]

Land Valuation Act section 7 makes an effective valuation the value for a
tax or rate on Norfolk land value, including where another Act refers to
rateable or taxable value. Section 8 recognises improved capital value or
unimproved value. Obtain the valuation's actual basis and effective date;
do not substitute a purchase price, a transfer-fee value or an assumed
valuation method. A valuation continues until the next takes effect,
subject to amendments and objections; it does not automatically expire
because an inspection cycle has passed. [VALUE, sections 7–22 and 27][VALUE]

Liability generally attaches to the owner, with particular Crown-lessee
and joint-liability provisions. An ownership transfer does not automatically
erase earlier rates, charges or recovery rights. Confirm exemptions,
apportionment and applicable notices rather than treating private ownership
or a nonprofit label as conclusive. [LGA, sections 554–561 and 571–572][LGA]

## Ordinary rates adopted for 2026–27

For a confirmed category, use:

`ordinary rate = base amount + (applicable land value × amount in the dollar)`

The second column is **added** to the value-based amount. The last column
contains dollar multipliers, **not percentages**. Sections 497–500 establish
the base-plus-ad-valorem structure and the aggregate base-amount limit.
Norfolk's old permission for a base-only ordinary rate concerned years
ending before July 2018; it does not make the current value component
optional. [LGA]; [APPLIED, Schedule 4 items 30–33][APPLIED]; [JUNE]

All amounts below are Australian dollars. Category descriptions are the
adopted resolution's conditions, subject to the statutory classification
and actual Council declaration. [JUNE]

| Council subcategory and adopted boundary | Base amount A$ | Amount in the dollar |
|---|---:|---:|
| Residential Small: area at most 0.3 ha | 155.09 | 0.00133340 |
| Residential Medium: over 0.3 ha, at most 1 ha | 240.26 | 0.00133340 |
| Residential Large: over 1 ha | 390.25 | 0.00133340 |
| Farmland Small: area at most 1 ha | 266.99 | 0.00163743 |
| Farmland Medium: over 1 ha, at most 3 ha | 358.65 | 0.00163743 |
| Farmland Large: over 3 ha | 753.83 | 0.00163743 |
| Business Accommodation A: qualifying non-hotel tourist accommodation house, at most 10 accommodation units | 3,194.42 | 0.01110969 |
| Business Accommodation B: qualifying non-hotel house, over 10 but fewer than 21 accommodation units | 4,729.90 | 0.01110969 |
| Business Accommodation C: qualifying non-hotel house, at least 21 accommodation units | 5,010.04 | 0.01110969 |
| Business Accommodation D: hotel | 5,010.04 | 0.01110969 |
| Shops/Retail A: area at most 1,000 m², excluding the specified supermarket/shopping and building-supplies categories | 1,269.71 | 0.01110969 |
| Shops/Retail B: area over 1,000 m², with the corresponding exclusions | 2,320.79 | 0.01110969 |
| Building Supplies | 1,696.51 | 0.01110969 |
| Cafe/Restaurant A: area at most 1,000 m² | 950.18 | 0.01110969 |
| Cafe/Restaurant B: area over 1,000 m² | 2,653.68 | 0.01110969 |
| Service Station: the resolution specifies area over 1,000 m² | 1,681.52 | 0.01110969 |
| Car Rentals | 1,429.20 | 0.01110969 |
| Clubs/Bars A: area at most 1,000 m² | 950.18 | 0.01110969 |
| Clubs/Bars B: area over 1,000 m² | 2,653.68 | 0.01110969 |
| Supermarket/Shopping Small: area at most 1,000 m² | 1,778.60 | 0.01110969 |
| Supermarket/Shopping Large: area over 1,000 m² | 6,895.49 | 0.01110969 |
| Business Other: residual business subcategory | 1,943.38 | 0.01110969 |

Accommodation categories use the Tourist Accommodation Act's hotel, house
and unit definitions. This reference does not supply those definitions or
resolve an actual classification: retain that source gate before choosing
a row. A unit is not automatically a bedroom. The Service Station area
condition is reproduced rather than silently removed; an unresolved smaller
site needs Council classification evidence. [JUNE]

The resolution also shows **Mining with hyphens for both amounts**.
Hyphens are not affirmative authority for a nil rate. Obtain the applicable
determination before calculating that branch. Norfolk section 513A's
minimum ordinary-rate revenue is a **Council-wide aggregate**, not a
minimum amount payable by each property. [JUNE];
[APPLIED, Schedule 4 item 35][APPLIED]

## Annual waste charges adopted for 2026–27

Council levies these under section 501 in the June resolution. Apply the
specified charging unit and relief conditions separately from the ordinary
rate. These are not the separate waste import levy. [JUNE]

| Adopted category | Annual charge A$ | Charging or discount condition |
|---|---:|---|
| Residential Small | 340.65 | 50% discount if vacant |
| Residential Medium | 467.05 | 50% discount if vacant |
| Residential Large | 700.58 | 50% discount if vacant |
| Farmland Small | 340.65 | 50% discount if vacant |
| Farmland Medium | 467.05 | 50% discount if vacant |
| Farmland Large | 700.58 | 50% discount if vacant |
| Accommodation A, B, C and D | 151.12 | Per accommodation unit |
| Shops/Retail A | 1,701.52 | Confirm Council classification |
| Shops/Retail B | 3,145.50 | Confirm Council classification |
| Building Supplies | 2,270.20 | Confirm Council classification |
| Cafe/Restaurant A | 1,215.66 | Confirm Council classification |
| Cafe/Restaurant B | 3,669.38 | Confirm Council classification |
| Service Station | 2,325.13 | Confirm Council classification |
| Car Rentals | 1,987.14 | Confirm Council classification |
| Clubs/Bars A | 1,215.66 | Confirm Council classification |
| Clubs/Bars B | 3,669.39 | Confirm Council classification |
| Supermarket/Shopping Small | 2,380.05 | Confirm Council classification |
| Supermarket/Shopping Large | 9,227.27 | Confirm Council classification |
| Business Other | 2,667.46 | Confirm Council classification |
| Commonwealth Heritage Quality Row | 14,193.01 | Separate adopted waste row |
| Hospitals | 25,444.26 | Separate adopted waste row |
| Schools | 25,444.26 | Separate adopted waste row |

The vacant-land discount is stated for the six residential/farmland rows.
Do not extend it to business or public-service rows without authority.
Cafe/Restaurant B and Clubs/Bars B differ by **A$0.01** in the source;
retain the distinct charges. The last three waste rows do not themselves
establish an ordinary-rate category or remove a statutory exemption.
[JUNE]; [LGA, sections 554–556][LGA]

Norfolk modifications deem the domestic-waste requirement in section
496(1) satisfied while the section 8 waste import levy is imposed, and
disapply section 504 while that levy is imposed. They also remove sewerage
services from section 501(1). Do not import an unmodified NSW domestic
waste, sewerage or cost-limit rule into the Norfolk calculation.
[APPLIED, Schedule 4 items 29, 33A and 34][APPLIED]

## Payment, relief and overdue amounts

Section 562 permits a single payment or quarterly instalments. The normal
single-payment deadline is **31 August**. The normal quarterly dates are
**31 August, 30 November, 28 February and 31 May**. If the notice was not
served by **1 August**, the single payment or first two quarterly
instalments are due by **30 November or 30 days after service, whichever
is later**. Establish service before selecting a date. [LGA, section 562]
[LGA]

For instalments, divide the rates or charges into quarters, put the
remainder in the first instalment, and move amounts exceeding a multiple
of **10 cents** in later instalments into the first. Reconcile each notice
component and the first-instalment adjustment; do not assume a bank's
four equal transfers reproduce the statutory allocation. [LGA, section 562]
[LGA]

Pensioner relief requires an eligible pensioner, the sole/principal dwelling,
liability, application and sufficient evidence. The Dictionary and current
Regulation section 134 prescribe the relevant pension/card and other
qualifying classes. A pension or age alone is insufficient. Section 575
specifies a conditional half reduction with joint-liability apportionment
and these annual caps: **A$250 for ordinary rates and domestic-waste
charges together**, and separate **A$87.50** water and sewerage caps.
Section 580 permits regulatory variation. Verify the applicable relief
rules, approved application and actual Council determination before
awarding a reduction. [LGA, Dictionary and sections 575–580][LGA];
[REG, sections 134–136][REG]

Do not automatically count Council's **section 501 waste charge** as a
section 575 domestic-waste charge. Confirm its legal treatment before
combining it with ordinary rates for a concession. Nor do the NSW water
and sewerage caps establish that Norfolk imposes those charges under the
same provisions. If eligibility begins during the year, section 575(4)
uses the **full quarters remaining after eligibility begins**. Sections
577 and 582 contain discretionary relief, not an automatic entitlement.
[LGA]; [APPLIED]

The June resolution adopts **9.5%** overdue interest for **1 July 2026 to
30 June 2027**. Section 566 provides for daily accrual at the Council rate
subject to the applicable ministerial maximum, and section 567 permits
specified hardship write-offs. This reference confirms the adopted Council
figure but **holds an actual interest calculation** until the applicable
Norfolk ministerial authority/ceiling, notice, overdue balance, dates,
payments and relief are verified. A NSW minister's notice alone is not
assumed to resolve the Norfolk Act section 18B power substitution.
[JUNE]; [LGA, sections 566–567][LGA]; [NI]

## Separate objections and review clocks

| Matter | Selected statutory trigger and limit | Boundary |
|---|---|---|
| Land valuation objection | Normally 60 days after **issue** of the valuation notice; late-objection conditions apply before the first anniversary | The clock is not simply service of the rates notice. A new owner does not automatically get a new original-objection period. [VALUE, sections 27, 39 and 42–43][VALUE] |
| Council category change | Section 525 application; the deemed outcome after 40 days has its own conditions | Confirm the declaration and actual decision. [LGA] |
| Category appeal | Section 526: 30 days after the **declaration** | Apply the Norfolk court/tribunal substitution before selecting the forum. [LGA]; [APPLIED, Schedule 4 item 1][APPLIED] |
| Whether land is rateable or subject to the charge | Section 574: 30 days after **service** of the relevant notice | This is a distinct remedy from categorisation or valuation review. [LGA] |

For Local Government Act references to the NSW Land and Environment Court,
Norfolk's inserted section 6A substitutes the Norfolk Supreme Court for
Chapter 17 powers and the local Administrative Review Tribunal for other
powers. The federal Administrative Review Tribunal has a separately
specified route for Land Valuation Act section 79(1) decisions. Read
`nf-property-transfers` for the local/federal distinction and selected
general review rules, then verify the actual decision, standing, current
forum, notice, period, fees and full procedure. Do not substitute one
universal objection period or send every matter to a NSW court. [APPLIED];
[ART-REG, sections 27–28][ART-REG]

Land Valuation Act section 83 specifically leaves a valuation in force
despite objection or appeal and says it cannot be stayed in proceedings.
A general tribunal stay power is not a promise that this valuation can be
stayed. Section 85 addresses adjustments after a valuation changes.
Payment, debt and collection consequences need their own applicable rules;
an objection is not assumed to suspend liability. [VALUE]

## Other charges require their own basis

**Waste import levy:** Waste Management Act section 8 makes the importer
liable. Current Regulations section 3 generally sets **A$41 per cubic metre
or tonne, whichever is greater**, for sea or air goods, subject to the
specified exclusions. Equine/bovine livestock containers instead attract
**A$150 per container**; motor vehicles attract **A$100 per cubic metre or
tonne, whichever is greater**. Mail, qualifying accompanied air-passenger
personal effects, and specified deceased-remains containers are excluded
under the stated conditions. Establish goods, transport, measurements,
classification and current collection rules before an actual import
calculation. Payment is not governed by the annual property instalment
dates merely because both charges concern waste. [WASTE, sections 8–10]
[WASTE]; [WASTE-REG, sections 2–3][WASTE-REG]

**Approved service fees:** Waste disposal/entry fees and other approved
Council service fees have separate legal bases, units and adopted fee
schedules. Sections 608–610F govern relevant local-government fees, with
Norfolk modifications recognising other Norfolk laws and limiting specified
double charging. Electricity, telecoms, water assurance, fire, airport and
other fees are not included in the annual-property subtotal below. Verify
their own charging event, adoption, amendments, exemptions and GST treatment;
this guide does not infer a fee's current amount or tax treatment from its
appearance in an agenda. [WASTE, section 10][WASTE]; [LGA];
[APPLIED, Schedule 4 items 44A–44E][APPLIED]

**Historical absentee levy:** the current Absentee Landowners Levy Act
defines levy day to exclude **2017 and later years** and expressly identifies
**15 September 2016 as the last levy day**. Do not impose its old annual
percentage as an additional 2026–27 property tax. That cessation does not
prove a historical debt was forgiven: sections 13–15 retain debt and
land-charge provisions and qualified purchaser/mortgagee protections.
Historical assessments and recovery require their own review. [ABSENTEE,
sections 2, 5 and 13–15][ABSENTEE];
[CONTINUED, Schedule 1 items 1AAAA–1AAAB][CONTINUED]

## Fictional 2026–27 calculations

These examples assume the adopted June tables remain applicable, confirmed
Council classification and valuation, and no exemption, concession, arrears,
interest or other service charge. They are selected-component calculations,
not actual notices or complete property costs. [JUNE]; [LGA]

1. **Residential Small, occupied, value A$450,000:** the value-based amount
   is A$450,000 × 0.00133340 = **A$600.03**. Add the A$155.09 base to obtain
   **A$755.12 ordinary rates**. Add A$340.65 waste for a selected annual
   subtotal of **A$1,095.77**.
2. **Residential Large, confirmed vacant, value A$600,000:** A$800.04 plus
   A$390.25 gives **A$1,190.29 ordinary rates**. The selected vacant waste
   charge is A$700.58 × 50% = **A$350.29**. The subtotal is **A$1,540.58**.
   The vacancy discount has not halved the ordinary rate.
3. **Farmland Medium, occupied, value A$1,000,000:** A$1,637.43 plus
   A$358.65 gives **A$1,996.08 ordinary rates**. Add A$467.05 waste:
   **A$2,463.13**. The farmland use test is assumed separately from area.
4. **Accommodation A, ten confirmed units, value A$1,000,000:**
   A$11,109.69 plus A$3,194.42 gives **A$14,304.11 ordinary rates**.
   Waste is ten × A$151.12 = **A$1,511.20**. The subtotal is
   **A$15,815.31**. An eleventh unit requires the B category check; the
   ten-unit base is not carried forward automatically.
5. **Cafe/Restaurant B versus Clubs/Bars B**, each with value A$1,000,000:
   each ordinary rate is **A$13,763.37**. Their waste charges yield
   subtotals of **A$17,432.75** and **A$17,432.76**, respectively.
6. **Instalments for the A$755.12 ordinary-rate component only:** later
   quarters of **A$188.70** each leave **A$189.02** for the first quarter.
   A$189.02 plus three × A$188.70 reconciles to A$755.12. Allocate the
   separate waste component using the notice's applicable treatment.

Do not apply transfer-fee-unit rounding or a business transaction levy's
rounding rule to annual rates. If a value multiplication or vacant discount
produces fractions of a cent, retain the calculation and verify Council's
applicable assessment rounding before stating the payable amount.

## Computation and review checks

1. Establish the current annual resolution and amendments; reconcile the
   notice, valuation and Council declaration to the selected period.
2. Decide rateability and primary category before applying area/business
   boundaries. Exactly 0.3, 1 and 3 hectares and exactly 1,000 m² belong to
   the row whose upper limit includes them; accommodation boundaries depend
   on the defined unit count and hotel status. [JUNE]
3. Add base plus value times multiplier. Record each charge's unit, vacancy
   conditions and separate relief. A hyphen, an unclassified site or an
   absent service charge remains unresolved rather than becoming zero.
4. Test pensioner and other relief against its legal charge class,
   application, ownership and eligibility conditions; do not infer approval
   from a fictional example.
5. Keep issue, declaration and service dates separate. Allocate instalments
   and verify overdue-interest authority before calculating interest.
6. Reconcile components, relief, rounding, instalments, prior payments and
   adjustments to the actual notice. Complete the workflow's deliverables
   and review checks; these reference tables do not waive any required slot.

Still open: actual parcel and accommodation classification, exemption and
valuation evidence; later amendments; Council rounding; full concession
and ministerial-interest authority checks; complete review and collection
procedures; all other local fees; and remaining country topics. These gates
do not prevent use of the selected adopted parameters for an appropriately
bounded reference calculation.

## Primary sources and provenance

Checked **18 October 2026**. This is a **Tier 2 source-cited draft awaiting
professional review**. The current Register records were checked alongside
selected operative provisions; whole Acts were not represented as fully
reviewed. The June public resolution's category descriptions and leaf-table
cells were checked together, including the per-unit and one-cent cases.
The September report's three native PDF pages were read in full; that is
not proof of a later Council vote. No private ownership roll or client
information was queried.

[NI]: https://www.legislation.gov.au/C2004A02035/2024-12-11/text
[APPLIED]: https://www.legislation.gov.au/F2016L00729/2023-06-28/text
[LGA]: https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-1993-030
[REG]: https://legislation.nsw.gov.au/view/whole/html/inforce/current/sl-2021-0460
[VALUE]: https://www.legislation.gov.au/C2015Q00162/2019-11-16/text
[JUNE]: https://norfolk.resolve.red/portal/meeting/676/10826?showMinutes=1
[JULY]: https://norfolk.resolve.red/portal/meeting/641/10963?showMinutes=1
[AUGUST]: https://norfolk.resolve.red/portal/meeting/642/11051?showMinutes=1
[SEPT]: https://norfolk.resolve.red/portal/meeting/643/11178?type=1&docId=2391
[ART-REG]: https://www.legislation.gov.au/F2024L01166/2026-01-01/text
[WASTE]: https://www.legislation.gov.au/C2015Q00254/2019-08-13/text
[WASTE-REG]: https://www.legislation.gov.au/C2015Q00335/2019-08-13/text
[ABSENTEE]: https://www.legislation.gov.au/C2015Q00072/2017-10-18/text
[CONTINUED]: https://www.legislation.gov.au/F2015L00835/2023-02-08/text

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
