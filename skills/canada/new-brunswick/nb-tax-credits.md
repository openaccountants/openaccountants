---
name: nb-tax-credits
description: "New Brunswick 2026 tax-credit decisions: non-refundable SBITC with dated strategic-sector changes, CRA benefit formulas, historical 2025 LITR and seniors-renovation filing instructions, R&D and current film-grant routing."
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.0"
category: international
type: situation-rules
---

# New Brunswick tax credits v2.0

## Scope

Apply New Brunswick's individual and corporate credit conditions for **2026**, in CAD, while keeping historical **2025-2026 filing-cycle** references clearly dated. This companion to `nb-individual-return` distinguishes non-refundable provincial tax reductions, refundable return credits, separate CRA benefit payments and provincial grants. It is not an approved accountant's publication.

### Quick reference: decide the claim route first

| Item | Figure and conditions | Official source |
|---|---|---|
| 2026 basic personal amount | CAD 13,664 base; credit at 9.4%, limited by NB tax | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nb-jan/t4032nb-january-general-information.html |
| 2025 LITR, historical filing cycle | CAD 802 basic plus CAD 802 spouse OR eligible dependant; maximum CAD 1,604; subtract 3% of adjusted family income above CAD 21,920; non-refundable; unused spouse transfer permitted | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf |
| 2025 pension amount, historical filing cycle | Lesser of eligible federal pension amount and CAD 1,000; credit at 9.4% | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf |
| 2025 seniors renovation, historical filing cycle | 10% of eligible expenses up to a shared CAD 10,000 base; refundable through Schedule NB(S12), subject to principal-residence and senior tests | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html |
| NBHST credit, current programme | Annual maximum CAD 300 individual + CAD 300 spouse + CAD 100 per child under 19; first child of single parent CAD 300 instead; reduce by 2% of AFNI above CAD 35,000; quarterly CRA payment | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-new-brunswick.html |
| 2025 tuition credit, historical filing cycle | Eligible provincial tuition base at 9.4%; use NB(S11), assessed carryovers and permitted transfer only | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf |
| NB research and development credit | 15% of eligible SR&ED expenditure; fully refundable after provincial tax, not limited to profitable corporations | https://www2.gnb.ca/content/gnb/en/departments/finance/taxes/taxcredit.html |
| Current LIFT micro-production grant | Up to 30% of total NB spend, maximum CAD 100,000; budget below CAD 400,000; discretionary grant, not an automatic T2 tax credit | https://www.gnb.ca/en/topic/culture-heritage/grants-finance/investment-production.html |
| Current LIFT major-production grant | Up to 25% base plus bonuses to 35% of total NB spend; budget above CAD 400,000; actual approval and funding required | https://www.gnb.ca/en/topic/culture-heritage/grants-finance/investment-production.html |

| Item | Figure and conditions | Official source |
|---|---|---|
| Individual SBITC, non-strategic | 50% of eligible investment up to CAD 250,000; maximum CAD 125,000 credit; non-refundable | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html |
| Individual SBITC, strategic after 17 March 2026 | 50% of eligible investment up to CAD 1,000,000; maximum CAD 500,000 credit; requires the prescribed strategic-sector classification | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html |
| Corporation/trust SBITC after 17 March 2026 | 25%; non-strategic investment cap CAD 500,000 / credit CAD 125,000; strategic investment cap CAD 1,000,000 / credit CAD 250,000; non-refundable | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html |
| Combined SBITC investment ceiling | CAD 1,000,000 across strategic and non-strategic investments; apply investor-category and year limits before claiming | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html |
| Unused SBITC | Carry back three years or forward seven years, subject to tax, the applicable-year limits and amounts already used; not a cash refund | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html |
| Holding restriction | Four years after issue/purchase as applicable; early redemption or disposal can trigger repayment; statutory exceptions need separate review | https://laws.gnb.ca/en/document/cs/2016,%20c.112 |

## Ask the client first

1. Which tax year and benefit-payment period, and which province on the last day of the year? Obtain arrival, departure, death and interprovincial moving dates, Canadian residence status and every business permanent establishment.
2. What are taxable income, net income and adjusted family net income, separately? Obtain all slips, foreign income, deductions, CPP/EI details and the spouse's return. Do not default an unknown marital status to single.
3. Which age, dependant, disability, pension, tuition, medical, donation, volunteer and investment facts apply? Obtain certificates, receipts, shared claims and carryover assessments before using a credit.
4. Is this an individual, an unincorporated business or a corporation? Identify self-employment, farming/fishing, instalments and prior assessments. A corporate credit cannot be placed on a personal return.
5. What is the requested output: a planning estimate, the actual annual filing or a separate CRA-administered benefit calculation? Do not call a partial provincial computation a final refund.

For investment claims additionally obtain the complete specified-issue registration, Minister's certificate, share/debenture terms, bank evidence of payment, investment and disposal dates, connected persons and earlier usage. For renovations obtain the senior's age, family relationship, principal residence, expected occupancy, invoices, who paid and assistance. For corporate film/R&D work obtain establishment, activity, project dates, labour/cost records, assistance, approvals and tax years.

## The method, step by step

### Family income and the low-income reduction

Reconcile both family members' net income and the form's adjusted-family-income additions and subtractions. A marital change is a fact to investigate and report, not permission to assume the lower single threshold. For **2025 only**, the actual NB428 formula is `max(0, 802 + qualifying_spouse_or_eligible_dependant_802 - 3% * max(0, adjusted_family_income - 21920))`, capped by the available NB tax. The spouse and eligible-dependant additions are alternatives; the family maximum is CAD 1,604. The other spouse may use the authorised unused amount, so choosing the first claimant and recording the transfer matters. [2025 NB428, pages 3-4](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf).

The 2025 form's preliminary eligibility screens are net income below CAD 48,653 for a single claimant or adjusted family income below CAD 75,387 where there is a spouse/eligible dependant. Those screens are not the phase-out's starting threshold. The old guide's CAD 818/1,326/674 and approximate CAD 20,851/35,851 set did not match that actual-year form and is not a 2026 substitute. Death and special returns need their specific annual provisions; the 2025 instructions expressly allow the deceased spouse amount and authorised unused transfer. [2025 CRA instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

### CRA-paid benefits, not a refund line invented on NB428

The current NBHSTC formula is in the table: the special single-parent first-child amount must be included before reducing for AFNI. CRA combines it with quarterly federal consumption-tax benefit payments. Obtain the benefit year, prior-year assessed family income, marital changes, custody and the actual CRA determination; do not multiply a monthly child benefit by an assumed full eligibility year and deduct it from income tax. The child tax benefit's current basic monthly amount is up to CAD 20.83 per child under 18, reduced above AFNI CAD 20,000. Working-income and school supplements are separate components with their own tests. [CRA NB benefit page](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-new-brunswick.html).

The 2025 annual instructions say to file both required returns for timely automatic calculation. Do not ask for a separate NB479 benefits application where that form is not in the actual package. Newcomers, status/custody changes and non-filers need the applicable CRA benefit application/update process; the old RC151/RC65 references do not establish the current eligibility year, current amount or income-tax claim. [CRA 2025 benefit instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

### Seniors' home renovation, 2025 historical filing instructions

A qualifying claimant is an NB resident at year end, aged at least 65 or living/expecting to live with a qualifying senior family member. For 2025 expenses, the guide permits the qualifying residence expected to be occupied by the end of 2027; it is not limited to a home already occupied on the invoice date. The improvement must be enduring, integral and improve access, mobility, function or safety. Ramps, lifts, widened doors, accessible counters, grab bars, non-slip flooring and appropriate lighting can qualify; routine plumbing/roof repairs, aesthetic work, ordinary windows/heating/insulation, portable medical devices, appliances, vehicles, monitoring, homecare and housekeeping do not qualify merely because they help a senior. [CRA 2025 eligibility and exclusions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

Reduce expenses by related government assistance other than tax credits. The household/shared-residence cap cannot be multiplied by claimants or successive residences. The 2025 guide provides separate-residence exceptions for qualifying medical separation or a marriage breakdown lasting the specified period; document the actual facts and addresses. A person outside the residence may pay on the eligible resident's behalf if supporting documents are obtained. A qualifying medical-expense claim can coexist for the same qualifying expense under the guide's rules. Death and bankruptcy are not blanket refusals: the guide specifies final-return and pre/post-bankruptcy allocation while preserving the annual shared cap. [CRA 2025 special cases](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

Complete NB(S12), calculate 10% of the eligible base up to CAD 10,000 and transfer Schedule 12 line 7 to **T1 line 47900**. On paper attach Schedule 12, retaining invoices and other records rather than sending them all. Do not call this NB428 line 47900, promise a refund without the full T1 or invent a late-January payment extension. Those are 2025 instructions; final 2026 form details remain held.

### Tuition and other personal credit records

For 2025, NB(S11) calculates current eligible tuition, use by the student, the permitted transfer and the amount carried forward. Preserve the assessed old-year balance and the student's written designation, and do not transfer a carryforward as current fees. Spouse transfers use the appropriate NB(S2); medical periods, disability certification and donation receipts have separate tests. The old tuition cash-back graduate rebate is closed to new applications, subject to the 2015 Act's narrow savings, and must not be confused with the ordinary tuition credit. [CRA 2025 tuition rules](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html); [2015 chapter 43](https://www2.gnb.ca/content/dam/gnb/Departments/ag-pg/PDF/ActsLois/2015/Chap-43.pdf).

### Small Business Investor Tax Credit

The SBITC is non-refundable for individuals as well as corporations and trusts. The word “refundable” in the old personal-credit table and its cash-refund example was wrong. The present programme and Small Business Investor Tax Credit Act sections 20-22 support the rates and caps above. New strategic-sector and corporate rates have their own effective date; do not apply them to an earlier investment merely because the return is prepared now.

Obtain investor identity, date of payment and issue, security type, specified-issue registration, the Minister's tax credit certificate, issuer business activities and NAICS classification, past share disposals, assistance, connected/control relationships and all earlier claims. Individual investors must meet the province's age/residence requirements; corporate/trust investors have their own establishment and control tests. The registered eligible business must meet the private-business, active-operation, asset, payroll and registration requirements. The current programme uses a group net tangible-asset ceiling, not the old guide's invented employee-count shortcut. Do not infer eligibility from a business's trading address or a “tech” description.

The current programme describes a minimum individual investment of CAD 1,000 and age 19; the corporate/trust minimum is CAD 50,000. Issuer registration includes at least three investors and total capital of at least CAD 10,000, group net tangible assets below CAD 50 million and the NB payroll conditions: normally 75%, or 50% where more than half the business's goods/services are exported. Those conditions are cumulative, with the programme's exceptions; record the actual approval rather than making an eligibility certificate from a checklist. [Official programme](https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html).

Eligible securities must be newly issued in a registered specified issue and fully paid; replacement securities, issuer-financed purchases and tax-credit avoidance arrangements need the exclusions in sections 1, 3 and the registration provisions. Convertible debentures are now expressly addressed in the amended Act. Do not treat all shares, a purchase from an existing shareholder, an ordinary loan or a discretionary investment as eligible. [Act definitions and registration](https://laws.gnb.ca/en/document/cs/2016,%20c.112).

The old guide's blanket refusal for an individual holding 10% is not the Act's general investor test. Section 21's associate definition refers to 10% holdings, but its prohibition is directed to corporate/trust investors obtaining 50% or more of the registered corporation's votes, or otherwise controlling it, alone or with the specified associates/affiliates/shareholders/directors/officers. Check the whole connected arrangement and the registration conditions; do not approve an individual solely because they are below 10% or reject them solely because they are above it. [Act section 21](https://laws.gnb.ca/en/document/cs/2016,%20c.112).

The issuer applies for the certificate within the programme's period after issue; the present programme says within 30 days after the sale, not the old guide's assertion that the issuer creates its own certificate within 90 days. For an individual, use the applicable-year Form T1258, reconcile all NB-SBITC-1 certificates, determine current use and available carryovers and attach the specified evidence on paper. For the 2025 filing cycle the claim is NB428 line 96; the first 60 days' investment election and no-double-claim restriction must be checked. Corporate/trust filing uses its own current form and certificate, not an invented personal NB479 or a generic Schedule 305. [CRA 2025 filing map](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html).

Retain issue and purchase dates and a four-year monitoring schedule. Do not redeem, dispose, transfer, reorganise or claim hardship as an automatic exception; apply Act sections 26-33 to bankruptcy, loss of eligible status, early redemption, disposal, death and other relevant facts. Record statutory repayment and any permitted exception with its source. A later certificate does not itself waive an investment's holding condition. Federal cost-base, RRSP, capital-gains exemption and other-assistance interactions must be verified separately; there is no blanket permission to stack any federal incentive with this credit.

### Corporate research and film work

For R&D, confirm an NB permanent establishment and actual qualifying work in NB, reconcile eligible SR&ED expenditure with federal definitions and assistance adjustments, and prepare the actual current T2 Schedule 360 and supporting workpapers. The current provincial page confirms the fully refundable 15% enhancement and that unused current enhanced credit does not need a carryover merely because tax is insufficient. Historical non-refundable balances require their own year. Do not treat every software payroll cost as scientific research or stack government assistance without adjusting the base. [GNB R&D explanation](https://www2.gnb.ca/content/gnb/en/departments/finance/taxes/taxcredit.html).

The current film-production route read is **LIFT**, a discretionary provincial grant. Its NB-spend rates, budget streams, eligible production-company requirements and application process differ from the old guide's asserted refundable labour tax credit. Incorporated NB-based producers must meet the current ownership/activity requirements and apply through the provincial arts portal; the published round has a 1 December 2026 deadline, and funding is not guaranteed. A pre-project plan, actual financing and full guidelines matter. Do not prepare a purported 25%/30% labour-based T2 claim, enforce invented Part A/Part B tax-credit tests or use an unsupported “50% total cost” cap. Any actual legacy certificate or transition is held for its own legal evidence. [Current LIFT programme](https://www.gnb.ca/en/topic/culture-heritage/grants-finance/investment-production.html).

### Filing and follow-up

For the 2025 filing map, NB428 Part A is tax, Part B non-refundable credits and Part C the remaining provincial-tax computation. T1258/NB-SBITC-1 support SBITC; NB(S11) supports tuition; NB(S12) supports the refundable seniors' credit on T1. Use CRA-certified software/NETFILE for T1 submission, preserve approval and the confirmation, then compare the assessment and carryover balances. Provincial programme applications and corporate returns use their own systems, not the personal return. Once assessed, use the actual CRA change-return process for a correction; the old blanket ten-year amendment promise does not override a programme certificate/application deadline. [CRA change-return process](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Ava: non-refundable investment credit, not CAD 85,200 cash

Retain Ava in Moncton, age 41, employment income CAD 185,000, investing CAD 200,000 in TideTech Inc., an agritech-sensor business in Dieppe with 18 employees and a 4.2% holding. Payroll withholding is not itself her final tax. Her original case says a certificate was supplied in June 2025 by TideTech; establish that it is the actual Minister-issued NB-SBITC-1 and not merely an issuer-created document. Her March 15, 2025 investment belongs to the **2025 historical case**; those facts alone do not establish an eligible specified issue. Assume the Minister's valid NB-SBITC-1 confirms the entire qualifying investment and Ava has CAD 14,800 of NB tax available before this credit. The non-refundable 50% credit is CAD 100,000, current use CAD 14,800, remaining NB tax zero and unused credit CAD 85,200. The unused amount can be considered under the three-year carryback/seven-year carryforward rules, with the actual prior/future tax and limits. It is **not a refundable credit balance**. Do not apply the new strategic-sector cap retroactively. The holding schedule starts from the actual issue/purchase terms; if the purchase and issue were March 15, 2025 the ordinary four-year restriction reaches March 2029, subject to the statute's details. [CRA 2025 SBITC instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html); [current programme](https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html).

```oa-check
name: Ava historical 2025 NB SBITC corrected refundability
inputs:
  eligible_investment: 200000
  nb_tax_before: 14800
steps:
  - credit: eligible_investment * 0.50
  - used: min(credit, nb_tax_before)
  - tax_after: nb_tax_before - used
  - unused: credit - used
expected:
  credit: 100000
  used: 14800
  tax_after: 0
  unused: 85200
```

### Choose the authorised family claimant, 2025 LITR transfer

A qualifying couple's adjusted family income is CAD 21,920. The family reduction is CAD 1,604; one spouse has CAD 500 eligible NB tax and the other CAD 1,200. If the first spouse applies, use CAD 500 and transfer the authorised CAD 1,104 unused amount, leaving CAD 96 on the other spouse. Claiming two full family reductions would be wrong. Compare the available family use before selecting the claimant and record the transfer on both forms. These are the **2025 form amounts**, not an unsourced 2026 estimate. [NB428 pages 3-4](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf).

```oa-check
name: NB historical 2025 LITR family transfer
inputs:
  family_income: 21920
  tax_a: 500
  tax_b: 1200
steps:
  - reduction: max(0, 802 + 802 - max(0, family_income - 21920) * 0.03)
  - used_a: min(tax_a, reduction)
  - transfer: max(0, reduction - used_a)
  - tax_b_after: max(0, tax_b - transfer)
expected:
  reduction: 1604
  used_a: 500
  transfer: 1104
  tax_b_after: 96
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

Additional stops: no certificate means no final SBITC claim; missing qualifying residence or cost evidence means no renovation claim; a desired early share disposal needs the actual recapture analysis. Non-resident, part-year, Indigenous, death, bankruptcy, corporate-control and partnership cases require their actual rules rather than a blanket denial. Do not invent full refundability, programme acceptance, hardship relief or a transferable carryover.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: GNB current SBITC programme: all investor categories, post-17-March-2026 changes, investment/credit caps and registration/certificate procedure | https://www.gnb.ca/en/topic/business-economy/taxes/business-investor-credit.html | 2026-11-14 |
| Read for: Small Business Investor Tax Credit Act, sections 1-3, 20-22 and 26-33: security definitions, connected/control test, certificate and holding/repayment | https://laws.gnb.ca/en/document/cs/2016,%20c.112 | 2026-11-14 |
| Read for: CRA 2025 NB annual instructions: LITR spouse transfer, tuition, SBITC T1258 and complete renovation special cases and filing path | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/new-brunswick/5004-pc.html | 2026-11-14 |
| Read for: CRA 2025 NB428 all four pages: actual historical LITR values/formula, credit order and output | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-25e.pdf | 2026-11-14 |
| Read for: CRA January 2026 NB payroll instructions: current basic personal amount only | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032nb-jan/t4032nb-january-general-information.html | 2026-11-14 |
| Read for: CRA NB benefits: HST credit formula including single-parent first child and monthly child benefit | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-new-brunswick.html | 2026-11-14 |
| Read for: 2015 chapter 43, operative closure, savings and commencement: no new tuition cash-back application | https://www2.gnb.ca/content/dam/gnb/Departments/ag-pg/PDF/ActsLois/2015/Chap-43.pdf | 2026-11-14 |
| Read for: GNB R&D page: enhanced refundable credit versus old non-refundable balances | https://www2.gnb.ca/content/gnb/en/departments/finance/taxes/taxcredit.html | 2026-11-14 |
| Read for: GNB LIFT production page: current grants, stream rates/caps, applicant criteria, current round and non-guaranteed funding | https://www.gnb.ca/en/topic/culture-heritage/grants-finance/investment-production.html | 2026-11-14 |
| Read for: ITA section 150(1)(b),(d): ordinary, business and death filing rules | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return instructions: assessed-return prerequisite, routes and excluded changes | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

Not yet confirmed: Final 2026 annual forms and line numbers; current 2026 LITR values and ordinary tuition/senior-renovation continuation details beyond the explicitly historical 2025 instructions; exact newcomer RC151/status-update route and exceptional amendment periods; the old January renovation payment concession; any genuine legacy film-tax-credit certificate, labour percentage, Part A/Part B deadline or transition (current LIFT is a different grant); federal SBITC cost-base/RRSP/LCGE/other-assistance interactions; the old vague OBBBA/flow-through stacking assertion. No unconfirmed legacy amount is a current claim instruction.
