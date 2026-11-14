---
name: ns-tax-credits
description: "Nova Scotia 2026 personal and corporate credits: correct refundable volunteer amount, dated family benefits, two-limb digital-media calculation, approved-project capital credit and annual-form evidence limits."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ns-tax-credits"
  jurisdiction: "CA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Nova Scotia tax credits v2.0

## Scope

Apply Nova Scotia personal and corporate credit rules for **2026**, in CAD. Keep annual income-tax claims separate from the **July 2026-June 2027 benefit period** and clearly dated **2025 annual form** instructions. Personal NS428/NS479 work, corporate DMTC/capital/R&D work and provincial applications have different bases, claimants and evidence. This publication has no accountant approval.

### Quick reference

| Item | Figure and conditions | Official source |
|---|---|---|
| 2026 basic personal / spouse / eligible-dependant maxima | CAD 11,932 each where the relevant status/support tests are met; convert eligible bases at 8.79%; no old income-based supplemental reduction | https://notices.novascotia.ca/files/ftb-taxation/ftb-tn-personal-income-tax-indexation-update-2025-12-31.pdf |
| 2026 age amount | CAD 5,826 maximum base; verify actual age/eligibility; not a separate income-based supplement | https://notices.novascotia.ca/files/ftb-taxation/ftb-tn-personal-income-tax-indexation-update-2025-12-31.pdf |
| Separate age tax credit | CAD 1,000 non-refundable tax reduction, age at least 65 by year end, NS resident on 31 December and taxable income below CAD 24,000; distinct from the ordinary age amount | https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-age-tax-credit-en.pdf |
| 2026 infirm dependant maximum | CAD 2,931 base for a qualifying infirm dependant aged at least 18, with the relevant support/income tests | https://notices.novascotia.ca/files/ftb-taxation/ftb-tn-personal-income-tax-indexation-update-2025-12-31.pdf |
| Current volunteer firefighter/ground SAR credit | CAD 500 refundable dollar credit; at least six months qualifying service and programme evidence; not a credit base | https://www.novascotia.ca/volunteer-firefighter-and-ground-search-and-rescue-worker-tax-credit |
| ALTC, July 2026-June 2027 | Annual CAD 255 individual OR couple, plus CAD 60 per child; reduce by 5% of AFNI above CAD 30,000; quarterly separate CRA payment | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html |
| NS child benefit, July 2026-June 2027 | Up to CAD 127.08 per month per qualifying child under 18; partial between AFNI CAD 26,000 and CAD 34,000; not CAD 150 per quarter | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html |
| Nova Scotia HST | 14% from 1 April 2025 for supplies governed by the NS place-of-supply and transition rules | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html |

| Item | Figure and conditions | Official source |
|---|---|---|
| DMTC ordinary | Lesser of 50% of qualifying expenditure and 25% of total expenditure; certified eligible product/corporation only | https://www.novascotia.ca/digital-media-tax-credit |
| DMTC regional | Lesser of 60% of qualifying expenditure and 30% of total expenditure if the prescribed outside-Halifax regional labour condition is met; not simply any Sydney address | https://www.novascotia.ca/digital-media-tax-credit |
| Qualifying-expenditure base | Eligible salaries + 65% of eligible remuneration + eligible marketing/distribution up to CAD 100,000 per product; apply the statutory cost exclusions | https://novascotia.ca/just/regulations/regs/incdigitalmedia.htm |
| DMTC period / certificate deadline | Qualifying expenditure before 1 January 2031; apply no later than 30 months after the expenditure tax-year end; Part A optional/Part B mandatory | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/nova-scotia-provincial-corporation-tax/nova-scotia-digital-media-tax-credit.html |
| Capital investment credit, post-30-September-2022 property | 25% of eligible property cost net of assistance; maximum CREDIT CAD 100 million per approved project duration; refundable, not a 20-year carryforward credit | https://www.novascotia.ca/capital-investment-tax-credit |
| Earlier capital investment cohort | 15% and maximum CREDIT CAD 30 million per approved project for the programme's pre-1-October-2022 cohort; not the current ordinary rate | https://www.novascotia.ca/capital-investment-tax-credit |
| Capital project / application | Qualifying project investment above CAD 15 million; application window extended through 31 December 2035; project and property must be approved | https://news.novascotia.ca/en/2026/09/04/capital-investment-tax-credit-extended |
| NS R&D credit | 15% of eligible NS R&D expenditure; fully refundable after taxes; NS permanent establishment and eligible work required; Schedule 340 within 18 months of year end | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/nova-scotia-provincial-corporation-tax/nova-scotia-research-development-tax-credit.html |

## Ask the client first

1. Which tax year and benefit-payment period, and which province on the last day of the year? Obtain arrival, departure, death and interprovincial moving dates, Canadian residence status and every business permanent establishment.
2. What are taxable income, net income and adjusted family net income, separately? Obtain all slips, foreign income, deductions, CPP/EI details and the spouse's return. Do not default an unknown marital status to single.
3. Which age, dependant, disability, pension, tuition, medical, donation, volunteer and investment facts apply? Obtain certificates, receipts, shared claims and carryover assessments before using a credit.
4. Is this an individual, an unincorporated business or a corporation? Identify self-employment, farming/fishing, instalments and prior assessments. A corporate credit cannot be placed on a personal return.
5. What is the requested output: a planning estimate, the actual annual filing or a separate CRA-administered benefit calculation? Do not call a partial provincial computation a final refund.

For corporate projects also collect corporate/PE status, product/property/activity classification, acquisition/payment/year-end dates, regional employee evidence, cost categories and assistance, group/project limits, preliminary decisions and final certificates. For personal volunteer/sports/food-bank work collect service reports or invoices, qualifying ages/programmes, reimbursement/duplicate claims and the actual claimant.

## The method, step by step

### Affordable living and other cash benefits

ALTC is a quarterly CRA payment, not a non-refundable line that multiplies by the provincial credit rate. Compute the dated annual benefit as `max(0, 255 + 60 * qualifying_children - 0.05 * max(0, AFNI - 30000))`. The base is CAD 255 for either an individual or a couple, not per adult. Use the assessed family-income period and actual custody/status. The NS child benefit is monthly with CCB; the current maximum and AFNI band are in the table. Do not put either on an invented NS-BEN schedule or simply net it against personal tax. [Current CRA programme page](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html).

The old guide's single parent/two children/AFNI CAD 25,000 ALTC example produces CAD 375 annually or CAD 93.75 for an illustrative full quarter; couple/one child/CAD 40,000 produces zero. Those examples remain below with the current benefit period. A CRA determination can reflect partial periods, changes and allocation; an annual formula does not promise all instalments. Poverty Reduction Credit and temporary affordability payments have separate qualifying programmes; their old generic age/income/maxima are held rather than treated as current tax credits.

### Indexed non-refundable bases, LITR and age

The 2026 basic personal/spouse/eligible-dependant and ordinary age maxima are sourced above. Do not retain the old frozen CAD 8,481 base or the old income-based supplementary amount. The separate age tax credit is a CAD 1,000 reduction in tax, subject to year-end residence, age at least 65 and taxable income below CAD 24,000; it is not an extra age-amount base multiplied by 8.79%. [Current indexation page](https://www.novascotia.ca/personal-income-tax-rates-and-indexation); [age-tax-credit factsheet](https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-age-tax-credit-en.pdf).

The **2025 annual instructions** allow the low-income reduction for a year-end NS resident aged at least 19, married/common-law or a parent, with a prison exclusion and specified deceased-return treatment. Choose a single family claimant, calculate adjusted family income from both returns, and distinguish CAD 300 spouse OR CAD 300 eligible dependant from CAD 165 for other qualifying dependent children. Do not count the same child in both categories. The guide defines those other children by age/status/residence and only one claimant. The old higher family threshold, blanket “all unused transfers” rule and exact current phase-out are not authorised without the actual year's readable law/form. The original single/CAD 18,000 LITR example is retained as a held calculation, not a current CAD 150 promise. [2025 CRA family rules](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

For pension, disability, medical, tuition, spouse transfers and donations obtain the actual year's worksheet, certification, receipt period, net reimbursements and assessed carryovers. The 2025 pension maximum is CAD 1,173 in that guide; do not use the old CAD 1,000 for that historical year. Current-year tuition transfer is limited by the permitted designation and own use; old carryforwards cannot be transferred. Provincial tax on split income, minimum tax, foreign tax credit and R&D recapture have separate NS428 adjustments; a low ordinary-income computation does not dispense with those checks. [2025 annual map](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

### Volunteer service: provincial conditions are not the federal hours test

The current provincial programme gives a refundable CAD 500 dollar credit. Qualifying volunteers must be resident at year end, serve at least six months, receive no wages/compensation beyond reasonable reimbursement/allowance, and satisfy the applicable participation/reporting test. Firefighters need at least 20% of calls/training/meetings and inclusion on the fire chief's report; ground search/rescue has its own organisation report. The programme describes the annual report due by 31 January following the service year. Do not replace those conditions with 200 hours, infer eligibility from 220 hours alone, or say 199 hours automatically bars the NS credit. The federal volunteer credit/exemption has separate conditions and is a separate calculation. [Current provincial programme](https://www.novascotia.ca/volunteer-firefighter-and-ground-search-and-rescue-worker-tax-credit).

The historical 2025 return enters CAD 500 on NS479 line 1; it is not CAD 43.95 (500 times 8.79%). Death cases have the guide's day-of-death residence and other conditions. Keep the service evidence and reports with the claim. [CRA 2025 NS479 instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

### Food bank and children's sports/arts: do not call live programmes repealed

The 2025 CRA instructions expressly include the food-bank credit for farmers. It is 25% of qualifying NS-produced agricultural products donated to an eligible NS registered-charity food bank, with the linked charitable-donation claim. Shared claims cannot exceed the gift, unused eligible amounts can carry forward five years subject to the farming-income condition, and death/bankruptcy have their specified allocation rules. The historical form route is NS428 line 88 from the qualifying donations field 62150. A purchase of groceries or a donation to any charity is not automatically this farming credit. [2025 CRA instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

The sports/arts programme is refundable and uses NS479; it has not simply been repealed. The official factsheet and 2025 guide describe qualifying expenditure up to CAD 500 per child, under 19 at year end, with qualifying supervised arts/sports/development/nature activities. The 2025 guide specifies six-week weekly, five-day camp or specified eight-week choice-programme tests. Ordinary food, accommodation, travel and beverages are excluded; qualifying integral uniform/equipment costs can be included. Reduce non-taxable reimbursement/assistance and prevent duplicated deductions/credits; payments to the spouse or an under-18 provider and the specific emigration/death/bankruptcy restrictions need review. Shared claims cannot exceed the child's maximum, and disagreement can prevent either claimant. Do not multiply the cap by parents or treat a generic course as qualifying. The final annual-form conversion/output is held until the actual NS479 is read; do not promise a CAD 500 cash refund merely from a CAD 500 receipt. [Provincial factsheet](https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-childrens-sports-arts-refundable-tax-credit-en.pdf); [2025 annual rules](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

### Digital media: qualify the product and both expenditure bases

The corporation must be a taxable Canadian corporation incorporated in Canada/province, have an NS permanent establishment and not be the prescribed labour-sponsored venture corporation. Foreign ownership alone is not the blanket disqualification invented by the old guide. The product must meet the actual interactive educate/inform/entertain definition and two of text/sound/images. Ordinary application/operating-system software, primarily promotional or interpersonal-communication products and prohibited adult/hateful content are excluded. Do not import every NL product exclusion into NS, or add an unsupported requirement to own all copyright. [DMTC Regulations sections 2, 4-5](https://novascotia.ca/just/regulations/regs/incdigitalmedia.htm).

Build two supported workpapers. Qualifying expenditure is eligible salaries plus 65% of eligible remuneration plus eligible marketing/distribution up to CAD 100,000 per product. Total expenditure follows the prescribed eligible-production outlay plus eligible marketing/distribution less government assistance. Local permanent-establishment, arm's-length, directly-attributable, reasonable-cost and payment timing rules matter. Eligible salaries cannot be profit/revenue-based; contractor and subcontractor amounts need the regulation's look-through tests. Ordinary payment is within the expenditure year or 60 days after year end; the regulation has a subsequent-year rule for eligible late-paid salaries/remuneration. Marketing has a specific completion-related window and excludes ordinary order fulfilment/shipping. Do not treat every T4A or every overhead charge as qualifying labour. [Regulations sections 6-10](https://novascotia.ca/just/regulations/regs/incdigitalmedia.htm).

Take the lesser of the two percentage limbs in the table. For the regional uplift, at least half of eligible salaries must meet the normal-reporting-to-an-eligible-NS-establishment-outside-Halifax condition; a project title or mailing address alone is insufficient. Keep staff residence/reporting locations, timesheets and product cost allocations. Remove government assistance from the appropriate base and prevent overlapping section 41/47 expenditure claims; federal incentives require their own cost-base/assistance analysis. Do not add percentages to the entire project or freely stack assistance. [Current DMTC programme](https://www.novascotia.ca/digital-media-tax-credit); [Regulations sections 6-10](https://novascotia.ca/just/regulations/regs/incdigitalmedia.htm).

Part A preliminary eligibility is optional, not a mandatory pre-project condition. Part B tax-credit certificate application is mandatory no later than 30 months after the end of the tax year in which the costs were incurred, not 30 months after product completion. Include corporate standing, product evidence, expenditure statements and the prescribed employee/location/certification information. The programme now covers qualifying expenditure before 1 January 2031; “sunset 2025, likely extension” is stale. The CRA claim is T2 Schedule 5 line 567, single certificate number at line 838 or Schedule 347 for multiple certificates; file the certificates and retain records. Refundable credit offsets taxes first. [Current programme](https://www.novascotia.ca/digital-media-tax-credit); [CRA corporate instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/nova-scotia-provincial-corporation-tax/nova-scotia-digital-media-tax-credit.html).

### Capital Investment Tax Credit: approved project, refundable credit

Current eligible property acquired on/after 1 October 2022 attracts 25%, subject to the approved project's maximum credit, not a 15% non-refundable credit with twenty-year carryover. The property's cost is net of assistance and must fit the actual capital-asset/activity rules. The official programme describes qualified property for prescribed manufacturing/processing, farming, fishing, logging, grain storage, peat harvesting and qualifying freight/space activities. Personal assets, unsupported used/replacement costs and an ordinary acquisition without a qualifying project must not be swept into the base. The project investment threshold is above CAD 15 million, not a standalone CAD 2 million machine. [Current programme](https://www.novascotia.ca/capital-investment-tax-credit); [2026 extension](https://news.novascotia.ca/en/2026/09/04/capital-investment-tax-credit-extended).

Part A eligibility approval and Part B certificate are mandatory; preliminary application before acquisition is encouraged but should not be represented as a different invented statutory precondition. Once eligibility and property are established, the programme requires Part B within **18 months after the taxation year-end**. Assemble property invoices, dates, acquisition/available-use evidence, project costs, assistance and approval, then use the actual certificate/T2 route. The CAD 100 million ceiling is a **credit ceiling over the project**, not annual spending or an automatic claim each year. The earlier pre-October-2022 cohort uses its own rate/cap. The extension permits applications through the end of 2035; it does not remove property or project eligibility. Federal CCA/assistance interactions and recapture require separate analysis before a disposal or stacking recommendation. [Programme](https://www.novascotia.ca/capital-investment-tax-credit).

### R&D, film and investment-credit routes

NS R&D is a fully refundable 15% credit for eligible work and expenditure with an NS permanent establishment, not a CCPC-only cash promise. Prepare Schedule 340 within 18 months after year end, claim Schedule 5 line 566, and use Schedule 340/line 221 for any recapture. Disposal or conversion to commercial use can trigger recapture. Government assistance and the federal SR&ED base must be reconciled; being a software company does not establish eligible scientific research. [CRA current instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/nova-scotia-provincial-corporation-tax/nova-scotia-research-development-tax-credit.html).

The old film tax-credit and the current screen-production funding route are not interchangeable. A genuinely legacy credit needs production dates, actual transitional law and its certificate; a current grant needs its current programme decision and assistance treatment. The original asserted post-July-2015 closure and legacy exceptions cannot be used to create a current tax claim without that evidence. Do not route a film grant through the DMTC formula merely because both use media labour. This topic remains held under Sources until the actual current film programme and transition are read.

For **2025 annual filing only**, equity tax credit uses T1285/NSETC-1; innovation equity uses T225/NSIETC-1; venture capital uses T224/NSVCTC-1. Confirm approved issuer/fund, security, payment date, age/residence, certificates and all previous claims before considering any current rate or carryover. The old 35%/35%-45% catalogue, connected-person exclusion, holding period and annual cap are not current permission to invest or claim until the applicable programme law is read. The 2025 guide separately gives labour-sponsored venture credit at 20% up to CAD 2,000 with its certificate, not a generic equity rate. [CRA 2025 investment routes](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

### Filing, records and follow-up

Use the actual year's provincial 428 for tax/credits and 479 for specified refundable credits, with T1 line 42800/47900 only where directed. No NS-BEN form was established by the package read. Use CRA-certified NETFILE software or the actual paper package, review all calculations, obtain approval, save confirmation and check the assessment/benefit notices. Corporate and provincial certificate applications remain separate, with their own clocks. Do not assume a permitted tax-return adjustment extends a programme filing deadline. [CRA 2025 guide](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html); [CRA change-return process](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### ALTC comparison: retain both household examples

Single parent, two qualifying children, AFNI CAD 25,000: annual ALTC CAD 375 and illustrative full quarter CAD 93.75. Couple, one qualifying child, AFNI CAD 40,000: maximum CAD 315 less CAD 500 phase-out, floored at zero. These belong to the **July 2026-June 2027 payment period** and use that period's assessed AFNI. [CRA current benefits](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html).

```oa-check
name: NS ALTC two retained household examples
inputs:
  afni_a: 25000
  children_a: 2
  afni_b: 40000
  children_b: 1
steps:
  - annual_a: max(0, 255 + children_a * 60 - max(0, afni_a - 30000) * 0.05)
  - quarter_a: annual_a / 4
  - annual_b: max(0, 255 + children_b * 60 - max(0, afni_b - 30000) * 0.05)
expected:
  annual_a: 375
  quarter_a: 93.75
  annual_b: 0
```

### Halifax versus Sydney DMTC: apply both caps

Retain the old project's numbers. Assume certifications establish a Halifax eligible product with total expenditure CAD 1,000,000 and qualifying expenditure CAD 700,000 after assistance and all prescribed adjustments. Credit is the lesser of CAD 350,000 and CAD 250,000: **CAD 250,000**, not CAD 175,000. For the Sydney project assume the actual regional labour test is documented, total expenditure CAD 500,000 and qualifying expenditure CAD 400,000: lesser of CAD 240,000 and CAD 150,000 gives **CAD 150,000**, not CAD 120,000. If Sydney fails the regional test, ordinary limbs give CAD 125,000; the city name alone does not justify the uplift. [Current programme](https://www.novascotia.ca/digital-media-tax-credit).

```oa-check
name: NS DMTC ordinary and regional decision
inputs:
  halifax_qualifying: 700000
  halifax_total: 1000000
  sydney_qualifying: 400000
  sydney_total: 500000
steps:
  - halifax_credit: min(halifax_qualifying * 0.50, halifax_total * 0.25)
  - sydney_regional: min(sydney_qualifying * 0.60, sydney_total * 0.30)
  - sydney_without_regional: min(sydney_qualifying * 0.50, sydney_total * 0.25)
expected:
  halifax_credit: 250000
  sydney_regional: 150000
  sydney_without_regional: 125000
```

### Lunenburg seafood machine: project approval changes the answer

Retain the CAD 2,000,000 line in Lunenburg. It does **not** by itself meet a project threshold above CAD 15 million, so the actual standalone case cannot claim merely from the invoice. If it is instead proven eligible property in an approved qualifying project and the net eligible 2026 cost is CAD 2,000,000 with project cap available, 25% gives CAD 500,000. This is a conditional refundable credit after tax, not the old CAD 300,000 non-refundable balance carried twenty years. Do not invent a larger project to approve the real taxpayer. [Capital programme](https://www.novascotia.ca/capital-investment-tax-credit); [project threshold](https://news.novascotia.ca/en/2026/09/04/capital-investment-tax-credit-extended).

```oa-check
name: NS CITC approved-project conditional 2026 slice
inputs:
  net_eligible_property: 2000000
  available_project_credit_cap: 100000000
steps:
  - conditional_credit: min(net_eligible_property * 0.25, available_project_credit_cap)
expected:
  conditional_credit: 500000
```

### Halifax family and volunteer evidence

Retain Parents A and B, incomes CAD 40,000/CAD 20,000, ages 42 and children aged 8/11. Assume those income figures are already their taxable income, each has the sourced CAD 11,932 BPA, no spouse/eligible-dependant amount and separately evidenced provincial credit dollars of CAD 400/CAD 200. This is a component illustration: combined provincial tax after those stated inputs is CAD 3,131.06. Parent A's 220 volunteer hours alone is **not** enough for the NS claim; if the separate six-month/participation/report conditions are proven, the CAD 500 refundable provincial credit reduces that provincial net cash slice to CAD 2,631.06. Without that evidence do not claim it. This is not a complete T1 or a recomputed LITR entitlement. Current family AFNI CAD 60,000 yields zero ALTC under its separate period formula. The old CAD 43.95 saving was wrong. [Current bands/bases](https://www.novascotia.ca/personal-income-tax-rates-and-indexation); [volunteer criteria](https://www.novascotia.ca/volunteer-firefighter-and-ground-search-and-rescue-worker-tax-credit).

```oa-check
name: NS Halifax family known provincial components and conditional volunteer
inputs:
  income_a: 40000
  income_b: 20000
  bpa: 11932
  other_credit_a: 400
  other_credit_b: 200
steps:
  - gross_a: 30995 * 0.0879 + (income_a - 30995) * 0.1495
  - gross_b: income_b * 0.0879
  - tax_a: max(0, gross_a - bpa * 0.0879 - other_credit_a)
  - tax_b: max(0, gross_b - bpa * 0.0879 - other_credit_b)
  - combined: round(tax_a + tax_b, 2)
  - with_evidenced_volunteer: combined - 500
expected:
  combined: 3131.06
  with_evidenced_volunteer: 2631.06
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

Additional stops: corporate project/media work requires a final certificate and evidence for the right base and period; below-threshold standalone capital property does not become eligible by assumption. Volunteer hours alone do not pass provincial conditions. No-current-source investment, film, LITR, poverty or graduate incentive remains a held question, not a denial that the programme could exist.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: NS current indexation page and principal credit table: actual 2026 values and old income-based supplement removal | https://www.novascotia.ca/personal-income-tax-rates-and-indexation | 2026-11-14 |
| Read for: NS indexation notice both pages: annual credit maxima and scope of indexation | https://notices.novascotia.ca/files/ftb-taxation/ftb-tn-personal-income-tax-indexation-update-2025-12-31.pdf | 2026-11-14 |
| Read for: NS age-credit factsheet: separate CAD 1,000 tax reduction and actual age/residence/income conditions | https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-age-tax-credit-en.pdf | 2026-11-14 |
| Read for: CRA 2025 NS guide: historical Parts A-C, family LITR inputs, food-bank and sports/arts rules, investment-form routes and refundable volunteer line | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html | 2026-11-14 |
| Read for: NS current volunteer programme: refundable dollars, six-month/participation conditions and reporting | https://www.novascotia.ca/volunteer-firefighter-and-ground-search-and-rescue-worker-tax-credit | 2026-11-14 |
| Read for: CRA NS benefits: current dated ALTC formula and monthly child benefit | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html | 2026-11-14 |
| Read for: NS sports/arts factsheet, both pages: eligible expenditure, child/programme conditions and NS479 route | https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-childrens-sports-arts-refundable-tax-credit-en.pdf | 2026-11-14 |
| Read for: Current DMTC programme: ordinary/regional two-limb rates, project/corporation eligibility and application stages | https://www.novascotia.ca/digital-media-tax-credit | 2026-11-14 |
| Read for: DMTC Regulations sections 2-10: product/corporation exclusions, expenditure bases, payment, assistance and application deadline | https://novascotia.ca/just/regulations/regs/incdigitalmedia.htm | 2026-11-14 |
| Read for: CRA DMTC instructions: pre-2031 expenditure period, T2 destination and certificate handling | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/nova-scotia-provincial-corporation-tax/nova-scotia-digital-media-tax-credit.html | 2026-11-14 |
| Read for: NS Capital Investment Tax Credit page: acquisition cohorts, net eligible cost, refundable project ceilings and Part A/B process | https://www.novascotia.ca/capital-investment-tax-credit | 2026-11-14 |
| Read for: September 2026 official CITC extension: project threshold and 2035 application window | https://news.novascotia.ca/en/2026/09/04/capital-investment-tax-credit-extended | 2026-11-14 |
| Read for: CRA NS R&D page: eligible PE/work, refundable rate, deadline, T2 lines and recapture | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/nova-scotia-provincial-corporation-tax/nova-scotia-research-development-tax-credit.html | 2026-11-14 |
| Read for: Federal ITA section 150(1)(b),(d): ordinary/business/death filing rules | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return instructions: assessment and adjustment process | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

Not yet confirmed: Final 2026 personal annual forms/line numbers; readable current LITR formula/threshold, including the original single/18,000-income example (the legislature and NS428 PDF reads failed); exact final sports/arts expense-to-credit conversion until the actual NS479 is read; current non-indexed pension/disability/medical/donation/dividend details beyond the historical guide; current Poverty Reduction Credit, graduate and temporary affordability programmes; film-tax-credit closure/transitions and current film-production fund; current equity/innovation credit rates, caps, holding/control and assistance rules beyond the dated 2025 filing routes; corporate CITC recapture/CCA and federal assistance interactions not established by the programme overview. Never label those held figures current or substitute prior-year defaults.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ns-tax-credits` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ns-tax-credits. If neither is available, confirm every figure against the official source pages cited above before relying on it.
