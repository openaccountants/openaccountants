---
name: ca-infant-formula-sales-tax
description: >
  California sales and use tax classification of infant formula and nearby
  infant feeding products, after SB 1151 (Stats. 2026, Ch. 680, in effect 27
  September 2026), which writes "infant formula" into the R&TC 6359 food
  products exemption as declaratory of existing law. Covers the definition chain
  (R&TC 6359(b)(4), Health and Safety Code 114094.5, 21 U.S.C. 321(z)), the
  exclusions that still apply (medicines and medical foods, dietary
  supplements, vending machines, meals and places charging admission), CDTFA
  annotations on baby formulas, PediaSure and medical foods, Pedialyte and baby
  food, the Regulation 1602(b) 10% rule for gift packs, and boundary rows for
  diapers (R&TC 6363.9) and breast pumps (R&TC 6370.2). Not menstrual products,
  restaurant food or the general sales tax method. Trigger on "is infant formula
  taxable in California", "baby formula sales tax California", "SB 1151",
  "R&TC 6359 infant formula", "medical food sales tax California", "baby gift
  basket sales tax".
version: 0.1
jurisdiction: US-CA
category: state-tax
tax_year: 2026
last_updated: 2026-11-22
tier: 2
domain: tax
type: situation-rules
---

# California sales tax on infant formula and infant feeding products, after SB 1151 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from the chaptered text of SB 1151 (Stats. 2026, Ch. 680) and the codified R&TC 6359, 6363.9, 6369 and 6370.2 and Health and Safety Code 114094.5 in the official California Legislature bulk data archive; 21 U.S.C. 321(z) and 360ee(b)(3) on govinfo.gov; CDTFA Regulations 1574, 1591, 1602 and 1603, the CDTFA law guide page for R&TC 6359, CDTFA Sales and Use Tax Annotations 245.0060, 245.0080, 245.0732, 245.0940, 245.1633, 425.0151 and 425.0382, CDTFA Publication 31 (November 2024), the CDTFA notices page and the CDTFA rate table effective 1 October 2026. All were read on 2026-11-22 (California, Pacific time). No accountant has reviewed it.

**Answer first.**

- **Infant formula is an exempt food product.** R&TC 6359(a) exempts "food products for human consumption". SB 1151 added to the list of food products: "(4)(A) Infant formula, as defined in Section 114094.5 of the Health and Safety Code. (B) This paragraph does not constitute a change in, but is declaratory of, existing law" ([R&TC 6359(b)(4), archive entry LAW_SECTION_TBL_121933.lob](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip)).
- **It is declaratory, so nothing changes for sellers who already treated formula as exempt.** CDTFA's annotations have treated baby formulas as exempt food since 1963 ([Annotation 245.0060](https://cdtfa.ca.gov/lawguides/vol2/suta/245-0060.html)), and Publication 31 lists "Baby formulas (such as Isomil)" as nontaxable ([CDTFA Publication 31, p. 1](https://cdtfa.ca.gov/formspubs/pub31.pdf)).
- **The definition.** H&SC 114094.5(d)(2) gives "infant formula" the meaning in 21 U.S.C. 321(z): "a food which purports to be or is represented for special dietary use solely as a food for infants by reason of its simulation of human milk or its suitability as a complete or partial substitute for human milk" ([21 U.S.C. 321(z)](https://www.govinfo.gov/content/pkg/USCODE-2024-title21/html/USCODE-2024-title21-chap9-subchapII-sec321.htm)).
- **What can still make a sale taxable:**
  - the product is a **medicine** or **medical food**, or is sold as a **dietary supplement or adjunct** (R&TC 6359(c)(1); [Regulation 1602(a)(4)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1602.html); [Annotation 245.0732](https://cdtfa.ca.gov/lawguides/vol2/suta/245-0732.html));
  - the **way it is sold**: as part of a meal, for consumption at the seller's tables, sold within and for consumption within a place charging admission, or through a vending machine (R&TC 6359(d); vending machine receipts from cold food are partly exempt under [Regulation 1574(b)(2)(C)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1574.html));
  - it is part of a **gift pack** whose nonfood items are more than 10% of the value (Regulation 1602(b)).
- **Nearby baby products:** diapers for infants, toddlers and children are exempt from 1 January 2020 (R&TC 6363.9). Breast pumps and listed supplies are exempt from 1 April 2024 to 31 March 2029 (R&TC 6370.2). Bottles not specific to a breast pump, and other baby gear, are taxable at the full rate unless another exemption applies.

**Tax year.** Tax year 2026. SB 1151 took effect immediately as a tax levy (SEC. 2). The codified section reads "Amended by Stats. 2026, Ch. 680, Sec. 1. (SB 1151) Effective September 27, 2026". SB 1151 states that paragraph (4) "does not constitute a change in, but is declaratory of, existing law", and CDTFA's annotations have treated baby formulas as exempt food since 1963 (Annotation 245.0060). Sales tax is a transaction tax, so there is no annual period.

**Circular 230 disclosure.** This material is general information, not written advice on a specific transaction under 31 CFR 10.37. It is not intended to be used, and cannot be used, to avoid penalties.

## Scope and who this is for

In scope:

- **Retailers** selling infant formula and other infant feeding products in California (grocery stores, pharmacies, online sellers, convenience stores), deciding which lines to tax.
- **Purchasers** checking whether California use tax applies to formula bought from out-of-state sellers.

The job: classify each infant feeding product and each sale as exempt food or taxable, and work out the tax on a mixed basket or a gift pack.

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| The general sales tax method: permits, rates by address, returns, other food rules (hot food, the 80-80 rule, restaurants) | `california-sales-tax` |
| Menstrual hygiene products (R&TC 6363.10) | refer |
| Prescription medicines and medical devices generally (R&TC 6369, Regulation 1591) | refer; `california-sales-tax` row on prescription medicines |
| Vending machine operators' permits, records and the tax-included computation (Regulation 1574) | refer |
| California Redemption Value on beverage containers (Publication 31 says infant formula and medical food are not subject to CRV) | refer to CalRecycle |
| WIC and CalFresh program rules | refer |
| Refunds of tax charged on formula in the past | refer (see Not yet confirmed) |

## Ask the client first

- What exactly is the product? Get the label: is it presented "solely as a food for infants" as a substitute for human milk, or is it a toddler or growing-up drink, an electrolyte drink, a medical food, or a supplement?
- Does the label call it a "supplement", "dietary supplement" or "food adjunct"?
- Is it sold over the counter, or dispensed on a prescription, furnished by a physician or health facility, or sold to a health facility?
- How is it sold: off the shelf, in a vending machine, in a restaurant or cafe, or inside a venue that charges admission?
- Is it sold alone or in a gift pack or kit with nonfood items? What are the retail values of the food, the nonfood items and the container?
- What else is in the sale: diapers, breast pump items, bottles, other baby gear?
- What is the seller's address (or the delivery address) for the rate?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Infant formula | Exempt (0%) | "'food products' includes ... (4)(A) Infant formula, as defined in Section 114094.5 of the Health and Safety Code"; "declaratory of existing law" | [R&TC 6359(b)(4), SB 1151 SEC. 1 (archive)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip) |
| Definition of infant formula | 21 U.S.C. 321(z) | "represented for special dietary use solely as a food for infants" as a substitute for human milk | [H&SC 114094.5(d)(2) (archive entry LAW_SECTION_TBL_99593.lob)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip); [21 U.S.C. 321(z)](https://www.govinfo.gov/content/pkg/USCODE-2024-title21/html/USCODE-2024-title21-chap9-subchapII-sec321.htm) |
| Medicines, and preparations sold as dietary supplements or adjuncts | Not food products | "'food products' does not include ... Medicines ... and preparations in liquid, powdered, granular, tablet, capsule, lozenge, and pill form sold as dietary supplements or adjuncts" | [R&TC 6359(c)(1) (archive)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip) |
| Complete dietary food | Food (exempt) if it supplies daily at least 70 grams of high quality protein, 900 calories, and listed vitamins and minerals | Applies to products labelled as supplements | [Regulation 1602(a)(4)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1602.html) |
| Medical foods (Orphan Drug Act definition) | Taxable as medicines, "including over-the-counter sales", unless sold in an exempt manner under Regulation 1591(d)(1) to (6) | CDTFA annotation dated 10/21/09 | [Annotation 245.0732](https://cdtfa.ca.gov/lawguides/vol2/suta/245-0732.html); [Annotation 425.0151](https://cdtfa.ca.gov/lawguides/vol2/suta/425-0151.html) |
| Meals, seller's tables, places charging admission | 6359 exemption does not apply | "None of the exemptions in this section apply" in the listed cases; for admission places, food "sold within, and for consumption within" the place, presumed unless the retailer keeps evidence the form makes consumption there unlikely | [R&TC 6359(d)(1), (2), (4) (archive)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip); [Regulation 1603(d)(1), (3)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1603.html) |
| Vending machines | 33% of gross receipts from cold food products taxable (after the tax-included adjustment); sales of 15 cents or less, and bulk vending sales of 25 cents or less, have their own rules | "The following percentages of the gross receipts from the sales of such products are subject to the tax: ... 33% thereafter" | [R&TC 6359(d)(5) (archive)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip); [Regulation 1574(b)(2)(A) to (C)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1574.html) |
| Gift pack: nonfood share | 10% or less of retail value, excluding the container, and container 50% or less of the whole package | Whole package exempt; above 10%, segregate if documented, else tax may be measured on the whole package | [Regulation 1602(b)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1602.html) |
| Diapers for infants, toddlers and children | Exempt from 1 January 2020 | "designed, manufactured, processed, fabricated, or packaged for use by infants, toddlers, and children" | [R&TC 6363.9 (archive entry LAW_SECTION_TBL_122005.lob)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip) |
| Breast pumps, collection and storage supplies, kits, breast pads | Exempt from 1 April 2024 to 31 March 2029 | "On and after April 1, 2024, and before April 1, 2029"; bottles not specific to a breast pump are excluded unless in a manufacturer's kit | [R&TC 6370.2(a), (b)(2)(B) (archive entry LAW_SECTION_TBL_122088.lob)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip) |
| Combined rate, City of Sacramento (used in the worked cases) | 8.75% (0.0875) | Rate table effective 1 October 2026 | [CDTFA rate table, October 2026](https://cdtfa.ca.gov/taxes-and-fees/SalesTaxRates10-1-26.xlsx) |

### Steps

1. **Is it infant formula?** It must be represented "solely as a food for infants" as a simulation of, or substitute for, human milk (21 U.S.C. 321(z)). Standard cow's-milk and soy formulas qualify; CDTFA treated ProSobee and Isomil, soy formulas, as exempt food in 1965 ([Annotation 245.0940](https://cdtfa.ca.gov/lawguides/vol2/suta/245-0940.html)). Formula sold in ready-to-feed disposable bottles with nipples is still exempt ([Annotation 245.0060](https://cdtfa.ca.gov/lawguides/vol2/suta/245-0060.html); [Annotation 245.0080](https://cdtfa.ca.gov/lawguides/vol2/suta/245-0080.html)).
2. **If it is not infant formula, is it still a food product?** Many infant and child feeding products are food under the general rules:
   - **Baby food** and noncarbonated drinks are food products; Publication 31 lists baby food and Pedialyte as nontaxable (pp. 1 and 2).
   - **PediaSure** was held to be a complete dietary food for children aged 1 to 10, and so exempt ([Annotation 245.1633](https://cdtfa.ca.gov/lawguides/vol2/suta/245-1633.html), dated 9/9/99).
   - **Products labelled as supplements** are not food unless they meet the complete dietary food test in Regulation 1602(a)(4). Vitamin drops and protein supplements are taxable.
3. **Check for the medicine exclusion.** A product that is a "medical food" under the Orphan Drug Act ("formulated to be consumed or administered enterally under the supervision of a physician and ... intended for the specific dietary management of a disease or condition", [21 U.S.C. 360ee(b)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title21/html/USCODE-2024-title21-chap9-subchapV-partB-sec360ee.htm)) is a medicine under CDTFA's annotations, and taxable over the counter. It is exempt when dispensed on prescription, furnished by a physician to a patient, furnished by a health facility on a physician's order, or sold to a physician or health facility ([R&TC 6369(a)](https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip); [Regulation 1591(d)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1591.html)). Feeding tubes are taxable equipment, not food ([Annotation 425.0382](https://cdtfa.ca.gov/lawguides/vol2/suta/425-0382.html), dated 10/2/89).
4. **Check how it is sold.** Even infant formula loses the 6359 exemption when served as part of a meal, furnished for consumption at the seller's tables or counters, or sold within, and for consumption within, a place charging admission (other than the listed parks, marinas, campgrounds and RV parks) (R&TC 6359(d)). Inside an admission place, food is presumed sold for consumption there unless the retailer keeps evidence that the form makes that unlikely; CDTFA's examples are canned jams, cake mixes, spices and cooking chocolate (Regulation 1603(d)(3)). Through a vending machine, 33% of the gross receipts from cold food products is taxable after the tax-included adjustment (Regulation 1574(b)(2)(C)).
5. **Apply the gift pack rule.** For a package mixing formula or baby food with toys, clothes or other nonfood items, apply Regulation 1602(b): exempt in full if nonfood items are 10% or less of the retail value excluding the container and the container is 50% or less of the whole; otherwise tax the nonfood items' retail price (with documentation) or the whole package (without it).
6. **Tax the rest of the basket.** Diapers for children are exempt (R&TC 6363.9); breast pumps, listed supplies, kits and breast pads are exempt until 31 March 2029 (R&TC 6370.2). Ordinary baby bottles, pacifiers, toys and clothing are taxable at the combined rate for the location.

**AUDIT FLASH POINT: specialised formulas, food or medicine.** R&TC 6359(b)(4) makes "infant formula" a food product, but 6359(c)(1) still says food products do not include "medicines", and CDTFA's 2009 annotations treat Orphan Drug Act "medical foods" as medicines taxable over the counter. A formula for infants with a specific medical condition, labelled for use under medical supervision, could be argued either way. The sources read do not settle it. Refer, and ask CDTFA for written advice for a product line.

**AUDIT FLASH POINT: toddler and growing-up drinks.** The federal definition requires a product represented "solely as a food for infants". A drink marketed for toddlers is not "infant formula" under 6359(b)(4). It may still be an exempt food product (a milk-based drink under 6359(b)(2), or a complete dietary food), or taxable if labelled as a supplement. No age line was found in the sources read; classify from the label and refer close cases.

**Annotations are guidance, not law.** CDTFA annotations summarise past rulings (here dated 1963 to 2009) and do not bind CDTFA in later cases. Annotation 245.1633 cites "subdivision (a)(5) of Regulation 1602"; in the current text the complete dietary food rule is in (a)(4).

## Boundary and exception table

| Situation | Result | Basis |
| --- | --- | --- |
| Powdered cow's-milk infant formula, off the shelf | Exempt | R&TC 6359(b)(4) |
| Soy infant formula | Exempt | R&TC 6359(b)(4); Annotation 245.0940 |
| Ready-to-feed formula in disposable bottles with nipples | Exempt | Annotations 245.0060, 245.0080 |
| Infant formula sold from a vending machine | Partly taxable: 33% of cold food receipts, after the tax-included adjustment | R&TC 6359(d)(5); Regulation 1574(b)(2)(C) |
| Sealed tub of infant formula sold in a shop inside a theme park that charges admission | Presumed taxable unless the retailer keeps evidence it is unlikely to be consumed inside; refer | R&TC 6359(d)(4); Regulation 1603(d)(3) |
| Jarred baby food | Exempt | Publication 31, p. 2 |
| Pedialyte | Exempt | Publication 31, p. 2 |
| PediaSure, used as labelled | Exempt (complete dietary food) | Annotation 245.1633; Regulation 1602(a)(4) |
| Infant vitamin drops labelled as a dietary supplement | Taxable | R&TC 6359(c)(1); Regulation 1602(a)(4) |
| Medical food sold over the counter | Taxable (medicine) | Annotation 245.0732 |
| Medical food dispensed on prescription by a pharmacist | Exempt (medicine sold in an exempt manner) | R&TC 6369(a)(1); Regulation 1591(d)(1) |
| Specialised infant formula for a medical condition | Unsettled; refer | AUDIT FLASH POINT above |
| Toddler "growing-up" milk drink | Not infant formula; classify as other food or supplement | 21 U.S.C. 321(z); R&TC 6359(b)(2) |
| Children's diapers | Exempt | R&TC 6363.9 |
| Breast pump kit, sold 2026 | Exempt | R&TC 6370.2 |
| Ordinary baby bottles sold separately | Taxable | R&TC 6370.2(b)(2)(B)(i) (not covered by the breast pump exemption) |

## Worked cases

Both cases are made up for illustration, at the City of Sacramento combined rate of 8.75% from the CDTFA rate table effective 1 October 2026.

**Case 1: mixed baby basket at a grocery store, December 2026.**

- **Items:**
  - 3 tubs of powdered infant formula at USD 30 each, USD 90: exempt (R&TC 6359(b)(4)).
  - Jarred baby food, USD 15: exempt (Publication 31).
  - Pedialyte, USD 8: exempt (Publication 31).
  - Children's diapers, USD 40: exempt (R&TC 6363.9).
  - Infant vitamin drops labelled "dietary supplement", USD 12: taxable (Regulation 1602(a)(4)).
  - Two ordinary baby bottles, USD 20: taxable (not breast pump supplies).
- **Exempt:** USD 90 + 15 + 8 + 40 = USD 153.
- **Taxable:** USD 12 + 20 = USD 32.
- **Sales tax:** USD 32 x 8.75% = USD 2.80. Basket total USD 185 + USD 2.80 = USD 187.80.

```oa-check
name: Mixed baby basket, infant formula and other exempt items, taxable supplement and bottles
inputs:
  infant_formula: 90
  baby_food: 15
  pedialyte: 8
  diapers: 40
  vitamin_drops_supplement: 12
  baby_bottles: 20
  rate: 0.0875
steps:
  - exempt_total: infant_formula + baby_food + pedialyte + diapers
  - taxable_total: vitamin_drops_supplement + baby_bottles
  - sales_tax: taxable_total * rate
  - basket_with_tax: exempt_total + taxable_total + sales_tax
expected:
  exempt_total: 153
  taxable_total: 32
  sales_tax: 2.80
  basket_with_tax: 187.80
```

**Case 2: "new baby" gift baskets and the 10% rule.**

- **Basket A, USD 60:** formula and baby food with a retail value of USD 50, a small plush toy worth USD 4, and a gift box worth USD 6. The case assumes the gift box is the "container" under Regulation 1602(b), which does not define the term.
  - Nonfood share, excluding the container: USD 4 / USD 54 = 7.4%, which is 10% or less.
  - Container share: USD 6 / USD 60 = 10%, which is 50% or less.
  - The whole package is exempt (Regulation 1602(b)). Tax: USD 0.
- **Basket B, USD 68:** the same food and gift box, with a larger toy worth USD 12.
  - Nonfood share: USD 12 / USD 62 = 19.4%, more than 10%.
  - With documentation of component costs, segregate and tax the toy's retail price: USD 12 x 8.75% = USD 1.05.
  - Without that documentation, the tax may be measured by the whole package: USD 68 x 8.75% = USD 5.95.

```oa-check
name: Baby gift baskets under the Regulation 1602(b) 10 percent rule
inputs:
  food_value: 50
  toy_a: 4
  toy_b: 12
  container: 6
  rate: 0.0875
steps:
  - package_a: food_value + toy_a + container
  - nonfood_pct_a: round(toy_a / (food_value + toy_a) * 100, 1)
  - container_pct_a: round(container / package_a * 100, 1)
  - package_b: food_value + toy_b + container
  - nonfood_pct_b: round(toy_b / (food_value + toy_b) * 100, 1)
  - tax_b_segregated: toy_b * rate
  - tax_b_whole_package: package_b * rate
expected:
  package_a: 60
  nonfood_pct_a: 7.4
  container_pct_a: 10.0
  package_b: 68
  nonfood_pct_b: 19.4
  tax_b_segregated: 1.05
  tax_b_whole_package: 5.95
```

## When to refuse or refer

- **Specialised and medical formulas.** Any formula labelled for a disease or condition, or for use under medical supervision.
- **Past tax charged on formula.** A customer or seller asking for a refund because tax was charged on formula before SB 1151.
- **New product lines.** A retailer launching or reclassifying a line of infant or toddler nutrition products: ask CDTFA for written advice.
- **Restaurants, cafes and venues** selling formula or baby food with meals or inside admission areas: use `california-sales-tax` for the meal rules.
- **Menstrual products, medical devices and prescription items** outside infant feeding.

## Filing and payment

- **No separate return.** Report on the seller's regular sales and use tax return, using the return method in `california-sales-tax`. For diapers, Publication 31 says to include the sales in total gross sales and claim the deduction as "diapers" ([Publication 31, pp. 7 to 8](https://cdtfa.ca.gov/formspubs/pub31.pdf)).
- **Records.** Keep product labels or specifications showing why each product is classified as infant formula, food, supplement or medicine, and the cost documentation needed for the gift pack rule.
- **Use tax.** A California purchaser of infant formula from an out-of-state seller owes no use tax on it, because R&TC 6359(a) exempts storage, use or other consumption as well as sales.

## Completion checklist

- [ ] Each product's label read: infant formula, other food, supplement, or medical food.
- [ ] Infant formula checked against 21 U.S.C. 321(z) ("solely as a food for infants").
- [ ] Medical foods and specialised formulas referred, or checked against an exempt manner of sale under R&TC 6369(a).
- [ ] Manner of sale checked: meals, tables, admission places (Regulation 1603(d)), vending machines (Regulation 1574).
- [ ] Gift packs tested under Regulation 1602(b), with cost documentation kept.
- [ ] Diapers and breast pump items classified under R&TC 6363.9 and 6370.2.
- [ ] Taxable items taxed at the combined rate for the location.

## Sources

Read dates are California (Pacific time) local dates: all sources for this skill were opened on 22 November 2026, Pacific time.

| Source | URL | Read on |
| --- | --- | --- |
| SB 1151 (Cervantes), chaptered text, Stats. 2026, Ch. 680, approved and chaptered 27 September 2026, from the official California Legislature bulk data archive (version 20250SB115195CHP, entry BILL_VERSION_TBL_18803.lob; bill status: Chaptered, 2026, Chapter 680). Read in full, for SEC. 1 (R&TC 6359 as amended, including (b)(4)), SEC. 2 (tax levy, immediate effect) and the Legislative Counsel's Digest. | https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip | 2026-11-22 |
| Same archive, codified law table. Read for R&TC 6359 ("Amended by Stats. 2026, Ch. 680, Sec. 1. (SB 1151) Effective September 27, 2026", with the note on the 1992 Prop. 163 amendment, LAW_SECTION_TBL_121933.lob); H&SC 114094.5 (LAW_SECTION_TBL_99593.lob); R&TC 6363.9 (LAW_SECTION_TBL_122005.lob); R&TC 6369 (LAW_SECTION_TBL_122084.lob); R&TC 6370.2 (LAW_SECTION_TBL_122088.lob). | https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip | 2026-11-22 |
| 21 U.S.C. 321, United States Code 2024 edition, govinfo.gov. Read for the definition of "infant formula" in subsection (z). | https://www.govinfo.gov/content/pkg/USCODE-2024-title21/html/USCODE-2024-title21-chap9-subchapII-sec321.htm | 2026-11-22 |
| 21 U.S.C. 360ee, United States Code 2024 edition, govinfo.gov. Read for the definition of "medical food" in subsection (b)(3). | https://www.govinfo.gov/content/pkg/USCODE-2024-title21/html/USCODE-2024-title21-chap9-subchapV-partB-sec360ee.htm | 2026-11-22 |
| CDTFA Regulation 1602, Food Products. Read for subdivision (a)(3) and (a)(4) (medicines and supplements, the complete dietary food test) and (b) (combination packages). | https://cdtfa.ca.gov/lawguides/vol1/sutr/1602.html | 2026-11-22 |
| CDTFA Regulation 1591, Medicines and Medical Devices. Read for subdivision (d), the exempt manners of sale. | https://cdtfa.ca.gov/lawguides/vol1/sutr/1591.html | 2026-11-22 |
| CDTFA Regulation 1603, Taxable Sales of Food Products. Read for subdivision (d), places where admission is charged, and the cross-reference to Regulation 1574. | https://cdtfa.ca.gov/lawguides/vol1/sutr/1603.html | 2026-11-22 |
| CDTFA Regulation 1574, Vending Machine Operators. Read for subdivision (b)(2)(A) to (C), food products sold through vending machines and the 33% partial exemption. | https://cdtfa.ca.gov/lawguides/vol1/sutr/1574.html | 2026-11-22 |
| CDTFA Business Taxes Law Guide, R&TC 6359. Read for the text and history shown; the page did not yet show subdivision (b)(4) added by SB 1151. | https://cdtfa.ca.gov/lawguides/vol1/sutl/6359.html | 2026-11-22 |
| CDTFA Sales and Use Tax Annotations 245.0060 (Baby Formulas, 12/9/63), 245.0080 (Baby Formulas in Disposable Formula Bottles, 3/29/65), 245.0732 (Medicines, Medical Foods, 10/21/09), 245.0940 (Hypo-Allergenic Baby Formula, 12/14/65), 245.1633 (PediaSure, 9/9/99), 425.0151 (Medicines, 10/21/09) and 425.0382 (Entriflex, Keofred, and Enteral Tubes, 10/2/89). Read in full, each, and the 245 index. | https://cdtfa.ca.gov/lawguides/vol2/suta/245-0000.html | 2026-11-22 |
| CDTFA Publication 31, Grocery Stores (November 2024). Read for the nontaxable sales list (pp. 1 and 2), diapers and menstrual products (pp. 7 to 8), breast pumps (p. 8) and the CRV table (p. 9). | https://cdtfa.ca.gov/formspubs/pub31.pdf | 2026-11-22 |
| CDTFA notices page. Read for any notice on SB 1151 or infant formula: none found. | https://cdtfa.ca.gov/notices.htm | 2026-11-22 |
| CDTFA rate table effective 1 October 2026. Read for the City of Sacramento row (0.0875). | https://cdtfa.ca.gov/taxes-and-fees/SalesTaxRates10-1-26.xlsx | 2026-11-22 |
| leginfo.legislature.ca.gov, SB 1151 bill status page. Secondary reference only: returned a security check page (HTTP 403, "Just a moment...") to a direct request on 2026-11-22, not bypassed. Not read. | https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB1151 | not read |

Not yet confirmed: whether retailers that charged tax reimbursement on infant formula before SB 1151 must refund it, and how (the excess tax reimbursement rules were not read); whether a specialised infant formula that is also a "medical food" is food under 6359(b)(4) or a medicine under 6359(c)(1); the age line, if any, for "infants" in the federal definition (21 CFR not read); the California Constitution, article XIII, section 34 (Proposition 163), noted on the codified R&TC 6359 but not read; the vending machine cold food factor computation in Regulation 1574 (read only for the 33% rule); and any CDTFA guidance issued on SB 1151 after 22 November 2026.

**Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
