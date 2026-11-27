---
name: finland-vat-return
description: >
  Prepare and review an ordinary Finland VAT return for 2026. Establish
  registration, supply location, tax point, taxable consideration and rate before
  assigning return fields. Covers domestic sales, ordinary EU goods and
  services, exports, import VAT including the Åland tax border, construction
  reverse charge, input deductions, mixed use, passenger vehicles and property
  investment adjustments. Includes the current and preceding-year small-business
  test, 2026 reduced rates, filing periods, corrections and statutory sanctions.
  Trigger on Finnish VAT, ALV-ilmoitus, OmaVero, reverse charge, EU sale, import
  or deductible input VAT. Use with vat-workflow-base and eu-vat-directive;
  special margin, travel, marketplace and other sector schemes need separately
  verified treatment.
version: 2.9
jurisdiction: FI
category: international
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Finland VAT return v2.9

## Who this applies to

Prepare an ordinary Finnish VAT return for 2026 in **OmaVero (MyTax)**. Load `vat-workflow-base` and `eu-vat-directive`. Establish the parties, receiving/supplying establishment, customer business status, goods movement, supply/advance dates, net or gross price, registration and purchase use before calculating. A merchant name or bank statement alone does not establish any of these facts. Keep unresolved transactions out of filing-ready totals.

The transaction map below covers domestic sales, ordinary EU goods/services, non-EU services, imports and Åland, construction reverse charge and conditional deductions. Special-scheme calculations and the explicit holds below are not usable filing conclusions.

## Rates, bands and thresholds

| Item | Rule applicable in 2026 | Official source |
|---|---|---|
| General rate | 25.5%; formerly 24% before 1 September 2024. Select the rate by the supply/advance tax point, including old-period corrections. | [VAT Act §84](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Vero rate history](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/arvonlisaveroprosentit/) |
| Reduced rate | 13.5% from 1 January 2026, formerly 14%, for the listed §85 categories subject to the exclusions below. | [VAT Act §85, Act 1358/2025](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |
| Newspapers/magazines | 10% for qualifying print/electronic publications; predominantly advertising, video or audible music is excluded. | [VAT Act §85a](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |
| Finnish small-business exemption | Counted turnover **at most €20,000 in each of the current and preceding calendar years**, without voluntary registration. Other-EU establishment needs the additional SME conditions below; non-EU establishment cannot use it. | [VAT Act §§3–3a](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |
| Longer tax period, on application | Quarter: calendar-year accounting turnover/revenue at most €100,000; year: at most €30,000. These are not automatic periods. | [Procedure Act §§11–15](https://www.finlex.fi/fi/lainsaadanto/2016/768) |
| Cash basis | Calendar-year §3 turnover at most €500,000, or the other statutory accounting-status route; ordinary domestic supplies only, with the 12-month backstop and cessation rules below. | [VAT Act §§137,143](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |
| Small-error alternative | VAT difference at most €500; next-due-return deadline and data-only exclusions apply. | [Procedure Act §25](https://www.finlex.fi/fi/lainsaadanto/2016/768); [Vero correction instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| EU consumer distance goods/TBE exception | Combined relevant sales at most €10,000 in both current and preceding years, with the single-member-state and customer/transport conditions below. | [VAT Act §§63a,69i,69m](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |

The 13.5% list includes food/feed, restaurant/catering, passenger transport, accommodation, medicines and specified pharmacy products, menstrual/incontinence protection and children's nappies, books, qualifying sport and culture including specified live streams. Performer fees require voluntary registration for that activity. Art has the specified creator/successor/occasional-seller conditions and excludes margin-scheme sales; copyright compensation must be that received by a representative organisation; public broadcasting covers the specified statutory receipts. Alcohol and tobacco remain general-rate, including alcohol served with a meal. Live animals, tap water and poisons do not qualify as food under §85. Advertising-dominated or principally video/music publications are not reduced-rate books. Do not use the old 10% classifications for books, medicines, transport or accommodation in 2026. [VAT Act §§84–85a][law]; [Vero rates][rates].

## The base

### Registration and tax period

1. **Small-business test:** aggregate the VAT-exclusive value of Finnish-place sales: taxable supplies, the specified zero/exempt supplies (including exports, EU goods sales, property rights and non-incidental financial/insurance services). Exclude fixed assets and incidental financial/insurance sales. Purchases are not turnover. Split non-calendar accounting years into calendar years; do not annualise a short trading year. If the preceding year exceeded €20,000, low current-year turnover does not restore exemption immediately. [VAT Act §3][law]; [Vero §§2–2.3][small].
2. If current-year counted turnover crosses €20,000, liability starts at the crossing, with the crossing sale taxable **in full**. A Finnish business may register voluntarily for business activity below the limit; VAT then applies to all its taxable sales, not selected invoices. Ordinary voluntary registration starts no earlier than application receipt/submission. Exempt financial/insurance/health activity does not become taxable through that ordinary election. Property-option registration has a separate retrospective exception: do not apply the ordinary no-backdating rule to it. [VAT Act §§12,173][law]; [Vero §2.4][small].
3. Deregistration for low turnover needs the current and preceding calendar-year test, **at most** €20,000 each, and a request; it is not retrospective. It does not require two fully completed low-turnover years: a business can qualify during the current year when the preceding year also qualifies. Property-option deregistration depends on cessation of its statutory conditions. [VAT Act §§3,174][law]; [Vero §2.4][small].
4. A supplier established in another EU country additionally needs the €100,000 Union-turnover tests and the cross-border SME identification/permission conditions; do not grant exemption from the Finnish €20,000 test alone. A non-EU-established supplier cannot use the exemption even with a Finnish fixed establishment. Acquisition/reverse-charge obligations need separate assessment even when domestic sales are exempt. [VAT Act §§3–3a,9,26c][law]; [Vero §§5–6][small]. The cross-border SME registration and non-ordinary acquisition cases remain non-usable holds: Check this point with one of our partner accountants.
5. Normal period: calendar month. Apply for a permitted longer period and follow the existing period until Vero's decision. A longer period normally starts next calendar year; a shorter period starts with the next shorter period. A start-up applying when activity begins can use its elected period from commencement. The period normally stays the same at least one year. Report a longer-period turnover-limit crossing immediately; Vero can shorten the period. Filing/payment defaults can prevent acceptance. Natural persons, estates and partnerships carrying on only primary production, and qualifying visual artists with no other VAT-taxable activity, normally have an annual period irrespective of turnover. [Procedure Act §§11–15][procedure]; [Vero periods][period].
6. File every allocated period, including no activity. Zero-rate sales with deductible related inputs are reportable activity, not a no-activity return. Small-business relief (*alarajahuojennus*) is unavailable for accounting periods starting on/after 1 January 2025; do not claim it for the 2026 calendar-year period. Relief for an earlier-starting accounting period is a non-usable hold: Check this point with one of our partner accountants. [Vero return instructions][return].

### Base and timing

Tax base is agreed consideration **excluding VAT**, including price supplements. For a VAT-inclusive price: net = gross / (1 + rate); VAT = gross − net. Separate supplies need their own classifications; do not split a composite supply arbitrarily. Discounts, cancellation credits and bad debts reduce the base under §78; recovered bad debts increase it. Corresponding purchase credits/cancellations adjust deductions under §118. Allocate adjustments under §§139/145a using proper accounting treatment. [VAT Act §§73,78,118,139,145a][law].

Ordinary sales follow delivery/performance and pre-supply receipts under §15. The in-year invoice method under §136 reconciles unbilled amounts to the final financial-year month; cessation closes outstanding amounts. A qualifying §137 cash-basis method uses collections, no later than 12 months after supply except bad debts, and closes uncollected balances on cessation. The linked §143 domestic purchase method uses payment and closes unpaid balances on cessation. General-rule reverse-charge cross-border services keep §138 performance/advance timing. EU goods sales/acquisitions normally go to the following month, or the delivery/receipt month if the delivered/received goods were invoiced then (§§138a–138b). Do not let invoice date alone move advances, EU transactions or imports. [VAT Act §§15,135a–143][law].

Import base starts with customs value, adding duties and other included taxes/charges except VAT, and freight, insurance and incidental costs to the first Finnish destination or a further known EU destination, without double counting. Retain customs decision and supporting documents. Åland importers determine their customs value themselves. [VAT Act §§88,91,93,102a][law]; [Vero Åland][aland].

Property transfers/rent, healthcare, social care, statutory education, finance and insurance have defined exemptions; a supplier's industry name does not establish eligibility. Ordinary exempt activity lacks input deduction; qualifying exports/EU supplies and the specified non-EU financial/insurance routes under §131 differ. Property letting can opt into VAT for the specified property/part when §30's continuous-use and letting-chain conditions, or its listed public-user alternatives, are met. Complex exemption boundaries and property-option applications are non-usable holds: Check this point with one of our partner accountants. [VAT Act §§27–44,102,117,131][law].

### Transaction map

Use current MyTax field labels, not the obsolete numeric-code matrix. Retain bases in the workpaper even when the return asks only for tax. Deduction is conditional under the next section. [Vero return instructions][return].

| Supported transaction | Entries |
|---|---|
| Domestic taxable sale | VAT **amount**, by rate, in “Tax on domestic sales by tax rate”. Include supported own-use/deemed supplies; do not report only the sales base. [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Ordinary EU goods acquisition, transported to Finland | Base in “Purchases of goods from other EU countries”; acquisition VAT in “Tax on purchases of goods from other EU countries”; qualifying input VAT in “Tax deductible for the tax period”. A margin-scheme or exempt-small-seller invoice is not an ordinary acquisition by default. [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/); [VAT Act §26c](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |
| EU general-rule service, Finnish place and purchaser liability established | Base in “Purchases of services from other EU countries”, VAT in “Tax on purchases of services from other EU countries”, plus qualifying input VAT. EU special-rule services supplied in Finland use domestic-output tax when purchaser liability applies; construction uses its separate rows. [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Non-EU service, taxable Finnish place and purchaser liability established | VAT in domestic-sales tax by rate, plus qualifying input VAT; no separate purchase-base entry. Applies to qualifying business suppliers of any size. A foreign hotel does not create Finnish reverse charge. [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/); [VAT Act §§9,65,67](https://www.finlex.fi/fi/lainsaadanto/1993/1501) |
| Import reported to Vero by VAT-registered business importer | Base in “Imports of goods from outside the EU”, VAT in “Tax on imports of goods from outside the EU”, qualifying deduction in the same period. Ordinary timing is the customs-decision issue month, also for Åland one/two-step declarations since May 2023. Correct changed customs decisions. Tax-exempt import: retain base and leave tax/deduction blank. Customs-collected or §100a special-procedure cases need their separate route. [VAT Act §§135a,141](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Qualifying EU goods sale | Base in “Sales of goods to other EU Member States”, with recapitulative statement. Require transport from Finland to another EU VAT state, the qualifying buyer and communicated non-Finnish VAT ID, and the statutory exclusions/statement conditions. A margin-scheme sale is not an ordinary zero-rated EU sale. [VAT Act §§72a–72b](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| General B2B service taxable in customer's EU state | Base in “Sales of services to other EU Member States” and recapitulative statement when customer liable there; do not include services exempt in the taxing state in that statement. [VAT Act §§65,162](https://www.finlex.fi/fi/lainsaadanto/1993/1501); [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Supported exports/other deduction-preserving foreign or zero-rate sales | “Turnover taxable at zero VAT rate”; retain export/transport and entitlement evidence. Exempt sales without deduction (such as qualifying healthcare) do not belong here. [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/) |
| Special schemes | OSS/IOSS VAT uses the applicable separate return; OSS sales also enter ordinary zero-rate turnover, without Finnish domestic-output VAT. Used-goods margin VAT instead enters ordinary domestic-sales tax at its supported rate, after a separate eligible-margin computation. Full scheme calculations are held below. [Instructions](https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/); [Vero margin §5.2](https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48682/kaytettyjen-tavaroiden-arvonlisaverotus3/) |

**Foreign-service gate:** identify the receiving establishment and general/special place rule, then liability. A participating Finnish fixed establishment or the seller's voluntary Finnish VAT registration prevents the ordinary §9 buyer reverse charge. Private purchasers and the other statutory exceptions, including passenger transport and §69d event services, have seller liability; §69d's virtual B2B exception must be considered before treating all event services alike. If supplied outside Finland, do not create Finnish VAT from supplier geography. [VAT Act §§9,65–69d][law].

### Deduction controls

Ordinary domestic deduction requires VAT-taxable business use, seller liability and the required invoice/receipt. For self-assessed acquisitions/reverse charge, retain invoice or statutory substitute and the required tax declaration/assessment; imports need customs decision and associated documents. Claim only qualifying Finnish VAT. Directly attribute taxable, exempt and private use; apportion shared qualifying costs by evidenced use. No universal turnover formula, rounding-up rule or half-deduction applies. [VAT Act §§102–102a,114,117][law].

**Entertainment VAT is fully blocked**, irrespective of any separate income-tax treatment: food or alcohol rates do not create a buyer deduction. Private costs, commuting, residential/recreational premises and related restricted costs must also be screened. Staff meals, parking, work clothing, gifts and business travel are not automatic deductions: establish business purpose and the particular restriction first. [VAT Act §§102,114,117][law].

For an ordinary passenger car, even minor private/commuting/entertainment use blocks **all** purchase, leasing and running-cost VAT. Exclusive deductible-business use can qualify. Taxi, rental, driving-instruction and resale exceptions require their actual use tests; vans/lorries use the evidenced deductible-business share. Keep a separate driving log or equivalent evidence per vehicle, at least 6 years, and correct earlier deductions if use disproves entitlement. [VAT Act §114][law]; [Vero vehicles][vehicles].

### Construction and property investments

For taxable construction services/leased construction workers under §8c, the buyer must nonoccasionally sell the specified services/property, or resell the service to such a buyer. Goods-only and private-consumer purchases do not qualify. Confirm buyer status; seller invoices net with buyer VAT ID and reverse-charge notation, and reports “Sales of construction services and scrap metal”. Buyer reports “Purchases of construction services and scrap metal”, the 25.5% VAT in “Tax on purchases of construction services and scrap metal”, and only its qualifying deduction. Foreign-seller construction purchaser liability under §9 can also use these rows even when the buyer does not sell construction services. [VAT Act §§8c,9,31(3),209e][law]; [Vero return instructions][return].

Qualifying new-construction/major-renovation investments have a **10-year** adjustment period from the start of the completion/qualifying receipt year, excluding the pre-completion/receipt part of that year. Annual adjustment = original input VAT × (original deductible fraction − current deductible fraction) / 10. Positive repays deduction; negative increases it. There is no general 10-percentage-point minimum change. Destruction is excepted. Transfer, permanent withdrawal or deregistration can trigger adjustment for remaining years; statutory transfer of rights/duties needs its own conditions and evidence. Preserve original VAT/use history. Movable assets do not acquire a blanket immunity from later own-use or deduction corrections. Transfer applications and unusual own-use cases are non-usable holds: Check this point with one of our partner accountants. [VAT Act §§120–121g][law].

## Deadlines and filing

Monthly and quarterly VAT filing/payment normally fall on the **12th of the second month after the period**. Quarterly dates: 12 May, 12 August, 12 November, 12 February, subject to bank-day adjustment. Annual VAT is due at the end of February following the year. If due date is a Saturday, Sunday or public holiday, use the next business day. March and January–March 2026 are due **12 May 2026**; annual 2026 is due **1 March 2027** because 28 February is Sunday. A shortened/ceased period can have its own closing deadline; follow the period decision. VAT-return filing deadlines cannot be extended. [Procedure Act §17][procedure]; [Vero filing calendar][return]; [Vero periods][period].

1. Reconcile sales, purchases, credit notes, customs and VAT-ID/transport evidence to the allocated period and the fields above. Preserve each transaction's euro amount and conversion evidence; do not derive VAT from a bank merchant label.
2. Sign into MyTax, select the VAT return and allocated tax period, enter **tax** or **base** as the field requires, and review the calculated net. Output/self-assessed VAT minus deductible input VAT = payable/refundable VAT. Use no activity only for a genuinely empty reportable period.
3. Submit; retain acknowledgement, complete return and reconciliation. Pay using MyTax's reference/payment details by the deadline. A negative result is subject to Vero's refund approval and account treatment; do not invent a carry-forward or cash-refund date. [Vero return instructions][return].
4. Correct errors promptly with a **complete replacement return for the original period**, including unchanged correct entries. For a tax difference at most €500, the alternative permits changing the tax on the return whose deadline is next after discovery, by that deadline. It cannot correct data-only errors (zero-rate turnover, exempt EU sales, construction/scrap bases). If the alternative's deadline was missed, use a replacement. The €500 limit is independent of tax-period length. [Procedure Act §25][procedure]; [Vero corrections][return].
5. The correction limit is 3 years from the beginning of the calendar year following the relevant accounting period/tax year, not 3 years from the filing deadline. Pay underdeclared tax and assess late charges. [Vero corrections][return].

Recapitulative statements for covered EU sales are monthly and due by the **20th of the following month**, even if the domestic VAT period is longer. No statement entry is created merely by buying EU goods. VAT-ID and transport evidence and the statement's relief conditions matter separately. Intrastat and machine-file/API specifications are non-usable holds: Check this point with one of our partner accountants. [VAT Act §§72a–72b,162][law].

## Penalties and interest

For an original late return: €3 per day, at most €135 for the daily component; after 45 days, add 2% of late positive tax. The **tax-based component** is capped at €15,000 per tax type/period. A replacement within 45 days of the original due date has no late fee; later additional payable tax or overstated-refund corrections use the 2% route without another daily component. Valid-reason/non-taxpayer-cause exceptions and the no-double-charge rule where a tax increase is imposed apply. [Procedure Act §§35–36][procedure].

Tax increase for deficient/omitted information is ordinarily 10% of additional tax; repeated failure or manifest disregard gives 15–50%; estimated assessment gives 25%; a qualifying unclear/unreasonable case gives 3%. If no tax is assessed, maximum €200. Minor failure, valid reason and statutory unreasonable-case exceptions can prevent an increase. These are conditional routes, not a choice of lowest rate. [Procedure Act §§37–38][procedure].

Ordinary overdue-tax interest is **9.5% for days in 2026**, running from the day after due date through payment inclusive, using actual calendar days. Overpaid refunds and assessment changes can have different starting points. Do not extend the 2026 statement to another year without its rate. [Vero interest][interest].

## Cross-border points

Goods need the dispatch/installation/destination rule before export or EU relief. General B2B services follow the receiving establishment, or business seat absent a receiving establishment; general B2C follows the supplier's establishment/seat. Property services follow property location. Passenger transport, events (including virtual-participation distinctions), restaurant, hire and electronic services require their own rules; no blanket foreign-invoice rule applies. [VAT Act §§63–72b][law].

EU consumer distance goods and telecommunications/broadcast/electronic services ordinarily follow destination. The €10,000 combined current/preceding-year exception requires establishment in only one member state, the specified customer location and goods sent to another member state. Crossing switches treatment from that moment; a destination election binds at least two calendar years. **Use the 2026 §69m wording**, not Act 597/2026's changes commencing in 2027. Full OSS/IOSS/non-Union OSS, marketplaces, stock locations and the cross-border SME interaction are non-usable holds: Check this point with one of our partner accountants. [VAT Act §§63a,69i,69m][law].

Åland is outside EU VAT/excise territory. Goods crossing its tax border, including mainland Finland, require customs/import-export treatment. For ordinary VAT-registered business imports reported to Vero, use customs-decision issue-period reporting and conditional deduction; old approval-date examples concern pre-May-2023 imports. Customs-collected/nonbusiness and indirect-representative exceptions do not belong in the business's ordinary Vero import rows. Åland-to-Germany implementation and specialist border cases are non-usable holds: Check this point with one of our partner accountants. [Vero Åland][aland]; [VAT Act §§135a,141][law].

## Two worked examples that recompute

All example transaction amounts are hypothetical, not official figures. Net/gross and classification assumptions are conditions, not conclusions from merchant names.

Separate supported net food €700 and wine €100 supplies in 2026:

```oa-check
name: Finland assumed 2026 restaurant separate rates
inputs:
  net_food_price: 700
  net_wine_price: 100
  food_rate: 0.135
  wine_rate: 0.255
steps:
  food_vat: net_food_price * food_rate
  wine_vat: net_wine_price * wine_rate
  output_vat: food_vat + wine_vat
expected:
  food_vat: 94.50
  wine_vat: 25.50
  output_vat: 120
```

Confirmed Finnish general-rule service, €1,000 net, purchaser liable and evidenced 70% deductible/30% non-deductible use:

```oa-check
name: Finland assumed reverse charge mixed use
inputs:
  established_service_base: 1000
  vat_rate: 0.255
  established_deductible_share: 0.70
steps:
  reverse_charge_vat: established_service_base * vat_rate
  deductible_vat: reverse_charge_vat * established_deductible_share
  net_vat_cost: reverse_charge_vat - deductible_vat
expected:
  reverse_charge_vat: 255
  deductible_vat: 178.50
  net_vat_cost: 76.50
```

### Original ordinary decision cases

These retain the original A–O case inputs. Sources: [rates][rates], [return entries/corrections][return], [small-business rules][small], [vehicles][vehicles].

- A: €4,000 net ordinary domestic consulting → €1,020 output VAT. B: qualifying restaurant service on **15 January 2026**, €800 net → €108; separate food €700/wine €100 variant → €120 as above.
- C: current-year €19,700, preceding year at most €20,000, €900 net general-rate sale on **20 May** → €20,600 counted turnover; crossing sale taxable in full, €229.50 VAT.
- D: €12,000-turnover business voluntarily registered **1 February**; €1,000 net taxable sale **10 February** → €255 VAT.
- E: €2,000 ordinary EU inventory acquisition, fully deductible → base €2,000, acquisition VAT €510, deduction €510, net €0; no blank-field shortcut.
- F: EU service mixed use → €255/€178.50/€76.50 as above. G: €1,000 non-EU service, Finnish place and buyer liability established → domestic-output tax €255; no base entry; €255 deduction only if wholly qualifying.
- H: customs-supported base €4,000 at 25.5% → import VAT/deduction €1,020 each. For an exempt import retain €4,000 base, both VAT fields blank.
- I: ordinary passenger car with customer visits and occasional private trips → no car-related VAT deduction. J: no sales, purchases, imports or other reportable VAT → file no activity.
- K/L: omitted €4,000 net sale gives €1,020 VAT, requiring complete replacement. Eligible €400 tax error can use next-due-return alternative by its deadline; €501 cannot; neither can an excluded data-only error.
- M: client entertainment, food €200 + €27 VAT and wine €80 + €20.40 VAT → both deductions €0.
- N: March/Q1 2026 → 12 May 2026; annual 2026 → 1 March 2027. O: registered sole trader, calendar-year 2026, turnover under €30,000 → no abolished relief.
- Prior penalty control: original return **50 days late**, **€4,000 payable VAT**, no waiver/tax increase → min(50 × €3, €135) + €4,000 × 2% = **€215**.

### Historical cases retained with corrected routes

Use the same evidence/deduction gates; the old field numbers are not instructions. [VAT Act §§9,15,65,67,73,84,102,114][law]; [return][return].

| Original case | Supported outcome or explicit non-usable hold |
|---|---|
| EC1/Test11: Åland → mainland goods €3,000 | Assuming confirmed import base €3,000 and wholly deductible general-rate business goods: import VAT/deduction €765 each. Keep customs evidence; EC11 Åland → Germany remains held above. |
| EC2/Test4: entertainment €500 + €67.50 VAT; €150 + €20.25 VAT | Deduct €0. An asserted 50% income-tax treatment establishes no VAT entitlement. |
| EC3: €10,000 advance August 2024, €25,000 contract, completion October 2024 | If VAT-exclusive general-rate consideration: advance VAT €2,400 at 24%; €15,000 balance VAT €3,825 at 25.5%. Price basis must be evidenced. |
| Test10: advance €5,000 on 15 August 2024, balance €15,000 on completion 20 October 2024, total €20,000 | On the same VAT-exclusive assumptions: €1,200 and €3,825. Do not substitute 2026 dates or rates. |
| EC4/Test5: plumbing/subcontract construction €50,000 / €30,000, buyer regularly sells construction | If §8c and full deduction established: construction purchase bases €50,000/€30,000; tax/deduction €12,750/€7,650. |
| EC5: IT company's office renovation €30,000 | If domestic builder liable and buyer fails §8c's buyer tests, ordinary VAT €7,650, deductible only to qualifying use. A foreign builder needs the separate §9 gate. |
| EC6/Test2: US SaaS €100/month / €50 | If Finnish general-rule buyer reverse charge and full deduction established: domestic-output VAT/input €25.50/€12.75, no non-EU purchase-base box. |
| EC7: Estonia hotel invoice showing **22%** VAT | No Finnish reverse charge or Finnish-input deduction from that invoice. Invoice-rate correctness and possible foreign refund are unproven; do not call foreign VAT irrecoverable. Check this point with one of our partner accountants. |
| EC8/Test7: Finnish business hotel €120 + €12 VAT at 10%; €100 + €10 VAT at 10% | Original invoice facts preserved, but 10% is not the 2026 accommodation rate. Date/rate-corrected invoice and deduction must be established before use. Check this point with one of our partner accountants. |
| EC9: car €40,000 + €10,200 VAT, director's business and private driving | Ordinary passenger-car mixed-use deduction €0. Test9 €30,000 + €7,650, general business use without use records: neither automatic denial nor automatic deduction; obtain exclusive-use evidence or hold. Check this point with one of our partner accountants. |
| EC10: taxi €35,000 + €8,925 VAT, exclusively qualifying taxi use | Conditional full deduction €8,925 under §114(2), not the old fictitious §114a citation. |
| EC12/Test6: Finnish IT consultancy to Swedish business / €2,000 to Danish VAT-registered business | Subject to general-rule receiving-establishment/liability evidence: EU-services sale base, no Finnish output VAT, monthly statement. No Swedish/Danish liability is inferred solely from a company name. |
| EC13/Test8: China customs value €20,000 + duty €1,000; US goods €8,000 + duty €400 + freight €200 | If these include all required costs and represent the full import bases: €21,000 → VAT €5,355; €8,600 → VAT €2,193, with conditional matching deductions. |
| EC14: €2,000 credit in November 2024 for July 2024 supply | VAT-exclusive general-rate credit → €480 at original 24%; allocate by proper accounting credit-note timing, not a universal invoice-date rule. |
| EC15/Test12: VAT-registered business, €12,000 turnover in 2025, asks for relief | No relief for a calendar-year 2025 period. Deregistration needs current/preceding-year facts and request; original €15,000 threshold is superseded. EC16 financial-group proposal remains held below. |
| Test1: office equipment €1,000 net + €255 VAT | Conditional input deduction €255 with ordinary domestic evidence and wholly qualifying use. |

### Original bank-statement cases: no merchant-name classification

The six original dated inputs remain unchanged. **These are not filing-ready outcomes.** Obtain invoice, net/gross basis, location/liability and use evidence before applying the transaction map. [VAT Act §§9,65,73,102a,114][law].

| Original input | Decision gate |
|---|---|
| `03.04.2026 ; NOTION LABS INC ; -14.68 EUR` | US/general-rule service route only if invoice proves it; €14.68 is not assumed net. Check this point with one of our partner accountants. |
| `10.04.2026 ; GOOGLE IRELAND LIMITED ; -850.00 EUR` | EU service route only if invoiced entity, Finnish place and buyer liability established. Check this point with one of our partner accountants. |
| `15.04.2026 ; RAVINTOLA NOKKA ; -220.00 EUR` | Purpose/rate/gross split unresolved; proved entertainment permits no VAT deduction, never the old 50%. Check this point with one of our partner accountants. |
| `18.04.2026 ; VERKKOKAUPPA.COM ; Laptop ; -1,595.00 EUR` | Invoice and use required; no invented net/gross or input VAT. Check this point with one of our partner accountants. |
| `22.04.2026 ; STUDIO KREBS GMBH ; +3,500.00 EUR` | Customer status, receiving establishment and invoice determine EU service route; amount alone is insufficient. Check this point with one of our partner accountants. |
| `28.04.2026 ; NESTE ; Fuel ; -80.00 EUR` | Vehicle class/use and invoice determine deduction; not a blanket business-fuel claim. Check this point with one of our partner accountants. |

## Ask the client first

- Legal entities, registration decisions/VAT IDs, supplying/receiving establishments and business/consumer status?
- Actual supply, contract, supply/advance dates, price basis, currency/euro conversion, invoices and credit notes?
- Goods dispatch, customs decision issue date and complete import-base evidence, including Åland?
- Current/preceding calendar-year turnover; allocated MyTax period, prior return and correction discovery date?
- Taxable/exempt/private purchase use, vehicle class/logs, construction buyer status and property-investment history?

## Sources

| Official source | Scope actually read | Read date |
|---|---|---|
| [VAT Act 1501/1993][law] | Finnish body: §§3–3a,8c–9,12,15,26c,27–44,63–67,69d,69m,70,72a–72b,73,78,84–85a,88,91,93,102–102a,114,117–118,120–121e,131,135a–143,145a,162,173–174,209e; distinguish displayed historical and 2027 text | 2026-11-27 |
| [Procedure Act 768/2016][procedure] | Finnish §§11–17,25,35–38: periods, deadline, corrections and sanction conditions | 2026-11-27 |
| [Vero rates][rates] | Finnish categories, exclusions and dated transitions | 2026-11-27 |
| [Vero return instructions][return] | Finnish fields, zero-rate/OSS reporting, deductions, no activity, deadlines, replacement/€500/3-year routes and relief abolition | 2026-11-27 |
| [Vero periods][period]; [small-business guidance][small] | Finnish period decisions/start-up exception; turnover, crossing, voluntary registration/deregistration and other-EU/non-EU boundaries | 2026-11-27 |
| [Vero vehicles][vehicles] | Finnish car exceptions, private use, logs, retention and subsequent correction | 2026-11-27 |
| [Vero Åland][aland]; [used goods §5.2][margin] | Finnish tax border/import issue-period transition; margin tax belongs in ordinary return | 2026-11-27 |
| [Vero interest][interest] | Finnish 2026 rate, actual-day and inclusive start/end rule | 2026-11-27 |

Not yet confirmed: full margin/travel/VAT-group/marketplace schemes, cross-border SME administration, exceptional exemptions and property-option/transfer applications, gifts/promotional-value rules, staff-meal own use, international passenger/freight zero-rating, gambling/postal and unusual sector classification, special import procedures/indirect representation, Intrastat, API/file specifications and all held invoice cases. **No usable conclusion is supplied for those points. Check this point with one of our partner accountants.**

Historical operational holds also preserve the subjects formerly asserted without proof: bank-specific CSV layouts/date conventions; Y-tunnus/VAT-ID example `1234567-8` / `FI12345678` (illustrations, not valid IDs); supplier-pattern defaults for banks/insurers/government/utilities/post/logistics/software/payment processors/professional services/food retailers/payroll/owner transfers/cash; merchant-based entity inference; risk thresholds €3,000/€200/>40%/>4/€5,000; promotional-gift amount about €50; Malta comparisons including €35,000 and movable-capital €1,160; EU comparison €85,000/€100,000. **These historical values confer no legal safe harbour or classification. Check this point with one of our partner accountants.** No tax rate, country, exemption or deduction may be inferred from those defaults.

[law]: https://www.finlex.fi/fi/lainsaadanto/1993/1501
[procedure]: https://www.finlex.fi/fi/lainsaadanto/2016/768
[rates]: https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/arvonlisaveroprosentit/
[return]: https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/
[period]: https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ilmoitus-ja-maksuohjeet/verokauden-muutos/
[small]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48658/arvonlisaveroton-vahainen-toiminta/
[vehicles]: https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ajoneuvon-ja-sen-kayttokulujen-arvonlisavero/
[aland]: https://www.vero.fi/yritykset-ja-yhteisot/verot-ja-maksut/arvonlisaverotus/ulkomaankauppa/maahantuonnin-arvonlisavero/ahvenanmaan-veroraja-ja-tavaroiden-maahantuonti/
[margin]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48682/kaytettyjen-tavaroiden-arvonlisaverotus3/
[interest]: https://www.vero.fi/henkiloasiakkaat/maksaminen/nain-maksat/viivastyskorko-kun-maksu-myohastyy/
