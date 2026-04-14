---
name: global-travel-expenses
description: >
  Travel expense classification patterns for freelancers and small businesses worldwide.
  Covers flights, hotels, ground transport, meals, per-diem rates by country, and
  co-working while travelling. Includes the business purpose test and deductibility
  rules across jurisdictions.
version: 0.1
category: patterns
depends_on: []
---

# Global Travel Expense Pattern Library v0.1

## What this file is

**Functional role:** Transaction pattern recognition and deductibility rules for travel expenses
**Status:** Active reference data

Travel expenses are the second most error-prone category in freelancer bookkeeping (after payment processors). The core challenge: business travel is deductible, personal travel is not, and mixed-purpose trips require apportionment. This file provides pattern-matching rules for common travel vendors and jurisdiction-specific deductibility rules.

---

## The business purpose test

> **Would this trip have happened without the business reason?**
>
> - If YES --> the travel cost is NOT deductible (it is a personal expense that coincidentally overlapped with some business activity)
> - If NO --> the travel cost IS deductible (the trip was undertaken for business purposes)
>
> **Mixed-purpose trips:** If a trip has both business and personal days, only the business portion is deductible. Transport to/from the destination is typically fully deductible if the primary purpose is business (majority of days = business).

---

## Vendor lookup table

### Flights

| Bank statement text | Vendor | Category | Deductible? | VAT treatment | Notes |
|---|---|---|---|---|---|
| `RYANAIR` | Ryanair | Travel - Flights | Yes, if business purpose | EU: VAT exempt (international) or zero-rated. Domestic flights: local VAT may apply. | Budget carrier. IE entity. |
| `FR RYANAIR` | Ryanair | Travel - Flights | Yes, if business purpose | Same as above. | Card statement variant. |
| `EASYJET` | easyJet | Travel - Flights | Yes, if business purpose | Same VAT treatment as Ryanair. | UK entity. |
| `EASYJET *` | easyJet | Travel - Flights | Yes, if business purpose | Same as above. | |
| `BRITISH AIRWAYS` | British Airways | Travel - Flights | Yes, if business purpose | International flights: zero-rated/exempt. UK domestic: standard rate. | UK entity. |
| `BRITISH AIRWAY` | British Airways | Travel - Flights | Yes, if business purpose | Same as above. | Truncated. |
| `LUFTHANSA` | Lufthansa | Travel - Flights | Yes, if business purpose | DE entity. International: exempt. DE domestic: 19% VAT. | |
| `LH LUFTHANSA` | Lufthansa | Travel - Flights | Yes, if business purpose | Same as above. | |
| `AIR FRANCE` | Air France | Travel - Flights | Yes, if business purpose | FR entity. International: exempt. FR domestic: 10% TVA. | |
| `KLM` | KLM | Travel - Flights | Yes, if business purpose | NL entity. International: exempt. | Part of Air France-KLM. |
| `DELTA AIR` | Delta Air Lines | Travel - Flights | Yes, if business purpose | US entity. US domestic: 7.5% excise tax (not reclaimable). | |
| `UNITED AIRLINES` | United Airlines | Travel - Flights | Yes, if business purpose | US entity. Same as Delta. | |
| `AMERICAN AIRLINE` | American Airlines | Travel - Flights | Yes, if business purpose | US entity. Same as Delta. | |
| `SOUTHWEST AIR` | Southwest Airlines | Travel - Flights | Yes, if business purpose | US entity. Same as Delta. | |
| `QANTAS` | Qantas | Travel - Flights | Yes, if business purpose | AU entity. Domestic: 10% GST (claimable). International: GST-free. | |
| `EMIRATES` | Emirates | Travel - Flights | Yes, if business purpose | AE entity. No VAT on international flights. | |
| `VUELING` | Vueling | Travel - Flights | Yes, if business purpose | ES entity. International: exempt. ES domestic: 10% IVA. | |
| `WIZZAIR` | Wizz Air | Travel - Flights | Yes, if business purpose | HU entity. International: exempt. | Budget carrier. |
| `WIZZ AIR` | Wizz Air | Travel - Flights | Yes, if business purpose | Same as above. | |
| `NORWEGIAN` | Norwegian Air | Travel - Flights | Yes, if business purpose | NO entity. International: exempt. | |
| `TAP PORTUGAL` | TAP Air Portugal | Travel - Flights | Yes, if business purpose | PT entity. International: exempt. | |
| `AIRMALTA` | Air Malta | Travel - Flights | Yes, if business purpose | MT entity. International: exempt. | |
| `BOOKING.COM *FL` | Booking.com (Flight) | Travel - Flights | Yes, if business purpose | NL entity. Acts as agent — VAT on service fee only. Flight itself follows airline VAT rules. | Booking.com is an intermediary. |
| `EXPEDIA *` | Expedia | Travel - Flights | Yes, if business purpose | US entity. Agent model — VAT varies. | Check if Expedia or airline is the merchant. |
| `SKYSCANNER` | Skyscanner | Travel - Flights | Skyscanner redirects to airlines/agents. The charge is from the actual seller. | N/A — Skyscanner does not charge directly. | If you see a Skyscanner charge, it is likely through a partner. |
| `KIWI.COM` | Kiwi.com | Travel - Flights | Yes, if business purpose | CZ entity. Acts as agent or MoR depending on booking. | Check invoice carefully. |
| `GOOGLE *FLIGHTS` | Google Flights | Travel - Flights | Google redirects — charge is from airline/agent. | N/A. | Google Flights does not sell tickets directly. |

### Hotels and accommodation

| Bank statement text | Vendor | Category | Deductible? | VAT treatment | Notes |
|---|---|---|---|---|---|
| `BOOKING.COM` | Booking.com | Travel - Accommodation | Yes, if business purpose | NL entity (Booking.com B.V.). Hotel charges VAT, not Booking.com. Booking.com's commission is a separate B2B service. | Booking.com is an agent — the hotel is the supplier. |
| `BOOKING *` | Booking.com | Travel - Accommodation | Yes, if business purpose | Same as above. | |
| `BDC *HOTEL` | Booking.com | Travel - Accommodation | Yes, if business purpose | Same as above. | Card statement format. |
| `AIRBNB` | Airbnb | Travel - Accommodation | Yes, if business purpose | IE entity for EU (Airbnb Ireland UC). Airbnb is a MARKETPLACE — VAT treatment differs from hotels. Airbnb charges VAT on its service fee. The host may or may not charge VAT. | Airbnb invoices are split: accommodation (from host) + service fee (from Airbnb). Only Airbnb's service fee has clear VAT treatment. |
| `AIRBNB *` | Airbnb | Travel - Accommodation | Yes, if business purpose | Same as above. | |
| `HOTELS.COM` | Hotels.com (Expedia) | Travel - Accommodation | Yes, if business purpose | US entity (Expedia group). Agent model in most markets. | |
| `EXPEDIA *HOTEL` | Expedia | Travel - Accommodation | Yes, if business purpose | Check if merchant model or agency model — VAT treatment differs. | |
| `MARRIOTT` | Marriott | Travel - Accommodation | Yes, if business purpose | Hotel charges local VAT/tourism tax at the rate of the hotel's country. | Large hotel chain. |
| `HILTON` | Hilton | Travel - Accommodation | Yes, if business purpose | Same as Marriott. | |
| `HILTON *` | Hilton | Travel - Accommodation | Yes, if business purpose | Same as above. | |
| `IHG *` | IHG (Holiday Inn, etc.) | Travel - Accommodation | Yes, if business purpose | Same as Marriott. | InterContinental Hotels Group. |
| `ACCOR` | Accor (Novotel, ibis, etc.) | Travel - Accommodation | Yes, if business purpose | FR entity. Local VAT applies at hotel location. | |
| `PREMIER INN` | Premier Inn | Travel - Accommodation | Yes, if business purpose | UK entity. 20% VAT on accommodation. | UK budget hotel chain. |
| `TRAVELODGE` | Travelodge | Travel - Accommodation | Yes, if business purpose | UK entity. 20% VAT. | UK budget chain. |
| `HOSTELWORLD` | Hostelworld | Travel - Accommodation | Yes, if business purpose | IE entity. Agent model. | Budget accommodation. |

### Ground transport

| Bank statement text | Vendor | Category | Deductible? | VAT treatment | Notes |
|---|---|---|---|---|---|
| `UBER *TRIP` | Uber | Travel - Ground transport | Yes, if business purpose | NL entity for EU (Uber B.V.). UK: Uber charges 20% VAT. US: no sales tax on most rides. | Uber provides VAT invoices in most EU/UK markets. |
| `UBER *` | Uber | Travel - Ground transport | Yes, if business purpose | Same as above. | |
| `UBER EATS` | Uber Eats | Meals (NOT transport) | See meals rules below | Different from Uber rides. | Do not classify as transport. |
| `BOLT` | Bolt (Taxify) | Travel - Ground transport | Yes, if business purpose | EE entity. EU: local VAT rules apply. | European ride-hailing. |
| `BOLT.EU` | Bolt (Taxify) | Travel - Ground transport | Yes, if business purpose | Same as above. | |
| `LYFT` | Lyft | Travel - Ground transport | Yes, if business purpose | US entity. | Primarily US market. |
| `LYFT *RIDE` | Lyft | Travel - Ground transport | Yes, if business purpose | Same as above. | |
| `EUROSTAR` | Eurostar | Travel - Ground transport | Yes, if business purpose | UK/FR/BE entity depending on route. Zero-rated for international segments in UK. | International rail. |
| `THALYS` | Thalys (now Eurostar) | Travel - Ground transport | Yes, if business purpose | Same as Eurostar. | Merged with Eurostar. |
| `SNCF` | SNCF | Travel - Ground transport | Yes, if business purpose | FR entity. 10% TVA on domestic rail. | French national rail. |
| `SNCF *` | SNCF | Travel - Ground transport | Yes, if business purpose | Same as above. | |
| `DB BAHN` | Deutsche Bahn | Travel - Ground transport | Yes, if business purpose | DE entity. 7% VAT on domestic passenger transport. | German rail. |
| `DB FERNVERKEHR` | Deutsche Bahn (long-distance) | Travel - Ground transport | Yes, if business purpose | Same as above. | |
| `TRENITALIA` | Trenitalia | Travel - Ground transport | Yes, if business purpose | IT entity. 10% IVA on domestic rail. | Italian rail. |
| `RENFE` | Renfe | Travel - Ground transport | Yes, if business purpose | ES entity. 10% IVA on domestic rail. | Spanish rail. |
| `NS.NL` | NS (Dutch Railways) | Travel - Ground transport | Yes, if business purpose | NL entity. 9% BTW on domestic rail. | |
| `TFL *` | Transport for London | Travel - Ground transport | Yes, if business purpose | UK entity. Zero-rated public transport. No VAT to reclaim. | Tube, bus, Overground, Elizabeth line. |
| `TRAINLINE` | Trainline | Travel - Ground transport | Yes, if business purpose | UK entity. Agent — VAT is on the train ticket, not Trainline's fee (which is zero). | Booking platform. |
| `HERTZ` | Hertz | Travel - Car rental | Yes, if business purpose | Local entity. VAT at local rate on rental. | Car rental. |
| `HERTZ *` | Hertz | Travel - Car rental | Yes, if business purpose | Same as above. | |
| `SIXT` | Sixt | Travel - Car rental | Yes, if business purpose | DE entity. Local VAT applies. | |
| `SIXT *` | Sixt | Travel - Car rental | Yes, if business purpose | Same as above. | |
| `ENTERPRISE` | Enterprise Rent-A-Car | Travel - Car rental | Yes, if business purpose | Local entity. | |
| `EUROPCAR` | Europcar | Travel - Car rental | Yes, if business purpose | FR entity. Local VAT applies. | |
| `AVIS` | Avis | Travel - Car rental | Yes, if business purpose | Local entity. | |
| `BUDGET RENT` | Budget (Avis group) | Travel - Car rental | Yes, if business purpose | Same group as Avis. | |
| `FREENOW` | FREE NOW (MyTaxi) | Travel - Ground transport | Yes, if business purpose | DE/IE entity. Local VAT rules. | Taxi app. |
| `CABIFY` | Cabify | Travel - Ground transport | Yes, if business purpose | ES entity. | Spain/LatAm ride-hailing. |
| `GRABPAY` | Grab | Travel - Ground transport | Yes, if business purpose | SG entity. Local VAT/GST rules. | Southeast Asia. |
| `LIME *` | Lime | Travel - Ground transport | Yes, if business purpose | US entity. | E-scooters/bikes. |

### Meals while travelling

| Bank statement text | Vendor | Category | Deductible? | VAT treatment | Notes |
|---|---|---|---|---|---|
| `[RESTAURANT NAME]` | Various restaurants | Travel - Meals | Partially deductible (varies by country — see table below) | Local VAT on food/drink at local rates. | Must be during business travel. Meals at home city are generally NOT deductible (unless client entertainment). |
| `UBER EATS` | Uber Eats | Travel - Meals | Same as restaurant meals | Platform model — VAT varies. | Delivery during business travel. |
| `DELIVEROO` | Deliveroo | Travel - Meals | Same as restaurant meals | UK/EU entity. | Same note. |
| `JUST EAT` | Just Eat | Travel - Meals | Same as restaurant meals | NL entity (Just Eat Takeaway). | Same note. |

**Meal deductibility by jurisdiction:**

| Jurisdiction | Deductible % | Conditions | Notes |
|---|---|---|---|
| **US** | 50% of actual cost (meals while travelling for business) | Must be away from "tax home". Lavish/extravagant meals disallowed. No deduction for meals with no business purpose. | The 100% temporary deduction for restaurant meals expired after 2022. Back to 50% for 2023+. |
| **UK** | 100% | Must be "wholly and exclusively" for business. Subsistence while travelling on business qualifies. Regular commute meals do NOT qualify. | HMRC allows reasonable meal costs while travelling for business. |
| **Germany** | Actual cost NOT deductible for self-employed meals. Use per-diem (Verpflegungspauschale) instead. | See per-diem table below. | Self-employed: actual meal costs are not deductible. Only the flat per-diem rate applies. |
| **France** | Actual cost minus "normal meal cost" (repas pris a domicile). 2025: approx. EUR 5.35 deducted per meal. | Only the excess over normal home-eating cost is deductible. Cap of ~EUR 20.70 per meal. | Complex calculation. Per-diem is simpler. |
| **Australia** | 100% if incidental to travel | Must be travelling overnight for business. Day-trip meals generally not deductible. | Overtime meal allowance is separate. |
| **Canada** | 50% of actual cost | Must be while travelling for business (away from metropolitan area for 12+ hours). | Long-haul truck drivers: 80%. |
| **Spain** | Deductible up to EUR 26.67/day (domestic) or EUR 48.08/day (international) | These are the maximum amounts. Excess is not deductible. | Per Reglamento del IRPF art. 9. |
| **Italy** | 75% of actual cost (up to 2% of revenue) | Cap linked to total revenue. | Complicated cap system. |
| **Netherlands** | 80% of actual cost | 20% is deemed personal benefit (forfaitaire bijtelling). | Always 80%, regardless of purpose. |
| **India** | 100% if genuinely for business | Must be for business travel. Personal meals not deductible. | Keep receipts. |

### Per-diem rates by jurisdiction (alternative to actual costs)

Many jurisdictions allow a flat daily allowance instead of tracking actual meal/incidental costs. Per-diem simplifies record-keeping and is often more generous than actual costs for modest spenders.

| Jurisdiction | Domestic per-diem rate | International per-diem rate | Hours threshold | Notes |
|---|---|---|---|---|
| **US** | Varies by city (GSA rates). Range: $59-$79/day for meals & incidentals (M&IE). High-cost cities up to $79. | Set by State Department per destination city. | Must be away overnight. | GSA rates updated annually at gsa.gov. Can use "high-low" simplified method: $310/$75 (high-cost) or $220/$75 (other). |
| **UK** | Benchmark scale rates: Breakfast GBP 11, Lunch GBP 11, Dinner GBP 26, plus incidentals GBP 5-10/night. | Same rates or actual. | Must be travelling for business. | HMRC Employment Income Manual EIM05231. Sole traders can use these as a benchmark. |
| **Germany** | EUR 16/day (travel 8-24 hours), EUR 32/day (24-hour absence), EUR 16 for arrival/departure days. | Varies by country (BMF publishes list annually). E.g., US $66, UK GBP 52, FR EUR 58 for 24-hour absence. | 8+ hours absence from home/primary workplace. | Verpflegungspauschale. First 3 months of same location only. After 3 months at same destination: no more per-diem. |
| **France** | Forfait repas: ~EUR 20.70/meal (employee). Self-employed (BNC): actual costs or forfait at URSSAF rates. | Varies by country. | Must be away from normal workplace. | URSSAF baremes. Complex for self-employed. |
| **Australia** | ATO reasonable travel allowance rates (updated annually). 2024-25: varies by salary band. Tier 1 (lowest salary): AUD 131.65/day (meals), AUD 309/night (accommodation capital cities). | Varies by country (ATO publishes table). | Must be travelling overnight. | Tax Determination TD 2024/3 (or latest). |
| **Canada** | Treasury Board rates. 2025: CAD 23.40 breakfast, CAD 23.55 lunch, CAD 52.15 dinner, CAD 17.30 incidentals = CAD 116.40/day. | NJC rates by destination. | Must be away from metropolitan area 12+ hours. | Only 50% of meal per-diem is deductible for tax (same as actual). |
| **Spain** | EUR 26.67/day (domestic), EUR 48.08/day (international). Accommodation: EUR 53.34/day (domestic), EUR 91.35/day (international). | See domestic column — international rate is higher. | Must be outside municipality of workplace. | Reglamento IRPF art. 9. These are tax-free maximums for employees. Self-employed: consult advisor. |
| **Italy** | EUR 46.48/day (domestic lump sum) or actual with 75% deductibility. | EUR 77.47/day (varies by destination, MEF decree). | Must be outside municipality of workplace. | Complex interaction between 75% meal cap and 2%-of-revenue overall cap. |
| **Netherlands** | No official per-diem for self-employed. Must use actual costs (80% deductible for meals). | Same — no per-diem available. | N/A. | NL does not offer per-diem for zelfstandigen. |
| **India** | No statutory per-diem for self-employed. Actual costs only. | Same. | N/A. | Keep all receipts. |
| **Malta** | No official per-diem. Actual costs, must demonstrate business purpose. | Same. | N/A. | IRD practice: reasonable costs accepted with documentation. |

### Co-working while travelling

| Bank statement text | Vendor | Category | Deductible? | VAT treatment | Notes |
|---|---|---|---|---|---|
| `WEWORK` | WeWork | Travel - Co-working / Office expenses | Yes, if business purpose | Local entity. Local VAT on office rental. Most jurisdictions: standard-rated. | Day pass or hot desk. |
| `WEWORK *` | WeWork | Travel - Co-working / Office expenses | Yes, if business purpose | Same as above. | |
| `SPACES` | Spaces (IWG/Regus) | Travel - Co-working / Office expenses | Yes, if business purpose | NL/local entity. Standard-rated VAT. | Part of IWG group. |
| `REGUS` | Regus (IWG) | Travel - Co-working / Office expenses | Yes, if business purpose | Same group as Spaces. | |
| `IWG *` | IWG (Regus/Spaces) | Travel - Co-working / Office expenses | Yes, if business purpose | Same as above. | |
| `HUBBLE HQ` | Hubble | Travel - Co-working / Office expenses | Yes, if business purpose | UK entity. 20% VAT. | UK co-working marketplace. |
| `DESKPASS` | Deskpass | Travel - Co-working / Office expenses | Yes, if business purpose | US entity. | Co-working day pass aggregator. |
| `CROISSANT` | Croissant | Travel - Co-working / Office expenses | Yes, if business purpose | US entity. | Co-working membership. |
| `[LOCAL COWORKING]` | Various local co-working spaces | Travel - Co-working / Office expenses | Yes, if business purpose | Local VAT rates apply. | Many small co-working spaces appear under their own name. |

---

## Mixed-purpose trip apportionment rules

### Rule: primary purpose determines transport deductibility

| Scenario | Transport (flights/trains) | Accommodation | Meals |
|---|---|---|---|
| 5 business days, 0 personal days | 100% deductible | 100% deductible | Per local rules (see above) |
| 5 business days, 2 weekend personal days | 100% deductible (primary purpose is business) | Business days only | Business days only |
| 3 business days, 4 personal days | NOT deductible (primary purpose is personal) in US. Apportioned in some other jurisdictions. | Business days only | Business days only |
| Business conference + 1 extra day tourism | 100% transport if primary purpose is conference | Conference days + 1 extra night | Conference days only |
| Spouse/partner travels along | Only the employee/freelancer's costs. No deduction for companion. | Single-room rate only (not the couple supplement). | Freelancer's meal only. |

**US-specific rule (IRC Section 274(c)):** For foreign travel of 7+ days where personal days exceed 25% of total days, transport must be apportioned (business days / total days).

---

## Common mistakes

1. **Deducting daily commute as business travel.** Travel from home to your regular place of work is commuting, not business travel. It is never deductible (in any jurisdiction). Travel from your regular place of work to a client site, or travel to a temporary workplace, is business travel.

2. **Not separating Airbnb service fee from accommodation cost.** Airbnb invoices split the charge into accommodation (paid to host) and service fee (paid to Airbnb). The VAT treatment differs. The accommodation portion may or may not include VAT depending on the host's VAT status.

3. **Claiming meals at home city.** Meals are only deductible as travel expenses when you are away from your tax home on business. Lunch at your local cafe is not a business travel expense.

4. **Ignoring per-diem as an alternative.** Many freelancers track actual receipts for meals when the per-diem flat rate would be simpler and sometimes more generous. Check the per-diem rate first.

5. **Forgetting tourism taxes.** Many cities charge a tourism/city tax (taxe de sejour, Kurtaxe, tassa di soggiorno). This IS part of the accommodation cost and IS deductible if the stay is for business.

6. **No business purpose documentation.** Always record WHY you travelled: client name, meeting purpose, conference name, project reference. Without this, the deduction is indefensible on audit.

---

## Disclaimer

This file provides general guidance for classifying travel expenses. Tax rules on travel deductibility, per-diem rates, and meal caps change annually. Always verify rates against the relevant tax authority's current publications. This is not tax advice. A qualified professional should review all classifications before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
