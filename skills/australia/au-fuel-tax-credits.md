---
name: au-fuel-tax-credits
description: >
  Use this skill to prepare or review an Australian fuel tax credit claim for a
  GST-registered sole trader, partnership, company or trust for 2026-27, or a
  late 2025-26 claim: Fuel Tax Act 2006 entitlement, the 4.5 tonne GVM and
  environmental tests, the rate on the acquisition date and its changes during
  the year, the road user charge for heavy vehicles, apportionment, simplified
  methods for claims of $10,000 or less, records, adjustments, error corrections
  and BAS labels 7C and 7D. Trigger on "fuel tax credits", "FTC", "road user
  charge", "label 7D", "off-road diesel" or "basic method for heavy vehicles".
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27 (rates read 2 November 2026; 2025-26 liquid fuel rates kept for late claims)"
tier: 2
last_updated: 2026-11-12
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
---

# Australian Fuel Tax Credits v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide builds a fuel tax credit claim workpaper from fuel acquisitions and usage evidence: who is entitled, which litres qualify, which rate applies to each litre, how the road user charge reduces heavy vehicle credits, which apportionment or simplified method is used, how a change of use or an error is corrected, and what goes at labels 7C and 7D. It loads on top of `workflow-base`, whose reviewer brief, intake and self-check rules apply. The law and rates are as read on 2 November 2026; every rate below carries its effective period.

It covers GST-registered businesses of any entity type that acquire liquid or gaseous taxable fuel for use in carrying on their enterprise, for fuel acquired from 1 July 2025 onwards. It does not cover:

- GST on fuel purchases, input tax credits and the GST labels: `australia-gst`.
- The rest of the BAS, PAYG labels and BAS due dates: `au-gst-bas`, `au-bas-preparation` and `au-lodgment-deadlines-penalties`. `au-gst-bas` gives labels 7C and 7D as an overview only and puts detailed fuel tax credit calculations out of scope; this guide holds them.
- Income tax on fuel costs and on the credit itself, and the business schedule: `au-deductions-offsets` and `au-sole-trader-schedule`.
- Fuel in cars provided to employees: `au-fbt`.
- Primary producers' income tax concessions: `au-primary-production`.
- Fuel manufacturers and importers, fuel packaging or supply claims, fuel blends, aviation fuels, non-profit emergency vehicles claiming without GST registration (s 41-5(3)), the fuel tax return for entities that are not registered for GST (s 65-5(2)) and GST instalment payers' special attribution (s 46-5): refer (R-AU-FTC-5).
- Rates for fuel acquired before 1 July 2025: read the ATO year pages linked from the [rates index](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business) or the historical rates file on data.gov.au that page links; this guide carries none.

**The reviewer is the customer of this output.** The output is a claim workpaper and a reviewer brief, not a lodged BAS. Lodgment belongs to the registered agent or the business.

## Ask the client first

Collect these before any rate is applied. Missing items become Needs Input, not assumptions.

1. **Acquisition records for each period claimed**: tax invoices, fuel card or supplier statements and bulk tank records showing fuel type, litres (or kilograms) and acquisition date. For fuel the business manufactured or imported, the home consumption or import date instead ([s 43-5(2A)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-5)).
2. **Registrations**: GST registration status on each acquisition date, the GST accounting basis (cash or non-cash), the BAS cycle and confirmation that the separate fuel tax credit registration is active. Both registrations are required ([ATO, Registering](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/registering)).
3. **Vehicle and plant register**: gross vehicle mass (GVM) for each unit, diesel or other engine, manufacture date (and any replacement engine's date), whether the unit is on the ATO's list of heavy vehicles used mainly off public roads, and the auxiliary equipment fitted.
4. **Usage evidence**: odometer or telematics output, engine hours and meter readings, route distances, logbooks, job sheets, contracts and delivery dockets showing where each unit works.
5. **Site geography**: which roads each unit uses and the evidence for treating each as public or not (gates, permits, network connections, land titles).
6. **Hire and contract arrangements**: wet or dry hire, whether fuel is supplied, charged, on-sold or replaced in kind, and any contract term naming the party that claims.
7. **History**: prior-period 7C and 7D amounts, the apportionment method used and when it was last reviewed, total fuel tax credit entitlement for the preceding 12 months, current GST turnover, and whether the ATO has notified any compliance activity.

## The method, step by step

### Step 1: Entitlement and registration

- A business is entitled to a fuel tax credit for taxable fuel it acquires, manufactures or imports 'to the extent that' it does so for use in carrying on its enterprise ([Fuel Tax Act 2006 s 41-5(1)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/41-5)).
- It must be registered, or required to be registered, for GST at the time it acquires, manufactures or imports the fuel; registration at claim time is not enough ([s 41-5(2)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/41-5)). The ATO also requires fuel tax credit registration when the claim is lodged ([ATO, Eligibility, QC44501](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/eligibility)).
- Exclude fuel used for private purposes, fuel lost, stolen or otherwise disposed of, fuel with no excise or customs duty paid, aviation gasoline and aviation kerosene, and additives such as diesel exhaust fluid ([ATO, Ineligible fuels and activities, QC44509](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/eligibility/ineligible-fuels-and-activities)).

### Step 2: Name one claimant for each litre

Only one entity can claim for the same fuel. Who 'acquired' the fuel is a question of fact, not of who burnt it: in a hire arrangement, read FTR 2007/1 and FTR 2009/1 against the contract and the fuel's actual supply ([ATO, Completing your BAS, QC44518](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/claiming/completing-your-business-activity-statement)). A contract term naming the claimant does not create an entitlement the facts do not support (same page). Record the evidence and leave the conclusion to the reviewer (R-AU-FTC-2).

### Step 3: Classify each unit and each use

1. **Light vehicles on public roads.** No credit for fuel to the extent it is for use in a vehicle with a GVM of 4.5 tonnes or less travelling on a public road ([s 41-20](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/41-20)), except a vehicle of exactly 4.5 tonnes acquired before 1 July 2006, which the ATO includes as a heavy vehicle ([PCG 2021/2 para 4](https://www.ato.gov.au/law/view/document?docid=COG/PCG20212/NAT/ATO/00001), read 12 November 2026). Establish the acquisition date before excluding an exactly 4.5-tonne vehicle. The same vehicle working off public roads, for example on a farm or a mine site, can still be claimed at the 'all other business uses' rate ([ATO, QC44509](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/eligibility/ineligible-fuels-and-activities)).
2. **Environmental criteria.** No credit for fuel for a motor vehicle unless it was manufactured on or after 1 January 1996, is in an accredited audited maintenance program, meets Rule 147A of the Australian Vehicle Standards Rules 1999, or complies with an endorsed maintenance schedule ([s 41-25(1)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/41-25)). The test does not apply to a vehicle used in a primary production business primarily on an agricultural property, a vehicle not powered by a diesel engine, or a vehicle not used on a public road ([s 41-25(2)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/41-25)). A pre-1996 vehicle with a post-1996 replacement engine needs the engine conditions on the [ATO public roads page, QC44648](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/heavy-vehicles/travelling-on-public-roads).
3. **Public road or not.** A road accessible to the public and integrated into the public road network is a public road whoever owns or maintains it; roads solely within private property that serve the owner are not ([ATO, QC44648](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/heavy-vehicles/travelling-on-public-roads); FTR 2008/1). Document the geography; do not assert it (R-AU-FTC-1).
4. **Travelling or not.** Fuel used for travelling on a public road includes stopping or idling during the journey and running the vehicle's systems, including cabin air-conditioning and bus passenger air-conditioning (ATO, QC44648; FTD 2016/1). Movement of a vehicle doing road construction, maintenance or repair, such as a grader or bulldozer, is not travelling and takes the 'all other business uses' rate (same page). Fuel that powers auxiliary equipment of a heavy vehicle takes the 'all other business uses' rate ([ATO 2026-27 rates page, column heading](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business/from-1-july-2026-to-30-june-2027)).
5. **Road user charge.** To the extent fuel is for use in a vehicle travelling on a public road, the credit is reduced by the road user charge ([s 43-10(3)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-10)), unless that travel is incidental to the vehicle's main use ([s 43-10(4)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-10); FTR 2008/1). The ATO's published rates already net off the charge, and the credit is nil where the charge exceeds the fuel tax credit rate ([ATO 2025-26 rates page, notes 3 and 4](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business/from-1-july-2025-to-30-june-2026)).

### Step 4: Apportion the litres

Use any method that is fair and reasonable for the business: constructive (add eligible quantities at each rate), deductive (subtract ineligible fuel from the total), percentage use (a sampled ratio applied over later periods, reviewed when operations change) or estimated use ([ATO, Calculating eligible quantities, QC18683](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/calculating-eligible-quantities); PCG 2016/8; FTD 2010/1). Calculate separately for each rate ([ATO, Working out your fuel tax credits, QC44511](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits)). Litres apportioned across all uses must equal litres acquired, unit by unit and period by period.

ATO conversion rates for gaseous fuels: 1 kg of LPG = 1.885 litres of LPG; 1 megajoule of CNG = 0.01893 kg of CNG (ATO, QC44511).

### Step 5: Simplified methods, only where eligible

**Small claimants (PCG 2016/2).** The guideline applies to liquid fuel where the total fuel tax credit entitlement for the previous 12 months is $10,000 or less and there is a reasonable expectation that the current 12 months will be $10,000 or less ([PCG 2016/2 para 4](https://www.ato.gov.au/law/view/document?docid=COG/PCG20162/NAT/ATO/00001)). The ATO web page describes the same group as claiming 'less than $10,000' each year ([ATO, Simplified fuel tax credits, QC48520](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/simplified-fuel-tax-credits)); apply the guideline's wording and flag an entitlement of exactly $10,000. The guideline does not apply where a Subdivision 41-B disentitlement applies (para 6). Its methods, usable together or separately (para 8):

- Method 1: litres equal total dollars spent on fuel in the period divided by the average GST-inclusive price for the fuel type in the area (para 9).
- Method 2: where the rate changes in a tax period because of indexation, all fuel is treated as acquired on the last day of the period (para 11).
- Method 3: alternative records, such as dollar-only statements, substantiate the claim (para 14).

**Basic method for heavy vehicles (PCG 2021/2).** Available for diesel acquired on or after 1 October 2020 used in a heavy vehicle (GVM over 4.5 tonnes, or 4.5 tonnes or more if acquired before 1 July 2006) both on and off public roads, by a GST-registered claimant meeting the same $10,000 tests; a claimant with no claims in the prior 12 months need not meet the prior-period test ([PCG 2021/2 paras 4 to 6 and footnote 3](https://www.ato.gov.au/law/view/document?docid=COG/PCG20212/NAT/ATO/00001)):

1. On-road litres = kilometres on public roads x diesel consumption rate. Kilometres are either actual, or derived as total kilometres x 98.4% (para 9).
2. Off-road litres, including auxiliary equipment = total eligible diesel less on-road litres (para 10).
3. Credit = on-road litres x heavy vehicle rate plus off-road litres x 'all other business uses' rate (para 11).

A vehicle on this method for a period uses it for all its fuel; it cannot be combined with PCG 2016/11 percentages (para 12). Accepted diesel consumption rates for rigid trucks, in litres per kilometre ([ATO, Basic method for heavy vehicles, QC64655](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/basic-method-for-heavy-vehicles)):

| Rigid truck gross weight | Litres per km |
|---|---|
| Over 4.5 tonnes to 12 tonnes | 0.18 |
| Over 12 tonnes to 16.5 tonnes | 0.23 |
| Over 16.5 tonnes to 24 tonnes | 0.28 |
| Over 24 tonnes to 30 tonnes | 0.32 |
| Over 30 tonnes | 0.35 |

Articulated combinations use PCG 2021/2 Schedule 1, not read for this guide (Needs Input when one arises). Engine diagnostic 'driving fuel' economy may replace the table rate (PCG 2021/2 para 18).

**Any claimant.** A heavy vehicle on the ATO's list of vehicles used mainly off public roads (for example a harvester or backhoe) can claim all its fuel at the 'all other business uses' rate; fuel powering auxiliary equipment can use the ATO's PCG 2016/11 percentages ([ATO, QC48520](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/simplified-fuel-tax-credits)). Read the list and the percentage table at the ATO before relying on either; this guide carries neither.

### Step 6: Price each litre at the rate on its acquisition date

The credit is the effective fuel tax at the rate in force on the day the fuel was acquired or imported, or entered for home consumption if manufactured ([s 43-5(2), (2A)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-5)); the road user charge reduction uses the rate on the same day ([s 43-10(6)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-10)). Split each BAS period at every rate change unless PCG 2016/2 Method 2 genuinely applies. Rates are indexed in February and August, the road user charge changes on its own instrument, and heavy vehicle rates fall to nil when the charge exceeds the rate ([ATO rates index, QC44494, updated 29 July 2026](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business)). The CPI indexation factor for rates from 3 August 2026 was 1.020 (same page).

**2026-27 rates, cents per litre (LNG and CNG: cents per kilogram).** Source: [ATO, From 1 July 2026 to 30 June 2027, QC107638, updated 29 July 2026](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business/from-1-july-2026-to-30-june-2027), read 2 November 2026.

| Fuel acquired | Fuel type | Heavy vehicle travelling on a public road | All other business uses |
|---|---|---|---|
| From 3 August 2026 (current on 2 November 2026) | Liquid fuels such as diesel or petrol; blends B5, B20, E10 | 21.3 | 53.7 |
| From 3 August 2026 | E85 | 0 | 23.015 |
| From 3 August 2026 | LPG (duty paid) | 0 | 17.5 |
| From 3 August 2026 | LNG or CNG (duty paid) | 0 | 36.8 |
| From 3 August 2026 | B100 | 0 | 19.7 |
| 1 July to 2 August 2026 | Liquid fuels such as diesel or petrol; blends B5, B20, E10 | 20.2 | 36.6 |
| 1 July to 2 August 2026 | E85 | 0 | 15.690 |
| 1 July to 2 August 2026 | LPG (duty paid) | 0 | 12.0 |
| 1 July to 2 August 2026 | LNG or CNG (duty paid) | 3.2 | 25.1 |
| 1 July to 2 August 2026 | B100 | 0 | 13.4 |

The 1 July to 2 August 2026 rates reflect excise and excise-equivalent customs duty reduced by 30.4% of the full rate, that is, 69.6% of the unreduced rate from 1 July 2026 to the day before the August adjustment day (Treasury Laws Amendment (Fuel Excise Relief No. 2) Act 2026 (No. 59, 2026) Sch 1 items 1 to 9); from 1 April to 30 June 2026 the reduction was 60.9% and the road user charge was zero ([ATO rates index](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business)). Any rate for fuel acquired after the next indexation day must be read from the ATO page then current.

**2025-26 rates for liquid fuels (diesel, petrol, B5, B20, E10), cents per litre.** Source: [ATO, From 1 July 2025 to 30 June 2026, QC105117, updated 28 April 2026](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business/from-1-july-2025-to-30-june-2026), read 2 November 2026. Other fuel types for 2025-26 are on that page.

| Fuel acquired | Heavy vehicle travelling on a public road | All other business uses |
|---|---|---|
| 1 April to 30 June 2026 | 20.6 | 20.6 |
| 2 February to 31 March 2026 | 20.2 | 52.6 |
| 4 August 2025 to 1 February 2026 | 19.2 | 51.6 |
| 1 July to 3 August 2025 | 18.4 | 50.8 |

**Road user charge.** The Transport Minister sets it by legislative instrument under [s 43-10(8)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-10).

| Period | Liquid fuels (per litre) | Gaseous fuels (per kilogram) | Source |
|---|---|---|---|
| From 3 August 2026 | $0.324 | $0.432 | [Fuel Tax (Road User Charge) Determination 2026 (F2026L00789)](https://www.legislation.gov.au/F2026L00789/latest/text) ss 6 and 7, item 2 ('August adjustment day'); date per ATO 2026-27 rates page note 4 |
| 1 July to 2 August 2026 | $0.164 | $0.219 | Same determination, item 1; ATO 2026-27 rates page note 3 |
| 1 April to 30 June 2026 | Nil | Nil | ATO 2025-26 rates page note 5 |
| 1 July 2025 to 31 March 2026 | $0.324 | $0.432 | ATO 2025-26 rates page notes 3 and 4 |

Until 1 July 2027 the Minister may set or vary a 2025-26 or 2026-27 rate for a day before the determination is made ([s 43-10(13)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/43-10), inserted by Treasury Laws Amendment (Fuel Excise Relief) Act 2026 (No. 22, 2026) Sch 3 item 1, commenced 2 April 2026). Recheck the determination's latest version on the Federal Register before lodging any claim for those years.

### Step 7: Separate a change of use from an error

- **Change of use.** Using fuel differently from the use intended at acquisition gives a fuel tax adjustment equal to the difference in entitlement ([s 44-5](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/44-5)). Fuel with no reasonable prospect of use, such as stolen fuel, gives an adjustment equal to the credit ([s 44-10](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/44-10)). Report it on the BAS for the period the business becomes aware of the actual use or loss, priced at the rate that applied when the fuel was acquired ([ATO, Adjustments, QC18882](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/making-adjustments-and-correcting-errors/adjustments)).
- **The direction trap.** Under the Act a *decreasing* fuel tax adjustment is the one that increases the credit, and an *increasing* fuel tax adjustment is the one that reduces it, because the names describe the net fuel amount ([s 44-5(3), (4)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/44-5); [s 60-5](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/60-5)). On the BAS, an adjustment that increases the credit goes to 7D and one that decreases the credit goes to 7C (ATO, QC18882).
- **Errors.** A figure wrong when the BAS was lodged is an error, not an adjustment. Each error is treated separately and can be corrected only once ([ATO, Errors, QC18882](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/making-adjustments-and-correcting-errors/errors); LI 2023/33). A debit error (over-claim) may be corrected on a later BAS at 7C only if it is within the time limit and the value limit below, the business is not subject to a related compliance activity, and the error is not due to recklessness or intentional disregard; otherwise revise the original period. A credit error (under-claim) goes at 7D on a later BAS within the 4-year period of review, has no value limit, and is also blocked by a related compliance activity (same page).

Debit error limits by current GST turnover ([ATO, Errors, QC18882](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/making-adjustments-and-correcting-errors/errors), read 2 November 2026):

| Current GST turnover | Correct on a BAS lodged within | Net debit errors must be |
|---|---|---|
| Less than $20 million | 18 months of the due date of the BAS containing the error | Less than $12,500 |
| $20 million to less than $100 million | 12 months of that due date | Less than $25,000 |
| $100 million to less than $500 million | 12 months of that due date | Less than $50,000 |
| $500 million to less than $1 billion | 12 months of that due date | Less than $100,000 |
| $1 billion and over | 12 months of that due date | Less than $560,000 |

Credit errors may be offset against debit errors in working out the net figure (same page).

### Step 8: Attribute, check the time limit and label

1. **Attribution.** For a GST-registered business the credit is attributable to the same tax period as the input tax credit for the fuel, or the period one would have been attributable to ([s 65-5(1)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/65-5)); route the GST timing rules to `australia-gst`. An election to attribute an unassessed credit to a later period is irrevocable ([s 65-5(4) to (6)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/65-5)).
2. **Time limit.** The entitlement ceases to the extent it is not taken into account in an assessment within 4 years after the day the return for the attributable period was due, and also to the extent no return taking it into account was given within 4 years after the acquisition day ([s 47-5(1), (2)](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/47-5)). [s 47-10](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/47-10) now holds one exception: a request, made within the 4 years, for the Commissioner to treat a document as a tax invoice under GST Act s 29-70(1B), agreed to after the 4 years. A missed credit claimed on a later BAS uses the rate from the acquisition date ([ATO, QC44518](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/claiming/completing-your-business-activity-statement)).
3. **Labels.** 7D holds the period's credits plus adjustments that increase the credit; write '0' if there is nothing to report rather than leaving it blank. 7C holds adjustments that decrease the credit and debit error corrections (ATO, QC44518 and QC18882). Report whole dollars; the ATO's own worked example drops the cents ($1,991.52 claimed as $1,991: [ATO, QC64655](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/basic-method-for-heavy-vehicles)). The net fuel amount is 7C less 7D ([s 60-5](https://www.ato.gov.au/law/view/document?docid=PAC/20060072/60-5)).
4. **GST instalment payers.** Credits are claimed only on a BAS, not an annual GST return; registering for fuel tax credits moves a GST instalment payer to a quarterly BAS (ATO, QC44518). Refer the attribution detail (R-AU-FTC-5).
5. **Records.** Keep records in writing, in English or readily translated, for 5 years, showing fuel acquired, its use, the apportionment method and the rate used ([ATO, Records you need to keep, QC44516](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/records-you-need-to-keep)).

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Acquisition date unknown for fuel in a period with a rate change | Price at the lower of the rates in force in the period as an estimate; flag, and hold the line open until the dates are evidenced, because Step 6 requires the rate on each acquisition date |
| GVM unknown | No credit for public road travel pending GVM evidence and, if exactly 4.5 tonnes, acquisition-date evidence; flag |
| Manufacture date of a diesel vehicle used on public roads unknown | Treat as before 1 January 1996 without evidence of an environmental criterion; flag |
| Road classification undocumented | Treat as a public road (lower heavy vehicle rate; nil for light vehicles); flag (R-AU-FTC-1) |
| Small claimant status uncertain | Do not use PCG 2016/2 or PCG 2021/2; apportion and split by rate |
| September 2026 quarter, small claimant | Split at 3 August 2026; PCG 2016/2 Method 2 covers indexation changes and that change also ended a temporary excise reduction (Treasury Laws Amendment (Fuel Excise Relief No. 2) Act 2026 (No. 59, 2026) Sch 1 items 1 to 9) and changed the road user charge (Worked case F) |
| Hire chain claimant unclear | No claim by either party in the workpaper until the reviewer decides (R-AU-FTC-2) |
| Change of use or error | Treat as an error until the original intention at acquisition is evidenced |

## Worked cases

All facts are hypothetical. Rates are the ATO figures in Step 6 for the stated acquisition dates.

### Case A: a quarter that straddles the 3 August 2026 rate change

An earthmoving business, GST-registered and claiming well over $10,000 a year, buys diesel in the September 2026 quarter. Telematics and fuel issue records show: 1 July to 2 August 2026, 6,000 litres for off-road plant and 2,000 litres for heavy trucks travelling on public roads; 3 August to 30 September 2026, 9,000 litres off-road and 3,000 litres on public roads. All units exceed 4.5 tonnes GVM and were built after 1 January 1996. Each block is priced at the rate in force on its acquisition date. Applying the 30 September rates to all fuel, which a business of this size cannot do, would over-claim by $1,048.

```oa-check
name: AU 2026-27 September quarter split at the 3 August 2026 rate change
inputs:
  offroad_litres_to_2_aug: 6000
  onroad_litres_to_2_aug: 2000
  offroad_litres_from_3_aug: 9000
  onroad_litres_from_3_aug: 3000
  other_rate_to_2_aug_cents: 36.6
  onroad_rate_to_2_aug_cents: 20.2
  other_rate_from_3_aug_cents: 53.7
  onroad_rate_from_3_aug_cents: 21.3
steps:
  - credit_offroad_to_2_aug: offroad_litres_to_2_aug * other_rate_to_2_aug_cents / 100
  - credit_onroad_to_2_aug: onroad_litres_to_2_aug * onroad_rate_to_2_aug_cents / 100
  - credit_offroad_from_3_aug: offroad_litres_from_3_aug * other_rate_from_3_aug_cents / 100
  - credit_onroad_from_3_aug: onroad_litres_from_3_aug * onroad_rate_from_3_aug_cents / 100
  - label_7d: floor(credit_offroad_to_2_aug + credit_onroad_to_2_aug + credit_offroad_from_3_aug + credit_onroad_from_3_aug)
  - end_rate_total: floor((offroad_litres_to_2_aug + offroad_litres_from_3_aug) * other_rate_from_3_aug_cents / 100 + (onroad_litres_to_2_aug + onroad_litres_from_3_aug) * onroad_rate_from_3_aug_cents / 100)
  - overclaim_if_end_rate_used: end_rate_total - label_7d
expected:
  credit_offroad_to_2_aug: 2196
  credit_onroad_to_2_aug: 404
  credit_offroad_from_3_aug: 4833
  credit_onroad_from_3_aug: 639
  label_7d: 8072
  end_rate_total: 9120
  overclaim_if_end_rate_used: 1048
```

### Case B: basic method for a heavy vehicle, December 2026 quarter

A GST-registered courier with one diesel rigid truck (gross weight over 30 tonnes, manufactured in 2019, so it meets s 41-25(1)(a)) had a total fuel tax credit entitlement of $3,900 in the previous 12 months and expects no more than $10,000 in the current 12 months, so PCG 2021/2 is available. In the December 2026 quarter it buys 3,900 litres of diesel and its logbook shows 10,000 kilometres in total; it uses derived kilometres. No rate change occurs in the quarter, so every litre takes the rates in force from 3 August 2026.

```oa-check
name: AU 2026-27 basic method for heavy vehicles December quarter
inputs:
  total_km: 10000
  derived_km_percent: 98.4
  litres_per_km: 0.35
  total_diesel_litres: 3900
  onroad_rate_cents: 21.3
  other_rate_cents: 53.7
steps:
  - derived_onroad_km: pct(total_km, derived_km_percent)
  - onroad_litres: derived_onroad_km * litres_per_km
  - offroad_litres: total_diesel_litres - onroad_litres
  - onroad_credit: onroad_litres * onroad_rate_cents / 100
  - offroad_credit: offroad_litres * other_rate_cents / 100
  - label_7d: floor(onroad_credit + offroad_credit)
expected:
  derived_onroad_km: 9840
  onroad_litres: 3444
  offroad_litres: 456
  onroad_credit: 733.572
  offroad_credit: 244.872
  label_7d: 978
```

### Case C: change of use reported in the December 2026 quarter

A grain grower bought 1,000 litres of diesel on 20 July 2026 for its harvester and claimed it at the 'all other business uses' rate in the September 2026 quarter. In November 2026 it used that fuel in a 10-tonne diesel truck, manufactured in 2012 (s 41-25(1)(a)), carting grain on public roads instead. The adjustment is priced at the 20 July 2026 rates and reported in the December 2026 quarter, the period it became aware of the actual use. Under the Act it is an increasing fuel tax adjustment; on the BAS it goes to 7C because it reduces the credit.

```oa-check
name: AU 2026-27 change of use adjustment priced at the acquisition-date rates
inputs:
  litres: 1000
  claimed_rate_cents: 36.6
  actual_use_rate_cents: 20.2
steps:
  - credit_claimed: litres * claimed_rate_cents / 100
  - credit_for_actual_use: litres * actual_use_rate_cents / 100
  - label_7c_adjustment: credit_claimed - credit_for_actual_use
expected:
  credit_claimed: 366
  credit_for_actual_use: 202
  label_7c_adjustment: 164
```

### Further positions

- **Case D: a farm ute.** A 3-tonne GVM ute uses diesel on the farm's internal tracks and on the public road to town. Fuel for the public road travel gets no credit (s 41-20); fuel for work on the farm's private tracks is claimable at the 'all other business uses' rate if the split is evidenced. Without a logbook or other fair and reasonable apportionment, the default treats it all as public road use.
- **Case E: an LNG prime mover.** Gas acquired from 3 August 2026 for a heavy vehicle travelling on public roads has a nil credit, because the 43.2 cents a kilogram charge exceeds the gas rate; gas acquired between 1 July and 2 August 2026 for the same use earned 3.2 cents a kilogram. The ATO's ineligible activities page (updated 6 December 2022) lists transport gaseous fuels in heavy vehicles on public roads as ineligible; follow the period-specific rate tables and flag the conflict for the reviewer.
- **Case F: a small claimant's September 2026 quarter.** A contractor whose entitlement is well under $10,000 asks to price all of the quarter's diesel at the 30 September 2026 rate. PCG 2016/2 Method 2 is framed for a rate change 'because of indexation' (para 11), whilst the ATO web page describes using the end-of-period rate 'when there is a change of rate'. The 3 August 2026 change was mainly the end of the temporary excise reduction (Treasury Laws Amendment (Fuel Excise Relief No. 2) Act 2026 (No. 59, 2026) Sch 1 items 1 to 9) and a road user charge change. Default: split at 3 August 2026, and record the end-of-period figure only as a reviewer note.
- **Case G: exactly $10,000.** A claimant's entitlement for the previous 12 months is exactly $10,000. PCG 2016/2 para 4 and PCG 2021/2 para 6 say '$10,000 or less', so the guidelines are available; the ATO web page says 'less than $10,000'. Apply the guideline wording and flag the boundary.
- **Case H: a pre-1996 tip truck.** A 1994 diesel tip truck works on public roads for a civil contractor. No credit unless the truck meets one of the s 41-25(1) criteria, evidenced by audited maintenance program membership, a Rule 147A (DT80) test report or an endorsed maintenance schedule. The same truck used only inside a quarry would be outside s 41-25 because it is not used on a public road.
- **Case I: a debit error above the value limit.** A business with GST turnover under $20 million finds a single $14,000 over-claim on a BAS lodged 10 months ago. It is inside the 18-month time limit but not under $12,500, so it cannot be corrected on a later BAS: the original period must be revised, and penalties and interest may apply (ATO, Errors). Route the disclosure decision to the reviewer (R-AU-FTC-3).

## When to refuse or refer

Stop the affected calculation where a fact, source condition or scope requirement in this guide is unresolved, and return Needs Input or refer it for qualified review.

**Topical refusals**

- **R-AU-FTC-1, road classification and main use.** *Trigger:* the claim depends on whether a road is public, or whether public road travel is incidental to a vehicle's main use. *Message:* "Whether this road is a public road, or this travel is incidental to the vehicle's main use, is a question of fact for the reviewer on documented evidence. The workpaper records the evidence and the tests in FTR 2008/1; it does not decide them."
- **R-AU-FTC-2, claimant in a hire or contract chain.** *Trigger:* more than one party could claim the same fuel. *Message:* "Only one entity can claim each litre, and the claimant is whoever acquired the fuel as a matter of fact (FTR 2009/1). Both parties' claims are held until the reviewer decides who acquired it."
- **R-AU-FTC-3, historical over-claims and disclosure.** *Trigger:* a debit error outside the LI 2023/33 time or value limits, a suspected reckless or deliberate over-claim, or a request to decide on a voluntary disclosure. *Message:* "This error cannot be corrected on a later BAS. Revising the original period and any voluntary disclosure are decisions for the registered agent and the business; the workpaper quantifies the error only."
- **R-AU-FTC-4, compliance activity on foot.** *Trigger:* the ATO has notified a review, audit or verification of fuel tax credits. *Message:* "Errors related to the matter or period under review generally cannot be corrected on a later BAS. Discuss them with the ATO through the registered agent before any correction."
- **R-AU-FTC-5, out-of-scope regimes.** *Trigger:* fuel manufactured or imported by the claimant, packaging or supply claims, blends, aviation fuels, a non-profit emergency vehicle claim without GST registration, a fuel tax return or GST instalment attribution. *Message:* "This claim falls outside this guide. Refer it to a practitioner who handles that regime."
- **R-AU-FTC-6, unread rates.** *Trigger:* fuel acquired before 1 July 2025 (other than 2025-26 liquid fuels), after the next indexation day, or in an articulated combination on the basic method. *Message:* "The rate or consumption figure for this fuel is not carried in this guide. Read it from the ATO page or instrument in force for the acquisition date, record the source and date, and resubmit."

**Reviewer attention thresholds (guide policy, not law)**

- Any period whose 7D exceeds $10,000 for a claimant that used PCG 2016/2 or PCG 2021/2 in the previous 12 months.
- Any claim where a road classification or main use conclusion moves the credit by more than $1,000 in a period.
- Any adjustment or error correction above $5,000, and any net debit error above 80% of the applicable value limit.
- Any credit claimed more than 3 years after the due date of the BAS for the attributable period.

**Prohibitions**

- Never state a fuel tax credit rate, road user charge, GVM threshold, safe harbour percentage, entitlement ceiling or error limit from memory; read it from the source for the acquisition date.
- Never price fuel at the use date or the BAS period end without an applicable simplified method.
- Never claim for a light vehicle's public road travel, or for one litre twice.
- Never lodge, revise a BAS, contact the ATO or decide on a disclosure.

## Completion checklist

- [ ] Litres apportioned across all uses equal litres acquired, for each unit and period; nothing apportions more fuel than was acquired.
- [ ] Each rate band's litres tie to the acquisition-date split, and the banded credits tie to 7D.
- [ ] Every unit is classified against the 4.5 tonne GVM test and, if diesel and used on public roads, the s 41-25 environmental criteria, with register evidence.
- [ ] The apportionment method is named, dated and rechecked for fleet, route or work-mix changes since it was set.
- [ ] Simplified method eligibility is evidenced from the preceding 12 months' entitlement, and no basic method vehicle also uses PCG 2016/11 percentages.
- [ ] Adjustments and error corrections are on the right label: credit increases at 7D, decreases at 7C; 7D shows '0' rather than blank.
- [ ] The net fuel amount rebuilt from s 60-5 agrees to 7C less 7D.
- [ ] Every claimed period is inside both s 47-5 limbs.
- [ ] Each rate and road user charge figure cites its ATO page or instrument and the date it was read; the s 43-10(13) recheck is recorded for 2025-26 and 2026-27 claims.
- [ ] Reviewer brief additions: the method used for each unit, the rate tables applied by date, each conservative default triggered, and each refusal raised.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fuel Tax Act 2006 ss 41-5, 41-20, 41-25, 43-5, 43-10 (including (13)), 44-5, 44-10, 47-5, 60-5 and 65-5 (ATO legal database, CCH consolidation) | https://www.ato.gov.au/law/view/document?docid=PAC/20060072/41-5 (and the matching docid for each section) | 2026-11-02 |
| Treasury Laws Amendment (Fuel Excise Relief No. 2) Act 2026 (No. 59, 2026), as made, Sch 1 items 1 to 9 (rate reduction period ends the day before the August adjustment day) | https://www.legislation.gov.au/C2026A00059/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| Treasury Laws Amendment (Fuel Excise Relief) Act 2026 (No. 22, 2026), as made, Sch 3 item 1 (inserts s 43-10(13)) | https://www.legislation.gov.au/C2026A00022/asmade/2026-04-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-02 |
| Fuel Tax Act 2006 s 47-10 (ATO legal database) | https://www.ato.gov.au/law/view/document?docid=PAC/20060072/47-10 | 2026-11-02 |
| Fuel Tax (Road User Charge) Determination 2026 (F2026L00789), made 22 June 2026, commenced 1 July 2026, ss 5 to 7 | https://www.legislation.gov.au/F2026L00789/latest/text | 2026-11-02 |
| ATO, Rates - business (QC44494, updated 29 July 2026): indexation, 1.020 factor, 2026 excise reductions | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business | 2026-11-02 |
| ATO, From 1 July 2026 to 30 June 2027 (QC107638, updated 29 July 2026): Tables 1 and 2, notes 1 to 4 | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business/from-1-july-2026-to-30-june-2027 | 2026-11-02 |
| ATO, From 1 July 2025 to 30 June 2026 (QC105117, updated 28 April 2026): Tables 1 to 4, notes 3 to 5 | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/rates-business/from-1-july-2025-to-30-june-2026 | 2026-11-02 |
| PCG 2016/2, paras 3 to 14 (small claimants) | https://www.ato.gov.au/law/view/document?docid=COG/PCG20162/NAT/ATO/00001 | 2026-11-02 |
| PCG 2021/2, paras 4 to 24 and footnotes (basic method for heavy vehicles) | https://www.ato.gov.au/law/view/document?docid=COG/PCG20212/NAT/ATO/00001 | 2026-11-02 |
| ATO, Simplified fuel tax credits (QC48520, updated 6 July 2021) | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/simplified-fuel-tax-credits | 2026-11-02 |
| ATO, Basic method for heavy vehicles (QC64655, updated 2 June 2021): consumption table, worked example | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/basic-method-for-heavy-vehicles | 2026-11-02 |
| ATO, Working out your fuel tax credits (QC44511, updated 6 July 2021): steps, gaseous fuel conversions | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits | 2026-11-02 |
| ATO, Calculating eligible quantities (QC18683, updated 6 July 2021) | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/calculating-eligible-quantities | 2026-11-02 |
| ATO, Records you need to keep (QC44516, updated 22 February 2023) | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/working-out-your-fuel-tax-credits/records-you-need-to-keep | 2026-11-02 |
| ATO, Completing your business activity statement (QC44518, updated 30 August 2024): 7C, 7D, earlier periods, contracts, GST instalments | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/claiming/completing-your-business-activity-statement | 2026-11-02 |
| ATO, Adjustments and Errors (QC18882, updated 9 October 2023): labels, time and value limits | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/making-adjustments-and-correcting-errors/errors | 2026-11-02 |
| ATO, Travelling on public roads (QC44648, updated 22 February 2023): public roads, travelling, environmental criteria | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/in-detail/heavy-vehicles/travelling-on-public-roads | 2026-11-02 |
| ATO, Eligibility (QC44501), Registering (QC44510) and Ineligible fuels and activities (QC44509, updated 6 December 2022) | https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/fuel-schemes/fuel-tax-credits-business/eligibility/ineligible-fuels-and-activities | 2026-11-02 |

Named but not read for this guide: FTR 2007/1, FTR 2008/1, FTR 2009/1, FTD 2010/1, FTD 2016/1, PCG 2016/8, PCG 2016/11, LI 2023/33 itself (its limits are taken from the ATO Errors page) and the ATO list of heavy vehicles used mainly off public roads. Read each before relying on a position that turns on it.

Method adapted by its author from the `fuel-tax-credits` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

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
