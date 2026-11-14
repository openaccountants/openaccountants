---
name: nb-individual-return
description: "New Brunswick individual provincial tax for calendar 2026: sourced brackets and basic personal amount, federal coordination, NB428 workflow, credit conditions, residence exceptions and explicitly dated 2025 annual-form instructions."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nb-individual-return"
  jurisdiction: "CA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# New Brunswick individual return v2.0

## Scope

Compute New Brunswick provincial individual tax for the **2026 calendar tax year**, in CAD, alongside a separately completed federal T1. The place is Canada, province New Brunswick, not a US state. CRA administers the personal return; provincial programme approvals remain with the named provincial authority. Use `nb-tax-credits` for the detailed investment, renovation and benefit workflows. This skill is not professionally approved.

### Quick reference

The return year and payment period are separate: 2026 income is generally filed in 2027; a July 2026 to June 2027 benefit payment can be based on 2025 family income. The rates immediately below are 2026 rates. Annual form boxes expressly marked 2025 remain a historical filing map.

| Portion of 2026 taxable income, CAD | Provincial rate | Official source |
|---|---|---|
| Over 0 through 52,333 | 9.400% | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over 52,333 through 104,666 | 14.00% | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over 104,666 through 193,861 | 16.00% | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |
| Over 193,861 | 19.500% | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |

| Item | Figure and conditions | Official source |
|---|---|---|
| 2026 basic personal amount | CAD 13,664 base; credit at 9.4%, limited by NB tax | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nb-jan/t4032nb-january-general-information.html |
| 2025 LITR, historical filing cycle | CAD 802 basic plus CAD 802 spouse OR eligible dependant; maximum CAD 1,604; subtract 3% of adjusted family income above CAD 21,920; non-refundable; unused spouse transfer permitted | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf |
| 2025 pension amount, historical filing cycle | Lesser of eligible federal pension amount and CAD 1,000; credit at 9.4% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf |
| 2025 seniors renovation, historical filing cycle | 10% of eligible expenses up to a shared CAD 10,000 base; refundable through Schedule NB(S12), subject to principal-residence and senior tests | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html |
| NBHST credit, current programme | Annual maximum CAD 300 individual + CAD 300 spouse + CAD 100 per child under 19; first child of single parent CAD 300 instead; reduce by 2% of AFNI above CAD 35,000; quarterly CRA payment | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-new-brunswick.html |

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

### New Brunswick credit sequence and retained special topics

Use NB428 Part A for tax on taxable income, Part B for non-refundable credit bases and Part C for provincial tax, additions, dividend/foreign-tax credits and low-income reduction. The current basic personal amount does not mean that the spouse/eligible-dependant amount is identical. Establish the claimant's support and household tests and the other person's net income. Carry forward only what that credit permits; CPP/EI, age and disability bases are not all transferable or refundable. [2025 annual instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

For the **2025 filing cycle only**, NB428 gives age maximum CAD 6,037 subject to the worksheet; spouse/eligible-dependant base CAD 11,550 less the person's income, capped at CAD 10,499; disability CAD 10,010 for an eligible adult; pension maximum CAD 1,000; medical threshold the lesser of 3% of the claimant's net income and CAD 2,798. Tuition uses NB(S11), with student use first, a permitted current-year transfer and assessed carryforwards; an old carryforward is not freely transferable. Medical-period and reimbursement rules, disability certification, dependant transfers and donations require their actual schedules. The 2025 donation rates are 9.4% on the first CAD 200 and 17.95% on the qualifying excess, not the top ordinary-income rate. These are **not certified 2026 limits**. [2025 NB428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf).

The low-income reduction is non-refundable and uses adjusted family income, not a generic single-person income cutoff. For 2025 the formula is in the table; eligible spouses can transfer the unused reduction. It is not an automatic zero-tax result for every person below an approximate threshold. Current benefit payments such as the NB child tax benefit, working-income supplement and harmonized sales tax credit are administered separately by CRA. Use the credit skill and the actual benefit-period notice, including the special first-child rule for a single parent. [CRA benefits](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-new-brunswick.html).

The seniors' renovation programme concerns enduring access, mobility and safety work at a qualifying principal residence. Ordinary repairs, decoration, freestanding devices and household services do not become qualifying expenses merely because the occupant is a senior. Shared claims and assistance reduce what is available. In the 2025 filing cycle complete NB(S12), then T1 line 47900; there is no general NB479 map in the package read. [CRA 2025 senior-renovation instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

The old tuition cash-back/rebate promise is not a current graduate entitlement. The 2015 amending Act limited the scheme to 2006-2014 taxation years, barred new applications from 1 January 2016 and preserved specified existing entitlements/applications. Do not turn that transitional saving into a new 2026 claim. Ordinary tuition credits remain a different question. [2015 Act, sections 1-4 and 8](https://www2.gnb.ca/content/dam/gnb/Departments/ag-pg/PDF/ActsLois/2015/Chap-43.pdf).

SBITC uses a non-refundable certificate-based claim. Its post-17-March-2026 strategic-sector and corporate changes must not be applied to old purchases. Follow `nb-tax-credits` for the category, cap, certificate, carryover and holding-period tests. The old “50% of CAD 125,000 invested” summary confused investment and credit ceilings. [Official programme](https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html).

Truck drivers and other workers crossing provincial borders do not choose province from their employer's depot. Confirm actual residence and any business allocation first. Language choice is an administrative issue, not a different NB tax system; the CRA form is available in French and English. Do not invent a separate Revenu Nouveau-Brunswick personal filing portal. The exact 2026 dividend-credit percentages, housing/POS relief, capital-exemption ceiling and old “newcomer graduate rebate” figures are held under Sources until separately confirmed.

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Employment-income comparison, taxable income CAD 70,000

Retain the old employment example's income but make the assumptions explicit: full-year ordinary NB resident; taxable income after deductions is CAD 70,000; no age, spouse or investment claim. The provincial basic personal base is CAD 13,664. For this illustration the already-verified provincial CPP and EI **credit dollars** supplied by the return workpaper are CAD 400 and CAD 100, respectively, not an assertion about 2026 maximum contributions. Gross NB tax is CAD 7,392.68 and the illustrative NB amount after those credits is CAD 5,608.27. The old CAD 5,813 and combined CAD 16,065 cannot be carried forward as a final result. Complete the federal return and all other adjustments before giving total tax or take-home pay. Sources: the current rates and BPA rows above; 2025 NB428 illustrates the base-CPP/EI credit mapping only.

```oa-check
name: NB employment workpaper provincial slice 2026
inputs:
  income: 70000
  bpa: 13664
  cpp_credit: 400
  ei_credit: 100
steps:
  - band_1: max(0, min(income, 52333) - 0) * .094
  - band_2: max(0, min(income, 104666) - 52333) * .14
  - band_3: max(0, min(income, 193861) - 104666) * .16
  - band_4: max(0, income - 193861) * .195
  - gross_tax: band_1 + band_2 + band_3 + band_4
  - bpa_credit: bpa * 0.094
  - provincial_tax: round(max(0, gross_tax - bpa_credit - cpp_credit - ei_credit), 2)
expected:
  gross_tax: 7392.682
  provincial_tax: 5608.27
```

### Deduction now or later, within the same provincial band

An eligible CAD 1,000 deduction reduces the same taxpayer's taxable income from CAD 70,000 to CAD 69,000. Both amounts remain in the second NB band, so the provincial saving is CAD 140. The separate federal saving and any benefit effect need their own calculation. If room or deductibility is missing, neither option is authorised. This comparison uses the actual bands, not a single rate applied across a threshold.

```oa-check
name: NB eligible deduction comparison 2026
inputs:
  before: 70000
  deduction: 1000
steps:
  - after: before - deduction
  - provincial_saving: deduction * 0.14
expected:
  after: 69000
  provincial_saving: 140
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: CRA current-year table: the complete NB and federal 2026 bands | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| Read for: CRA January 2026 NB payroll instructions: basic personal amount, not final annual form boxes | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nb-jan/t4032nb-january-general-information.html | 2026-11-14 |
| Read for: CRA 2025 NB annual instructions: Parts A-C, tuition, shared claims, low-income transfer, renovation eligibility/exclusions and Schedule 12 filing route | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html | 2026-11-14 |
| Read for: CRA 2025 NB428, all four pages: old-year credit bases, LITR formula, transfer and T1 destination | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf | 2026-11-14 |
| Read for: CRA NB benefit page: monthly child/working-income programmes, single-parent HST-credit rule and AFNI formula | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-new-brunswick.html | 2026-11-14 |
| Read for: GNB current SBITC page: investor classes, 2026 effective date, rates/caps and administrative conditions | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html | 2026-11-14 |
| Read for: 2015 chapter 43, sections 1-4 and 8: tuition-rebate closure and savings | https://www2.gnb.ca/content/dam/gnb/Departments/ag-pg/PDF/ActsLois/2015/Chap-43.pdf | 2026-11-14 |
| Read for: CRA HST page: place of supply, supply classification and NS-specific rate transition | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html | 2026-11-14 |
| Read for: Federal ITA section 150(1)(b),(d): ordinary, business and death filing rules | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA changing-a-return page: assessment prerequisite, CRA account steps and exclusions | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

| CRA GST/HST place-of-supply opening rates: current participating-province rate and supply classification | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html | 2026-11-14 |

Not yet confirmed: Final 2026 annual NB428/NB(S11)/NB(S12) instructions and line numbers; 2026 age, spouse, eligible-dependant, pension, disability, medical and donation limits other than the sourced BPA; 2026 LITR base/threshold/cap (the table is explicitly 2025); exact 2026 provincial dividend-credit percentages; the old generic housing rebate and point-of-sale exemption claims; current capital-gains/LCGE limits and the old cancelled-inclusion-change narrative; the old renovation January-payment concession. Do not use the old figures to fill those gaps.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nb-individual-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nb-individual-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
