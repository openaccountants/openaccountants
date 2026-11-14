---
name: sri-lanka-sscl
description: "ALWAYS read this skill before touching any Sri Lanka Social Security Contribution Levy (SSCL) work for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Use whenever asked about SSCL on turnover for importers, manufacturers, service providers, wholesalers and retailers, or financial-service businesses in Sri Lanka. Trigger on phrases like Sri Lanka SSCL, Social Security Contribution Levy, 2.5% turnover levy Sri Lanka, liable turnover, SSCL registration threshold, SSCL return. Gives the 2.5% rate, the liable-turnover fractions by activity (100%, 85%, 50%, 25%), the Rs. 15 million quarterly and Rs. 60 million four-quarter registration test, the excluded articles, monthly payment and quarterly return dates."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sri-lanka-sscl"
  jurisdiction: "LK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sri Lanka Social Security Contribution Levy (SSCL), v2.0

Built from the law: not yet approved by an accountant. Produced by OpenAccountants (openaccountants.com). Not tax advice. Period covered: quarters in the year of assessment 2026/27.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country and authority | Sri Lanka, Inland Revenue Department (IRD) |
| Tax | Social Security Contribution Levy, a turnover levy separate from VAT and income tax |
| Principal Act | Social Security Contribution Levy Act, No. 25 of 2022, in force from 1 October 2022; amended by the SSCL (Amendment) Act No. 24 of 2025 |
| Basis | Accrual; charged for every quarter on liable turnover |
| Currency | LKR |

- **In:** every taxable person (individual or entity, including a body of persons, an executor, an NGO and a charitable institution) who imports any article, manufactures any article, provides a service of any description, or carries on wholesale or retail sale of any article including importation and sale (other than a sale by the manufacturer already covered as a manufacturer).
- **Status:** in force. The IRD page for SSCL, read on 14 November 2026, sets out the levy as current. Re-confirm at the date of supply if a change is reported.
- **Not here:** VAT (`sri-lanka-vat`), income tax (`sri-lanka-income-tax`, `sri-lanka-corporate-tax`), withholding (`sri-lanka-withholding-tax`).

## Ask the client first

1. Activity class: importer, manufacturer, service provider (financial services, real estate, other) or wholesaler and retailer (registered distributor or other)?
2. Turnover by quarter and for the last four quarters, excluding exempt articles and services.
3. SSCL registration status and TIN.
4. Any excluded items: pharmaceuticals, Special Commodity Levy articles sold unprocessed by the importer, exports, petrol, diesel or kerosene sold at a filling station, LP gas, fresh milk, green leaf, cinnamon or rubber bought from local producers.
5. Bad debts written off or recovered in the quarter; VAT included in the figures.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Rate | 2.5% of liable turnover | Every quarter from 1 October 2022 | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Social%20Security%20Contribution%20Levy%20%28SSCL%29.aspx |
| Liable turnover, importation of any article | 100% of turnover | Value for VAT under VAT Act section 6, less exempt articles | same |
| Liable turnover, manufacture of any article | 85% of turnover | Sums receivable for articles manufactured and sold in Sri Lanka | same |
| Liable turnover, financial services | 100% of the value addition attributable to financial services | As under the VAT Act section 25C notification | same |
| Liable turnover, land and improvements | 100% of the value of improvement | Sale value less market value of the bare land, VAT Act section 5(7) | same |
| Liable turnover, other services | 100% of turnover | Section 3(2)(c)(iii) | same |
| Liable turnover, sale by a registered distributor of a Sri Lankan manufacturer or producer | 25% of turnover | Section 3(2)(d) | same |
| Liable turnover, other wholesale or retail sale, including importation and sale | 50% of turnover | Section 3(2)(d) | same |
| Registration threshold | Turnover for a quarter over or likely over Rs. 15,000,000, or for four consecutive quarters over or likely over Rs. 60,000,000 | Any period from 1 January 2024; excluding exempt articles or services | same |

### Steps

1. Classify each activity. A person with several activities computes each class separately.
2. Take turnover for the quarter (sums receivable, received or not), excluding exempt articles and services, bad debts incurred in the quarter (add back recoveries), VAT, and any Export Development Rebate for an approved international event.
3. Apply the liable-turnover fraction for the class.
4. Multiply liable turnover by 2.5%.
5. Pay monthly on self-assessment and file the quarterly return (Filing and payment below).
6. Register when the quarter or four-quarter test is met.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Activity class unclear | Apply the higher fraction (up to 100%) and flag |
| Registration borderline | Treat as registrable and flag |
| Whether SSCL applies to a supply | Apply 2.5% on the liable fraction and flag for review |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Applying 2.5% to gross turnover for a class below 100% | Wrong: over-states the levy; apply the fraction first |
| Export of an article | Excluded from turnover |
| Petrol, diesel or kerosene sold at a filling station; LP gas | Excluded from wholesale and retail turnover |
| Pharmaceuticals | Excluded |
| Special Commodity Levy article sold by the importer without processing | Excluded |
| Fresh milk, green leaf, cinnamon or rubber bought from a local producer | Excluded |
| Bad debt recovered in a later quarter | Included in that later quarter's turnover |
| Exempt articles (Part IA) and exempt services (Part II) of the First Schedule | Out of turnover; the schedule list itself is not reproduced here |

## Worked cases

### Case 1: manufacturer

A manufacturer sells articles it makes in Sri Lanka for Rs. 100,000,000 in a quarter. Liable turnover is 85%.

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

A wholesaler with Rs. 100,000,000 of quarterly sales of goods made by a Sri Lankan manufacturer. Selling as that manufacturer's registered distributor puts 25% of turnover in the base; selling as an ordinary wholesaler puts 50% in. The distributor route halves the levy.

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
- R-LK-SSCL-2: changes made by the SSCL (Amendment) Act No. 24 of 2025. Its text was not read; escalate any question that turns on it.
- R-LK-SSCL-3: sector treatment (financial services value addition, real estate improvement value). Escalate the computation of the value addition or improvement.
- R-LK-SSCL-4: cross-skill. Income tax, corporate tax, VAT and WHT go to the Sri Lanka skill for each.
- Never file or instruct filing; produce a working paper for practitioner review.

## Filing and payment

| Obligation | Due date | Source |
| --- | --- | --- |
| Payment, first month of the quarter | On or before the 20th day of the second month of the quarter | IRD SSCL page |
| Payment, second month | On or before the 20th day of the third month of the quarter | IRD SSCL page |
| Payment, third month | On or before the 20th day of the month after the quarter ends | IRD SSCL page |
| Quarterly return | On or before the 20th day of the month after the quarter ends | IRD SSCL page |
| Channel | Online through IRD e-Services | IRD SSCL page |

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
| Read for the SSCL section (registration test and the liable turnover table) of the IRD tax chart, the latest on the site | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |

Not yet confirmed: the text of the SSCL (Amendment) Act No. 24 of 2025 and what it changed (not linked from the IRD SSCL page; documents.gov.lk did not serve it to a script); the full First Schedule lists of exempt articles and services; any SSCL change announced for 2026/27 that is not on the IRD SSCL page.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sri-lanka-sscl` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sri-lanka-sscl. If neither is available, confirm every figure against the official source pages cited above before relying on it.
