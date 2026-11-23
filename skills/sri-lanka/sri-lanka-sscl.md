---
name: sri-lanka-sscl
description: ALWAYS read this skill before touching any Sri Lanka Social Security Contribution Levy (SSCL) work for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Use whenever asked about SSCL on turnover for importers, manufacturers, service providers, wholesalers and retailers, or financial-service businesses in Sri Lanka. Trigger on phrases like Sri Lanka SSCL, Social Security Contribution Levy, 2.5% turnover levy Sri Lanka, liable turnover, SSCL registration threshold, SSCL return. Gives the 2.5% rate, liable-turnover fractions (100%, 85%, 50%, 25%), registration tests (Rs. 9 million quarterly or Rs. 36 million over four consecutive quarters from 1 July 2026), exemptions, payment and return dates.
version: "2.1"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (2026-27); SSCL is charged by quarter"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Sri Lanka Social Security Contribution Levy (SSCL), v2.1

Built from the law: not yet approved by an accountant. Produced by OpenAccountants (openaccountants.com). Not tax advice. Period covered: quarters in the year of assessment 2026/27.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country and authority | Sri Lanka, Inland Revenue Department (IRD) |
| Tax | Social Security Contribution Levy, a turnover levy separate from VAT and income tax |
| Principal Act | Social Security Contribution Levy Act, No. 25 of 2022, in force from 1 October 2022, including amendments under Acts No. 24 of 2025 and No. 10 of 2026 |
| Basis | Accrual; charged for every quarter on liable turnover |
| Currency | LKR |

- **In:** every taxable person (individual or entity, including a body of persons, an executor, an NGO and a charitable institution) who imports any article, manufactures any article, provides a service of any description, or carries on wholesale or retail sale of any article including importation and sale (other than a sale by the manufacturer already covered as a manufacturer).
- **Status:** in force. Use the operative legislation for the quarter. The general IRD SSCL page still displays the registration thresholds that applied before 1 July 2026.
- **Not here:** VAT (`sri-lanka-vat`), income tax (`sri-lanka-income-tax`, `sri-lanka-corporate-tax`), withholding (`sri-lanka-withholding-tax`).

## Ask the client first

1. Activity class: importer, manufacturer, service provider (financial services, real estate, other) or wholesaler and retailer (registered distributor or other)?
2. Turnover by quarter and for the last four quarters, excluding exempt articles and services.
3. SSCL registration status and TIN.
4. Any exclusions, including eligible pharmaceuticals, articles subject to Special Commodity Levy, exports, wholesale or retail sales of petrol, diesel, kerosene or motor vehicles, LP gas and specified local agricultural purchases.
5. Bad debts written off or recovered in the quarter; VAT included in the figures.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Rate | 2.5% of liable turnover | Every quarter from 1 October 2022 | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Social%20Security%20Contribution%20Levy%20%28SSCL%29.aspx |
| Liable turnover, importation of any article | 100% of turnover | Value for VAT under VAT Act section 6, less exempt articles | same |
| Liable turnover, manufacture of any article | 85% of turnover | Sums receivable for articles manufactured and sold in Sri Lanka | same |
| Liable turnover, financial services | 100% of value addition for non-exempt services | Apply the Chapter IIIA VAT attribution method. A supply subject to 20.5% VAT on financial services is exempt from SSCL from 1 July 2026 | First Schedule Part II item 25 and Second Schedule item 3(a) |
| Liable turnover, land and improvements | 100% of the value of improvement | Sale value less market value of the bare land, VAT Act section 5(7) | same |
| Liable turnover, other services | 100% of turnover | Section 3(2)(c)(iii) | same |
| Liable turnover, sale by a registered distributor of a Sri Lankan manufacturer or producer | 25% of turnover | Apply the statutory distributor test in section 60 | Second Schedule item 4(a) |
| Liable turnover, other wholesale or retail sale, including importation and sale | 50% of turnover | Apply to wholesale or retail sales in Sri Lanka, excluding Part IB items | Second Schedule item 4(b) |
| Registration threshold, before 1 July 2026 | Turnover for a quarter exceeds or is likely to exceed Rs. 15,000,000, or for four consecutive quarters exceeds or is likely to exceed Rs. 60,000,000 | Periods from 1 January 2024 to 30 June 2026, excluding exempt articles and services. In 2026, apply within 15 days of meeting either test | Section 4(1)(c) |
| Registration threshold, from 1 July 2026 | Turnover for a quarter exceeds or is likely to exceed Rs. 9,000,000, or for four consecutive quarters exceeds or is likely to exceed Rs. 36,000,000 | Apply within 15 days of exceeding or being likely to exceed either threshold. Importation itself is dealt with at Customs | Section 4(1)(d), inserted by Act No. 10 of 2026 |

### Steps

1. Classify each activity. A person with several activities computes each class separately.
2. Apply the turnover definition for the relevant activity in section 3(2). For domestic turnover measured by amounts receivable, use the accrual amount. Remove exempt supplies, bad debts incurred in the quarter, VAT paid for the quarter and any Export Development Rebate for a minister-approved international event. Include bad debts recovered in the quarter.
3. Apply the liable-turnover fraction for the class.
4. Multiply liable turnover by 2.5%.
5. For registered domestic activities, pay monthly on self-assessment and file the quarterly return. Customs collects the levy on chargeable imports at importation.
6. Test both registration thresholds for domestic activities, including subsequent domestic sales of imports. Use aggregate section 3 turnover before applying the liable-turnover fractions. The Commissioner-General may exclude a single isolated transaction from this test under section 4(2).

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Activity class unclear | Obtain the facts needed to choose the applicable fraction. Show conditional calculations if unresolved |
| Registration borderline | Check turnover, exemptions and whether either threshold is likely to be exceeded |
| Whether SSCL applies to a supply | Check the charging provision and applicable exemption before calculating the liability |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Applying 2.5% to gross turnover for a class below 100% | Wrong: over-states the levy; apply the fraction first |
| Export of an article | First Schedule Part IA covers exports by manufacturers and specified supplies to exporters with evidence. Part IB covers articles exported in the wholesale and retail class |
| Petrol, diesel or kerosene; LP gas | Excluded from wholesale and retail turnover. The fuel exemption applies to sales from 1 July 2025, including sales outside filling stations |
| Pharmaceuticals | First Schedule Part IA applies to pharmaceuticals identified by Customs codes. Part IB exempts pharmaceuticals in wholesale and retail sales |
| Special Commodity Levy article | Exempt at import if subject to that levy. The importer's domestic sale is also exempt if the only processing, if any, is adaptation for sale |
| Fresh milk, green leaf, cinnamon or rubber | Excluded from wholesale and retail turnover if bought from a local manufacturer or producer. Qualifying rubber is latex, crepe or sheet rubber |
| Motor vehicles from 1 May 2026 | The former import exemption ends and Customs collects SSCL on chargeable imports. Domestic wholesale and retail sales are exempt |
| Services of a container terminal operator | Exempt from 17 December 2025 where related to international transportation |
| Financial services subject to 20.5% VAT under Chapter IIIA | Exempt from SSCL for supplies subject to that VAT rate from 1 July 2026 |
| Bad debt recovered in a later quarter | Included in that later quarter's turnover |
| Exempt articles and services | First Schedule Part IA applies to import and manufacture, Part IB to wholesale and retail, and Part II to services |

## Worked cases

### Case 1: manufacturer

A registered manufacturer sells non-exempt articles it makes in Sri Lanka for Rs. 100,000,000 of section 3 turnover in a quarter. Liable turnover is 85%.

```oa-check
name: Manufacturer, one quarter
inputs:
  turnover: 100000000
steps:
  - liable: turnover * 0.85
  - sscl: liable * 0.025
expected:
  liable: 85000000
  sscl: 2125000
```

### Case 2: decision, sell as a registered distributor or as an ordinary wholesaler

A wholesaler has Rs. 100,000,000 of quarterly turnover from non-exempt goods made by a Sri Lankan manufacturer. The 25% fraction applies if the manufacturer appointed the wholesaler to sell those goods in the wholesale market at prices set by the manufacturer under section 60. The ordinary wholesale fraction is 50%. On those facts the distributor's levy is half the ordinary wholesaler's levy.

```oa-check
name: Registered distributor against ordinary wholesale, one quarter
inputs:
  turnover: 100000000
steps:
  - distributor_levy: turnover * 0.25 * 0.025
  - wholesale_levy: turnover * 0.50 * 0.025
  - difference: wholesale_levy - distributor_levy
expected:
  distributor_levy: 625000
  wholesale_levy: 1250000
  difference: 625000
```

## When to refuse or refer

- R-LK-SSCL-1: exempt articles and services. The First Schedule lists drive the result; escalate where an exemption is claimed beyond the exclusions above.
- R-LK-SSCL-2: confirm the date of import or supply before applying a change in threshold or exemption.
- R-LK-SSCL-3: sector treatment (financial services value addition, real estate improvement value). Escalate the computation of the value addition or improvement.
- R-LK-SSCL-4: cross-skill. Income tax, corporate tax, VAT and WHT go to the Sri Lanka skill for each.
- Never file or instruct filing; produce a working paper for practitioner review.

## Filing and payment

| Obligation | Due date | Source |
| --- | --- | --- |
| Chargeable import | At importation, collected by Customs | Section 19 |
| Payment, first month of the quarter | On or before the 20th day of the second month of the quarter | IRD SSCL page |
| Payment, second month | On or before the 20th day of the third month of the quarter | IRD SSCL page |
| Payment, third month | On or before the 20th day of the month after the quarter ends | IRD SSCL page |
| Quarterly return | On or before the 20th day of the month after the quarter ends | IRD SSCL page |
| Quarterly return channel | IRD e-Services or the applicable IRD office, in the specified form | Section 8 and IRD SSCL page |

## Completion checklist

- [ ] Activity class and fraction identified for each stream
- [ ] Exclusions, bad debts and VAT removed from turnover
- [ ] 2.5% applied to liable turnover, not gross turnover
- [ ] Registration test checked on the quarter and on four quarters
- [ ] Monthly payments and the quarterly return diarised

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for scope of liability, turnover definitions, exclusions, registration threshold, rate and liable-turnover fractions, payment and return dates on the IRD SSCL page | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Social%20Security%20Contribution%20Levy%20%28SSCL%29.aspx | 2026-11-14 |
| IRD 2025/26 tax chart for the liable turnover table and earlier registration figures | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Principal Act, sections 2–4, 8, 16–19, 60 and First and Second Schedules | https://www.ird.gov.lk/en/publications/Acts_SSCL/SSCL_Act_No.%2025_2022_E.pdf | 2026-11-22 |
| Consolidated Act up to March 2024 for the registration tests before 1 July 2026 | https://www.ird.gov.lk/en/publications/Acts_SSCL/SSCL_Cons_Act_-_2024_Changes.pdf | 2026-11-22 |
| Amendment Act No. 24 of 2025 for fuel, container terminal and financial services exemptions | https://www.ird.gov.lk/en/publications/Acts_SSCL/SSCL_Act_No_24_2025_E.pdf | 2026-11-22 |
| Amendment Act No. 10 of 2026 for thresholds, dates and motor vehicle treatment | https://www.ird.gov.lk/en/publications/Acts_SSCL/SSCL_Act_No_10-2026_E.pdf | 2026-11-22 |
| IRD implementation notice for the 2026 registration and motor vehicle changes | https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/780/PN_SSCL_2026-04_1_E.pdf | 2026-11-22 |
| VAT Amendment Act No. 14 of 2026, section 8, for the 20.5% financial services VAT rate | https://www.parliament.lk/uploads/acts/gbills/english/6427.pdf | 2026-11-22 |
