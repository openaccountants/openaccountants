---
name: slovakia-vat-return
description: "Slovak VAT (DPH) for tax year 2026 under Act No. 222/2004 Coll. as in force from 1 January 2026: the 23% standard rate, the 19% rate (most food, electricity, non-alcoholic drinks served in restaurants), the 5% rate (basic food, medicines, books, restaurant meals, accommodation, sports and fitness entry), the foods moved from 19% to 23% in 2026, the monthly or quarterly return and control statement due 25 days after the period, refunds, domestic reverse charge, the 50% cap on passenger car input VAT, the EU SME scheme, fines and late-payment interest. Trigger on: Slovak VAT return, DPH priznanie, kontrolny vykaz, suhrnny vykaz, nadmerny odpocet, prenesenie danovej povinnosti, Slovakia 23% VAT. Out of scope: which registration a client needs (slovakia-vat-registration-4-7-7a), income tax (slovakia-pit, sk-corporate-income-tax), payroll (sk-payroll-social)."
version: 2.2
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia VAT return (2026)

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

This skill covers the Slovak VAT return for a business registered in Slovakia for 2026: rates, what goes into the return, the control statement, the EC sales list, refunds, penalties and interest. Every figure is taken from Act No. 222/2004 Coll. on VAT (the "VAT Act") in the version in force from 1 January 2026 to 31 December 2026, and from Act No. 563/2009 Coll. (the Tax Procedure Code). It links to the other Slovakia skills and does not repeat them:

- [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md): whether a client must register under § 4, § 7 or § 7a, the EUR 50,000 and EUR 62,500 turnover tests, and what a § 7 or § 7a registrant may not deduct.
- [slovakia-pit](slovakia-pit.md) and [sk-corporate-income-tax](sk-corporate-income-tax.md): income tax of individuals and companies.
- EU rules on place of supply, intra-EU supplies and OSS are in [eu-vat-directive](../eu/eu-vat-directive.md); the general return workflow is in [vat-workflow-base](../../foundation/vat-workflow-base.md).

## Who this applies to

- **VAT payers (platitel) under § 4.** A taxable person with its seat, place of business or fixed establishment in Slovakia (or, failing that, its residence or usual abode there) becomes a payer from 1 January of the year after its turnover passed EUR 50,000, or at the supply that takes turnover in the current year past EUR 62,500 (VAT Act § 4(1)(a) and (b)). Voluntary registration is allowed (§ 4(6) and (7)). The registration tests sit in the sibling skill.
- **Foreign persons registered under § 5.** A business with no seat, place of business, establishment or residence in Slovakia becomes a payer from its first taxable supply in Slovakia, unless all its Slovak supplies fall in the § 5(2) list (for example supplies where the customer accounts for the tax, or supplies covered by OSS). It applies to the Bratislava Tax Office within five working days (§ 5(1) to (3)).
- **Persons who are not payers but owe tax under § 69.** Someone registered only under § 7 or § 7a, or not registered at all, who receives a reverse-charge supply files a return only for the month the liability arose, and does not pay if the tax is EUR 5 or less (§ 78(3)).
- **Out:** a business below the § 4 thresholds that is not a payer charges no VAT and files no periodic VAT return. It must still check § 7 and § 7a.

**Group payer.** A qualifying Slovak VAT group is one taxable person: members must be financially, economically and organisationally linked under § 4a, and the group becomes a payer on registration under § 4b. Its representative acts for the group and members have joint and several liability. Use the group's VAT number and registration decision for the return; a voluntary ordinary registration is under § 4, not § 4a ([VAT Act §§ 4a–4b](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-4a)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate | 23% (since 1 January 2025) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(1)) |
| Reduced rate, goods in Annex 7 point 1: food for human consumption not in point 2, bottled drinking water without sugar or flavouring (not mains water), salt, electricity | 19% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf (§ 27(2)(a)) |
| Reduced rate, Annex 7a point 1: drinks served as restaurant and catering services (CPA 56), except alcoholic drinks over 0.5% alcohol | 19% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf (§ 27(2)(b)) |
| Reduced rate, Annex 7 points 2 and 3: listed fresh meat, freshwater fish, milk, yoghurt, butter, honey, fresh vegetables, apples and pears, fresh bread and rolls, juices with at most 5 g added sugar per 100 ml, medicines (chapter 30), listed medical aids, printed books, newspapers and periodicals (advertising at most 50%) | 5% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf (§ 27(3)(a)) |
| Reduced rate, Annex 7a point 2: accommodation (CPA 55), food served as restaurant and catering services (CPA 56), online books and audio books, entry to theatre, opera, ballet and similar events, museums, sports events, fitness centres | 5% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf (§ 27(3)(b)) |
| Reduced rate, registered social enterprises using 100% of after-tax profit for their main aim; state-supported rental housing | 5% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(3)(c) to (e)) |
| Foods moved from 19% to 23% on 1 January 2026 (Acts 261/2025 and 385/2025): mainly sweets, cakes, jams, ice cream, muesli, sweetened soft drinks, salty snacks; listed dietetic foods stay at 19% | 23% | 2026 | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/sadzby-dane |
| Imported goods declared under the § 68cb low-value scheme | Not covered by § 27(2)(a) or (3)(a), so 23% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(2)(a), (3)(a)) |
| Rate used when rates change | Rate in force on the day the tax liability arises | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(5)) |
| Registration turnover, payer from 1 January of the next year | Over EUR 50,000 in the calendar year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 4(1)(a)) |
| Registration turnover, payer at the supply that crosses it | Over EUR 62,500 in the current calendar year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 4(1)(b)) |
| Quarterly tax period allowed | More than 12 months since the end of the month of registration, and turnover under EUR 100,000 in the preceding 12 months | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 77(2)) |
| Passenger cars (M1, L1e, L3e) acquired, leased long term or run from 1 January 2026 to 30 June 2028 | 50% of input VAT deductible, unless an exception applies | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 85n(1) to (5)) |
| Domestic reverse charge on mobile phones and integrated circuits | Invoice tax base EUR 5,000 or more | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 69(12)(h), (i)) |
| Control statement, simplified invoices listed by supplier | When deducted VAT on simplified invoices in the period is EUR 3,000 or more | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 78a(6)) |
| EC sales list may be quarterly | Goods in § 80(1)(a) to (c) at or under EUR 50,000 in the quarter and in the four previous quarters | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 80(2)) |
| Fast refund condition: tax, customs and insurance arrears in the last 6 months | Not more than EUR 1,000 in total | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 79(2)(c)) |
| Non-payer owing reverse-charge tax: no payment due | Tax of EUR 5 or less | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 78(3)) |
| EU SME scheme, Slovak business exempt in other member states | EU turnover not over EUR 100,000 in the current and the previous calendar year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 68g(1)) |
| EU SME scheme, business from another member state exempt in Slovakia | Slovak turnover not over EUR 62,500 this year and EUR 50,000 last year; EU turnover not over EUR 100,000 in both years | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 68f(1)) |

**Historical corrections.** For a correction, use the rate applicable to the original taxable transaction under § 25(7). For example, the January 2024 law had a 20% standard rate and a 10% reduced rate for its listed supplies, alongside a separate 5% route. Those are historical rates, not alternatives for a 2026 supply. Establish the actual original date and category rather than applying today's rate to every credit note ([current § 25(7)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-25); [January 2024 § 27](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20240101.html#paragraf-27)).

## The taxable base

- **Output tax.** Tax is charged on domestic supplies at the rate in force on the day the liability arises. The return also carries the tax the payer self-assesses as customer: intra-EU acquisitions of goods, services from foreign persons under § 69(3), and domestic reverse-charge supplies under § 69(12).
- **Domestic reverse charge (§ 69(12)).** Applies only when both supplier and customer are payers registered under § 4, § 4b, § 4c or § 5. It covers metal waste and scrap; greenhouse gas emission allowances; real estate the supplier has opted to tax under § 38(8); real estate sold in a forced sale; goods supplied when a security is enforced; cereals and oilseeds in chapters 10 and 12 not normally sold for final consumption; iron and steel in chapter 72 and headings 7301, 7308 and 7314; mobile phones and integrated circuits where the invoice tax base is EUR 5,000 or more; and construction work in section F of the classification, including goods supplied with installation in section F. The supplier invoices without VAT. The customer declares the tax and, if entitled, deducts it.
- **Input tax.** A payer deducts tax on purchases used for taxable supplies. There is no deduction for hospitality and entertainment (§ 49(7)(a)). Where purchases serve both taxable and exempt supplies, the deductible share follows the coefficient in § 50.
- **Passenger cars from 1 January 2026 (§ 85n).** For an M1 car, or an L1e or L3e motorcycle, acquired as a long-term asset, leased on a contract that is not short-term, or for goods and services bought to run one, from 1 January 2026 to 30 June 2028, the payer deducts 50%. Private use then counts as neither a supply of services nor a supply of goods. The cap does not apply to vehicles used only for car rental, paid passenger transport including taxis, driving schools, or as demonstration or courtesy cars (§ 85n(4)). It also does not apply where the vehicle is used only for business and the payer keeps electronic records for each vehicle: VIN, registration number, odometer readings at the start, at each period end and at the end, and a log of every trip with the driver, date and time, business purpose, start and end place and kilometres (§ 85n(5) and (6)). The payer must notify the tax office of a § 85n(4) or (5) use by the return deadline for the period of the first deduction. That notice is not needed for vehicles acquired by 31 December 2025 (§ 85n(9)).
- **Excess deduction (nadmerny odpocet).** If deductible tax is more than tax due, the excess is first set against the next period's liability. Any part not used is refunded within 30 days of filing the next period's return (§ 79(1)). A monthly payer registered at least 12 months, with arrears of not more than EUR 1,000 in the last 6 months, can mark the return and be refunded within 30 days of the return deadline for the period itself (§ 79(2) and (3)). The refund clock stops while a request to fix the return or control statement is open (§ 79(4)).
- **Rounding.** Figures in the return are rounded to the nearest euro cent, with 0.005 rounded up (§ 78(7)).

**Mixed taxable/exempt inputs: § 50 coefficient.** First attribute each purchase to its actual use: eligible inputs exclusively serving supplies with a deduction right are deductible under the ordinary rules; inputs exclusively serving no-credit exempt supplies are not. Apply the coefficient only to common inputs serving both, after the applicable business/private-use and statutory deduction restrictions. Do not reduce every input merely because the business also makes an exempt supply ([§ 49(3)–(6)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-49); [Financial Administration, direct attribution and proportional deduction](https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/odpocitanie-dane)).

For a positive denominator, let `N` be the VAT-exclusive value of annual supplies carrying a deduction right and `D` the VAT-exclusive value of all annual supplies, after the following exclusions. Include supplies whose place is outside Slovakia, classifying them by their actual deduction entitlement under § 49(6); overseas location alone neither excludes them nor creates a deduction right. Exclude from **both N and D** a business/independent-business-part transfer, sales of assets used in the business other than inventory, occasional exempt financial services under § 39, and occasional property transfers/lettings. Ordinary recurring financial services/property letting are not excluded merely because of their category. Compute `k=ceil(100×N/D)/100`, rounding the **coefficient upward to two decimals**, then multiply eligible common input VAT by k. An exact0.95 stays0.95;0.9501 gives0.96;0.9901 gives1.00 through the ordinary rounding rule. Do not substitute the old unsupported95%-means-full-deduction shortcut ([§ 50(1)–(2)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-50)).

During the year use the previous year's coefficient. If it cannot be used, estimate a coefficient from the activity's nature **with the tax administrator's consent**. After year end calculate the coefficient from the completed year's actual values, recompute the annual deductible common-input VAT, and settle the difference from deductions already taken in the **last tax period of that year**, increasing or decreasing deduction as appropriate. Apply the same reconciliation for the part of a year during which a business became or ceased to be a payer. Where the accounting period is a financial year, that financial year replaces calendar year for these calculations ([§ 50(3)–(5)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-50)).

For example, suppose the prior coefficient is0.60, the year's eligible common input VAT is23,000, and the year's included supplies are240,000 with deduction rights and120,000 without. A separate50,000 disposal of a used business asset is excluded from both values. `N=240,000`, `D=360,000`, so the final coefficient is0.67 and annual common deduction15,410. If13,800 was deducted using0.60, increase deduction by1,610 in the last period. Separately attributable eligible input VAT is added in full; blocked/exclusively no-credit input is not added. In a separate case, suppose the provisional coefficient was0.67 and15,410 was actually deducted during the year on23,000 common VAT. If that case's supported final coefficient is0.61, the annual deduction is14,030: reduce the provisional15,410 deduction by1,380. These are illustrative exact-cent inputs, not a return-row mapping.


**Classify the underlying supply.** Salary payments for dependent employment and ordinary remittances of tax/social contributions, loan principal and profit distributions are not, merely because money moves, consideration for the business's taxable supply. Identify any underlying goods or service before entering output or input tax. A bank charge requires classification of the actual bank service under § 39; do not label every bank fee outside VAT ([§§ 2–3](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-2), [§ 39](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-39)).

**Domestic exemption catalogue.** In addition to insurance/financial services and the property rules, check the actual statutory exemption before treating a supply as exempt without input recovery: universal postal services and related goods under § 28; qualifying healthcare under § 29, which expressly does not exempt sales of medicines/medical aids; education meeting § 31's provider/legal conditions; and licensed lotteries/gambling under § 41. Not every courier, training course or health-related sale qualifies. Apply § 49(3) to the associated inputs rather than importing the deduction rights of exports or intra-EU supplies ([§§ 28–41/49](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-28)).

**Transfer of a business.** A transfer or contribution of an enterprise, or a part forming an independent organisational unit, is outside the goods/services supply rules under § 10(1) if the acquirer is or becomes a payer under § 4(1)(d), subject to § 10(2)'s predominantly exempt acquirer exception and its exception for a predominantly exempt transferor. Do not enter it as an ordinary exempt sale without checking those conditions ([§ 10](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-10)).

**Private use and business gifts.** Subject to the specific § 85n vehicle treatment already described, withdrawal of goods for private use or free disposal can be a deemed taxable supply where input tax on the goods or their components was wholly or partly deducted. Business-purpose gifts with a value no greater than 17 euros excluding VAT per item, and business samples, are excluded from that deemed-goods-supply rule. Private use/free services have the separate § 9(2)–(3) rules. Business gifts are not a separate blanket deduction block in § 49(7): establish business use, apply the hospitality/entertainment block where it actually applies, and then check any deemed output tax ([§§ 8(3)/9](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-8), [§ 49](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-49)).

**Capital-goods register.** Separate resale inventory from long-term business assets. Under § 52a/54, the adjustment period includes the first-use year and is five calendar years for qualifying movable assets, and 20 calendar years for the listed property/building categories. The statutory investment-asset definition includes individually functioning movable items costing more than 1,700 euros excluding VAT, and the property categories in § 54(2)(b)–(c). Record original input VAT, initial deduction, first-use year and changes between taxable/exempt or business/private use. Apply § 54 for changed deduction entitlement and § 54a/54d for changed business/private use; perform the applicable adjustment in the final tax period of the year using Annex 1. For a non-calendar accounting year, § 52a(3) substitutes that accounting year. For assets whose adjustment period began by 31 December 2024, § 85kp(2) preserves the pre-2025 § 54/54a/54d and Annex 1 rules; check that transition before applying the current first-use method. The specific § 85n vehicle override still applies ([§ 52a](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-52a), [§§ 54–54d/85kp](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-54)).

**Credit notes.** Cancellation, returned goods and later price decreases/increases require the § 25 tax-base correction, subject to its specific exceptions. Under § 25(6), a post-liability price reduction to another payer can be left uncorrected for tax-base/tax purposes if both parties agree in writing; do not extend this exception to cancellations or price increases generally. A supplier reports the difference in the period the correction document is issued; a reverse-charge customer reports in the period it receives that document, subject to the statutory no-document rule. A customer that previously deducted input tax must reduce it when the base falls under § 53(1)(a); use the period of receipt or, if no document arrives within 30 days of the relevant event, the period in which those 30 days expire under § 53(2)(a). Correct the linked self-assessed output tax where the recipient was liable. Use the original transaction's rate under § 25(7), not a blanket reversal in the original return ([§ 25](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-25), [§ 53(1)–(2)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-53)).

**Older office/property sale.** A sale of a building or qualifying part with its building land is exempt after the five-year test in § 38(1)/(7). That clock refers to first permitted/actual use, whichever is earlier, and can restart after the specified substantial works, including the 40% cost tests. An office sold six years after its relevant first-use event, without an intervening event restarting that clock, therefore meets the age condition. A payer can elect to tax an otherwise exempt qualifying non-residential sale under § 38(8); the election is barred for the listed residential categories. If the taxable sale falls under § 69(12)(c) between the prescribed registered payers, the buyer accounts for VAT. Do not invent a general buyer-consent condition absent from those provisions ([§ 38](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-38), [§ 69(12)(c)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-69)).

**Vehicle boundaries.** N1 vans and N2+ trucks are outside § 85n's defined M1/L1e/L3e class. That removes the special 50% rule, but does not establish unrestricted deduction for private use or exempt activities: apply § 49's ordinary business-use and deduction conditions. For diesel 200 euros plus 46 euros VAT used wholly for taxable business in an N1 delivery van, 46 euros is deductible. The § 85n(1) acquisition cap concerns assets acquired from 1 January 2026; do not retrospectively halve an acquisition deduction merely because a pre-2026 car remains in use. Equally, pre-2026 acquisition did not itself guarantee 100% recovery. For mixed-use running goods/services bought during 1 January 2026–30 June 2028, § 85n(3) applies even when the car was acquired earlier; the notification exception for pre-2026 vehicles in § 85n(9) does not exempt those running costs from the substantive rule ([§ 49](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-49), [§ 85n(1)/(3)/(9)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-85n)).

**Refund offsets and audited refunds.** Refunds remain subject to application against tax arrears under Tax Procedure Code § 79(1)/(7) and § 55(6)–(7); the old 10 euro minimum was not the statutory VAT rule. The Code's refund provision applies appropriately to excess VAT and uses a greater-than 5 euro cash-refund threshold under § 79(2)/(7). If an audit begins within the statutory refund window, VAT Act § 79(6) returns the amount established by the audit within 10 days after the audit ends, with the further final-decision/partial-protocol rules in § 79(6)–(7). There is no blanket 60-day audit or new-registration refund guarantee. A new payer that does not meet the 12-month fast-refund test follows the ordinary § 79(1) route already described. Statutory offsets count as a refund for these purposes ([VAT Act § 79](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-79); [Tax Procedure Code § 79(1)/(2)/(7)/(11)](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-79)).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Tax period | Calendar month. A calendar quarter if § 77(2) is met and the change is notified within 25 days after the end of the month the conditions were met; it takes effect from the next calendar quarter | VAT Act § 77 |
| VAT return and payment, Slovak payer | 25 days after the end of each tax period; tax paid in the same time | VAT Act § 78(1), (2)(a) |
| Deadline falling on a Saturday, Sunday or public holiday | Moves to the next working day | Tax Procedure Code § 27(4) |
| First return when the VAT number arrives after that deadline | Five working days from delivery of the registration decision | VAT Act § 78(2)(a)(1) |
| VAT return and payment, foreign payer | 25 days after the end of a period in which tax was due, exempt intra-EU or export supplies were made, exempt goods were acquired, or a deduction is claimed | VAT Act § 78(2)(b) |
| Non-payer liable under § 69 | 25 days after the end of the month the liability arose; no payment if EUR 5 or less | VAT Act § 78(3) |
| Control statement (kontrolny vykaz) | Electronically, in XML, for every period with a return, 25 days after the period. Not due if the return reports no supplies, or only exempt § 43 or § 47 supplies with no deduction (or only a § 49(2)(d) deduction) | VAT Act § 78a(1), (16) |
| Answer to a tax office request on the control statement | Five working days from delivery of the request | VAT Act § 78a(13) |
| EC sales list (suhrnny vykaz) | Monthly, 25 days after the period; quarterly if § 80(2) is met; a § 7 or § 7a registrant supplying § 15(1) services files for each quarter in which it supplied them | VAT Act § 80 |
| EU SME scheme quarterly report (Slovak business using the scheme abroad) | End of the month after the quarter | VAT Act § 68g(8) |

The control statement lists, invoice by invoice, every invoice issued for domestic taxable supplies or for domestic reverse-charge supplies under § 69(12)(f) to (j) (not simplified invoices) and every invoice received where the payer is the customer liable under § 69(2), (3), (6), (7) and (9) to (12), or deducts tax charged by another payer. Each line shows the counterparty's VAT number, invoice number, date of supply, tax base, tax, rate and deducted tax (§ 78a(2) and (4)). Simplified invoices received are given as totals, split by supplier once deducted VAT on them reaches EUR 3,000 in the period (§ 78a(6)). Retail sales are given as eKasa totals by rate (§ 78a(8)). A corrective statement replaces the original before the deadline; after the deadline, a supplementary statement carries only the changed lines (§ 78a(12)).

A payer that failed to register must file every missed return and control statement in date order, starting from the first period (§ 78(9), § 78a(14)).

**Electronic return.** VAT payers deliver submissions electronically through the Financial Administration portal. Use the prescribed form valid for the period being corrected or filed; do not reuse the old Guide's unverified DPHv25 box table ([Tax Procedure Code § 14(1)(a)/15(4)](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-14); [official portal's VAT-return guidance](https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/danove-priznanie)).

**Adjacent goods reporting only.** A business with an INTRASTAT-SK reporting obligation files its monthly report electronically by the 15th calendar day after the reference month, including when its VAT period is quarterly. A weekend/public-holiday deadline moves to the next working day. This statistical report is separate from the VAT return; this restoration does not add an unverified 2026 reporting threshold ([Financial Administration INTRASTAT instructions](https://intrastat.financnasprava.sk/index.php?page=vsinfo), “Spôsob plnenia spravodajskej povinnosti”).

**Correcting the VAT return.** Before the filing deadline, a corrective return replaces the previous return. After the deadline, where tax should be higher or excess/refund lower, submit a supplementary return and pay the additional tax by the end of the month after discovery under § 16(2); § 16(3)(b) also requires correction of wrong VAT transaction data. A supplementary return can claim the permitted lower-tax/higher-refund correction under § 16(4), subject to § 16(7)–(9). Do not use a blanket four-year amendment window: the ordinary assessment period is five years from the end of the year the filing obligation arose, with the restart/maximum rules in § 69 and the special last-year extension in § 16(5). The audit restriction generally begins after 15 days from the specified audit notice/start event; the old statement that all amendment rights stop as soon as an audit starts was too broad ([Tax Procedure Code § 16](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-16), [§ 69](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-69); [January 2026 text](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260101.html#paragraf-16)).

## Penalties and interest

| Breach | Consequence | Source |
|---|---|---|
| Return not filed on time | Fine EUR 100 to 30,000; EUR 100 to 60,000 if not filed by the date in a tax office request (only one of the two is imposed) | Tax Procedure Code § 154(1)(a), § 155(1)(a), (b), (3) |
| Registration not made on time | Fine EUR 100 to 30,000 | § 155(1)(c) |
| First breach, fines set within a range | The tax office does not impose a fine set within a range for a first breach | § 155(4) |
| Tax under-declared, found by the tax office | 3 times the ECB base rate a year (at least 10% a year) on the extra tax, counted daily from the deadline; at least 1% of the assessed sum and at most the sum itself. Two thirds of that fine if the assessment is paid within 15 days | § 155(1)(f), (2), (5), (17) |
| Supplementary return raising tax | ECB base rate a year (at least 3%); twice the ECB rate (at least 7%) if filed after an audit has started | § 155(1)(g), (h), (5) |
| Control statement missing, late, incomplete or wrong, or defects not fixed by the requested date | Fine up to EUR 10,000; up to EUR 100,000 for repeated breaches | VAT Act § 78a(15) |
| Fast refund obtained on false data | Fine up to 1.3% of the refund | VAT Act § 79(8) |
| Late payment | Interest at 4 times the ECB base rate, at least 15% a year, counted daily from the day after the due date, for at most four years; not charged if EUR 5 or less | Tax Procedure Code § 156(2), (6)(b) |
| Fines of EUR 5 or less | Not imposed | § 155(11) |

| Breach | Consequence | Source |
|---|---|---|
| Failure to meet the EC sales list's non-monetary filing duty |100 to 10,000 euros under the 2026 range; apply the first-breach rule in § 155(4) |[Tax Procedure Code § 154(1)(j)/155(1)(e)](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-155); [FS methodology identifies the statutory sanction classification](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Metodicke_pokyny/Nepriame_dane/2018/2018.01.04_MP_vykazov.pdf), section 6/p 8 |
| Persistent non-monetary breach after an unsuccessful fine |The specified § 155(1)(d)/(e) fine can be imposed repeatedly at the same amount while the breach persists; there is no general automatic doubling rule |[Tax Procedure Code § 155(16)](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-155) |

## Cross-border points

- **Services from abroad.** A Slovak business receiving a § 15(1) service from a foreign supplier accounts for the tax as customer (§ 69(3)). A non-payer receiving such a service from a supplier in another member state must first register under § 7a and then has no right to deduct; see the registration skill.
- **Intra-EU supplies of goods** are exempt under § 43 and go on the EC sales list. Exports are exempt under § 47. For goods exported under § 47(1)–(2), keep dispatch/transport evidence and the customs declaration confirming exit from the EU; § 47(3) supplies a specified alternative-evidence route for oral or deemed export declarations ([§ 47(3)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-47)).
**Import self-assessment.** Normally customs assesses import VAT under § 84a(1), but the payer must self-assess in its VAT return under § 84a(3) when the conditions in § 84a(2) are met. For the ordinary route, the person on whose account the customs declaration is lodged must, when import liability arises, have a Slovak seat/business establishment or the stated residence, a § 4 or § 4b VAT number, and effective authorised-economic-operator status. The centralised-customs-clearance route instead permits the specified § 4/4b/5 payer with effective AEO authorisation. Obtain the customs declaration and authorisation; this is not a general election available to every VAT-registered importer. Declare qualifying import tax for its liability period and claim input VAT only to the extent § 49/51 permits. For an eligible fully taxable importer with a complete 23% import VAT base of 50,000 euros, output import VAT is 11,500 and deductible input VAT 11,500, giving zero net import VAT. The 50,000 must be the statutory import tax base, not customs value alone when duties/incidental costs must be added ([§ 84a](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-84a), [§§ 24/49/51](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-24)). The § 68cb scheme for consignments of EUR 150 or less is a separate customs procedure for the person presenting the goods.
- **Foreign businesses** register under § 5 at the Bratislava Tax Office within five working days of becoming a payer. EU sellers to Slovak consumers can use OSS (§ 68a to 68c) instead.
- **EU SME scheme (from 1 January 2025).** A Slovak small business whose EU turnover stays at or under EUR 100,000 in the current and previous year can notify the Slovak tax office in advance and use small-business exemptions in other member states with an EX number (§ 68g). It files a quarterly report by the end of the following month. A business from another member state is exempt in Slovakia if its Slovak turnover stays at or under EUR 62,500 this year and EUR 50,000 last year and its EU turnover at or under EUR 100,000 (§ 68f). It loses the exemption from the supply that takes Slovak turnover past EUR 62,500 or EU turnover past EUR 100,000 (§ 68f(6)).
- **E-invoicing.** The version of the VAT Act in force from 1 January 2027 (Act 385/2025) changes invoicing and reporting. It is outside this 2026 skill.

**Specific international exemptions.** Section 46 exempts the Slovak part of qualifying international passenger transport and its specified associated baggage/vehicle services. Section 47(6) separately exempts services directly connected with exports and the specified customs-controlled goods. Do not label all international transport as exempt simply because a counterparty is foreign. Apply the actual statutory category, with associated deduction entitlement under § 49 ([§ 46](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-46), [§ 47(6)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-47)).

**Tax representative.** Section 69a allows a foreign importer that is not a Slovak payer to choose a tax representative for the § 48(3) exempt-import/onward-intra-EU-supply route. It is not a blanket requirement for every non-EU business. The representative must be an established Slovak payer with the verified written authority and special VAT identification required by § 69a; the provision carries its own return/list obligations ([§ 69a(1)–(6)/(10)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-69a)).

## Worked examples

**Example 1: a restaurant company, monthly return, March 2026.** Cafe Dunaj s.r.o. is a monthly payer. In March 2026 it sells EUR 40,000 net of goods and services at 23% (alcoholic drinks and takeaway sweets), EUR 10,000 net of restaurant meals at 5%, and EUR 2,000 net of non-alcoholic drinks served at the tables at 19%. Its domestic purchase invoices carry EUR 4,600 of deductible VAT. Output tax is 40,000 x 23% = 9,200, plus 10,000 x 5% = 500, plus 2,000 x 19% = 380, a total of 10,080. It deducts 4,600 and pays 5,480. The 25-day deadline ends on Saturday 25 April 2026, so the return, the control statement and the payment are due on Monday 27 April 2026 (Tax Procedure Code § 27(4)). Every invoice it issued (other than simplified invoices) and every full purchase invoice it deducts goes into the control statement line by line; simplified purchase invoices go in as totals and till sales as eKasa totals by rate.

```oa-check
name: Cafe Dunaj s.r.o., March 2026 return
inputs:
  sales_23: 40000
  meals_5: 10000
  drinks_19: 2000
  input_vat: 4600
steps:
  - out_23: sales_23 * 0.23
  - out_5: meals_5 * 0.05
  - out_19: drinks_19 * 0.19
  - output_vat: out_23 + out_5 + out_19
  - payable: output_vat - input_vat
expected:
  output_vat: 10080
  payable: 5480
```

**Example 2: a consultancy with a reverse charge and a new car, April 2026.** Tatra Consulting s.r.o., a monthly payer, invoices Slovak clients EUR 30,000 net at 23%. It buys EUR 2,000 of advertising from an Irish company (a § 15(1) service), with no VAT on the invoice. In April it also buys an M1 passenger car for EUR 25,000 plus EUR 5,750 VAT. The car is used for business and private trips and no trip log is kept, so § 85n(1) limits the deduction to 50%. A client lunch carries EUR 69 VAT, which is not deductible (§ 49(7)(a)). Other purchases carry EUR 1,150 of deductible VAT. Output tax is 30,000 x 23% = 6,900 plus the self-assessed 2,000 x 23% = 460, a total of 7,360. Input tax is the 460 reverse charge, plus 5,750 x 50% = 2,875 on the car, plus 1,150, a total of 4,485. The lunch VAT is left out. The company pays 2,875. The Irish invoice goes into the control statement as a received invoice where the company is the customer liable for the tax.

```oa-check
name: Tatra Consulting s.r.o., April 2026 return
inputs:
  sales_23: 30000
  eu_ads: 2000
  car_vat: 5750
  lunch_vat: 69
  other_input: 1150
steps:
  - out_sales: sales_23 * 0.23
  - rc: eu_ads * 0.23
  - car_input: car_vat * 0.5
  - lunch_input: lunch_vat * 0
  - output_vat: out_sales + rc
  - input_vat: rc + car_input + lunch_input + other_input
  - payable: output_vat - input_vat
expected:
  output_vat: 7360
  input_vat: 4485
  payable: 2875
```

## Ask the client first

1. Which registration do you hold (§ 4, § 5, § 7 or § 7a), and since when? This decides whether you file every period and whether you can deduct at all. Obtain the exact VAT number and registration decision, including any group registration. The ordinary Slovak VAT-number format is SK followed by 10 digits; checking its format is not verification that the number is valid or that § 7/7a gives payer deduction rights ([official tax-authority country-format table](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/international-commerce/vat-number/vat-numbers-issued-by-different-eu-countries/)).
2. Are you on monthly or quarterly periods, and did turnover in any 12-month run reach EUR 100,000?
3. What do you sell, and at which rate? Food and restaurant clients need the 2026 split between 23%, 19% and 5%.
4. Did you buy, lease or run an M1 car or an L1e or L3e motorcycle in 2026, and do you keep the § 85n trip log?
5. Did you receive services from foreign suppliers, or buy construction work, scrap, steel, cereals, or phones and chips at EUR 5,000 or more from Slovak payers?
6. Do you make exempt supplies (financial, insurance, housing rental) as well as taxable ones?

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 222/2004 Coll. on VAT, version in force 1 January 2026 to 31 December 2026 (§ 4, 5, 7a, 27, 49, 68cb, 68f, 68g, 69, 77, 78, 78a, 79, 80, 85n, 85o) | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html | 2026-10-23 |
| VAT Act Annex 7, goods at reduced rates (version from 1 January 2026) | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf | 2026-10-23 |
| VAT Act Annex 7a, services at reduced rates (version from 1 January 2026) | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf | 2026-10-23 |
| Act No. 563/2009 Coll., Tax Procedure Code, version in force from 1 September 2026 (§ 27, 154, 155, 156; same text of § 154 to 156 in the version from 1 January 2026) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Financna sprava, Sadzby dane (VAT rates and the 1 January 2026 changes) | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/sadzby-dane | 2026-10-23 |
| Current VAT Act §§ 2–4b, 8–10, 24–25, 28–42, 46–47, 49–54d, 69a, 79, 84a and transitions 85kp/85n | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html | 2026-10-27 |
| Tax Procedure Code §§ 14–16, 55, 69, 79 and 154–155; January and September 2026 amendment rules checked separately | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html and https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260101.html | 2026-10-27 |
| Historical January 2024 VAT Act § 27 for original-rate corrections | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20240101.html | 2026-10-27 |
| Financial Administration, VAT-return filing guidance | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/danove-priznanie | 2026-10-27 |
| Financial Administration, EC-sales-list methodology, section 6, read with the current statutory sanction range | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Metodicke_pokyny/Nepriame_dane/2018/2018.01.04_MP_vykazov.pdf | 2026-10-27 |
| Financial Administration, INTRASTAT-SK filing instructions | https://intrastat.financnasprava.sk/index.php?page=vsinfo | 2026-10-27 |
| Finnish Tax Administration, official EU VAT-number format table | https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/international-commerce/vat-number/vat-numbers-issued-by-different-eu-countries/ | 2026-10-27 |
| Financial Administration: direct attribution, overseas supplies, coefficient exclusions and annual reconciliation (§ 50) | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/odpocitanie-dane | 2026-10-27 |

Not yet confirmed: the row numbers of the 2026 VAT return form and the control statement layout (the official forms were not read, so this skill names no boxes); the ECB base rate on any given date, which sets the fine and interest percentages above the floors; whether the first-breach rule in Tax Procedure Code § 155(4) also covers the control statement fine in VAT Act § 78a(15); the annual § 50 method where the actual annual included-supplies denominator is zero.

> Contributed by Michael Cutajar.

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
