---
name: fi-individual-cross-border-residence
description: >
  Screen Finnish individual residence on arrival and departure, distinguish
  domestic status from treaty residence, assemble a nonresidency claim and
  reconcile foreign-tax credits and confirmed carryovers.
  Income-specific taxation, treaties, statutes and named Finnish accountant review remain open.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.4
---

# Finland individual cross-border residence v0.4

## Who this applies to

Use this draft for an individual arriving in Finland, leaving Finland or maintaining homes and activity in several countries. It is a residence-screening workflow, not a tax calculation or a conclusion about company residence, PE, social insurance or immigration status.

Vero's guidance bases domestic residence on the main abode/home or continuous presence exceeding six months. Temporary absences can leave continuity intact, and the period can cross calendar years. Exactly six months is not enough for that presence route, but the home route must still be checked. Do not replace the test with a universal 183-day count. [Detailed residence guidance, sections 2.4–2.5][detailed]

## Arrival and departure evidence

Income Tax Act sections 9 and 11 were directly checked on 23 October 2026: the home/presence and citizen-departure rules have a statutory basis, with separate positions for specified diplomatic, state and international service. Section 9 also distinguishes resident/nonresident parts of a year. Check those special facts before applying the ordinary timeline. [Income Tax Act][law]

Prepare a dated timeline with arrival, departure, every absence, home availability, work and family facts. Registration in a population system does not itself resolve tax residence; the detailed guidance requires the actual situation to be assessed. A short stay can still involve a main home. [Detailed guidance, section 2.4][detailed]

For a foreign citizen departing Finland, check whether the main home remains or continuing presence still meets the residence test before treating departure as ending residence. Special statutory positions and a change of citizenship need their own analysis. [Nonresident-income guidance][nonresident]

## Finnish citizens leaving Finland

Vero describes continued residence for the relocation year and the following three tax years. Earlier nonresidency requires a specific request and evidence that substantial Finnish ties have ended for the relevant period. A planned temporary move of two or three years does not establish that those ties were broken. [Three-year guidance][three]

The detailed guidance distinguishes ties broken at departure from ties broken later: the latter generally leads to a claim from the following year's beginning. It describes a claim on the year's tax return, in MyTax or using Form 50A. Check the actual facts and legal effective date before selecting the claimed period. [Detailed guidance, sections 3.2 and 6.1][detailed]

## Treaty residence and income scope

Domestic nonresidency and treaty residence are separate decisions. Vero's treaty guidance discusses permanent home, centre of vital interests, habitual abode, citizenship and competent-authority agreement. Use the actual treaty's wording and sequence rather than importing a generic tie-breaker. [Treaty-article guidance][treaties]

A person can remain subject to domestic residence rules while a treaty limits Finland's taxing rights. Conversely, nonresidency does not itself remove taxation of every Finnish-source receipt. Classify employment, pensions, rent, investments and business income separately and verify the applicable source and treaty article. [Nonresident-income guidance][nonresident]; [Treaty-article guidance][treaties]

No universal withholding rate or treaty exemption is supplied here. The relief section below concerns preparation under the credit/exemption framework; it does not determine the applicable treaty result. See the [payroll draft](fi-employer-payroll.md) for the ordinary wage-reporting preparation framework; it does not settle cross-border payroll eligibility.

## Relief for foreign tax: claim and reconciliation

Vero describes credit and exemption as separate double-tax-relief methods. Identify the applicable treaty/income treatment first. Report the foreign income, income category, source country and foreign tax even where Finnish withholding or prepayments have already been reduced to anticipate relief. [Individual double-tax relief][relief]

Under the credit method, the foreign tax credit cannot exceed the Finnish tax attributable to the income concerned. Establish the eligible foreign tax and the Finnish limitation calculation before reconciling the result; do not deduct the entire foreign assessment automatically. This Guide does not calculate that limitation from gross receipts. [Individual double-tax relief][relief]

The detailed guidance says unused credits can be used during the next five tax years for the same income source and category, within the relevant limitation. Once confirmed for carryover, the authority applies them automatically, oldest first, before current-year creditable foreign taxes. Preserve the original claim/decision and a vintage-by-vintage schedule; automatic later use does not remove the need to establish the original credit. [Detailed relief guidance, section 3.2.6][relief-detail]

Prepare a reconciliation of each year's eligible tax, limitation, credit used and unused balance. Keep foreign assessments, evidence of payment, income/expense allocation, currency conversion and treaty analysis. This is a practical workpaper, not a conclusion that every foreign levy qualifies. Refunds, amended assessments, loss years and changes of income category need separate review.

## Preparation checklist

This is our practical evidence framework:

- Record all citizenships, historical residence decisions and the intended claim period.
- Reconcile travel and accommodation records with the actual home and work timeline.
- Identify family, property, business and other continuing connections.
- Obtain foreign tax-residence evidence and identify the actual treaty.
- Inventory income by category, source, payer and date, with deductions and foreign tax records.
- Preserve the claim, supporting evidence, authority decision and changes in circumstances.

The outcome must identify the facts relied on, the domestic status, any treaty conclusion and the periods covered. A timeline alone does not establish a legal result.

## Worked example

Assume a Finnish citizen relocates during 2026 and no earlier nonresidency claim succeeds. The ordinary three-following-years window covers 2027, 2028 and 2029. Its last year is 2029; 2030 follows it. This does not prove nonresidency in 2030: home, presence and special rules still require review. The calculation is year arithmetic, not a statutory status engine.

```oa-check
name: Finland assumed departure residence window
inputs:
  relocation_year: 2026
  following_years: 3
steps:
  last_year_of_ordinary_window: relocation_year + following_years
  year_after_window: last_year_of_ordinary_window + 1
expected:
  last_year_of_ordinary_window: 2029
  year_after_window: 2030
```

### 2. Credit ceiling with an unused balance

Assume EUR 1,600 is eligible creditable foreign tax and EUR 1,200 is the correctly computed Finnish limitation, with no earlier unused credits. The current credit is EUR 1,200 and the unused amount is EUR 400. This assumes the credit method applies and does not establish eligibility or calculate the limitation itself.

```oa-check
name: Finland assumed foreign tax credit ceiling
inputs:
  eligible_foreign_tax: 1600
  established_finnish_limit: 1200
steps:
  credit_used: min(eligible_foreign_tax, established_finnish_limit)
  unused_credit: eligible_foreign_tax - credit_used
expected:
  credit_used: 1200
  unused_credit: 400
```

### 3. Earlier unused credit is used first

Assume the same source/category, a valid confirmed EUR 400 carryover still within its permitted years, EUR 500 current eligible foreign tax and EUR 700 current limitation. The earlier credit uses EUR 400, leaving EUR 300 capacity for current tax. Current unused credit is EUR 200. No claim is made about other credits or income baskets.

```oa-check
name: Finland assumed credit vintage ordering
inputs:
  confirmed_prior_credit: 400
  current_eligible_foreign_tax: 500
  current_limit: 700
steps:
  prior_used: min(confirmed_prior_credit, current_limit)
  remaining_limit: current_limit - prior_used
  current_used: min(current_eligible_foreign_tax, remaining_limit)
  current_unused: current_eligible_foreign_tax - current_used
expected:
  prior_used: 400
  remaining_limit: 300
  current_used: 300
  current_unused: 200
```

## Ask the client first

- What citizenships and prior residence decisions apply?
- Which homes were available, to whom, and on what dates?
- What travel, family, work and business connections continued after the move?
- Is the move permanent, and what evidence supports that?
- Which income and foreign tax assessments are involved?
- Has a nonresidency or treaty-residence claim already been made or decided?

## Sources and review limits

Official Vero text retrieved through the search index on 23 October 2026:

- [Income Tax Act][law], sections 9 and 11, read directly from embedded official Finnish statutory text. Retrieval hashes are in the country research record; selected sections do not establish a full amendment or treaty audit.

- [Detailed individual residence guidance][detailed].
- [Finnish citizens and the three-year rule][three].
- [Taxation of nonresident individuals][nonresident].
- [Treaty articles guidance][treaties].
- [Individual double-tax relief][relief]; [detailed individual relief guidance][relief-detail], section 3.2.6.

Not yet confirmed: remaining source-income and amendment scope, exact day-count and temporary-absence application, full substantial-ties and special-position cases, each treaty, income-specific source/rate rules, complete foreign-tax relief law, forms and current procedures. Named Finnish accountant review remains outstanding; the independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action). Cross-border coverage remains partial.

[law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535

[detailed]: https://www.vero.fi/en/detailed-guidance/guidance/48999/tax-residency-nonresidency-and-residency-in-accordance-with-a-tax-treaty--natural-persons4/
[three]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/moving_away_from_finland/finnish_citizens_and_the_3year_rul/
[nonresident]: https://vero.fi/en/detailed-guidance/guidance/334489/taxation-of-income-received-by-nonresidents-natural-persons/
[treaties]: https://www.vero.fi/en/detailed-guidance/guidance/85707/articles-of-tax-treaties3/

[relief]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/moving_away_from_finland/tax-treaties/elimination_of_double_taxation__receipt/
[relief-detail]: https://vero.fi/en/detailed-guidance/guidance/77657/relief-for-international-double-taxation-in-natural-persons-tax-assessment/
