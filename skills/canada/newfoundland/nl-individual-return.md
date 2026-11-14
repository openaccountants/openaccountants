---
name: nl-individual-return
description: "Newfoundland and Labrador individual income tax for calendar 2026: eight sourced bands, enacted personal/volunteer credits, annual-return workflow, benefit periods and regional, offshore and investment exceptions."
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
  - nl-tax-credits
---

# Newfoundland and Labrador individual return v2.0

## Scope

Compute Newfoundland and Labrador provincial individual income tax for the **2026 calendar year**, in CAD, alongside the federal T1. NL has its own provincial brackets and credits; Labrador is not a separate province. Use `nl-tax-credits` for detailed investment, benefit, corporate incentive and insurance-tax decisions. This is not an accountant-approved version.

### Quick reference

| Portion of 2026 taxable income, CAD | Provincial rate | Official source |
|---|---|---|
| Over 0 through 44,678 | 8.700% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 44,678 through 89,354 | 14.500% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 89,354 through 159,528 | 15.800% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 159,528 through 223,340 | 17.800% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 223,340 through 285,319 | 19.800% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 285,319 through 570,638 | 20.800% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 570,638 through 1,141,275 | 21.300% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| Over 1,141,275 | 21.800% | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |

| Item | Figure and conditions | Official source |
|---|---|---|
| 2026 basic personal base | CAD 13,094, credit at 8.7%; enacted retrospectively from 1 January 2026, not the superseded January payroll amount | https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| 2026 age/pension/disability maxima | Age CAD 7,142 subject to income reduction; pension CAD 1,000 subject to eligible income; disability CAD 7,549 with certification; these are bases, not refund dollars | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| 2026 spouse/eligible-dependant maximum | CAD 9,142 base each, subject to support/status and the person's income; alternatives, not both for the same person | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| 2026 volunteer firefighter OR search/rescue | CAD 6,000 base at 8.7% = derived CAD 522 maximum, non-refundable; eligible services and at least 200 hours; cannot claim both provincial volunteer categories | https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm |
| 2026 medical threshold | Deduct the lesser of 3% of net income and CAD 2,437 from eligible self/family medical expenses, with the applicable dependent rules | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| 2026 donations | 8.7% on the first CAD 200 of qualifying gifts; 21.8% on qualifying excess, subject to eligible-gift rules | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ |
| 2026 dividend tax credit | 3.2% of taxable other-than-eligible Canadian dividends and 6.3% of taxable eligible Canadian dividends; use grossed-up amount, not cash amount | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm |

| Item | Figure and conditions | Official source |
|---|---|---|
| NL Income Supplement, current CRA programme | Maximum annual CAD 520 single / CAD 589 with spouse, plus CAD 231 per child under 19; AFNI-dependent quarterly payment | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html |
| NL disability amount, current CRA programme | Maximum annual CAD 231 per DTC-eligible adult, subject to federal consumption-tax benefit and income-supplement eligibility; not the separate monthly disability benefit | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html |
| NL seniors benefit, July 2026 to June 2027 | Maximum CAD 1,882 annually per eligible family; qualifying age 64 by 31 December 2025; full at AFNI up to CAD 30,409 and partial above, subject to statutory rounding | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html |

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

Current ordinary taxable supplies whose place of supply is this province bear 15% HST, subject to zero-rating, exemption and specific rules. [CRA GST/HST rates and place of supply](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html).

HST is a supply tax, not an individual income-tax bracket. Determine taxable, zero-rated or exempt status and place of supply first. Reconcile tax collected and eligible input tax credits through `canada-gst-hst`. Small-supplier registration, new-housing rebates and point-of-sale relief each have their own tests. This return skill does not authorise the old generic housing-rebate ceilings or an assumed provincial children's-clothing/book rebate. [CRA place-of-supply and HST-rate instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html).

### Current credit computation and the source conflict resolved

The January 2026 CRA payroll guide lists a lower NL basic personal amount. It predates the enacted 2026 increase. Chapter 14, sections 1 and 5, changes the base to CAD 13,094 from 1 January 2026 and prevents further indexation of that amount before 2027; use the law and the updated provincial table. Do not use CAD 11,188 from the old payroll page for a final 2026 annual computation. [2026 amending Act](https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm); [updated provincial table](https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/).

Age, spouse, eligible dependant, infirm-dependant, caregiver and disability figures are conditional bases. The 2026 provincial table gives adoption maximum CAD 15,099, infirm-dependant/caregiver maxima CAD 3,553 and disability supplement maximum CAD 3,553. Check the relevant income reduction and support/certification tests before applying any maximum. Pension eligibility and the cap differ from the federal amount; child-care and student-loan credits require the actual eligible amount. Tuition and provincial education amounts use NL(S11), with assessed carryforward and designated current-year transfer; the provincial table retains CAD 200 full-time/CAD 60 part-time per eligible month. [Provincial 2026 table](https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/).

NL428 Part A is tax on taxable income, Part B the eligible non-refundable bases and Part C the rest of provincial tax. The **2025 filing map** places non-refundable investment credits before the low-income reduction; do not describe that reduction as a refundable NL479 benefit. It uses adjusted family income, a single family claimant and an authorised unused-spouse transfer. Regulation 18/26 prescribes CAD 842 basic/CAD 563 spouse-or-eligible-dependant additions for **2026**, but the actual indexed 2026 income thresholds still need their current source before this skill computes that reduction. Do not recycle the old approximate CAD 20,400/34,400 thresholds. [Act section 21.1](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm); [regulation 18/26](https://www.assembly.nl.ca/Legislation/sr/Regulations/rc260018.htm).

CRA-paid income supplement and seniors' benefits are distinct from the T1 tax reduction. Establish the payment year, age and prior-year assessed family income. The seniors' benefit is not an October-only GIS payment and is not entered as GIS at T1 line 14600. The early-childhood nutrition supplement, child benefit and disability support have their own eligible ages and payment rules. The old “CAD 60 monthly income supplement” and fixed CAD 1,516 senior amount must not be used as current benefit instructions. [CRA current NL benefits](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html).

### Investment, insurance and regional work

For DETC, the qualifying business's North East Avalon location means a different rate from the rest of the province. St. John's technology status alone does not produce a higher rate. The annual ceiling is a **credit** ceiling, not a CAD 50,000 investment ceiling. Obtain the Minister's certificate and use T1272; apply non-refundable use and carryover limits. Resort-property investments use their own T1297/certificate and venture funds their own certificate. None is a blanket cash refund. [2025 investment filing instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html); [official DETC FAQ](https://www.gov.nl.ca/fin/faq/tax-program/).

Insurance requires separate classification. The 15% retail sales tax under Revenue Administration Act section 91.1 is on taxable insurance premiums for NL risks, not a universal Insurance Companies Tax imposed on all policies. Personal-property, life, accident/sickness, automobile and other listed categories can be exempt; a policy covering several places requires a supported NL allocation. It is not HST and does not generate an HST input tax credit. Do not add a fictional 5% auto premium tax or a default 4% unlicensed-insurer rate to an insured's bill. [Insurance RST guidance](https://www.gov.nl.ca/fin/faq/faq-retail-sales-tax-on-inspremiums/); [Act section 91.1](https://www.assembly.nl.ca/legislation/sr/statutes/r15-01.htm).

Offshore employees, rotational workers, non-resident workers and people with an out-of-province home require a real residence and source-of-income analysis. Work on a platform does not establish eligibility for a northern-residents deduction, and a Labrador address alone does not prove the prescribed-zone residence period or travel limits. Load the federal northern-residence rules before using a daily deduction or a travel benefit. For fishers/farmers use the relevant statements, inventory and CCA rules; fishing EI benefits are distinct from ordinary employee EI or voluntary self-employed benefits. Expenses for vessels, gear, fuel and licences must be classified as current, capital or personal rather than deducted wholesale. Those specialist amounts remain held until their official federal source is read.

For high-income planning recompute every band, federal tax and benefit impact. The actual combined ordinary-income top statutory rate is derived 54.8% (33% federal plus 21.8% NL), not the old 54.3%; it does not apply to every dollar or every cash dividend. Pension splitting needs eligible pension income and the permitted election; an RRSP needs actual room and a deduction comparison; company extraction needs corporate tax plus salary/dividend personal tax, not “26% versus 54.3%”. The 2026 amendment changes eligible small-business provincial rates with separate effective dates and stub-year allocation, so it cannot support a universal incorporation recommendation. [Current federal rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html); [NL rates](https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/); [amending Act section 4](https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm).

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Simple provincial amount on CAD 50,000 taxable income

Assume an ordinary full-year single NL resident, no additional credits or minimum/split-income tax and taxable income already established at CAD 50,000. Apply the first two 2026 bands, then the enacted basic personal amount. Gross NL tax is CAD 4,658.68 and the provincial amount after this one credit is CAD 3,519.50. It is not a final T1 balance. Use actual CPP/EI and other credit facts when preparing a real return. [2026 rates and credit bases](https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/); [2026 amendment commencement](https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm).

```oa-check
name: NL basic provincial slice 2026
inputs:
  income: 50000
  bpa: 13094
steps:
  - band_1: max(0, min(income, 44678) - 0) * .087
  - band_2: max(0, min(income, 89354) - 44678) * .145
  - band_3: max(0, min(income, 159528) - 89354) * .158
  - band_4: max(0, min(income, 223340) - 159528) * .178
  - band_5: max(0, min(income, 285319) - 223340) * .198
  - band_6: max(0, min(income, 570638) - 285319) * .208
  - band_7: max(0, min(income, 1141275) - 570638) * .213
  - band_8: max(0, income - 1141275) * .218
  - gross_tax: band_1 + band_2 + band_3 + band_4 + band_5 + band_6 + band_7 + band_8
  - bpa_credit: bpa * 0.087
  - provincial_tax: round(max(0, gross_tax - bpa_credit), 2)
expected:
  gross_tax: 4658.676
  provincial_tax: 3519.50
```

### Volunteer category decision: choose one provincial amount, not neither federal nor provincial

Assume the evidence establishes eligibility for both provincial volunteer categories, at least 200 combined eligible hours and no disqualifying compensation treatment. The claimant has CAD 400 NL tax left before the volunteer credit. Either provincial category has a CAD 522 ceiling, so current provincial use is CAD 400 and the tax becomes zero; there is no CAD 122 refundable balance or carryover created by this claim. Do not claim two CAD 6,000 provincial bases. The separate federal volunteer claim is not prohibited merely because the provincial amount is claimed; check its own eligibility and honouraria election. [Act sections 17.3-17.4](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm); [2025 guide confirms federal/provincial coordination for its historical year](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html).

```oa-check
name: NL volunteer-category decision 2026
inputs:
  base: 6000
  provincial_tax_before: 400
steps:
  - credit_limit: base * 0.087
  - allowed: min(provincial_tax_before, credit_limit)
  - tax_after: provincial_tax_before - allowed
  - unused_not_refundable: credit_limit - allowed
expected:
  credit_limit: 522
  allowed: 400
  tax_after: 0
  unused_not_refundable: 122
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: NL Finance 2025/2026 comparison table: all current bands, ordinary credits, medical threshold, donation and dividend rates | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ | 2026-11-14 |
| Read for: NL Income Tax Act sections 9-23, 31 and 40: credit conditions/order, volunteer coordination, low-income transfer and allocation | https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm | 2026-11-14 |
| Read for: 2026 chapter 14 sections 1-5: basic-personal and volunteer increases, corporation-rate dates and retrospective commencement | https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm | 2026-11-14 |
| Read for: Regulation 18/26 sections 3 and 5: separate 2025/2026 LITR amounts and commencement | https://www.assembly.nl.ca/Legislation/sr/Regulations/rc260018.htm | 2026-11-14 |
| Read for: CRA current NL benefits: income supplement, disability amount, senior amount, eligibility and payment periods | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html | 2026-11-14 |
| Read for: CRA 2025 NL annual instructions and NL428: historical Parts A-C, credit forms and low-income-transfer path | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html | 2026-11-14 |
| Read for: CRA 2025 NL428, all pages: historical credit order, investment forms and LITR formula only | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5001-c/5001-c-25e.pdf | 2026-11-14 |
| Read for: Official DETC FAQ: geography, eligibility, credit cap, certificate, carryovers and redemption | https://www.gov.nl.ca/fin/faq/tax-program/ | 2026-11-14 |
| Read for: NL insurance RST FAQ: taxable/exempt policies, fees, allocation and unregistered sellers | https://www.gov.nl.ca/fin/faq/faq-retail-sales-tax-on-inspremiums/ | 2026-11-14 |
| Read for: Revenue Administration Act section 91.1: insured premium tax, allocation, collection and refund mechanics | https://www.assembly.nl.ca/legislation/sr/statutes/r15-01.htm | 2026-11-14 |
| Read for: CRA current-year table: federal and NL 2026 ordinary-income bands | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| Read for: CRA January 2026 NL payroll table: read to identify its superseded BPA, not relied on for the amended figure | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nl-jan/t4032nl-january-general-information.html | 2026-11-14 |
| Read for: CRA HST page: place-of-supply and classification rules | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html | 2026-11-14 |
| Read for: ITA section 150(1)(b),(d): filing dates including business and death exceptions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return instructions: assessment and adjustment process | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

| CRA GST/HST place-of-supply opening rates: current participating-province rate and supply classification | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html | 2026-11-14 |

Not yet confirmed: Final 2026 annual forms and box mapping; actual indexed 2026 LITR phase-out income thresholds (the CAD 842/563 components are confirmed); 2026 age-credit income threshold and full income-reduction worksheets not shown in the provincial maxima table; current federal northern-zone daily/travel amounts, fishing EI and capital-gains/LCGE numbers; old seasonal energy rebates, HST housing/POS rebates and blanket incorporation/dividend/gains effective-rate claims. No old approximate amount fills a current-year gap.
