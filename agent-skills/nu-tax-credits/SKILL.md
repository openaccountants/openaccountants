---
name: nu-tax-credits
description: "Apply Nunavut personal-credit eligibility and separate refundable credits in a calendar 2026 tax review, with the latest actual annual forms explicitly labelled 2025-2026 filing cycle. Covers cost-of-living adjusted income and single-parent supplement, political-credit limitation, volunteer-service evidence, ended carbon-credit payments and unresolved investment-credit claims. Retains the corporate ordinary-rate example and allocation checks without certifying an unsupported investment or children's activity credit."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nu-tax-credits"
  jurisdiction: "CA-NU"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nunavut credits and corporate-rate handoffs v 2.0

## Scope

Use this method with `nu-individual-return` and the federal T1 workpaper. It owns the optional personal-credit and separate refundable-credit questions; the individual-return method owns current ordinary territorial bands and basic personal amount. It also retains the existing corporate-rate/credit investigation and construction-company case. A corporate credit, monthly child benefit, direct tax credit, ordinary credit base and refundable amount are different jobs.

The current ordinary corporate figures below are 2026. The latest annual NU428/NU479 read is 2025, for the 2025-2026 filing cycle; use that label wherever its figures or fields are used. The official legal catalogue expressly says its consolidation is not up to date. Do not relabel an old consolidation or annual form as complete 2026 law, or derive an indexed 2026 optional amount from a rounded prior-year figure. [Act catalogue](https://www.nunavutlegislation.ca/en/consolidated-law/income-tax-act-consolidation), [actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

### Answer layer

- The cost-of-living credit is refundable and based on adjusted net income, not a non-refundable amount only for people with positive territorial tax.
- The political amount is separately limited after the cost-of-living credit in actual NU479. Being displayed on a refundable-credit form does not make the whole preliminary political credit refundable.
- The current volunteer programme differs from the old 200-hour/firefighter-only description. Establish the actual qualifying service and year, then use the correct amount and direct-credit line.
- The Nunavut carbon credit ended, with the last payment in April 2025. Do not promise continuing quarterly payments or federal-benefit stacking from this skill.
- The former blanket 45% risk-capital regime and children's physical-activity credit are not usable guidance without the missing official basis. Keep their investigation records, not an invented entitlement.

## Ask the client first

1. What return year, individual/corporation/trust, actual residence/arrival/departure and business permanent establishments apply?
2. What are reconciled federal net/taxable income, the NU479 adjusted-income reductions, T2203 allocation where applicable, and territorial tax before optional credits?
3. What marital/custody/dependant ages and impairment facts support a single-parent supplement or another family claim? Who else claims the same person/amount?
4. For volunteers or political contributions, what service dates, qualifying activities, compensation, written certification, candidate and original official receipts exist?
5. For investments, what actual legal programme, issuer registration before issuance, securities, cash/acquisition dates, certificate, relationship, prior claims, disposition/holding and carryover evidence exists?
6. For corporate work, what supported CCPC/small-business deduction, associated-group business limit, income nature, permanent-establishment allocation and any specific Agreement/exemption or incentive decision apply?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, period and conditions | Official source |
|---|---|---|
|Cost-of-living basic credit, actual 2025 annual cycle | 2% of adjusted net income, capped CAD 1,500. Refundable, with Nunavut-residence and statutory adjusted-income conditions; not a reduction that requires positive territorial tax | [NU479 2025](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [Act s.4.1](https://www.nunavutlegislation.ca/en/file-download/download/public/7081) |
|Single-parent supplement, actual 2025 annual cycle | 2% of adjusted net income above CAD 60,000, capped CAD 255.12, with actual single-parent/custody/child conditions. Do not substitute the government's generic 300 summary for this statute/form amount | [NU479 2025](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [Act s.4.1(1.3)-(1.5)](https://www.nunavutlegislation.ca/en/file-download/download/public/7081) |
|Political preliminary credit, actual 2025 annual cycle | 100% through CAD 100; otherwise CAD 100 plus 50% of the excess, capped CAD 500. Actual claim has the additional remaining-territorial-tax limit after cost-of-living credit | [NU479 2025 both pages](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [Act s.5](https://www.nunavutlegislation.ca/en/file-download/download/public/7081) |
|Volunteer direct credit, actual 2025 annual cycle |CAD 722 for qualifying residence and at least 50 eligible hours, with the distinct firefighting/SAR conditions below. It is not a 500 expense base or a 200-hour federal test | [2024 amending Act ss.3-5](https://www.nunavutlegislation.ca/en/file-download/download/public/8136), [actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf) |
|Nunavut ordinary corporate small-business rate,2026 | 3% on the qualifying business-limit base, ordinarily up to CAD 500,000 before applicable eligibility, association, allocation and reduction rules | [Government 2026 sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [CRA corporate rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) |
|Nunavut ordinary corporate higher rate,2026 | 12% on the applicable remaining territorial base; do not assume all investment income has the same combined federal burden as eligible active income | [Government 2026 sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [CRA corporate rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) |
|Federal rates used in the retained ordinary corporate case | 9% net for an eligible CCPC claiming the ordinary small-business deduction;15% net after the ordinary general reduction. Special zero-emission and financial-sector rules are separate | [CRA corporate rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) |

### Cost of living: compute the correct income and refundability

1. Establish year-end Nunavut residence, individual status and the statutory income base. On actual 2025 NU479 line 1 is federal 23600, reduced by specified 24400/25000 amounts and treaty-exempt foreign income at the printed stages/floors. A resident with a business permanent establishment outside Nunavut uses the allocated income specified by CRA rather than all net income without adjustment. The territorial Act's income definition excludes the specified social-assistance/paragraph 110(1)(f) amounts; a return field name alone does not override that law. [Actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [Act s.4.1(1)-(1.1)](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [CRA allocation instruction](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).
2. Compute the dated basic credit and, only with the necessary facts, the single-parent supplement. The parent definition covers the stated unmarried/separated status, dependent minor or impaired adult child and shared-care threshold. A positive taxable-income or positive-territorial-tax prerequisite is not imposed just because the old skill called it non-refundable. Do not default to the maximum from full-year residence alone. [Act s.4.1](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).
3. Keep the federal northern-residents deduction separate. It can change taxable income through its federal workpaper; it does not replace the cost-of-living adjusted-net-income calculation. It is wrong to infer that the two computations have no possible income interaction merely because their form locations differ. Use actual deductions/allocated income in the relevant year. [Act s.4.1 income definition](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).
4. Compute political contributions separately using the qualifying candidate, election period and receipt. Actual 2025 NU479 limits the political claim to the smaller of its preliminary amount and remaining NU428 line 66 tax after the cost-of-living total, with a zero floor. Attach required receipts for paper filing. Do not use the political amount to create an additional refundable balance beyond that limitation. [Act s.5](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

The Government of Nunavut overview says the single-parent maximum is 300, while the actual 2025 NU479 and the published Act s.4.1(1.3) say 255.12. Use the statute/form figure for this explicitly dated calculation. The exact 2026 current amendment/annual-form position is a named confirmation item, not silently set to either figure. [Government overview](https://www.gov.nu.ca/en/taxation-and-insurance/income-tax), [Act](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

### Volunteer service: territorial evidence is not the federal test

For the actual 2025 programme, distinguish eligible firefighting and eligible search-and-rescue service and their permitted combination. Firefighting eligibility includes unpaid service apart from reasonable expense reimbursement, membership in the qualifying municipal fire department and the required minimum service period. Qualifying hours include specified calls/on-call, training and meetings, with the required written confirmation. SAR has its own recognised-organisation/activities and certification route; do not copy every firefighter membership requirement onto SAR. The 2024 amending Act applies from 2025 and provides specific indexation/transitional text. Obtain the exact year amount rather than multiplying an already rounded 722 by a guessed annual index. [Amending Act ss.3-5](https://www.nunavutlegislation.ca/en/file-download/download/public/8136).

This is a direct credit in Part C of actual 2025 NU428, line 65, not an ordinary line 58315 amount multiplied by the territorial lowest rate. The actual 2025 source requires the current 50-hour test, not the federal 200-hour requirement. Preserve the evidence of service, certification and compensation and check the year's exact eligibility. The 2026 amount/annual field remains unconfirmed here. [Actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [2024 Act](https://www.nunavutlegislation.ca/en/file-download/download/public/8136).

### Carbon payments and child/family credits

The official CRA 2025 information states that the Nunavut carbon credit ended and its final payment was April 2025. The old ongoing April/July/October/January schedule and automatic federal Canada Carbon Rebate stack are not certified for 2026. Retain past payment notices for reconciliation; historical eligibility or an old entitlement does not create a future quarterly payment. [CRA 2025 changes](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html).

The Nunavut child benefit is a separate monthly benefit administered using the benefit application and T1 information, not a line 58440 cost-of-living credit. Actual NU428 line 58440 is the disability amount; NU479 carries cost-of-living credits. The original “T1 line 11700 basic personal amount carryover” was also wrong; obtain the actual federal net/taxable income and relevant personal/tuition fields. `nu-individual-return` owns the T1/territorial return sequence. [Actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

The old Nunavut children's physical-activity 500 claim, disability addition and line 58326 are not established by the official annual form or the statutes read. Keep activity receipts as evidence for a programme inquiry, but do not claim an Ontario/Manitoba-style credit under a Nunavut label. NU428's separately documented young-child credit has different eligibility and is not a sports-expense credit. The exact current 2026 optional family amounts must be checked against the correct year's law/form. [Actual 2025 NU428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf).

### Risk capital: retain the investigation, remove the invented blanket regime

Do not calculate a flat 45% credit or send a taxpayer to obtain a supposed standard T2 C-NU certificate from NBCC merely because the old file says so. The actual Income Tax Act's investment-credit provision is s.6.1 and refers to certificates under the Risk Capital Investment Tax Credits Act, S.N.W.T.1998,c.22. The published capital Act has separate labour-sponsored, employee, community-endorsed and direct territorial-business regimes, not the single 2012 act/regime described before. The official consolidations list subsequent amendments. [Income Tax Act s.6.1](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [capital Act](https://www.nunavutlegislation.ca/en/file-download/download/public/203), [current capital-Act catalogue](https://www.nunavutlegislation.ca/en/consolidated-law/risk-capital-investment-tax-credits-act-consolidation).

Preserve the entire claim workpaper: investor identity/residence/entity type, issuer registration and class, actual securities/payment/acquisition date, arm's-length/major-shareholder and connected-person facts, official certificate and issuing authority, tax year/carryover history, available territorial tax, holding/disposition/redemption and recapture conditions. Confirm a current operative programme and the applicable class before applying any rate or cap. A certificate is necessary evidence, not proof that every listed credit amount or period is correct.

The older published s.6.1 includes tax-use limits and distinct carryback/carryforward conditions, and the capital Act gives different rules for different classes. Current 2026 programme availability, certificate format, rate/tier, annual/lifetime amounts, issuer asset/employee tests, restricted sectors and holding/recapture mechanics were not established by a full current amendment/regulation read. Keep them on the named unconfirmed list. Do not replace the old 45% with a different historical percentage and call that current verification. [Income Tax Act s.6.1](https://www.nunavutlegislation.ca/en/file-download/download/public/7081), [capital Act and notice](https://www.nunavutlegislation.ca/en/consolidated-law/risk-capital-investment-tax-credits-act-consolidation).

Likewise, federal SR&ED, exploration/resource deductions and the investor credit belong to different taxpayers or bases and may have reduction/interaction rules. The old “no federal grind” promise is not adopted without its statutory analysis. Do not claim an investment credit in an unsupported line 58980 or invent a certificate-entry screen. Obtain the actual personal/corporate form and legal programme decision first.

### Corporate rates, allocation and training questions

For the ordinary 2026 case, establish the taxpayer's actual CCPC and small-business eligibility, business limit after sharing/reductions, income type and Nunavut allocation. The territorial low/higher rates apply to their respective supported bases. The ordinary combined 9%+3%=12% and 15%+12%=27% are **computed sums for the stated ordinary active-income conditions**, not universal effective corporate rates. Passive investment income, special activities, credits and refundable federal taxes can change the result. [Government 2026 sheet](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf), [CRA corporation rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html).

Use T2 Schedule 5 and the applicable Nunavut corporation calculation for the actual permanent-establishment allocation. A common wages/revenue formula is not an unconditional rule for every industry. Do not invent “Schedule 481 equivalent” or put a corporate computation on NU428. Where the actual corporation return/credit schedule is not in hand, retain a prepared workpaper and identify the missing schedule/fields.

The published Income Tax Act records s.6.3 business training credit as repealed in 2019. The old statement that any qualifying training wages generate a current refundable territorial credit is unsupported. Training expenditure and approved-programme evidence remain useful for investigating a separately authorised current incentive; a current programme or legislative reinstatement must be proved before a claim. [Act s.6.3](https://www.nunavutlegislation.ca/en/file-download/download/public/7081).

For an Inuit-owned company, trust or designated organisation, obtain the actual entity and exemption/Agreement provisions. Inuit ownership alone does not establish either an additional credit or universal exemption/taxability. Procurement preferences and economic-development support are separate from a tax deduction. Specific Article 24/Article 29 and Inuit-owned land/organisation cases remain a specialist legal workpaper, not a percentage adjustment inferred here.

## Boundary and exception table

| Original code or missing fact | Correct response |
|---|---|
|R-NU-1, residence unknown or outside ordinary claim | Establish actual residence and any valid non-resident/allocated-income rule rather than rejecting every territorial-tax job |
|R-NU-2, part-year residence | Use actual claimant/proration limits; no day-times-entire-tax shortcut |
|R-NU-3, missing investment certificate | Do not claim; establish the actual programme and authorised certificate, not a guessed T2 C-NU format |
|R-NU-4, unregistered issuer | Do not claim without actual eligibility/registration and issuance-timing evidence |
|R-NU-5, Inuit entity/Agreement issue | Refer the actual structure and provision; neither blanket exemption nor automatic standard tax is inferred |
|R-NU-6, contested corporate allocation | Obtain the actual Schedule 5/legal allocation before applying Nunavut rates |
|R-NU-7, shelter/partnership/investment structure | Independent specialist analysis of eligibility, relationship, securities, tax use and recapture, not a standard flat-credit default |
|No positive territorial tax | Does not by itself bar refundable cost-of-living credit; political credit still has its separate limitation |
|Unknown family status/income | No assumed maximum cost-of-living supplement; request the facts changing eligibility |
|Activity receipt | Does not establish a Nunavut sports credit merely because a different province has one |
|Volunteer service | Use actual territorial eligibility/certification/year, not the federal 200-hour test |
|Carbon payment after final historical payment | Do not promise a continuing 2026 payment without a new official entitlement |

## Worked cases

### Case 1: a refund can exist without positive territorial tax

For the actual 2025 filing cycle, an otherwise qualifying full-year resident has adjusted net income 22000 and no territorial tax before NU479. Basic cost-of-living credit is 440. A qualifying political contribution 500 produces a preliminary 300 credit, but the remaining-tax limitation is zero, so no political amount is added. NU479 is 440. This does not by itself establish the person's final federal T1 refund. It corrects the former refusal based solely on no positive tax. [Actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

```oa-check
name: Nunavut 2025 refundable living credit without positive tax
inputs:
  adjusted_net_income: 22000
  territorial_tax: 0
  qualifying_contributions: 500
steps:
  - basic_living: min(1500, adjusted_net_income * 0.02)
  - political_preliminary: min(500, min(qualifying_contributions, 100) + max(0, qualifying_contributions - 100) * 0.5)
  - political_allowed: min(political_preliminary, max(0, territorial_tax - basic_living))
  - refundable_form_total: basic_living + political_allowed
expected:
  basic_living: 440
  political_preliminary: 300
  political_allowed: 0
  refundable_form_total: 440
```

### Case 2: retained construction-company ordinary corporate example

“Aqsarniit Construction Ltd.” is the same hypothetical wholly Inuit-owned CCPC with its only permanent establishment in Iqaluit,300000 qualifying active taxable income, no investment income, no associated corporation sharing its fully available ordinary business limit and no investment-credit claim. For its calendar 2026 ordinary tax workpaper, federal 9% gives 27000, Nunavut 3% gives 9000 and the total is 36000, computed 12%. This follows stipulated ordinary eligibility, not an exemption/taxability conclusion from Inuit ownership. A real file still needs its CCPC, allocation and exemption documents. The old unsupported comparisons with several other provinces and procurement-revenue prediction are not tax inputs. [CRA ordinary rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html), [Nunavut 2026 rates](https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf).

```oa-check
name: Nunavut construction CCPC ordinary qualifying income 2026
inputs:
  active_taxable_income: 300000
  available_small_business_base: 500000
steps:
  - eligible_base: min(active_taxable_income, available_small_business_base)
  - federal_tax: eligible_base * 0.09
  - nunavut_tax: eligible_base * 0.03
  - total: federal_tax + nunavut_tax
  - effective_percent: total / active_taxable_income * 100
expected:
  eligible_base: 300000
  federal_tax: 27000
  nunavut_tax: 9000
  total: 36000
  effective_percent: 12
```

### Case 3: single-parent supplement and the political limitation

For the actual 2025 annual cycle, stipulate a qualifying single parent with adjusted net income 80000, eligible contribution 900 and NU428 line 66 tax 2000. Basic 1500 plus supplement 255.12 gives 1755.12. The preliminary political 500 is limited to 244.88, so NU479 is 2000, not 2255.12. Prove the actual single-parent/custody conditions before selecting this case. [Actual 2025 NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf), [Act s.4.1](https://www.nunavutlegislation.ca/en/file-download/download/public/7081).

```oa-check
name: Nunavut 2025 single parent and limited political credit
inputs:
  adjusted_net_income: 80000
  territorial_tax: 2000
  qualifying_contributions: 900
steps:
  - basic_living: min(1500, adjusted_net_income * 0.02)
  - single_parent: min(255.12, max(0, adjusted_net_income - 60000) * 0.02)
  - living_total: basic_living + single_parent
  - political_preliminary: min(500, 100 + max(0, qualifying_contributions - 100) * 0.5)
  - political_allowed: min(political_preliminary, max(0, territorial_tax - living_total))
  - form_total: living_total + political_allowed
expected:
  basic_living: 1500
  single_parent: 255.12
  living_total: 1755.12
  political_preliminary: 500
  political_allowed: 244.88
  form_total: 2000
```

## When to refuse or refer

Do not apply an unconfirmed investment/children's-activity/training incentive, assumed maximum credit, current carbon payment or generic jurisdiction transplant. Continue the supported ordinary/cost-of-living work rather than refuse the entire file for an unrelated niche gap. Refer actual disputed residence, Agreement/Indigenous entity, corporate allocation, investment-security/recapture and family/dependant issues with their documents. An AI rewrite and a Git commit are not professional approval.

## Filing and payment

For the actual 2025 personal return, complete NU428 after the federal workpaper, including the direct volunteer amount where eligible. Complete NU479's adjusted income, basic/single-parent total and political limitation separately, then carry its result to the actual refundable-credit field. NU428's final amount goes to T1 line 42800 and NU479 to 47900; line 58440 is a disability base, not cost of living. Attach schedules and required receipts on a paper return; retain receipts and certified service/investment evidence for review. Final 2026 annual field references remain unconfirmed. [Actual forms](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf), [NU479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf).

For corporate work, prepare the correct T2, Schedule 5 allocation and actual Nunavut corporation/credit schedules for the year. Do not claim a current risk-capital or training amount from this skill without its current legal programme, approved documentation and actual fields. Return preparation, acceptance and payment are distinct: retain the authorised accepted submission, assessment and settlement evidence. This method has not filed, registered, paid or obtained a certificate.

## Completion checklist

- Actual year/territory/entity and federal income/territorial tax reconciled.
- Cost-of-living adjusted income, resident eligibility and refundability correctly identified; no automatic maximum or tax-positive gate.
- Single-parent facts, statutory/form amount and political limitation separately checked.
- Volunteer year, unpaid-service/activity/certification and direct-credit treatment established.
- Ended carbon payments reconciled historically without a future schedule promise.
- Young-child/disability/tuition fields not mislabelled as sports or living credits.
- Investment issuer/class/certificate, relationships, current programme, holding/recapture and carryover facts retained as unresolved until proved.
- Corporate ordinary eligibility/base/allocation established; Inuit ownership not treated as an automatic tax percentage.
- Dated actual 2025 forms and current 2026 ordinary corporate rates kept distinct; all other unconfirmed items named.
- Accepted filing/assessment/payment evidence retained where an authorised filer acts.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
|Read for 2020 consolidation ss.4.1,5,6.1 and 6.3, including refundability, political credit, investment certificate/use/carryover structure and the recorded training-credit repeal; not a complete 2026 consolidation |https://www.nunavutlegislation.ca/en/file-download/download/public/7081| 2026-11-14|
|Read for the official warning and later amendment list; older PDF not relabelled current |https://www.nunavutlegislation.ca/en/consolidated-law/income-tax-act-consolidation| 2026-11-14|
|Read for capital Act header and separate class/certificate structure and bounded historic rate provisions; not certified as the current full programme/regulation |https://www.nunavutlegislation.ca/en/file-download/download/public/203| 2026-11-14|
|Read for capital Act's explicit later-amendment warning, not proof of a current 2026 flat rate |https://www.nunavutlegislation.ca/en/consolidated-law/risk-capital-investment-tax-credits-act-consolidation| 2026-11-14|
|Read all three pages for the volunteer/SAR replacement, evidence conditions, indexation/transitional text and 2025-onward application;2026 exact amount not inferred from a rounded base |https://www.nunavutlegislation.ca/en/file-download/download/public/8136| 2026-11-14|
|Read actual 2025 NU428 for ordinary disability/young-child categories, direct volunteer and territorial-tax handoff; not a 2026 annual form |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-c/5014-c-fill-25e.pdf| 2026-11-14|
|Read both actual 2025 NU479 pages for adjusted income, basic/single-parent calculation, political computation/limitation and refundability |https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5014-tc/5014-tc-25e.pdf| 2026-11-14|
|Read for 2025 changes, ended carbon payment, volunteer and refundable-credit eligibility and child-benefit routing; current-year optional figures still need their own source |https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nunavut/5014-pc.html| 2026-11-14|
|Read for the generic living-credit/single-parent summary; its 300 maximum is identified as conflicting with the actual statute/form, not used |https://www.gov.nu.ca/en/taxation-and-insurance/income-tax| 2026-11-14|
|Read for the one-page 2026 personal/corporate rate tables; unrelated tax tables not used as credit authority |https://www.gov.nu.ca/sites/default/files/documents/2026-01/January_2026_Nunavut_Tax_Rate_Sheet_-_EN.pdf| 2026-11-14|
|Read for ordinary federal small/general rates and territorial low/high rate/base distinctions; special exceptions kept separate |https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html| 2026-11-14|

Not yet confirmed: final 2026 NU428/NU479 fields and exact optional personal-credit/benefit amounts, including volunteer indexation and the current single-parent statute-versus-generic-summary difference; a complete current investment Act/regulation/amendment/programme read, exact authorised certificate and issuer agency/registration procedure, annual/lifetime limits, holding/recapture and federal interactions. Specifically the old 45%,1000000 investment/450000 credit,2000000 lifetime/900000 credit, four-year holding,50% assets/employees, restricted-sector list and automatic no-federal-grind claims are not established and are not usable figures. No official basis was found for the asserted Nunavut physical-activity 500/additional 500 credit or a reinstated current refundable business-training credit. Exact corporate schedule fields, special-industry allocation and Agreement/entity exemptions remain claimant-specific work. The actual 2025 annual cycle is explicitly dated; ordinary 2026 corporate rates are separately supported.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nu-tax-credits` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nu-tax-credits. If neither is available, confirm every figure against the official source pages cited above before relying on it.
