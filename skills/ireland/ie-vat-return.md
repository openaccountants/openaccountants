---
name: ie-vat-return
description: "Prepare and check an Irish VAT3 and annual RTD for 2026: registration, rates, input credit, authorised cash accounting, received services, EU goods, RCT construction, ROS filing and corrections. Includes dated 2025 comparisons and conditional worked cases. Specialist property, schemes and disclosures require a partner accountant."
version: 2.5
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-26
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Irish VAT returns (VAT3 and RTD), tax year 2026

Confirm registration, the period on ROS, the accounting basis and the evidence for each transaction before preparing the return. This Guide covers ordinary Irish business VAT3 returns and the annual RTD in euro. Section references are to the Value-Added Tax Consolidation Act 2010 (VATCA). Use `vat-workflow-base` and `eu-vat-directive` alongside it; other Irish routes are `ie-income-tax-form11`, `ie-corporation-tax`, `ie-payroll`, `ie-foreign-tax-and-withholding`, `ie-cross-border` and `ie-formation`.

## Who this applies to

For Irish-established sole traders, partnerships and companies making taxable supplies. For 2026, test annual turnover in both the current and previous calendar year under VATCA s.6. The registration thresholds below are not allowances for a business already accountable for VAT. Exempt businesses receiving taxable business services from abroad can also have registration obligations, without a received-services threshold (s.12).

Annual turnover excludes VAT and disposals of tangible/intangible capital assets. Include taxable supplies and supplies of immovable goods, specified financial services, insurance and reinsurance; the latter categories are excluded if incidental to the business's supplies and activities (s.92B). Under s.6(2)(b), aggregate relevant same-class goods or same-nature services where one person controls another supplier.

For ordinary taxable intra-EU goods acquisitions, s.9 provides a EUR 41,000 continuous-12-month exemption test for eligible otherwise non-accountable persons, including expected acquisitions. It does not exempt ordinary registered taxable traders from self-accounting below that amount; new means of transport and excise goods are excluded from this threshold test.

Original registration case: an Irish-established, services-only web designer reaches EUR 43,000 in September 2026, exceeding EUR 42,500; deal with compulsory registration. At or below the threshold, any voluntary election needs its own effective-date check.

For voluntary registration/effective dates, non-established suppliers, the EU cross-border SME exemption and its domestic/Union eligibility tests: **Check this point with one of our partner accountants.** Do not assume that a domestic turnover threshold protects a non-established supplier.

## Rates, bands and thresholds

Use the rate for the actual supply and tax point; these are not classifications inferred from a bank description. Figures below apply in 2026 unless a different period is stated.

| Item and operative condition | Rate or amount | Official source |
|---|---|---|
| Services, and standard/reduced-rated goods manufactured wholly or mainly from zero-rated materials | EUR 42,500 annual turnover | VATCA ss.2, 6; https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx |
| Goods threshold: at least 90% of turnover from qualifying taxable goods, excluding the manufactured goods above | EUR 85,000 annual turnover | VATCA ss.2, 6; https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx |
| Standard rate where no reduced, zero or exempt treatment applies; ordinary consultancy is an example | 23% | VATCA s.46; https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx ; https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/standard-rate-vat.aspx |
| Schedule 3 reduced-rate supplies, subject to its exceptions; hotel/guesthouse lettings remain here | 13.5% | VATCA s.46; https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx ; https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/reduced-rate-vat.aspx |
| Qualifying restaurant/catering, hot takeaway food, hot tea/coffee and hairdressing; restaurant alcohol, soft drinks and bottled water excluded | 13.5% throughout 2025 and to 30 June 2026; 9% from 1 July 2026 | VATCA s.46(1)(cb); https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx ; https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx |
| Other second-reduced-rate supplies: qualifying periodicals/e-periodicals and sporting facilities supplied by a person other than a non-profit organisation; electricity and qualifying heating/lighting gas have the dated energy provision | 9%; energy provision 1 May 2022 to 31 December 2030 | VATCA s.46(1)(ca), (caa); https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx ; https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx |
| Livestock within the statutory definition, including horses normally intended for food or agricultural production | 4.8% | VATCA ss.2, 46(1)(d); https://revisedacts.lawreform.ie/eli/2010/act/31/section/46/revised/en/html ; https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx |
| Schedule 2 supplies only when the relevant description and conditions are met | 0% | VATCA s.46(1)(b); https://revisedacts.lawreform.ie/eli/2010/act/31/section/46/revised/en/html |
| Flat-rate farmer addition, not a general sales VAT rate | 4.5% in 2026; 5.1% in 2025 | https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx |
| Authorised moneys received basis, turnover route: neither exceeded nor likely to exceed in any continuous 12 months | EUR 2,000,000 | VATCA s.80; https://revisedacts.lawreform.ie/eli/2010/act/31/section/80/revised/en/html |

For individual zero-rate classifications (food, medicines, sanitary products, books/e-books/audiobooks, newspapers, farm inputs, solar installations and children's clothing/footwear), qualifying apartments, heat pumps, or another unusual rate: **Check this point with one of our partner accountants.** The rate table alone does not establish eligibility. Do not apply a historical apartment rate to a new contract.

## The taxable base

**Tax point and price.** For ordinary invoiced supplies use the invoice issue date or the statutory deadline if issued late; for ordinary non-invoiced supplies use the supply/advance-payment tax point. Authorised cash accounting instead uses the rate at supply, not later receipt (ss.74, 80(2)(a)). Utilities and other special tax points need their own rule. The taxable amount includes consideration, taxes, commissions, costs and charges, excluding VAT. For foreign currency use the latest Central Bank of Ireland/ECB selling rate when tax becomes due, unless Revenue has agreed another method, consistently applied until withdrawn (s.37).

Original catering case: a business event with EUR 2,000 net food and EUR 500 wine, supplied and invoiced on 20 June 2026, gives EUR 270 food VAT and EUR 115 wine VAT. On 10 July 2026 the same inputs give EUR 180 food VAT and EUR 115 wine VAT. Assume ordinary separately priced catering/wine, no earlier advance or special tax point; hotel lettings are outside this change.

**Two-thirds rule.** Compare VAT-exclusive goods cost with the total VAT-exclusive contract price. If goods exceed two-thirds, apply the goods rate to the whole; otherwise the service rate. Exclusions include motor-vehicle/agricultural-machinery repairs and reverse-charge/connected construction. The original guitar case remains EUR 300, comprising EUR 220 materials and EUR 80 labour/overheads/profit: 220 > 300 × 2/3; VAT = 300 × 23% = EUR 69 (s.41; Revenue two-thirds guidance).

**Input credit.** T2 includes only VAT legally deductible for taxable supplies or qualifying activities, supported by prescribed invoices/customs documents (s.59). Paying VAT or entering it in T1 does not itself confer deduction. Exempt/non-business and mixed-use costs require an entitlement/apportionment assessment; for partial exemption: **Check this point with one of our partner accountants.** Refund time limits and adjustments to unpaid purchases also need that check.

**Blocked costs.** Section 60 blocks personal food/drink/accommodation/services, entertainment, specified advertising costs, petrol except stock-in-trade, passenger motor vehicles subject to statutory exceptions, non-business property expenditure, contract work delivering blocked goods and margin/auction-scheme VAT. The personal-services block has a taxable onward-supply exception, and qualifying conference accommodation has narrowly defined conditions. Diesel's absence from the petrol block does not establish a particular claim. For conferences, vehicle-trade/hire/driving-school exceptions, or uncertain expenditure: **Check this point with one of our partner accountants.**

**Qualifying car case.** Subject to taxable use/apportionment and documents, s.59(2)(d) permits 20% recovery where business use is at least 60% and VRT first registration is 2009–2020 with emissions below 156g/km, or from 2021 below 140g/km. The original fully taxable business's car is registered in 2026, below 140g/km, with at least 60% business use: EUR 4,000 VAT × 20% = EUR 800. A sale after 3 months gives N = 0 in s.62's formula, so reduce T2 by all EUR 800 in the disposal period. The formula is credit × (4 − N)/4, N = completed 182-day blocks, capped at 4. It also applies on a fall below 60% business use, measured to the first day of that taxable period; this clawback concerns purchase/acquisition/import, not lease charges. For a particular lease or vehicle classification: **Check this point with one of our partner accountants.**

**Moneys received basis.** Revenue authorisation is required. Section 80 permits the EUR 2,000,000 turnover route above, or at least 90% of annual turnover from unregistered persons. Revenue's web guidance additionally mentions customers unable to claim full deduction; where relying on registered customers with restricted recovery rather than the statutory unregistered-person route: **Check this point with one of our partner accountants.** Keep the authorisation. New registrants indicate the request on registration; existing registrants apply in writing to their Revenue office with identity, activities, historic/estimated unregistered-customer proportions and annual turnover. Approval starts in the period issued, or a later specified date. Normal invoicing remains required. Do not use cash accounting for connected-person transactions, RCT subcontract construction, pre-July-2008 long leases, intra-Community acquisitions of goods/services or imports.

Money received includes bank credits, agents' receipts, withheld PSWT/RCT, attachment payments and set-off on the offset date. In the original PSWT example, a EUR 1,230 gross fee includes EUR 230 VAT; EUR 200 withheld does not reduce deemed receipts: account for EUR 230 VAT. Revenue requires notification by the end of the following month when the unregistered-sales share falls below 90% over four consecutive months, or turnover over four months indicates the continuous-12-month limit will be exceeded. Marginal/temporary changes may be allowed; failure to notify causes cancellation from the period when notice should have been given. For transition adjustments: **Check this point with one of our partner accountants.**

## Cross-border points

- **Services.** Apply s.34(a)'s ordinary B2B rule only after establishing customer business status, which establishment receives the service and that no exception applies. Ordinary consultancy to a German business establishment is outside Irish VAT; obtain/validate its VAT number, invoice reverse charge and report ES1 and VIES where taxable in the destination. Non-EU B2B status/location also needs evidence. Property, event, transport, catering, vehicle-hire and other exceptions cannot be decided from the VAT number alone.
- **Received services.** Under s.12, a business in Ireland receiving an ordinary B2B service from a non-established supplier self-accounts where Ireland is the place of supply. There is no registration threshold. Use T1 and only the deductible portion in T2; ES2 is for EU suppliers only. Revenue's current tax-point guidance says the earliest of invoice/document, payment or the 15th of the month following receipt of services. The original ABC Ltd case assumes German consultancy and US software supplied to its Irish business establishment, no relevant exception, no supplier VAT, and full deduction: EUR 100,000 × 23% = EUR 23,000 T1/T2 and EUR 100,000 ES2; US software EUR 200 monthly × 23% = EUR 46 T1/T2, no ES2.
- **EU goods.** Ordinary taxable acquisitions into Ireland: T1 at the Irish goods rate, T2 only if deductible, value E2. Tax is due on the 15th of the next month or earlier supplier invoice (s.75). Original stock case: EUR 5,000 from Germany for taxable resale at 23% gives EUR 1,150 T1/T2, E2 EUR 5,000, assuming full credit and no special scheme. The same EUR 5,000 appears in RTD acquisitions and purchases for resale.
- **Goods supplied to EU businesses.** Zero-rating requires another-Member-State VAT registration, retained VAT number/country prefix, both VAT numbers on the invoice, dispatch/transport to that State with evidence, and correct VIES reporting. If conditions are not met, charge the appropriate Irish goods VAT; refer special cases and later corrections. Value E1.
- **Construction.** RCT principal/subcontract construction has a recipient reverse charge under s.16(3); construction between connected persons has s.16(5), requiring a taxable recipient. RCT principals receiving these services register irrespective of turnover. The subcontractor invoice omits rate/amount, includes its VAT number and “VAT on this supply to be accounted for by the principal contractor”. The principal self-accounts in the supply period, or on an advance payment, and deducts only if entitled; RCT is on VAT-exclusive consideration. Ordinary private-householder work follows normal supplier accounting. For unclear RCT status, connections, non-residents or rate eligibility: **Check this point with one of our partner accountants.**
- **Construction case.** Original subcontractor B's EUR 600,000 work for A Ltd assumes an ordinary construction supply actually liable at 13.5%, required RCT, full deduction and no other return items. A has EUR 81,000 T1/T2; B charges no VAT, has zero output on the job and EUR 13,000 deductible purchases, giving EUR 13,000 T4. Apartments, heat pumps and separately supplied materials/fittings/scaffolding require their own classification.
- **Imports.** Great Britain is outside the EU goods regime; Northern Ireland remains within it for goods, not services. Where postponed accounting is validly used on the customs declaration, the importer declares VAT in T1 and deductible VAT in T2; PA1 is customs value plus duty, including zero-rated imports. Otherwise inspect entry VAT/customs documents and deduction entitlement. For eligibility, exclusions, customs warehousing or valuation: **Check this point with one of our partner accountants.**
- **EU consumers, distance sales, TBE services and OSS/IOSS**, including the combined threshold, establishment/year tests and elections: **Check this point with one of our partner accountants.** Do not classify all consumer sales under one Irish-VAT rule.

## Deadlines and filing

Two-monthly periods start in January, March, May, July, September and November. The Collector-General may authorise four-monthly returns for annual VAT liability EUR 3,001–14,400, six-monthly for EUR 1–3,000, and monthly returns on request generally for constant repayment businesses. Use the authorised period on ROS.

Section 76 requires filing/payment by the 19th following the period. Revenue gives ROS filers the 23rd; file and pay by that date. The 2026 two-monthly ROS dates are 23 March, 23 May, 23 July, 23 September, 23 November and 23 January 2027. For authorised annual returns/monthly direct debit, including balance interest: **Check this point with one of our partner accountants.**

| VAT3 field | Entry, subject to the entitlement and timing rules above |
|---|---|
| T1 | VAT due on supplies, EU goods acquisitions, postponed imports and received services; include applicable construction reverse charge |
| T2 | Only deductible VAT, including eligible self-accounted VAT and flat-rate additions |
| T3 / T4 | Positive T1−T2 payable in T3, or positive T2−T1 repayable in T4 |
| E1 / E2 | Total value of goods sent to other EU countries / received from EU suppliers |
| ES1 / ES2 | Total value of services supplied to other EU countries / received from EU suppliers |
| PA1 | Customs value plus customs duty for postponed-accounting imports |

Credit notes can adjust T1/T2. A genuinely empty return uses numeric zeros, never “nil”. Equal nonzero T1 and T2 still retain those actual amounts: a zero net payment does not erase the transactions.

**ROS sequence.** Confirm registration/period/basis; collect invoices, credit notes, customs records and bank data; classify with evidence; calculate and reconcile the VAT3 boxes; select the business's VAT3 and correct period in ROS; check the figures before signing/submitting, arrange payment and retain confirmation. Revenue supports payment through ROS and myAccount. Do not assume VIES screen labels are identical to VAT3. For unavailable forms or a failed submission: **Check this point with one of our partner accountants.**

**RTD.** Every VAT-registered person files annually on ROS, due the 23rd of the month after the accounting-period end; a person exempt from mandatory electronic filing who does not pay/file on ROS has 19 days. Original dates: 31 August year end → 23 September; 31 December 2025 → 23 January 2026. Use the final-year VAT3/RTD in ROS. RTD figures are VAT-exclusive, by rate, without negative entries. Its sections are supplies (including applicable exempt/EU/export sales and non-EU services self-accounted by the recipient), EU acquisitions/postponed imports, purchases for resale and other deductible purchases. Section 2 items also enter section 3 or 4 as appropriate; apply deduction restrictions to section 4. Exclude EU supplies to non-registered persons where Irish VAT was not charged or VAT was accounted for under OSS. For adjustments or specialist RTD classifications: **Check this point with one of our partner accountants.**

**VIES.** Goods: monthly by the 23rd of the following month; quarterly reporting is available if the EUR 50,000 limit is not exceeded in the quarter or any of the preceding four quarters, with a switch when crossed in a month. Annual authorisation is a separate specialist route. Services taxable under the customer reverse charge: quarterly by the 23rd following the quarter, or monthly by election. A previously required filer submits a no-supplies statement unless Revenue authorises otherwise (ss.82–83). Reconcile reportable EU values with VAT3.

Repayments go to a financial-institution account; outstanding returns can hold them and other tax debts can absorb them. A previous-year RTD outstanding holds refunds under any taxhead. Keep ordinary records for six years from the latest related transaction; inquiries, claims, appeals and proceedings extend retention until final resolution and appeal periods expire (s.84). Property/special-scheme retention needs separate advice.

**Correcting returns.** A VAT3 can take three working days to process; Revenue's ROS help says proceed as for a new VAT3, then “Additional” lists amendable periods. For whether to amend, supplement or use a later-return self-correction, and the notice/time-limit/interest/disclosure conditions: **Check this point with one of our partner accountants.** Do not treat every error below EUR 6,000 as an interest-free next-return adjustment.

## Penalties and interest

Section 114 imposes simple interest of 0.0274% per day or part-day while payable VAT remains unpaid, and on an undue refund from receipt. EUR 10,000 for 30 chargeable days gives EUR 82.20. The original statutory examples below count from the 19th under ss.76/114. For the precise interest start date on an actual late ROS payment or a special payment arrangement: **Check this point with one of our partner accountants.** Their arithmetic is not a determination of Revenue's collection treatment.

Section 115 provides EUR 4,000 fixed penalties for specified registration, invoicing, return, RTD, VIES and records failures; applicable company-secretary penalties are separate. Do not describe every failure as automatically attracting every penalty.

Current incorrect-return penalties are in **s.116A**; s.116 does not apply to post-Finance-Act-2021 acts/omissions/disclosures. Careless-default reductions depend on significance, cooperation, disclosure validity and previous disclosures. Section 116A(9) removes the careless-default penalty where the aggregate specified VAT/income-tax/stamp-duty/CAT/excise liability does not exceed EUR 6,000 and its reduction condition is satisfied. This does not erase the tax or interest. For the full deliberate/careless matrix, incorrect documents/numbers, secretary liabilities, repeat disclosures, innocent errors and interventions: **Check this point with one of our partner accountants.** Never submit a declaration or disclosure without the person's informed authority.

## Worked examples

### Example 1: consultancy company, September to October 2026

Bray Advisory Ltd is registered, invoice-based and two-monthly on ROS. Original inputs: Irish consultancy EUR 60,000 net at 23%; German business consultancy EUR 20,000; US software EUR 1,000; deductible domestic VAT EUR 2,100 after excluding client entertainment. Assume supplies/invoices fall in September–October, services are ordinary B2B supplied to the relevant Irish/German business establishments, German status/VAT number are verified, destination services are taxable, and software has no supplier VAT and full credit.

T1 = 13,800 + 230 = EUR 14,030; T2 = 2,100 + 230 = EUR 2,330; T3 = EUR 11,700; ES1 = EUR 20,000 and quarterly VIES. Non-EU software is excluded from ES2. Statutory due date 19 November 2026; ROS date 23 November. Original payment 29 November and 10-day statutory-interest illustration: 11,700 × 0.0274% × 10 = EUR 32.06, subject to the ROS-interest referral above.

```oa-check
name: Bray Advisory Ltd, Sep-Oct 2026 VAT3 with a reverse-charged US service, paid 10 days after 19 November
inputs:
  irish_sales: 60000
  eu_b2b_services: 20000
  us_software: 1000
  domestic_input_vat: 2100
  days_late: 10
steps:
  - output_vat: irish_sales * 23 / 100
  - reverse_charge_vat: us_software * 23 / 100
  - t1: output_vat + reverse_charge_vat
  - t2: domestic_input_vat + reverse_charge_vat
  - t3: t1 - t2
  - es1: eu_b2b_services
  - interest: round(t3 * 0.0274 / 100 * days_late, 2)
expected:
  output_vat: 13800
  reverse_charge_vat: 230
  t1: 14030
  t2: 2330
  t3: 11700
  es1: 20000
  interest: 32.06
```

### Example 2: restaurant, July to August 2026, careless error

Harbour Kitchen Ltd sells EUR 90,000 net qualifying restaurant food and EUR 30,000 net standard-rated alcohol/soft drinks; all supplies/tax points are after 1 July 2026. EUR 4,000 input VAT is fully deductible. Correct output = 8,100 + 6,900 = EUR 15,000; T3 = EUR 11,000. At an erroneous 9% on drinks too, declared output = EUR 10,800 and T3 = EUR 6,800. Shortfall EUR 4,200 is 38.18% of the correct liability.

Preserve the original facts: the incorrect return was paid on time; before the notified intervention begins, on 23 November 2026, the company makes a prompted disclosure and cooperates fully. **The penalty cannot be fixed at EUR 840 from these facts alone.** If s.116A(9)'s aggregate is only this EUR 4,200 and its careless-default condition is met, the tax-geared penalty is zero. If that exception does not apply, and this is a first qualifying disclosure satisfying s.116A(1), (7)(b) and (17), 20% of EUR 4,200 is EUR 840. Prior disclosures or disqualifying circumstances change the result. **Check this point with one of our partner accountants.**

Original deadline dates: 19 September 2026, extended ROS date 23 September. The original 65-day statutory-interest illustration to 23 November gives EUR 74.80; apply the ROS-interest referral above before using that amount in a disclosure.

```oa-check
name: Harbour Kitchen Ltd, Jul-Aug 2026, drinks wrongly at 9%, prompted disclosure, interest from 19 September
inputs:
  food: 90000
  drinks: 30000
  input_vat: 4000
  days_late: 65
steps:
  - food_vat: food * 9 / 100
  - drinks_vat: drinks * 23 / 100
  - correct_t3: food_vat + drinks_vat - input_vat
  - declared_t3: (food + drinks) * 9 / 100 - input_vat
  - shortfall: correct_t3 - declared_t3
  - share_of_liability: round(shortfall / correct_t3, 4)
  - conditional_penalty_without_exception: shortfall * 20 / 100
  - penalty_if_aggregate_exception_applies: 0
  - interest: round(shortfall * 0.0274 / 100 * days_late, 2)
expected:
  food_vat: 8100
  drinks_vat: 6900
  correct_t3: 11000
  declared_t3: 6800
  shortfall: 4200
  share_of_liability: 0.3818
  conditional_penalty_without_exception: 840
  penalty_if_aggregate_exception_applies: 0
  interest: 74.80
```

### Example 3: invoice basis or authorised moneys received basis

The original Irish consultancy has EUR 600,000 annual turnover, EUR 50,000 net invoiced and EUR 30,000 net received in the two-month period, all ordinary eligible sales at 23%. Assume no unpaid earlier invoices, advances, connected sales or other excluded transactions, and that the cash-basis authorisation covers the period. It can apply under the turnover route; it cannot just choose the basis retrospectively.

Invoice-basis T1 is EUR 11,500; cash-basis sales T1 EUR 6,900; EUR 20,000 unpaid defers EUR 4,600 until receipt. If nothing remains unpaid, there is no timing difference. This compares sales T1 only: input deduction is not automatically deferred merely because the business has cash-basis authorisation (s.59). For transition balances or restricted purchases: **Check this point with one of our partner accountants.**

```oa-check
name: Invoice basis against moneys received basis, two-month period
inputs:
  invoiced: 50000
  received: 30000
  rate: 0.23
steps:
  - t1_invoice: invoiced * rate
  - t1_cash: received * rate
  - deferred: t1_invoice - t1_cash
expected:
  t1_invoice: 11500
  t1_cash: 6900
  deferred: 4600
```

### Historical transaction cases retained

These preserve the original data, including imperfect invoice figures. Apply the relevant rules above only when the stated evidence/eligibility is established. Bank entries alone do not prove the tax treatment; historic T4 input-credit and E1 service-sale mappings are replaced by T2 and ES1 respectively.

| Original case/input | Conditional result or hold |
|---|---|
| 3 April 2026, NOTION LABS INC, USD 16.00 / EUR 14.68 subscription | If the invoice and lawful currency conversion establish EUR 14.68 net ordinary US B2B software to the Irish establishment, no supplier VAT, full deduction and current-period tax point: EUR 3.38 T1/T2; no ES2. The bank conversion alone does not establish the taxable base. |
| 10 April 2026, GOOGLE IRELAND LIMITED, Google Ads April, EUR 1,045.50 debit | If a valid domestic invoice confirms 23% VAT and fully deductible business advertising: net EUR 850, VAT EUR 195.50 in T2. Billing brand/location alone is insufficient. |
| 15 April 2026, CHAPTER ONE RESTAURANT, client dinner EUR 280 debit; Q1 | If this is client entertainment, no T2 credit under s.60; preserve the EUR 280 expense input without inventing its VAT amount. |
| 18 April 2026, MUSGRAVES WHOLESALE, food supplies EUR 2,400 debit; Q2 | No automatic zero rate or personal-cost inference. Inspect goods/invoice and use. **Check this point with one of our partner accountants.** |
| 22 April 2026, STUDIO KREBS GMBH, IE-2026-018 IT consultancy, EUR 3,500 credit; Q3 | If ordinary B2B consultancy to the verified German business establishment, with destination reverse charge and taxable there: ES1 EUR 3,500 and VIES, no Irish output VAT; E1 is for goods. |
| 28 April 2026, BMW FINANCIAL SERVICES IE, car lease May EUR 650 debit; Q4 | Vehicle, VRT/emissions, use, invoice and tax period are missing. No automatic total block or recovery. **Check this point with one of our partner accountants.** |
| Test 1: Irish office supplies, gross EUR 246, net EUR 200, VAT EUR 46 | With a valid correctly charged invoice and fully deductible use: EUR 46 T2. |
| Test 2: AWS US software, EUR 100 monthly, no supplier VAT | Under the received-services conditions above and full deduction: EUR 23 T1/T2, no ES2. |
| Test 3: SAP Germany software, EUR 500 monthly, no supplier VAT | Under the same conditions: EUR 115 T1/T2, ES2 EUR 500. |
| Test 4: Italian goods, EUR 2,000, no supplier VAT, standard-rated in Ireland | If an ordinary taxable acquisition into Ireland, fully deductible: EUR 460 T1/T2 and E2 EUR 2,000. |
| Test 5: French consultancy customer, EUR 1,000, valid VAT number | With ordinary B2B place of supply in France and destination taxable reverse charge: ES1 EUR 1,000 and VIES, no Irish output VAT. |
| Test 6: staff car EUR 30,000, stated VAT EUR 5,610 at 23% | Original VAT does not precisely reconcile: 30,000 × 23/123 = EUR 5,609.76. Eligibility is missing too. Retain the original figures as disputed data; obtain the invoice and apply the vehicle conditions. **Check this point with one of our partner accountants.** |
| Test 7: taxi petrol EUR 100, stated VAT EUR 18.70 | If petrol bought for fuel, not stock-in-trade: input blocked; no T2. |
| Test 8: delivery van diesel EUR 150, stated VAT EUR 28.05 | If the actual invoice, business use and deduction conditions confirm these figures: T2 EUR 28.05. Do not recover merely because it says diesel. |
| Test 9: Spanish hotel EUR 200 including EUR 20 Spanish VAT | Do not put Spanish VAT into Irish T2. For correct place of supply, refund/reimbursement or cost treatment: **Check this point with one of our partner accountants.** |
| Test 10: RCT construction EUR 10,000 net, no VAT, specified rate 13.5% | With confirmed RCT/reverse-charge scope, rate and full deduction: EUR 1,350 T1/T2. |
| Test 11: qualifying restaurant meal EUR 50 net after 1 July 2026 | At the stipulated 9% tax point: EUR 4.50 T1. |
| Test 12: US import customs value EUR 5,000, duty EUR 200, rate 23% | If valid postponed accounting applies and import VAT is fully deductible: PA1 EUR 5,200; T1/T2 EUR 1,196. Check the actual customs VAT base; other chargeable incidental expenses must not be omitted. |
| Test 13: cattle, EUR 10,000 plus stated 5.5% / EUR 550 farmer addition | Arithmetic at the original stated rate is EUR 550, but that is not the 2026 4.5% addition (arithmetically EUR 450). Hold for a corrected invoice and scheme/credit eligibility; no automatic EUR 550 T2 claim. **Check this point with one of our partner accountants.** |
| Test 14: client dinner EUR 200, stated VAT EUR 16.36 at 9% | If client entertainment, input blocked regardless of the supplier's rate; do not validate the invoice rate from the bank description. |

## Ask the client first

Obtain registration/effective date, VAT number, 2025/2026 turnover split, ROS period, accounting year end and cash authorisation; invoices/credit notes/customs documents; supply and payment dates; customer business status and receiving establishment; foreign purchases; exempt/mixed use; construction/RCT/connections; vehicle registration/emissions/use; prior disclosures and outstanding VAT3/VIES/RTD returns. Request missing facts only after searching the available record.

Do not infer input recovery from a merchant, VAT treatment from an IBAN, a standard rate from missing classification, or Irish VAT from an unknown customer. Hold the item for evidence and state the unresolved fact. Bank fees/insurance, government/statutory charges, utilities, post/logistics, transport, retail, payment processors, professional fees, wages/PRSI/PAYE, tax payments, own-account transfers, domestic invoices, commercial/residential rent, cash withdrawals, individuals, mixed-use phone/internet and large purchases are investigation categories, not automatic VAT classifications. A foreign supplier charging its own VAT does not establish that Irish self-accounting is unnecessary; hold for correct place-of-supply and invoice treatment.

Retain the historical referral routes: R-IE-1 VAT groups; R-IE-2 Capital Goods Scheme; R-IE-3 property/option to tax/developers; R-IE-4 partial exemption; R-IE-5 margin/auction/travel-agent schemes; R-IE-6 flat-rate farmers; R-IE-7 unclear RCT construction; R-IE-8 direct taxes (use the Irish companion Guides); and R-EU-5 consumer/OSS rules. Also refer sea fishers/racehorse trainers, Intrastat, bad debts, foreign VAT refunds, other exemptions, customs warehousing and unresolved eligibility or deliberate defaults: **Check this point with one of our partner accountants.** Do not file affected items using an assumed result.

## Sources

Official provisions and passages read on 2026-11-26 are listed below. The statute controls where guidance is broader; the cash-basis difference is stated above. No accountant approval is implied.

| Passage read and purpose | Official URL | Read on |
|---|---|---|
| VATCA ss.6, 9, 12, 16, 34: accountability and transaction scope | https://revisedacts.lawreform.ie/eli/2010/act/31/revised/en/html | 2026-11-26 |
| VATCA ss.37, 41, 46: price, two-thirds and rates | https://revisedacts.lawreform.ie/eli/2010/act/31/section/46/revised/en/html | 2026-11-26 |
| VATCA s.59: deduction conditions and qualifying vehicles | https://revisedacts.lawreform.ie/eli/2010/act/31/section/59/revised/en/html | 2026-11-26 |
| VATCA s.60: blocked expenditure and exceptions | https://revisedacts.lawreform.ie/eli/2010/act/31/section/60/revised/en/html | 2026-11-26 |
| VATCA s.62: vehicle adjustment formula | https://revisedacts.lawreform.ie/eli/2010/act/31/section/62/revised/en/html | 2026-11-26 |
| VATCA ss.74–76: tax points and return/payment duty | https://revisedacts.lawreform.ie/eli/2010/act/31/section/76/revised/en/html | 2026-11-26 |
| VATCA s.80: statutory eligibility, timing and exclusions | https://revisedacts.lawreform.ie/eli/2010/act/31/section/80/revised/en/html | 2026-11-26 |
| VATCA ss.82–84 and 92B: VIES, retention and turnover | https://revisedacts.lawreform.ie/eli/2010/act/31/section/92B/revised/en/html | 2026-11-26 |
| VATCA s.114: statutory interest; s.115: fixed penalties | https://revisedacts.lawreform.ie/eli/2010/act/31/section/114/revised/en/html | 2026-11-26 |
| VATCA s.116(24): retired provision; s.116A(1), (7)–(9), (17): current disclosure and small-liability conditions | https://revisedacts.lawreform.ie/eli/2010/act/31/section/116A/revised/en/html | 2026-11-26 |
| Revenue: Registration thresholds and turnover | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/persons-required-register-goods-services-abroad.aspx | 2026-11-26 |
| Revenue: Current 2025/2026 rates and farmer additions | https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx | 2026-11-26 |
| Revenue: Standard-rate consultancy | https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/standard-rate-vat.aspx | 2026-11-26 |
| Revenue: Reduced-rate hotel lettings | https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/reduced-rate-vat.aspx | 2026-11-26 |
| Revenue: Dated hospitality/energy and other second-reduced supplies | https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx | 2026-11-26 |
| Revenue: Invoice, acquisition and received-services tax points | https://www.revenue.ie/en/vat/accounting-for-vat/when-is-vat-due/index.aspx | 2026-11-26 |
| Revenue: Two-thirds test, exceptions and guitar case | https://www.revenue.ie/en/vat/vat-on-services/two-thirds-rule/index.aspx | 2026-11-26 |
| Revenue: Cash-basis guidance and exclusions | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/who-can-opt-moneys-received-basis.aspx | 2026-11-26 |
| Revenue: Cash-basis application and effective date | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/how-apply-moneys-received-basis.aspx | 2026-11-26 |
| Revenue: Deemed receipts and PSWT/RCT | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/sums-included-money-received-basis.aspx | 2026-11-26 |
| Revenue: Cash-basis cancellation | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/vat-moneys-received-basis-eligibility-cancellation.aspx | 2026-11-26 |
| Revenue: Received-service scope and German consultancy case | https://www.revenue.ie/en/vat/vat-on-services/exceptions-general-place-supply-rules-services/received-services/index.aspx | 2026-11-26 |
| Revenue: Business status/invoice/VIES duties | https://www.revenue.ie/en/vat/vat-on-services/when-is-vat-charged-on-services/vat-obligations-of-Irish-traders-supplying-services-to-business-customers-abroad.aspx | 2026-11-26 |
| Revenue: EU-goods zero-rate conditions | https://www.revenue.ie/en/vat/goods-and-services-to-and-from-abroad/intracommunity-supplies/supplies-of-goods-to-businesses-in-the-european-union-eu.aspx | 2026-11-26 |
| Revenue: EU acquisitions and stock case | https://www.revenue.ie/en/vat/goods-and-services-to-and-from-abroad/acquisitions-from-other-eu-member-states/self-accounting-for-vat.aspx | 2026-11-26 |
| Revenue: Return periods and ROS date | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/when-vat-becomes-payable.aspx | 2026-11-26 |
| Revenue: VAT3 fields and credit notes | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/completing-vat3-return.aspx | 2026-11-26 |
| Revenue: Repayment holds/offset | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/vat-repayment.aspx | 2026-11-26 |
| Revenue: Payment channels | https://www.revenue.ie/en/vat/accounting-for-vat/how-do-you-pay-vat/index.aspx | 2026-11-26 |
| RTD manual pp.3–9, 11: filing, fields, restrictions and holds | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part09-obligations-accountable-persons/return/VAT-RTD-S76.pdf | 2026-11-26 |
| Construction manual pp.3–7: registration, rates, RCT, connected parties and invoice/return timing | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part11-immovable-goods/construction-services/construction-servcies.pdf | 2026-11-26 |
| Postponed-accounting manual pp.3–4: importer, PA1 and NI/GB distinction | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part07-provisions-relating-to-imports-exports/postponed-accounting.pdf | 2026-11-26 |
| ROS help: processing and Additional amendment route | https://www.revenue.ie/en/online-services/services/ros/ros-help/something-is-not-working/issues-completing-and-submitting-returns/unable-to-amend-a-return.aspx | 2026-11-26 |
