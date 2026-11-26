---
name: germany-vat-return
description: "Prepare a German 2026 advance VAT return under standard taxation: filing rhythm, extension and special prepayment, ordinary domestic supplies and foreign B2B services, input VAT, 2026 form boxes and conditional worked cases. Trigger on Umsatzsteuer-Voranmeldung, UStVA, Vorsteuer, Kennzahl, Dauerfristverlängerung or German VAT return. Specialist schemes, goods exemptions and disputed classifications require referral."
version: 2.8
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-26
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Germany: advance VAT return for 2026

> **General reference only.** This skill is tax reference material for AI-assisted work. It has not been reviewed for any specific business's facts. Do not rely on it to file, pay or take a position without a qualified professional checking it.

Use this ordinary-return method only after standard taxation and the actual transaction facts are established. It is not a filing method for every business. Keep the original transaction period: the worked cases below remain in 2026 and use the stated 2025 comparatives.

## The method, step by step

1. Read the business records first: actual filing period, prior returns, standard/small-business status, activity, establishments, invoices and extension/prepayment evidence. Obtain the full-period bank statement, sales and purchase registers, prior UStVA and BWA/EÜR where available. Reconcile gaps before asking for missing facts.
2. Match each payment to its underlying supply and invoice. Keep Buchungstag and Wertstellung/Valuta as bank fields, separately from supply, invoice and advance-payment dates. A brand, IBAN, SEPA code or bank booking does not settle VAT classification. Keep uncertain lines in a review schedule; do not turn an unknown supplier into non-EU reverse charge or an unchecked customer into a consumer.
3. Establish the place of supply, liability, rate, tax period and deduction entitlement before selecting a box. Use the ordinary service rules below only when all their conditions are established. Stop the affected treatment and use the specialist referral where they are not.
4. In the working paper, keep Transactions, Kz Summary and Return Form linked to the evidence. Recalculate formulas and reconcile the return totals; retain unresolved lines and the possible tax effect separately. Agree materiality and unusual-transaction review prompts with the reviewer. An incomplete bank-only working paper is not ready to file.

## Filing rhythm, deadline and extension

For ordinary businesses, the default period is the calendar quarter. Previous-calendar-year VAT above **EUR 9,000** requires monthly returns; at **EUR 2,000 or less** the tax office may grant release from advance returns and payments. Release is not automatic. These tests concern VAT, not turnover. [UStG § 18(2)](https://www.gesetze-im-internet.de/ustg_1980/__18.html).

A previous-year refund surplus above **EUR 9,000** permits election for monthly filing by submitting January's return by **10 February**; it binds for that calendar year. For ordinary start-ups in **2021–2026**, use annualised actual VAT where the preceding year was a part year, or expected current-year VAT where activity begins this year, instead of automatically imposing monthly filing. Shelf companies and acquired company shells have separate rules: Check this point with one of our partner accountants. [UStG § 18(2), (2a)](https://www.gesetze-im-internet.de/ustg_1980/__18.html).

File electronically through [ELSTER](https://www.elster.de) and pay by the **10th day after the period**. The tax office may waive electronic transmission on hardship application. A deadline ending on Saturday, Sunday or a statutory public holiday moves to the next working day. [UStG § 18(1)](https://www.gesetze-im-internet.de/ustg_1980/__18.html), [AO § 108(3)](https://www.gesetze-im-internet.de/ao_1977/__108.html).

Apply for the **one-month extension** by the original deadline of the first return it should cover; it extends both filing and payment. The tax office must refuse or revoke it if the tax claim appears endangered. Monthly filers must declare and pay a **special prepayment of 1/11 of the preceding year's advance payments**. For a preceding part year, annualise, counting started months as whole months; for a new business, use expected current-year advance payments. A quarterly filer has no special-prepayment condition under this rule. [UStDV §§ 46–48](https://www.gesetze-im-internet.de/ustdv_1980/__46.html), [§ 47](https://www.gesetze-im-internet.de/ustdv_1980/__47.html), [§ 48](https://www.gesetze-im-internet.de/ustdv_1980/__48.html).

For a continuing monthly extension, declare and pay the year's special prepayment by the statutory deadline for the first return, normally **10 February**, using USt 1 H. Calculate the prior-year base before deducting the prior special prepayment; if the calculation produces a refund surplus, enter zero. Credit the assessed special prepayment in the last period for which the extension applies, normally December. See the [2026 USt 5 E instructions, lines 8–9](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2) and [UStDV § 48](https://www.gesetze-im-internet.de/ustdv_1980/__48.html).

## Ordinary rates, services and input VAT

The standard rate is **19%** for taxable supplies unless another rate or exemption applies. Restaurant and catering services excluding drinks are **7% from 1 January 2026**; drinks remain at the standard rate. For a qualifying combined food-and-drinks price, the BMF accepts **30% of the package price** as the drinks share. [UStG § 12(1), (2) no. 15](https://www.gesetze-im-internet.de/ustg_1980/__12.html), [BMF, 22 December 2025, UStAE 10.1(12) and commencement](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2025-12-22-verpflegungsdienstleistungen.pdf?__blob=publicationFile&v=5).

For an ordinary **§ 3a(2) B2B service**, the place is where the customer operates its business, or its receiving establishment. This rule is expressly subject to § 3a(3)–(8), §§ 3b and 3e. Property, catering/on-board services, transport hire and event admission/virtual participation require classification first: Check this point with one of our partner accountants. [UStG § 3a(2)](https://www.gesetze-im-internet.de/ustg_1980/__3a.html).

For an ordinary taxable service received in Germany from a supplier established in another EU state, **§ 13b(1)** creates reverse-charge tax at the end of the period when the service is performed. For a non-EU supplier's ordinary service within **§ 13b(2) no. 1**, tax arises on invoicing, no later than the end of the following calendar month. A business or legal-person recipient owes the tax for these branches. Confirm supplier establishment under § 13b(7), including whether a German establishment participates; use the actual supply date. Advance payments, continuous services exceeding a year and § 13b(6) excluded services are separate cases: Check this point with one of our partner accountants. [UStG § 13b(1)–(7)](https://www.gesetze-im-internet.de/ustg_1980/__13b.html).

For completed supplies for the business, ordinary invoice input VAT is the **legally owed German VAT**, with a compliant §§ 14/14a invoice held. Advance-payment deductions additionally require payment. An item used less than **10%** for the business fails the statutory business-use test. Reverse-charge VAT on services performed for the business is deductible under § 15(1) no. 4, subject to the deduction restrictions; it is not automatically deductible merely because it is owed. This method assumes no restriction or apportionment under § 15(1a)–(4b). If that assumption is not evidenced, use the referral below. [UStG § 15](https://www.gesetze-im-internet.de/ustg_1980/__15.html).

A § 3a(2) service performed in another EU state for a customer established there who owes that state's VAT is reported in **Kz 21 in the period of performance**, including any advances in that total. For a standard-taxed supplier with service-only ZM reporting who does not qualify for the annual-release route, report it to BZSt by the **25th day after the quarter** of performance, with the customer's VAT ID and amount. Monthly goods reporters include services in the last month's ZM of the quarter or elect to include them monthly after notifying BZSt; the annual-release route is referred below. [UStG § 18b](https://www.gesetze-im-internet.de/ustg_1980/__18b.html), [§ 18a(2), (3), (7), (8)](https://www.gesetze-im-internet.de/ustg_1980/__18a.html), [2026 instructions, line 35](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2). Cross-border invoice particulars, issue deadline and self-billing exceptions: Check this point with one of our partner accountants.

## The 2026 boxes and calculation

This is the ordinary-service subset of [USt 1 A / USt 1 E for 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2), not an entitlement test. Establish tax treatment first.

| Line | Kz | Entry after eligibility is established |
|---|---|---|
| 13 | 81 | Taxable supplies at 19%, net base |
| 14 | 86 | Taxable supplies at 7%, net base |
| 30 | 46 / 47 | § 13b(1) EU services: base / tax |
| 32 | 84 / 85 | Other § 13b(2) no. 1, 2, 4–12 supplies: base / tax; includes qualifying non-EU services |
| 35 | 21 | § 18b sentence 1 no. 2 services |
| 38 | 66 | Ordinary invoice input VAT under § 15(1) no. 1 |
| 41 | 67 | Deductible § 13b input VAT |
| 49 | 39 | Assessed special-prepayment credit in the applicable last period |
| 50 | 83 | Remaining amount payable; enter a minus sign for a surplus; always complete |

Line 37 sums tax in lines 13–18 and 25–32. Deduct lines 38–44 to reach line 45; add other tax amounts in lines 46–47 to reach line 48; deduct the applicable line 49 credit to reach line 50. Kz 65 is not the net amount payable. Enter bases in whole euros and VAT/input VAT with cents. The precise handling of fractional-euro bases needs the applicable filing instruction: Check this point with one of our partner accountants. Do not invent a rounding rule.

## Late payment

For tax self-assessed or assessed and unpaid by the due date, the surcharge is **1% per started month**, on overdue tax rounded down to the next multiple of **EUR 50**. It does not start before assessment/self-assessment. No surcharge is collected for lateness up to **3 days**, except cash/cheque payments under § 224(2) no. 1 AO. Bank transfers count when credited to the authority. [AO § 240](https://www.gesetze-im-internet.de/ao_1977/__240.html), [§ 224(2)](https://www.gesetze-im-internet.de/ao_1977/__224.html).

## Worked examples

### Example 1: An IT consultant's monthly return, with a late payment

Sources: the ordinary rate, reverse-charge, deduction, form and late-payment rules above apply to the stipulated facts.

Anna is a freelance IT consultant in Berlin on standard taxation. Her 2025 VAT was above EUR 9,000, so she files monthly in 2026 without an extension. For March 2026 she has the following completed supplies. Assume the consultancy, software and advertising are ordinary § 3a(2) business services, received at the stated business establishments; the foreign suppliers meet § 13b(7), with no participating German establishment. All relevant invoices are issued in March, there are no advance payments or special timing cases, and all purchases serve activities carrying full input deduction with no § 15 restrictions. The French customer is a business receiving the consultancy in France and owes French VAT; its VAT ID is evidenced. These are conditions of the example, not facts inferred from a bank description:
- fees from German clients of EUR 20,000 net, at 19%: EUR 3,800 VAT, Kz 81;
- fees from a French company of EUR 5,000 for consulting: not taxable in Germany, Kz 21 and the recapitulative statement, no VAT;
- German purchase invoices showing EUR 1,140 VAT: Kz 66;
- a US software subscription of EUR 200 billed by the US entity: Kz 84 EUR 200, Kz 85 EUR 38;
- online advertising of EUR 1,000 billed by an Irish company: Kz 46 EUR 1,000, Kz 47 EUR 190.

The reverse-charge tax of EUR 228 is also her input VAT in Kz 67. Output VAT is EUR 4,028, input VAT EUR 1,368, so Kz 83 is EUR 2,660. The return and payment are due Friday 10 April 2026. Assume she filed and self-assessed the tax by the due date. Her transfer reaches the tax office on Tuesday 14 April, 4 days late, past the 3-day grace period. The surcharge is 1% of EUR 2,650 (EUR 2,660 rounded down to a multiple of 50) for one started month: EUR 26.50.

```oa-check
name: IT consultant, March 2026 advance return with reverse charge and a late payment
inputs:
  domestic_net: 20000
  eu_service_sale: 5000
  domestic_input_vat: 1140
  non_eu_software: 200
  eu_advertising: 1000
  standard_rate: 19
  months_late: 1
steps:
  - kz81_tax: pct(domestic_net, standard_rate)
  - kz85_tax: pct(non_eu_software, standard_rate)
  - kz47_tax: pct(eu_advertising, standard_rate)
  - output_vat_line37: kz81_tax + kz85_tax + kz47_tax
  - kz67_input: kz85_tax + kz47_tax
  - input_vat_total: domestic_input_vat + kz67_input
  - kz83: output_vat_line37 - input_vat_total
  - overdue_rounded: floor(kz83 / 50) * 50
  - late_payment_surcharge: pct(overdue_rounded, 1) * months_late
expected:
  kz81_tax: 3800
  kz85_tax: 38
  kz47_tax: 190
  output_vat_line37: 4028
  kz67_input: 228
  input_vat_total: 1368
  kz83: 2660
  overdue_rounded: 2650
  late_payment_surcharge: 26.50
```

### Example 2: A restaurant's December return, buffet at two rates and the special prepayment

Sources: the restaurant rate, package allocation, special-prepayment and form rules above apply to the stipulated facts.

A restaurant GmbH, already trading throughout 2025, files monthly with the one-month extension. Assume ordinary taxable German restaurant services, a qualifying combined food-and-drinks price, lawful invoices and full input deduction without exclusions; there are no other transactions, tax adjustments or prepayments in December. Its 2025 advance returns showed Kz 83 amounts of EUR 61,000 in total, and its 2025 special prepayment of EUR 5,000 was credited in December 2025. The base for 2026 is EUR 66,000, so the 2026 special prepayment is EUR 6,000, declared on form USt 1 H and paid by 10 February 2026.

In December 2026 it sells only buffet packages, food and drinks for one price, for EUR 127,330 gross. Using the 30% drinks share (UStAE 10.1(12)), EUR 38,199 is drinks at 19% (net EUR 32,100, VAT EUR 6,099, Kz 81) and EUR 89,131 is food at 7% (net EUR 83,300, VAT EUR 5,831, Kz 86). Output VAT is EUR 11,930. Input VAT on invoices is EUR 4,200 (Kz 66), leaving EUR 7,730 in line 48. December is the last period, so the EUR 6,000 special prepayment is credited in Kz 39, and Kz 83 is EUR 1,730. With the extension it is due 10 February 2027. Had the whole price been taxed at 19%, in a purely mathematical comparison, output VAT would have been EUR 20,330.

```oa-check
name: Restaurant, December 2026 return with a 30% drinks share and the special prepayment credit
inputs:
  kz83_2025_total: 61000
  svz_2025: 5000
  package_gross: 127330
  drinks_share_pct: 30
  input_vat: 4200
steps:
  - svz_base: kz83_2025_total + svz_2025
  - svz_2026: svz_base / 11
  - drinks_gross: pct(package_gross, drinks_share_pct)
  - food_gross: package_gross - drinks_gross
  - drinks_net_kz81: drinks_gross * 100 / 119
  - food_net_kz86: food_gross * 100 / 107
  - drinks_vat: drinks_gross - drinks_net_kz81
  - food_vat: food_gross - food_net_kz86
  - output_vat: drinks_vat + food_vat
  - line48: output_vat - input_vat
  - kz83_december: line48 - svz_2026
  - output_vat_all_at_19: package_gross * 19 / 119
expected:
  svz_base: 66000
  svz_2026: 6000
  drinks_gross: 38199
  food_gross: 89131
  drinks_net_kz81: 32100
  food_net_kz86: 83300
  drinks_vat: 6099
  food_vat: 5831
  output_vat: 11930
  line48: 7730
  kz83_december: 1730
  output_vat_all_at_19: 20330
```

## Earlier transaction cases: preserve the original periods

These six historical cases remain hypothetical. Debit amounts are shown as positive costs here, preserving the original statement amounts and dates. A payment date alone does not decide the return period. The conditions below must be evidenced before a tax result is used.

- **5 April 2026, OpenAI software, EUR 23.78 debit.** If the actual invoice establishes a US supplier satisfying § 13b(7), an ordinary § 3a(2) business service, a net price of EUR 23.78 with no supplier VAT, April performance/invoicing and unrestricted input deduction, reverse-charge tax is EUR 23.78 × 19% = **EUR 4.52**, with the same deductible input tax. Use the line 32 / Kz 67 route, subject to the form's base-entry requirement. The statement's brand is not proof of these conditions.
- **10 April 2026, Google Ads, EUR 1,200 debit.** If the invoice establishes an Irish supplier within § 13b(1), an ordinary German-received B2B advertising service performed in April and full input deduction, reverse-charge tax is **EUR 228**, also deductible: Kz 46/47/67. The IE IBAN alone does not prove establishment.
- **15 April 2026, Restaurant zum Goldenen Hirsch, EUR 285.60 debit.** The receipt, business purpose, guests and food/drinks split are not established. Do not extract a single VAT amount from the bank total. Check this point with one of our partner accountants.
- **18 April 2026, Deutsche Telekom, EUR 59.95 debit.** If a valid domestic invoice establishes a completed ordinary 19% business service with full input deduction, gross EUR 59.95 gives net **EUR 50.38** and input VAT **EUR 9.57**, Kz 66. Without those facts the calculation is illustrative only.
- **22 April 2026, Kreativ Digital GmbH Wien, EUR 4,500 credit for March IT consulting, invoice RE-2026-042.** If ordinary § 3a(2) consultancy was received at the Austrian customer's Austrian business in March, and the evidenced business customer owes Austrian VAT, German VAT is **zero**, with **EUR 4,500 in March Kz 21**, not April merely because payment arrived then. Include it in the ZM for the performance period under the rules above. An AT IBAN or company name alone is insufficient.
- **30 April 2026, Sparkasse account fee labelled Q2/2026, EUR 12.90 debit; Allianz insurance, EUR 89.50 debit.** The contract/service and actual exemption or VAT treatment must be established. Do not exclude solely by bank or insurer name. Check this point with one of our partner accountants.

```oa-check
name: Earlier conditional German service cases, April bank entries and March consultancy
inputs:
  us_software_net: 23.78
  eu_advertising_net: 1200
  telecom_gross: 59.95
  austrian_consulting: 4500
  standard_rate: 19
steps:
  - us_reverse_charge: pct(us_software_net, standard_rate)
  - eu_reverse_charge: pct(eu_advertising_net, standard_rate)
  - telecom_net: telecom_gross * 100 / (100 + standard_rate)
  - telecom_input_vat: telecom_gross - telecom_net
  - german_vat_austrian_consultancy: austrian_consulting * 0
expected:
  us_reverse_charge: 4.52
  eu_reverse_charge: 228
  telecom_net: 50.38
  telecom_input_vat: 9.57
  german_vat_austrian_consultancy: 0
```

## Specialist topics and missing facts

The following topics remain in scope as handoffs. No tax outcome is supplied for them here.

- **Small businesses:** § 19 domestic and EU-wide scheme, turnover definition, start-up/crossing transaction, waiver/binding period, new vehicles and reverse-charge/acquisition filing duties. Check this point with one of our partner accountants.
- **Other reduced-rate classifications:** Annex 2 food, books/e-publications, water/prepackaging, flowers/plants; dental technicians, cultural admissions, hotels/camping with breakfast/parking/internet packages and passenger transport. Check this point with one of our partner accountants.
- **Solar:** operator/recipient, building and registered capacity conditions, components/storage, installation, acquisition/import and deduction. Check this point with one of our partner accountants.
- **Special regimes:** farming/forestry, VAT groups/Organschaft, travel agents, margin schemes, cash accounting and partial exemption. Check this point with one of our partner accountants.
- **Private use:** withdrawals, free services, vehicles/fuel, allocation, home-office/rent/utilities and deemed-supply bases/correction periods. Check this point with one of our partner accountants.
- **Restricted input tax:** exempt domestic/foreign activity and exceptions, mixed use/apportionment, gifts/recipient/year test, hunting/yachts/private living costs, reasonable evidenced entertainment, income-tax distinction, restaurant evidence/machine receipt/signature and incomplete invoices or small-amount invoice relief. Check this point with one of our partner accountants.
- **Foreign VAT:** invoice correction, actual legality/recoverability, refund eligibility and cost versus receivable treatment. Check this point with one of our partner accountants.
- **Foreign currency:** BMF monthly rates, advances, cash-accounting month, permitted daily rates and separate OSS rules. Check this point with one of our partner accountants.
- **Goods:** intra-EU exemption and actual VAT ID used, customer/acquisition conditions, ZM accuracy/correction, transport proof, independent evidence classes, arrival confirmation, presumption/rebuttal/fallback and customer-misinformation protection; exports, EU acquisitions, import VAT and new vehicles. Check this point with one of our partner accountants.
- **Domestic reverse charge:** construction/cleaning customer status, collateral, property transactions, gas/electricity/reseller gates, allowances/certificates, scrap/gold, phones/tablets/consoles/chips, Annex 4 metals, value tests and later price reductions, telecommunications and margin-scheme exclusions. Check this point with one of our partner accountants.
- **ZM alternatives:** goods/triangular reporting, monthly versus quarterly thresholds and crossing month, annual release/turnover tests and exclusions. Check this point with one of our partner accountants.
- **EU consumers and OSS:** distance sales and telecom/broadcast/e-services, establishment/combined threshold, waiver and reporting exclusions from the ordinary return. Check this point with one of our partner accountants.
- **Foreign businesses:** registration, competent tax office by country, reverse-charge/OSS exceptions and special input-tax refunds. Check this point with one of our partner accountants.
- **Annual return:** USt 2 A, reconciliation, ordinary/adviser/early-request deadlines, shorter periods and balance-payment dates. Check this point with one of our partner accountants.
- **Other sanctions:** discretionary advance-return/special-prepayment late filing, annual-return surcharge/formula/cap/exceptions, annual-assessment interest and fines. Check this point with one of our partner accountants.
- **E-invoices:** receiving, domestic issue duty/exclusions, formats, consent, transition/EDI, small invoices, small businesses, travel tickets and archiving. Check this point with one of our partner accountants.
- **Other form boxes:** 87, 35/36, 77, 76/80, 44/49, 41/43/48, 91, 89/93/90, 95/98, 94/96, 73/74, 42, 60, 45, 61/62/63/59/64, 65/69 and correction information 50/37. The official form is the destination for placement; entitlement and tax calculation need the underlying rule. Check this point with one of our partner accountants.
- **Corrections:** price changes, bad debts, recovery, rebates, credit notes, Gutschrift/self-billing, tax wrongly shown and input corrections. Check this point with one of our partner accountants.

## Bank review and companion guides

Use names and descriptions only to find documents: banks/payment processors and interest/loan/insurance charges; tax office/customs/IHK/HWK/broadcasting; utilities/telecoms; transport; food/supermarkets; rent; EU/non-EU software/advertising; professional services; payroll/social security; own-account movements, capital, loans and cash withdrawals. For mixed billing brands, Amazon purchases, restaurant payments, cars/home office or round-number transfers, obtain the invoice, purpose and actual parties. Keep signed amounts and reconcile both sides of internal transfers. No merchant dictionary or default replaces that evidence.

Before handoff, record standard versus § 19 status, 2025/current-2026 turnover, activity/legal form/establishments, staff, exempt supplies, Soll/Ist status, periodicity/extension/prepayment, foreign suppliers' billing entities, customers' business/VAT-ID evidence, restaurant package splits, solar facts and goods proof. Ask only for facts absent from the records. For bank-only inputs, missing invoices or material inconsistencies, keep the affected return on hold.

Companions: [annual return and special schemes](de-vat-annual-and-special-schemes.md), [e-invoicing](germany-einvoice.md), [income tax](germany-income-tax.md), [freelancer income tax](de-einkommensteuer-freelancer.md); `vat-workflow-base` for the working-paper workflow and `eu-vat-directive` for EU context. These links do not establish eligibility or current legal proof by themselves.

## Sources

Read on 26 November 2026: the cited operative sections of UStG §§ 12, 13b, 15, 18, 3a, 18a and 18b; UStDV §§ 46–48; AO §§ 108, 224 and 240; BMF restaurant letter of 22 December 2025; and the 2026 USt 1 A, USt 1 E and USt 5 E forms/instructions of 29 December 2025. Principal source texts: [UStG § 18](https://www.gesetze-im-internet.de/ustg_1980/__18.html), [UStG § 12](https://www.gesetze-im-internet.de/ustg_1980/__12.html), [2026 BMF forms and instructions](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2). Further links are beside the rules above. Existing official captures were reused only for these same German rules and 2026 forms; specialist referrals make no retained tax determination.
