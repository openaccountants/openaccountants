---
name: global-travel-expenses
description: "Apply the 2026 cross-country travel expense method to flights, lodging, transport, meals and coworking. Confirm taxpayer, business purpose, itinerary and reimbursement before country-specific limits. Preserve merchant recognition hints, distinguish employee allowances from business deductions and hold unconfirmed per-diem figures."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: cross-country-method
checked_on: 2026-11-14
---

# Business travel, meals and mixed-purpose trip costs v1.0

## Scope and required facts

Checked on 2026-11-14 for 2026. Obtain the claimant's country/subnational jurisdiction, employee/sole trader/company role, accounting/tax basis, ordinary workplace/tax home and trip itinerary with departure/return times, client/project/conference evidence, business/standby/private days, travel companions and their roles, actual itemised receipts/tax invoices, who contracted/paid, reimbursements and any allowance scheme. Record currencies, hotel/transport actual supplier versus booking agent, meals included in accommodation, and costs already claimed. A brand, city or business-looking narrative is not eligibility evidence.

This method separates flights, hotels/short stays, ground transport/car hire, travel meals and temporary coworking. Vehicle mileage belongs to `global-vehicle-expenses`, home workspace to `global-home-office`, and recurring SaaS/processor charges to their named methods. A freelancer's deduction is not automatically an employee's tax-free reimbursement scale.

## The method, step by step

1. **Prove the business reason.** Determine why the trip occurred, where work happened and whether costs were incurred for the actual business. A useful counterfactual ('would the trip happen without this work?') is not a statutory worldwide yes/no test. A business meeting during a holiday does not make the whole trip business; incidental holiday days do not automatically defeat every business cost.
2. **Build the itinerary and cost map.** Separate transport to/from the destination, local travel, accommodation, meals, entertainment, coworking, city/tourism taxes, tips, baggage and other services. Split bundled invoices on a supportable basis, identify credits/refunds and exclude companion/private additions where required. Do not add a booking intermediary's commission twice or infer that the intermediary is always agent or always principal from its name.
3. **Apply each country's journey rules.** Ordinary commuting, temporary-site travel, tax home, overnight/sleep-rest requirements and special work categories vary. The old 'never deductible in any jurisdiction' commute claim was false; a separate commute deduction or qualifying home office can matter. A local meal is not automatically travel, but some countries have a business-meal/extra-workplace-meal rule even in the home city. Preserve the purpose test and ask for the missing facts rather than making a universal city boundary.
4. **Allocate mixed-purpose costs under that country's rule.** Establish domestic/foreign travel, day counting, primary purpose, control, standby/weekend treatment and incremental private costs. Do not use a simple majority-of-days rule worldwide. The specific US foreign exceptions and destination costs below differ from domestic transport rules. A single extra tourism night is not automatically deductible, and a companion who actually meets the relevant business/employee conditions is not automatically excluded solely because they are a spouse.
5. **Choose an eligible actual-cost or allowance method.** Verify claimant, location, dates, published year, hours, supplied meals, duration limits, reimbursement and receipt rules. An employer scale, Treasury Board/NJC rate or URSSAF allowance is not automatically a sole trader's expense. Do not claim both an allowance and the same actual meal/hotel costs. Obtain the actual current locality rate if it is not printed here; no guessed global per-diem range is supplied.
6. **Apply the deductible fraction/cap in the correct order.** Separate private/reimbursed amounts and excess costs, then apply the country business-purpose restriction, daily maximum, deemed personal portion and percentage rule. A rate for food is not a lodging allowance. Keep income tax distinct from VAT/GST: zero rate, exemption and outside-scope are different outcomes, and foreign VAT is not automatically recoverable on the domestic return.
7. **Resolve the tax invoice and reporting.** Identify actual carrier/host/hotel/agent, place/route, services and tax charged. Airline, ride-hailing and booking-platform brand do not certify an entity, agency contract or tax rate. For UK passenger transport, Notice 744A includes qualifying domestic/scheduled-flight zero rating and exceptions; 'all UK domestic flights standard-rated' was wrong. Notice 700 requires actual input-tax evidence and gives specific business-travel subsistence/accommodation rules; cash employee allowances are not a VAT invoice. Other countries require their own law. [Notice 744A](https://www.gov.uk/guidance/the-vat-treatment-of-passenger-transport-notice-744a); [Notice 700 sections 10.6/12.1](https://www.gov.uk/guidance/vat-guide-notice-700).
8. **Reconcile and deliver.** Match card/bank to invoices and booking credits, avoid bill/payment duplicates, allocate service dates where the accounting basis requires, retain original/functional currencies and documented translation policy. The conditional AASB 121 reporting policy distinguishes recognition, closing balances and settlement, rather than using payment date universally. Output source-linked eligible/excluded costs, meal/allowance computation, tax treatment, report mapping and unresolved items; for a read-only ledger, provide postings/import for human approval. [HMRC records](https://www.gov.uk/self-employed-records/what-records-to-keep); [AASB 121](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf).

## United States

Publication 463's structural method is the 2025 edition used here; current 2026 per-diem localities/rates and form revisions are not restated. Determine tax home and a qualifying need for sleep/rest, ordinary/necessary purpose and no lavish/extravagant meal. Actual travel meals or the eligible federal M&IE method generally face the meal restriction below; actual lodging remains different from an employee reimbursement per diem. Retain time/place/business purpose even when receipts are not needed for a standard-meal method, and do not use a self-employed lodging flat rate that IRS does not provide. Current locality/fiscal-year tables, foreign State/DOD areas, partial-day proration and transport-industry exceptions require their actual source for the dates. [Publication 463, Travel Expenses](https://www.irs.gov/publications/p463).

| Rule | Condition/value | Official source |
|---|---|---|
| Ordinary unreimbursed eligible business meals | Generally 50% of actual or eligible standard-meal amount, with purpose/reimbursement/exception rules; not a blanket deduction for personal food | https://www.irs.gov/publications/p463 |
| Foreign-trip one-week exception | A week or less means 7 consecutive days; do not count US departure day, count return day for this specific exception | https://www.irs.gov/publications/p463 |
| Foreign-trip limited-personal-time exception | More than a week and less than 25% nonbusiness time; for this test count both trip-begin/end days; exactly 25% does not satisfy 'less than' | https://www.irs.gov/publications/p463 |

The other foreign exceptions are no substantial control under the stated employee conditions, and vacation not a major consideration; a self-employed person generally has substantial control. If none applies to a primarily business foreign trip, allocate transport by actual business/total days under IRS's rules. Business days can include travel, required-presence days, principal work days, certain weekends/holidays between business days and qualifying unavoidable standby. A personal side trip needs its own allocation. The old 'foreign travel7+days and personal over 25%' shortcut missed the one-week/exact 25% distinctions and other exceptions.

For domestic primarily-business travel, separate private extensions; destination business costs can still be considered on a primarily-personal trip without making transport deductible. For companions, generally exclude their costs unless actual employee/business-associate conditions and bona fide business purpose are met; incidental note-taking is not enough. Additional double-room/companion fare is not automatically the claimant's expense. Temporary versus indefinite assignment and ordinary commuting use the owning US method. Do not infer these rules apply to another country.

## United Kingdom

A sole trader/partner can claim supported business travel, eligible hotel rooms and meals on overnight business trips, not private travel, ordinary commuting or fines under HMRC's self-employed guidance. The old '100% all travelling food' shortcut did not establish the wholly/exclusively facts. Client entertainment is a separate issue. Employee travel/subsistence exemptions have their own qualifying-duty/temporary-workplace and reimbursement rules. [Self-employed travel](https://www.gov.uk/expenses-if-youre-self-employed/travel).

| Employee employer-payment benchmark | Value/condition under EIM30240 | Official source |
|---|---|---|
| Qualifying journey 5-hour band | GBP 5 maximum, subject to the continuous absence/qualifying travel and meal-cost conditions; not ordinary commuting | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30240 |
| Qualifying journey 10-hour band | GBP 10 maximum under the same conditions | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30240 |
| Qualifying journey 15 hours and ongoing at 8pm | GBP 25 maximum; no duplicate meal/accommodation reimbursement | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30240 |
| Late supplement | GBP 10 where the applicable 5/10-pound qualifying journey lasts beyond 8pm and conditions are met; not another universal overnight allowance | https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30240 |

These replace the old breakfast/lunch/dinner11/11/26 claim. EIM05231 relates to a retired regime and was not current 2026 support. No current benchmark overnight accommodation or staying-with-friends amount is supplied by EIM30240. Employers must establish qualifying occasions; its post-2019 rule differs from earlier expenditure-checking systems. Working Rule Agreements and bespoke scales are separate. Employees cannot claim the difference merely because an employer pays below the benchmark, although actual allowable excess can have relief. These are not a freelancer's automatic per-diem deduction. [Current EIM30240](https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30240).

## Germany

EStG 4(5)no5 uses9(4a) for additional own-business meals away from home/permanent business centre. Do not deduct the self-employed traveller's actual personal food instead of the statutory allowance; client entertainment is a separate category. [EStG 4](https://www.gesetze-im-internet.de/estg/__4.html).

| Domestic additional-meal rule | Current amount/condition under EStG 9(4a) | Official source |
|---|---|---|
| Full day | EUR 28 for 24-hour absence, not the old 32 | https://www.gesetze-im-internet.de/estg/__9.html |
| Arrival/departure with qualifying overnight | EUR 14, without a minimum absence-hours requirement on that arrival/departure day | https://www.gesetze-im-internet.de/estg/__9.html |
| No overnight | EUR 14 for more than 8 hours; cross-midnight no-overnight rule assigns the single amount to the predominant day | https://www.gesetze-im-internet.de/estg/__9.html |
| Same-location long assignment | First 3 months; interruption of at least 4 weeks can restart the period | https://www.gesetze-im-internet.de/estg/__9.html |
| Employer/arranged provided meals | Reduce full-day reference allowance by 20% breakfast and 40% each lunch/dinner, capped at applicable allowance; employee payments reduce the reduction; no double deduction for tax-free reimbursement | https://www.gesetze-im-internet.de/estg/__9.html |

Foreign destinations use the relevant BMF annual list and date/location rules; the old dollar/sterling foreign snippets are not current verified rates. Do not use employee supplied-meal facts for an unrelated sole-trader scenario without checking the applicable provision.

## France, BNC own extra meal costs

BOFiP's BNC rule requires actual justified professional need, reasonable location/work circumstances and receipts; no unsupported forfait/URSSAF shortcut. Meals can be justified at a workplace in the home city if facts meet the rule, so 'same city never deductible' was wrong. Client-business meals and personal additional meals have distinct contexts; purely personal/sumptuous congress costs and spouse travel do not qualify under the cited rule. [BOI-BNC-BASE-40-60-60 paragraphs 1-170](https://bofip.impots.gouv.fr/bofip/4628-PGP.html/identifiant=BOI-BNC-BASE-40-60-60-20260722).

|2026 BNC individual meal item | Amount/condition | Official source |
|---|---|---|
| Personal home-meal component | EUR 5.50 deducted from otherwise qualifying extra meal cost | https://bofip.impots.gouv.fr/bofip/4628-PGP.html/identifiant=BOI-BNC-BASE-40-60-60-20260722 |
| Ordinary excessive-cost reference | EUR 21.40 total meal cost; above this requires actual exceptional business/nearby-restaurant justification, not an absolute statutory ceiling | https://bofip.impots.gouv.fr/bofip/4628-PGP.html/identifiant=BOI-BNC-BASE-40-60-60-20260722 |

Without exceptional justification, maximum extra amount is derived 21.40 minus 5.50=EUR 15.90; with a lower actual qualifying meal use the lower actual cost minus the personal component, not a guaranteed flat deduction.

## Canada

| Business meal rule | Amount/condition | Official source |
|---|---|---|
| Ordinary food/beverage/entertainment limit |50% of lesser of actual incurred and reasonable amount, then business-use/exception rules; no universal 12-hour metropolitan-absence test | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html |
| Long-haul driver special percentage |80% during eligible period of at least 24continuous hours away from residential municipality/metropolitan area while transporting goods to/from beyond 160km radius; not all business travellers | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html |

CRA lists exceptions for businesses regularly supplying food for compensation, separately billed client reimbursements, eligible employee taxable/remote-work situations, all-staff events within the allowed annual count, charity fundraisers and qualifying temporary construction camps. Test the actual exception before applying a different amount. Government Treasury Board/NJC reimbursements are not a default self-employed travel deduction or a reason to invent the old 116.40/day amount. Use receipts and current statutory/CRA conditions; no ordinary 12-hour condition was found in the cited business-meal rule.

## Spain

LIRPF 30.2.5(c) requires the self-employed person's actual business-related restaurant/hospitality meal and electronic payment, using the employee quantitative limits. It is not a daily automatic payment without cost or business purpose. RIRPF 9 distinguishes actual supported accommodation from meal maxima and states employer assignment/place/time conditions; the self-employed rule must not be expanded into every employee exemption or a guessed extra lodging allowance. [LIRPF 30](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764); [RIRPF 9](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820).

| Normal meal maximum under RIRPF 9 | Domestic / foreign | Official source |
|---|---|---|
| Without qualifying overnight | EUR 26.67 / EUR 48.08 per day; actual eligibility/cost and claimant-specific conditions still required | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |
| With qualifying overnight | EUR 53.34 / EUR 91.35 per day for meals; these are not hotel allowances | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 |

For employee exemptions, verify municipality differs from both ordinary workplace and residence, actual day/place/reason and extended-assignment rules; transport-worker and flight-crew exceptions differ. Accommodation generally requires the actual justified amount. Input IVA remains subject toLIVA 95-96 and the fiscal-deductibility/other conditions, not automatic recovery of every receipt's tax. [LIVA](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740).

## Netherlands

| Limited business-cost option,2026 | Value/condition | Official source |
|---|---|---|
| Income-tax entrepreneur/other-work percentage alternative |80% of qualifying limited business costs instead of the threshold method; private costs are not made business costs by this election | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 |
| Income-tax threshold method | EUR 5700 for 2026 under the cited limited-cost overview; compare the qualifying costs above it with the percentage alternative | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 |
| Corporate-tax percentage alternative |73.5%, with the corporate threshold/base rules checked separately in the corporation-tax method | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 |

The old 'always 80% regardless of purpose' was false. Identify the actual restricted-cost category and claim regime; do not call every meal private-benefit forfait or apply an employee reimbursement scale automatically to an entrepreneur. Current self-employed per-diem availability beyond this actual limited-cost method was not certified here.

## Australia, Italy, India and Malta, retained questions to resolve

- **Australia:** distinguish actual business travel from living/relocation, overnight/day travel, employee reasonable-allowance substantiation concessions and a self-employed deduction. Salary band, destination and year matter. The old 2024-25 meal131.65/hotel309 amounts and generic '100% overnight' rule are not current 2026 guidance. Load `au-sole-trader-schedule` and the applicable current ATO travel determination before figures. No Australian approved file is edited.
- **Italy:** identify professional versus employee, tax year, reimbursement regime, food/hotel versus other travel, documentary/electronic-payment requirements and total-income limits. The old 75%/2%-of-revenue treatment and 46.48/77.47 employee lump sums were not confirmed from current official text; retain them only as historical questions below. Use `it-income-tax`; do not combine an employee lump sum with a professional's restricted actual costs.
- **India:** identify employee versus actual/professional presumptive business scheme, applicable FY/Income-tax Act, business nexus and reimbursement. The old universal100%/no-per-diem claims were not reopened under current 2026 legislation; do not add a separate travel deduction to presumptive profit without its actual rule. Use `india-income-tax` and retain receipts.
- **Malta:** identify actual business purpose, client/employer versus individual claimant, reimbursement and local/foreign tax invoice; route to `malta-income-tax` and `malta-vat-return`. The old categorical no-per-diem/IRD-practice statements and blanket reasonable-cost acceptance were not verified against current official law here, so no invented Maltese scale is supplied.

## Mixed-purpose itinerary decisions retained

- Five business days and no personal days: prove all listed costs, then apply the country's meal/other limits; 'business trip' does not mean every cost is 100% deductible.
- Five business days plus two weekend days: determine necessary business standby versus a private extension and the country domestic/foreign rule; there is no universal automatic full-flight deduction.
- Three business days and four personal days: determine primary purpose and destination business costs under the actual country rule; do not zero every cost or allocate automatically from a simple day majority.
- Conference plus one tourism day: conference facts do not automatically make an extra personal night deductible. Retain original versus incremental transport and hotel costs.
- Spouse/partner accompanies: allocate actual incremental private fare/room/meal costs; test any genuine business role and the country's conditions rather than inventing the same single-room rule worldwide.

## When to refuse or refer

Hold missing itinerary/business purpose, tax home, bill details, actual local law, current allowance rate, reimbursement or private split. A city tax can be part of an otherwise eligible hotel cost but is not automatically deductible everywhere. Distinguish Uber Eats/other food delivery from passenger transport, hotel versus host/service fee and coworking day-pass versus personal membership. No unsupported claim that an agent charges no fee or every hotel/airline entity always has the same VAT treatment. Foreign VAT recovery, temporary/indefinite assignment, companion business purpose, conventions, related parties and unconfirmed country allowances need the owning method.

## Worked cases

### France, an actual BNC meal without exceptional high-cost justification

Assume a qualifying 2026 meal costing EUR 25 with receipts and no exceptional reason to exceed the normal reference. Deduct 21.40 minus 5.50=EUR 15.90; personal/excess remainder is 9.10. A receipt alone does not establish the professional-need and location conditions.

```oa-check
name: French2026 BNC extra meal with ordinary upper reference
inputs:
  actual_meal: 25
  ordinary_upper: 21.40
  home_meal: 5.50
steps:
  - eligible_cost_reference: min(actual_meal, ordinary_upper)
  - deductible_extra: max(eligible_cost_reference - home_meal, 0)
  - excluded: actual_meal - deductible_extra
expected:
  eligible_cost_reference: 21.40
  deductible_extra: 15.90
  excluded: 9.10
```

### Germany, provided meals reduce an eligible employee full day

Assume an eligible domestic 24-hour employee trip within the three-month window, with employer-provided breakfast and lunch, no employee contribution and no duplicate reimbursement. Reduce28 by 20%×28 and 40%×28. The remaining allowance is EUR 11.20. The percentages use the full-day reference, not a smaller arrival-day amount.

```oa-check
name: German full-day meal allowance and supplied-meal reductions
inputs:
  full_day: 28
  breakfast_share: 0.20
  lunch_share: 0.40
steps:
  - breakfast_reduction: full_day * breakfast_share
  - lunch_reduction: full_day * lunch_share
  - allowance: max(full_day - breakfast_reduction - lunch_reduction, 0)
expected:
  breakfast_reduction: 5.60
  lunch_reduction: 11.20
  allowance: 11.20
```

## Historical merchant recognition hints

Find the actual contract and invoice from these historical strings. This is not a current merchant, agency or VAT directory. Every candidate remains subject to the method and country rules above.

- Ryanair; candidate `RYANAIR`; investigate Travel - Flights.
- Ryanair; candidate `FR RYANAIR`; investigate Travel - Flights.
- easyJet; candidate `EASYJET`; investigate Travel - Flights.
- easyJet; candidate `EASYJET *`; investigate Travel - Flights.
- British Airways; candidate `BRITISH AIRWAYS`; investigate Travel - Flights.
- British Airways; candidate `BRITISH AIRWAY`; investigate Travel - Flights.
- Lufthansa; candidate `LUFTHANSA`; investigate Travel - Flights.
- Lufthansa; candidate `LH LUFTHANSA`; investigate Travel - Flights.
- Air France; candidate `AIR FRANCE`; investigate Travel - Flights.
- KLM; candidate `KLM`; investigate Travel - Flights.
- Delta Air Lines; candidate `DELTA AIR`; investigate Travel - Flights.
- United Airlines; candidate `UNITED AIRLINES`; investigate Travel - Flights.
- American Airlines; candidate `AMERICAN AIRLINE`; investigate Travel - Flights.
- Southwest Airlines; candidate `SOUTHWEST AIR`; investigate Travel - Flights.
- Qantas; candidate `QANTAS`; investigate Travel - Flights.
- Emirates; candidate `EMIRATES`; investigate Travel - Flights.
- Vueling; candidate `VUELING`; investigate Travel - Flights.
- Wizz Air; candidate `WIZZAIR`; investigate Travel - Flights.
- Wizz Air; candidate `WIZZ AIR`; investigate Travel - Flights.
- Norwegian Air; candidate `NORWEGIAN`; investigate Travel - Flights.
- TAP Air Portugal; candidate `TAP PORTUGAL`; investigate Travel - Flights.
- Air Malta; candidate `AIRMALTA`; investigate Travel - Flights.
- Booking.com (Flight); candidate `BOOKING.COM *FL`; investigate Travel - Flights.
- Expedia; candidate `EXPEDIA *`; investigate Travel - Flights.
- Skyscanner; candidate `SKYSCANNER`; investigate Travel - Flights.
- Kiwi.com; candidate `KIWI.COM`; investigate Travel - Flights.
- Google Flights; candidate `GOOGLE *FLIGHTS`; investigate Travel - Flights.
- Booking.com; candidate `BOOKING.COM`; investigate Travel - Accommodation.
- Booking.com; candidate `BOOKING *`; investigate Travel - Accommodation.
- Booking.com; candidate `BDC *HOTEL`; investigate Travel - Accommodation.
- Airbnb; candidate `AIRBNB`; investigate Travel - Accommodation.
- Airbnb; candidate `AIRBNB *`; investigate Travel - Accommodation.
- Hotels.com (Expedia); candidate `HOTELS.COM`; investigate Travel - Accommodation.
- Expedia; candidate `EXPEDIA *HOTEL`; investigate Travel - Accommodation.
- Marriott; candidate `MARRIOTT`; investigate Travel - Accommodation.
- Hilton; candidate `HILTON`; investigate Travel - Accommodation.
- Hilton; candidate `HILTON *`; investigate Travel - Accommodation.
- IHG (Holiday Inn, etc.); candidate `IHG *`; investigate Travel - Accommodation.
- Accor (Novotel, ibis, etc.); candidate `ACCOR`; investigate Travel - Accommodation.
- Premier Inn; candidate `PREMIER INN`; investigate Travel - Accommodation.
- Travelodge; candidate `TRAVELODGE`; investigate Travel - Accommodation.
- Hostelworld; candidate `HOSTELWORLD`; investigate Travel - Accommodation.
- Uber; candidate `UBER *TRIP`; investigate Travel - Ground transport.
- Uber; candidate `UBER *`; investigate Travel - Ground transport.
- Uber Eats; candidate `UBER EATS`; investigate Meals (NOT transport).
- Bolt (Taxify); candidate `BOLT`; investigate Travel - Ground transport.
- Bolt (Taxify); candidate `BOLT.EU`; investigate Travel - Ground transport.
- Lyft; candidate `LYFT`; investigate Travel - Ground transport.
- Lyft; candidate `LYFT *RIDE`; investigate Travel - Ground transport.
- Eurostar; candidate `EUROSTAR`; investigate Travel - Ground transport.
- Thalys (now Eurostar); candidate `THALYS`; investigate Travel - Ground transport.
- SNCF; candidate `SNCF`; investigate Travel - Ground transport.
- SNCF; candidate `SNCF *`; investigate Travel - Ground transport.
- Deutsche Bahn; candidate `DB BAHN`; investigate Travel - Ground transport.
- Deutsche Bahn (long-distance); candidate `DB FERNVERKEHR`; investigate Travel - Ground transport.
- Trenitalia; candidate `TRENITALIA`; investigate Travel - Ground transport.
- Renfe; candidate `RENFE`; investigate Travel - Ground transport.
- NS (Dutch Railways); candidate `NS.NL`; investigate Travel - Ground transport.
- Transport for London; candidate `TFL *`; investigate Travel - Ground transport.
- Trainline; candidate `TRAINLINE`; investigate Travel - Ground transport.
- Hertz; candidate `HERTZ`; investigate Travel - Car rental.
- Hertz; candidate `HERTZ *`; investigate Travel - Car rental.
- Sixt; candidate `SIXT`; investigate Travel - Car rental.
- Sixt; candidate `SIXT *`; investigate Travel - Car rental.
- Enterprise Rent-A-Car; candidate `ENTERPRISE`; investigate Travel - Car rental.
- Europcar; candidate `EUROPCAR`; investigate Travel - Car rental.
- Avis; candidate `AVIS`; investigate Travel - Car rental.
- Budget (Avis group); candidate `BUDGET RENT`; investigate Travel - Car rental.
- FREE NOW (MyTaxi); candidate `FREENOW`; investigate Travel - Ground transport.
- Cabify; candidate `CABIFY`; investigate Travel - Ground transport.
- Grab; candidate `GRABPAY`; investigate Travel - Ground transport.
- Lime; candidate `LIME *`; investigate Travel - Ground transport.
- Various restaurants; candidate `[RESTAURANT NAME]`; investigate Travel - Meals.
- Uber Eats; candidate `UBER EATS`; investigate Travel - Meals.
- Deliveroo; candidate `DELIVEROO`; investigate Travel - Meals.
- Just Eat; candidate `JUST EAT`; investigate Travel - Meals.
- WeWork; candidate `WEWORK`; investigate Travel - Co-working / Office expenses.
- WeWork; candidate `WEWORK *`; investigate Travel - Co-working / Office expenses.
- Spaces (IWG/Regus); candidate `SPACES`; investigate Travel - Co-working / Office expenses.
- Regus (IWG); candidate `REGUS`; investigate Travel - Co-working / Office expenses.
- IWG (Regus/Spaces); candidate `IWG *`; investigate Travel - Co-working / Office expenses.
- Hubble; candidate `HUBBLE HQ`; investigate Travel - Co-working / Office expenses.
- Deskpass; candidate `DESKPASS`; investigate Travel - Co-working / Office expenses.
- Croissant; candidate `CROISSANT`; investigate Travel - Co-working / Office expenses.
- Various local co-working spaces; candidate `[LOCAL COWORKING]`; investigate Travel - Co-working / Office expenses.

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.irs.gov/publications/p463 | 2026-11-14 | Read for Publication 463(2025), tax-home/sleep-rest, actual and standard meal method, general50%limit, domestic/foreign mixed trips, four foreign exceptions, business-day counting, companion exceptions and records. No2025 per-diem amount is certified for 2026. |
| https://www.gov.uk/expenses-if-youre-self-employed/travel | 2026-11-14 | Read for actual UK sole-trader/partner travel, hotels/overnight meals, commuting/private/fine exclusions and car/capital distinction. |
| https://www.gov.uk/hmrc-internal-manuals/employment-income-manual/eim30240 | 2026-11-14 | Read for EIM30240 current employee benchmark5/10/25 rates, qualifying travel/costs, late supplement, no duplicate reimbursement, post-2019 checking rule and no lodging/friends benchmark. |
| https://www.gov.uk/guidance/the-vat-treatment-of-passenger-transport-notice-744a | 2026-11-14 | Read for Notice 744A sections 2-5 for actual passenger transport scope, domestic qualifying/scheduled-flight zero rating, exceptions, agent and margin-scheme distinctions. |
| https://www.gov.uk/guidance/vat-guide-notice-700 | 2026-11-14 | Read for Notice 700 sections 10.6,12.1 and 22.1-22.6 for actual tax evidence, business travel input restrictions and separate agent/principal supplies. |
| https://www.gesetze-im-internet.de/estg/__9.html | 2026-11-14 | Read for EStG 9(4a), domestic14/28 meal allowances, more-than 8 hours, arrival/departure, three-month/four-week reset and supplied-meal reductions. |
| https://www.gesetze-im-internet.de/estg/__4.html | 2026-11-14 | Read for EStG 4(5)no5 applying9(4a) to own-business additional meals, distinct from client-entertainment restrictions. |
| https://bofip.impots.gouv.fr/bofip/4628-PGP.html/identifiant=BOI-BNC-BASE-40-60-60-20260722 | 2026-11-14 | Read for BOI-BNC-BASE-40-60-60 paragraphs 1-170, business interest/evidence/location,2026 home value5.50, normal upper21.40 and exceptional higher-cost justification. |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/report-business-income-expenses/completing-form-t2125/line-8523-meals-entertainment-allowable-part-only.html | 2026-11-14 | Read for CRA line8523 ordinary50%lesseractual/reasonable, business use and exceptions; long-haul80%with 24hours/160km and employer/location conditions. No ordinary 12-hour threshold. |
| https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 | 2026-11-14 | Read for RIRPF article 9 meal versus actual lodging,26.67/48.08 withoutovernight and 53.34/91.35 withovernight, workplace/home municipalities, nine-month employer-assignment restriction and proof. |
| https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | 2026-11-14 | Read for LIRPF 30.2.5(c), actual own-business meal, restaurant/hospitality, electronic payment and linked employee quantitative limits. |
| https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 | 2026-11-14 | Read for LIVA 95-96, actual tax and travel/hospitality input restrictions, tax-deductible-cost exception and general conditions. |
| https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/inkomstenbelasting/veranderingen-inkomstenbelasting-2026/drempel-beperkt-aftrekbare-kosten-2026 | 2026-11-14 | Read for Belastingdienst2026 limited business costs5700 threshold and alternative80%income-tax/otherwork or73.5%corporation percentage. |
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for accurate identifiable business transactions, invoices/receipts/statements and unpaid traditional-accounting records. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23,27-30 for conditional framework initial/closing/settlement currency treatment, not a universal tax translation rule. |

Not yet confirmed:2026 US locality/high-low/transport-industry per-diem figures and final forms; foreign BMF meal tables; Australian salary/destination allowance determinations and actual-travel conditions; current Italian meal/hotel/reimbursement limits; Indian2026 scheme/Act-specific rules; Maltese current deduction/per-diem conditions. Historical TreasuryBoard/NJC and URSSAF amounts are not general self-employed tax rates. Current travel-vendor billing entities, routes, agency roles and VAT/GST assertions below are retained only for historical comparison, not usable guidance. No vendor source was used.

- Historical claim, not usable guidance, Ryanair `RYANAIR`: Deductible?: Yes, if business purpose; VAT treatment: EU: VAT exempt (international) or zero-rated. Domestic flights: local VAT may apply.; Notes: Budget carrier. IE entity.
- Historical claim, not usable guidance, Ryanair `FR RYANAIR`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes: Card statement variant.
- Historical claim, not usable guidance, easyJet `EASYJET`: Deductible?: Yes, if business purpose; VAT treatment: Same VAT treatment as Ryanair.; Notes: UK entity.
- Historical claim, not usable guidance, easyJet `EASYJET *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, British Airways `BRITISH AIRWAYS`: Deductible?: Yes, if business purpose; VAT treatment: International flights: zero-rated/exempt. UK domestic: standard rate.; Notes: UK entity.
- Historical claim, not usable guidance, British Airways `BRITISH AIRWAY`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes: Truncated.
- Historical claim, not usable guidance, Lufthansa `LUFTHANSA`: Deductible?: Yes, if business purpose; VAT treatment: DE entity. International: exempt. DE domestic: 19% VAT.; Notes:
- Historical claim, not usable guidance, Lufthansa `LH LUFTHANSA`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Air France `AIR FRANCE`: Deductible?: Yes, if business purpose; VAT treatment: FR entity. International: exempt. FR domestic: 10% TVA.; Notes:
- Historical claim, not usable guidance, KLM `KLM`: Deductible?: Yes, if business purpose; VAT treatment: NL entity. International: exempt.; Notes: Part of Air France-KLM.
- Historical claim, not usable guidance, Delta Air Lines `DELTA AIR`: Deductible?: Yes, if business purpose; VAT treatment: US entity. US domestic: 7.5% excise tax (not reclaimable).; Notes:
- Historical claim, not usable guidance, United Airlines `UNITED AIRLINES`: Deductible?: Yes, if business purpose; VAT treatment: US entity. Same as Delta.; Notes:
- Historical claim, not usable guidance, American Airlines `AMERICAN AIRLINE`: Deductible?: Yes, if business purpose; VAT treatment: US entity. Same as Delta.; Notes:
- Historical claim, not usable guidance, Southwest Airlines `SOUTHWEST AIR`: Deductible?: Yes, if business purpose; VAT treatment: US entity. Same as Delta.; Notes:
- Historical claim, not usable guidance, Qantas `QANTAS`: Deductible?: Yes, if business purpose; VAT treatment: AU entity. Domestic: 10% GST (claimable). International: GST-free.; Notes:
- Historical claim, not usable guidance, Emirates `EMIRATES`: Deductible?: Yes, if business purpose; VAT treatment: AE entity. No VAT on international flights.; Notes:
- Historical claim, not usable guidance, Vueling `VUELING`: Deductible?: Yes, if business purpose; VAT treatment: ES entity. International: exempt. ES domestic: 10% IVA.; Notes:
- Historical claim, not usable guidance, Wizz Air `WIZZAIR`: Deductible?: Yes, if business purpose; VAT treatment: HU entity. International: exempt.; Notes: Budget carrier.
- Historical claim, not usable guidance, Wizz Air `WIZZ AIR`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Norwegian Air `NORWEGIAN`: Deductible?: Yes, if business purpose; VAT treatment: NO entity. International: exempt.; Notes:
- Historical claim, not usable guidance, TAP Air Portugal `TAP PORTUGAL`: Deductible?: Yes, if business purpose; VAT treatment: PT entity. International: exempt.; Notes:
- Historical claim, not usable guidance, Air Malta `AIRMALTA`: Deductible?: Yes, if business purpose; VAT treatment: MT entity. International: exempt.; Notes:
- Historical claim, not usable guidance, Booking.com (Flight) `BOOKING.COM *FL`: Deductible?: Yes, if business purpose; VAT treatment: NL entity. Acts as agent , VAT on service fee only. Flight itself follows airline VAT rules.; Notes: Booking.com is an intermediary.
- Historical claim, not usable guidance, Expedia `EXPEDIA *`: Deductible?: Yes, if business purpose; VAT treatment: US entity. Agent model , VAT varies.; Notes: Check if Expedia or airline is the merchant.
- Historical claim, not usable guidance, Skyscanner `SKYSCANNER`: Deductible?: Skyscanner redirects to airlines/agents. The charge is from the actual seller.; VAT treatment: N/A , Skyscanner does not charge directly.; Notes: If you see a Skyscanner charge, it is likely through a partner.
- Historical claim, not usable guidance, Kiwi.com `KIWI.COM`: Deductible?: Yes, if business purpose; VAT treatment: CZ entity. Acts as agent or MoR depending on booking.; Notes: Check invoice carefully.
- Historical claim, not usable guidance, Google Flights `GOOGLE *FLIGHTS`: Deductible?: Google redirects , charge is from airline/agent.; VAT treatment: N/A.; Notes: Google Flights does not sell tickets directly.
- Historical claim, not usable guidance, Booking.com `BOOKING.COM`: Deductible?: Yes, if business purpose; VAT treatment: NL entity (Booking.com B.V.). Hotel charges VAT, not Booking.com. Booking.com's commission is a separate B2B service.; Notes: Booking.com is an agent , the hotel is the supplier.
- Historical claim, not usable guidance, Booking.com `BOOKING *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Booking.com `BDC *HOTEL`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes: Card statement format.
- Historical claim, not usable guidance, Airbnb `AIRBNB`: Deductible?: Yes, if business purpose; VAT treatment: IE entity for EU (Airbnb Ireland UC). Airbnb is a MARKETPLACE , VAT treatment differs from hotels. Airbnb charges VAT on its service fee. The host may or may not charge VAT.; Notes: Airbnb invoices are split: accommodation (from host) + service fee (from Airbnb). Only Airbnb's service fee has clear VAT treatment.
- Historical claim, not usable guidance, Airbnb `AIRBNB *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Hotels.com (Expedia) `HOTELS.COM`: Deductible?: Yes, if business purpose; VAT treatment: US entity (Expedia group). Agent model in most markets.; Notes:
- Historical claim, not usable guidance, Expedia `EXPEDIA *HOTEL`: Deductible?: Yes, if business purpose; VAT treatment: Check if merchant model or agency model , VAT treatment differs.; Notes:
- Historical claim, not usable guidance, Marriott `MARRIOTT`: Deductible?: Yes, if business purpose; VAT treatment: Hotel charges local VAT/tourism tax at the rate of the hotel's country.; Notes: Large hotel chain.
- Historical claim, not usable guidance, Hilton `HILTON`: Deductible?: Yes, if business purpose; VAT treatment: Same as Marriott.; Notes:
- Historical claim, not usable guidance, Hilton `HILTON *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, IHG (Holiday Inn, etc.) `IHG *`: Deductible?: Yes, if business purpose; VAT treatment: Same as Marriott.; Notes: InterContinental Hotels Group.
- Historical claim, not usable guidance, Accor (Novotel, ibis, etc.) `ACCOR`: Deductible?: Yes, if business purpose; VAT treatment: FR entity. Local VAT applies at hotel location.; Notes:
- Historical claim, not usable guidance, Premier Inn `PREMIER INN`: Deductible?: Yes, if business purpose; VAT treatment: UK entity. 20% VAT on accommodation.; Notes: UK budget hotel chain.
- Historical claim, not usable guidance, Travelodge `TRAVELODGE`: Deductible?: Yes, if business purpose; VAT treatment: UK entity. 20% VAT.; Notes: UK budget chain.
- Historical claim, not usable guidance, Hostelworld `HOSTELWORLD`: Deductible?: Yes, if business purpose; VAT treatment: IE entity. Agent model.; Notes: Budget accommodation.
- Historical claim, not usable guidance, Uber `UBER *TRIP`: Deductible?: Yes, if business purpose; VAT treatment: NL entity for EU (Uber B.V.). UK: Uber charges 20% VAT. US: no sales tax on most rides.; Notes: Uber provides VAT invoices in most EU/UK markets.
- Historical claim, not usable guidance, Uber `UBER *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Uber Eats `UBER EATS`: Deductible?: See meals rules below; VAT treatment: Different from Uber rides.; Notes: Do not classify as transport.
- Historical claim, not usable guidance, Bolt (Taxify) `BOLT`: Deductible?: Yes, if business purpose; VAT treatment: EE entity. EU: local VAT rules apply.; Notes: European ride-hailing.
- Historical claim, not usable guidance, Bolt (Taxify) `BOLT.EU`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Lyft `LYFT`: Deductible?: Yes, if business purpose; VAT treatment: US entity.; Notes: Primarily US market.
- Historical claim, not usable guidance, Lyft `LYFT *RIDE`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Eurostar `EUROSTAR`: Deductible?: Yes, if business purpose; VAT treatment: UK/FR/BE entity depending on route. Zero-rated for international segments in UK.; Notes: International rail.
- Historical claim, not usable guidance, Thalys (now Eurostar) `THALYS`: Deductible?: Yes, if business purpose; VAT treatment: Same as Eurostar.; Notes: Merged with Eurostar.
- Historical claim, not usable guidance, SNCF `SNCF`: Deductible?: Yes, if business purpose; VAT treatment: FR entity. 10% TVA on domestic rail.; Notes: French national rail.
- Historical claim, not usable guidance, SNCF `SNCF *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Deutsche Bahn `DB BAHN`: Deductible?: Yes, if business purpose; VAT treatment: DE entity. 7% VAT on domestic passenger transport.; Notes: German rail.
- Historical claim, not usable guidance, Deutsche Bahn (long-distance) `DB FERNVERKEHR`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Trenitalia `TRENITALIA`: Deductible?: Yes, if business purpose; VAT treatment: IT entity. 10% IVA on domestic rail.; Notes: Italian rail.
- Historical claim, not usable guidance, Renfe `RENFE`: Deductible?: Yes, if business purpose; VAT treatment: ES entity. 10% IVA on domestic rail.; Notes: Spanish rail.
- Historical claim, not usable guidance, NS (Dutch Railways) `NS.NL`: Deductible?: Yes, if business purpose; VAT treatment: NL entity. 9% BTW on domestic rail.; Notes:
- Historical claim, not usable guidance, Transport for London `TFL *`: Deductible?: Yes, if business purpose; VAT treatment: UK entity. Zero-rated public transport. No VAT to reclaim.; Notes: Tube, bus, Overground, Elizabeth line.
- Historical claim, not usable guidance, Trainline `TRAINLINE`: Deductible?: Yes, if business purpose; VAT treatment: UK entity. Agent , VAT is on the train ticket, not Trainline's fee (which is zero).; Notes: Booking platform.
- Historical claim, not usable guidance, Hertz `HERTZ`: Deductible?: Yes, if business purpose; VAT treatment: Local entity. VAT at local rate on rental.; Notes: Car rental.
- Historical claim, not usable guidance, Hertz `HERTZ *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Sixt `SIXT`: Deductible?: Yes, if business purpose; VAT treatment: DE entity. Local VAT applies.; Notes:
- Historical claim, not usable guidance, Sixt `SIXT *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Enterprise Rent-A-Car `ENTERPRISE`: Deductible?: Yes, if business purpose; VAT treatment: Local entity.; Notes:
- Historical claim, not usable guidance, Europcar `EUROPCAR`: Deductible?: Yes, if business purpose; VAT treatment: FR entity. Local VAT applies.; Notes:
- Historical claim, not usable guidance, Avis `AVIS`: Deductible?: Yes, if business purpose; VAT treatment: Local entity.; Notes:
- Historical claim, not usable guidance, Budget (Avis group) `BUDGET RENT`: Deductible?: Yes, if business purpose; VAT treatment: Same group as Avis.; Notes:
- Historical claim, not usable guidance, FREE NOW (MyTaxi) `FREENOW`: Deductible?: Yes, if business purpose; VAT treatment: DE/IE entity. Local VAT rules.; Notes: Taxi app.
- Historical claim, not usable guidance, Cabify `CABIFY`: Deductible?: Yes, if business purpose; VAT treatment: ES entity.; Notes: Spain/LatAm ride-hailing.
- Historical claim, not usable guidance, Grab `GRABPAY`: Deductible?: Yes, if business purpose; VAT treatment: SG entity. Local VAT/GST rules.; Notes: Southeast Asia.
- Historical claim, not usable guidance, Lime `LIME *`: Deductible?: Yes, if business purpose; VAT treatment: US entity.; Notes: E-scooters/bikes.
- Historical claim, not usable guidance, Various restaurants `[RESTAURANT NAME]`: Deductible?: Partially deductible (varies by country , see table below); VAT treatment: Local VAT on food/drink at local rates.; Notes: Must be during business travel. Meals at home city are generally NOT deductible (unless client entertainment).
- Historical claim, not usable guidance, Uber Eats `UBER EATS`: Deductible?: Same as restaurant meals; VAT treatment: Platform model , VAT varies.; Notes: Delivery during business travel.
- Historical claim, not usable guidance, Deliveroo `DELIVEROO`: Deductible?: Same as restaurant meals; VAT treatment: UK/EU entity.; Notes: Same note.
- Historical claim, not usable guidance, Just Eat `JUST EAT`: Deductible?: Same as restaurant meals; VAT treatment: NL entity (Just Eat Takeaway).; Notes: Same note.
- Historical claim, not usable guidance, WeWork `WEWORK`: Deductible?: Yes, if business purpose; VAT treatment: Local entity. Local VAT on office rental. Most jurisdictions: standard-rated.; Notes: Day pass or hot desk.
- Historical claim, not usable guidance, WeWork `WEWORK *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Spaces (IWG/Regus) `SPACES`: Deductible?: Yes, if business purpose; VAT treatment: NL/local entity. Standard-rated VAT.; Notes: Part of IWG group.
- Historical claim, not usable guidance, Regus (IWG) `REGUS`: Deductible?: Yes, if business purpose; VAT treatment: Same group as Spaces.; Notes:
- Historical claim, not usable guidance, IWG (Regus/Spaces) `IWG *`: Deductible?: Yes, if business purpose; VAT treatment: Same as above.; Notes:
- Historical claim, not usable guidance, Hubble `HUBBLE HQ`: Deductible?: Yes, if business purpose; VAT treatment: UK entity. 20% VAT.; Notes: UK co-working marketplace.
- Historical claim, not usable guidance, Deskpass `DESKPASS`: Deductible?: Yes, if business purpose; VAT treatment: US entity.; Notes: Co-working day pass aggregator.
- Historical claim, not usable guidance, Croissant `CROISSANT`: Deductible?: Yes, if business purpose; VAT treatment: US entity.; Notes: Co-working membership.
- Historical claim, not usable guidance, Various local co-working spaces `[LOCAL COWORKING]`: Deductible?: Yes, if business purpose; VAT treatment: Local VAT rates apply.; Notes: Many small co-working spaces appear under their own name.
