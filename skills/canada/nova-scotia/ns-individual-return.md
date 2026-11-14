---
name: ns-individual-return
description: "Nova Scotia calendar 2026 individual provincial tax: indexed bands and principal credits, corrected HST, separate age and volunteer credits, annual filing map and dated CRA family-benefit computations."
version: "2.0"
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
depends_on:
  - ca-fed-t1-return
  - ca-fed-cpp-ei
  - ns-tax-credits
---

# Nova Scotia individual return v2.0

## Scope

Calculate Nova Scotia provincial individual income tax for **calendar 2026**, in CAD, coordinated with the federal T1. Nova Scotia began indexing the relevant brackets and credit bases in 2025; the old frozen-band description is not current. Use `ns-tax-credits` for detailed personal/corporate credit decisions. No accountant has approved this version.

### Quick reference

| Portion of 2026 taxable income, CAD | Provincial rate | Official source |
|---|---|---|
| Over 0 through 30,995 | 8.7900% | https://www.novascotia.ca/personal-income-tax-rates-and-indexation |
| Over 30,995 through 61,991 | 14.9500% | https://www.novascotia.ca/personal-income-tax-rates-and-indexation |
| Over 61,991 through 97,417 | 16.6700% | https://www.novascotia.ca/personal-income-tax-rates-and-indexation |
| Over 97,417 through 157,124 | 17.500% | https://www.novascotia.ca/personal-income-tax-rates-and-indexation |
| Over 157,124 | 21.00% | https://www.novascotia.ca/personal-income-tax-rates-and-indexation |

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

## Ask the client first

1. Which tax year and benefit-payment period, and which province on the last day of the year? Obtain arrival, departure, death and interprovincial moving dates, Canadian residence status and every business permanent establishment.
2. What are taxable income, net income and adjusted family net income, separately? Obtain all slips, foreign income, deductions, CPP/EI details and the spouse's return. Do not default an unknown marital status to single.
3. Which age, dependant, disability, pension, tuition, medical, donation, volunteer and investment facts apply? Obtain certificates, receipts, shared claims and carryover assessments before using a credit.
4. Is this an individual, an unincorporated business or a corporation? Identify self-employment, farming/fishing, instalments and prior assessments. A corporate credit cannot be placed on a personal return.
5. What is the requested output: a planning estimate, the actual annual filing or a separate CRA-administered benefit calculation? Do not call a partial provincial computation a final refund.

## The method, step by step

### Assemble the return and the review file

1. Reconcile T4, T4A, T5, T3, pension and EI slips with records, including multiple seasonal employers. Include taxable investment and foreign income; do not infer taxable income from gross salary. Complete the federal T1 steps before the provincial calculation. Business income and substantiated expenses go through T2125; farming and fishing need their own statements and inventory/CCA records.
2. Determine the correct province and special-return route. December residence normally controls an individual's province, not the employer's office. Newcomers/emigrants, deaths, bankruptcy, non-residents and business income allocated across provinces need the applicable annual instructions, proration and, where required, T2203. They are not all automatically ineligible.
3. Apply each provincial band only to its portion of taxable income. Apply the provincial credit rate to eligible credit bases, not the taxpayer's top marginal rate. Keep base CPP/EI credit amounts distinct from deductions for additional CPP; never duplicate the same amount as both a deduction and a credit.
4. Use the year's provincial 428 form for tax, non-refundable credits, additions and reductions. Non-refundable credits normally stop at provincial tax owing. Use only authorised transfer/carryover rules; a family credit does not become two credits because two returns are filed.
5. Reconcile provincial tax to T1 line 42800. Enter refundable provincial credits only through the actual year's specified schedule and T1 line 47900 where directed. Separately display benefit payments administered by the CRA; they are not an automatic offset of the T1 balance.
6. Complete federal tax, provincial adjustments, CPP, EI where applicable, instalments, tax withheld and other refundable items before calculating the T1 balance. The gross provincial figure or a combined marginal rate cannot establish a refund.
7. In CRA-certified NETFILE software select the correct province and year, review all generated schedules and validation messages, and submit only after the taxpayer or authorised representative approves. Save the submission confirmation and filed schedules. If using paper, use the year's package and attach the specified forms and certificates. CRA My Account is for account access and the resulting assessment, not a substitute for the NETFILE return.
8. Compare the notice of assessment with the approved computation and carryover schedules, check the balance and benefit notices, and retain source documents. For an error, wait for the assessment, then use CRA account > Tax returns > Change my return, or the permitted ReFILE/paper route. Save the adjustment confirmation; elections, benefit applications and personal-detail updates can have separate procedures. [CRA change-a-return instructions](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

### Federal tax, capital income and planning

Calculate federal tax separately using the current federal table. For ordinary income the marginal rate before credits is the sum of the two rates that apply at that exact income. Do not reuse a combined table with obsolete thresholds, or apply the ordinary-income rate directly to cash dividends or a gross capital gain. [CRA 2026 rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html).

Canadian eligible and other-than-eligible dividends require the appropriate federal gross-up followed by the province's dividend tax credit on the taxable amount. Source the actual slip classification; do not assume every small-company dividend has the same treatment. Capital transactions require capital-versus-business classification, adjusted cost base, proceeds, losses, the applicable inclusion rule and any supported exemption. Principal-residence relief requires the designation and factual tests, not an automatic exemption for any home sale. For a qualifying-business or farm/fishing exemption, establish the ownership, asset and use tests and current indexed limit rather than using the old guide's generic ceiling.

Load `ca-fed-t1-return`, `ca-fed-cpp-ei` and `ca-capital-gains` for those federal jobs, and verify their current periods before use. RRSP deductions, pension splitting, incorporation, donations, employment expenses, CCA and loss timing need a comparison using actual taxable income, deduction room, eligibility, cash requirements and benefit effects. Do not recommend incorporation using a single combined corporate rate, or claim a deduction saves the same rate for every dollar. Do not silently alter another skill to resolve an inconsistency.

### HST and provincial programmes are separate

HST is a supply tax, not an individual income-tax bracket. Determine taxable, zero-rated or exempt status and place of supply first. Reconcile tax collected and eligible input tax credits through `canada-gst-hst`. Small-supplier registration, new-housing rebates and point-of-sale relief each have their own tests. This return skill does not authorise the old generic housing-rebate ceilings or an assumed provincial children's-clothing/book rebate. [CRA place-of-supply and HST-rate instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html).

### Indexed credits, separate age credit and family programmes

The 2026 provincial indexation notice and current table replace the old frozen thresholds and the income-reduced basic-personal supplement. Do not reapply an obsolete maximum-income restriction to the 2026 basic personal/spouse/eligible-dependant maxima. The ordinary age **base** is different from the separate CAD 1,000 age **tax credit** with its taxable-income condition. Eligibility, spouse income, support, the chosen claimant and available tax still matter. [Current indexation table](https://www.novascotia.ca/personal-income-tax-rates-and-indexation); [indexation notice](https://notices.novascotia.ca/files/ftb-taxation/ftb-tn-personal-income-tax-indexation-update-2025-12-31.pdf); [age-tax-credit factsheet](https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-age-tax-credit-en.pdf).

For the **2025 historical annual filing map**, NS428 Part A computes tax, Part B non-refundable bases and Part C provincial tax/adjustments/reductions. Pension base is capped at CAD 1,173 in that actual-year guide, not the old CAD 1,000. Tuition and education use NS(S11), eligible written current-year transfers and assessed carryforwards; old carryforwards do not transfer freely. Medical claims need the applicable twelve-month period, reimbursements and the actual annual threshold worksheet, not a blanket deduction of only 3% without checking the cap. Use actual disability certification/transfer rules rather than the old unsupported CAD 8,015. Donations need eligible receipts and the current-year provincial schedule. [2025 NS instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

The 2025 NS guide also sets the other-than-eligible dividend credit at 1.5%, replacing the old 2.99% assertion for that year. The current 2026 ordinary credit percentages/limits not explicitly confirmed in the current source table are held under Sources; do not assume federal and provincial changes occur together. Pension splitting, disability transfer and tuition allocation need the actual taxpayer/dependant facts before deciding the claimant. [2025 annual changes](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

The low-income reduction is a family-based, non-refundable calculation with a sole claimant, not a refundable benefit. The 2025 instructions distinguish the spouse/eligible-dependant addition and other qualifying children and prohibit counting the same child twice. Do not reuse the old invented higher family-income starting threshold without the actual year's law/form. The exact current formula remains held until its readable source is obtained. ALTC and the NS child benefit are separate CRA cash payments with explicitly dated benefit periods, in the table. There is no supported “NS-BEN” application in the package read. The Poverty Reduction Credit, temporary cost-of-living assistance and graduate-retention/scholarship-rebate claims need their own current programme evidence; no old benefit maximum or first-three-years rebate is authorised by this skill. [2025 NS tax map](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html); [CRA current benefits](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html).

The volunteer credit is **CAD 500 refundable**, subject to service and reporting conditions, not a CAD 3,000 federal base copied into the provincial return or CAD 500 multiplied by 8.79%. Its six-month/participation/reporting conditions differ from the federal eligible-hours rule. The historical 2025 claim is NS479 line 1. [Current provincial volunteer programme](https://www.novascotia.ca/volunteer-firefighter-and-ground-search-and-rescue-worker-tax-credit); [2025 NS479 instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html).

### Corporate incentives and retained specialist topics

A business-owner's T1 is not a corporation's incentive claim. Digital media requires an eligible corporation/product and certificate; the formula, regional test, cost base, assistance and expiry are in `ns-tax-credits`. Capital investment and research credits likewise require corporate/property/work eligibility and separate application evidence. No corporate refundable amount belongs on an employee's personal return merely because the employee works on the project.

NS HST is 14% from 1 April 2025 under the actual supply/transition rules. Separate the HST return, input tax credits, new-housing relief and point-of-sale exceptions from this T1 computation. Do not repeat the old general 15%, housing “36% below CAD 481,500” or blanket rebate assertions. A principal-residence sale still needs its designation and tests. A business commute across the provincial border does not select province from where the day's work occurred. Multiple employers, seasonal income, EI and CPP require full slip reconciliation. Self-employment CPP includes current contribution ceilings and additional CPP, so the old one-band contribution formula is not reused. [CRA HST](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html).

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Retained CAD 75,000 employment workpaper, corrected provincial slice

Assume an ordinary full-year NS resident, taxable income after deductions CAD 75,000, the 2026 basic personal base and no age/dependant/other provincial credits. For this illustration the separately verified provincial CPP and EI **credit dollars** supplied by the return workpaper are CAD 400 and CAD 100. These are example inputs, not maximum statutory contributions. Apply all three applicable indexed bands, then the basic-personal and supplied credits. The result below is only the provincial slice, not net pay or a federal/provincial final balance. The old frozen-band CAD 9,662 gross/CAD 8,485 net and combined CAD 19,737 are not carried forward. [2026 bands and bases](https://www.novascotia.ca/personal-income-tax-rates-and-indexation).

```oa-check
name: NS employment provincial slice indexed 2026
inputs:
  income: 75000
  bpa: 11932
  cpp_credit: 400
  ei_credit: 100
steps:
  - band_1: max(0, min(income, 30995) - 0) * .0879
  - band_2: max(0, min(income, 61991) - 30995) * .1495
  - band_3: max(0, min(income, 97417) - 61991) * .1667
  - band_4: max(0, min(income, 157124) - 97417) * .175
  - band_5: max(0, income - 157124) * .21
  - gross_tax: band_1 + band_2 + band_3 + band_4 + band_5
  - bpa_credit: bpa * 0.0879
  - provincial_tax: round(max(0, gross_tax - bpa_credit - cpp_credit - ei_credit), 2)
expected:
  gross_tax: 9526.9628
  provincial_tax: 7978.14
```

### Family benefit comparison across the income threshold

For the **July 2026-June 2027 ALTC period**, assume the claimant meets all benefit conditions and has two qualifying children. At AFNI CAD 25,000 the annual entitlement is CAD 375, or an illustrative full-quarter CAD 93.75. A couple with one qualifying child and AFNI CAD 40,000 has a maximum CAD 315 before a CAD 500 reduction, so entitlement is zero. These use the assessed income for the benefit period, not automatically current employment income or a deduction from T1 tax. [CRA current NS benefit page](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html).

```oa-check
name: NS ALTC family-period comparison July 2026 June 2027
inputs:
  income_a: 25000
  children_a: 2
  income_b: 40000
  children_b: 1
steps:
  - annual_a: max(0, 255 + children_a * 60 - max(0, income_a - 30000) * 0.05)
  - quarter_a: annual_a / 4
  - annual_b: max(0, 255 + children_b * 60 - max(0, income_b - 30000) * 0.05)
expected:
  annual_a: 375
  quarter_a: 93.75
  annual_b: 0
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: NS current indexation page: complete 2026 brackets, annual indexation and current principal credit bases | https://www.novascotia.ca/personal-income-tax-rates-and-indexation | 2026-11-14 |
| Read for: NS indexation notice, both pages: 2024/2025/2026 bases and elimination of old income-based supplement reduction | https://notices.novascotia.ca/files/ftb-taxation/ftb-tn-personal-income-tax-indexation-update-2025-12-31.pdf | 2026-11-14 |
| Read for: NS age-tax-credit factsheet: separate current CAD 1,000 credit, age/residence and taxable-income conditions | https://www.novascotia.ca/sites/default/files/documents/1-3953/tax-101-personal-income-tax-age-tax-credit-en.pdf | 2026-11-14 |
| Read for: CRA 2025 NS annual guide: actual-year changes, pension/tuition, Parts A-C, low-income family rules, NS479 and historical filing boxes | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/nova-scotia/5003-pc.html | 2026-11-14 |
| Read for: NS volunteer programme: current refundable-dollar amount, qualifying service and annual reports | https://www.novascotia.ca/volunteer-firefighter-and-ground-search-and-rescue-worker-tax-credit | 2026-11-14 |
| Read for: CRA NS benefit page: July 2026-June 2027 ALTC formula, monthly child benefit and AFNI tests | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-nova-scotia.html | 2026-11-14 |
| Read for: CRA 2026 rate page: federal ordinary-income bands | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| Read for: CRA HST page: NS 14% effective date and supply/transition rules | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html | 2026-11-14 |
| Read for: ITA section 150(1)(b),(d): filing dates and exceptions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return instructions: assessment prerequisite and actual correction route | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

Not yet confirmed: Final 2026 NS428/NS479/tuition annual forms and box numbers; exact 2026 LITR formula/threshold and current pension, disability, medical, donation and dividend-credit figures beyond the sourced indexed maxima (the legislature PDF and annual NS428 PDF could not be read); current Poverty Reduction Credit, graduate retention/scholarship rebate and temporary cost-of-living programmes; 2026 housing/POS rebate ceilings, federal CPP/LCGE/capital-inclusion figures and blanket incorporation-rate comparison. The scoped 2025 figures are historical, not default 2026 values.
