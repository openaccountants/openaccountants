---
name: pe-individual-return
description: "Prince Edward Island calendar 2026 individual tax: enacted six-band law, no post-2023 surtax, current conditional credits, provincial return workflow and separate benefit/investment decisions."
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
  - pe-tax-credits
---

# Prince Edward Island individual return v2.0

## Scope

Calculate Prince Edward Island provincial individual tax for **calendar 2026**, in CAD, alongside the federal T1. The current Income Tax Act has six bands, including 20% above CAD 200,000, and no post-2023 personal surtax. Use `pe-tax-credits` for detailed personal, community-equity, benefit and labour-rebate decisions. This version is not accountant approved.

### Quick reference

| Portion of 2026 taxable income, CAD | Provincial rate | Official source |
|---|---|---|
| Over 0 through 33,928 | 9.500% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Over 33,928 through 65,820 | 13.4700% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Over 65,820 through 106,890 | 16.600% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Over 106,890 through 142,520 | 17.6200% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Over 142,520 through 200,000 | 19.00% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Over 200,000 | 20.00% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |

| Item | Figure and conditions | Official source |
|---|---|---|
| 2026 basic personal base | CAD 15,000; ordinary non-refundable credit at 9.5%; not a CAD 15,000 tax exemption for all income types | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 spouse / eligible-dependant maximum | CAD 12,740 subject to status/support and the person's net income; CAD 1,274 income offset in statutory formula; not equal to the BPA | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 age amount | Maximum CAD 6,510 base for qualifying age 65; reduce base by 15% of eligible income above CAD 36,600; convert at 9.5% | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 pension / disability | Pension eligible base maximum CAD 1,000; certified adult disability base CAD 6,890 with separate child-supplement rules; non-refundable | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 donation credit | 9.5% on first CAD 200 of qualifying gifts; 20% on eligible excess, subject to statutory gift conditions | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 LITR | CAD 350 basic + CAD 350 spouse OR eligible dependant + CAD 300 each OTHER qualifying child + CAD 250 for each eligible senior spouse; less 5% of adjusted family income above CAD 23,000; non-refundable, authorised unused-spouse transfer | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| Current volunteer credit | CAD 1,000 refundable dollar credit; federal firefighter/SAR eligibility required and no volunteer-services income exemption elected; qualifying residence/death rules apply | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| 2026 children's wellness | Eligible shared expense base up to CAD 1,000 per qualifying child, under 18 at beginning of year; at 9.5%, derived maximum non-refundable credit CAD 95; programme and duplication tests apply | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf |
| PEI HST | 15% on ordinary taxable supplies whose place of supply is PEI; supply classification and exceptions first | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html |

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

### Use the enacted current law, not the old four-band/surtax guide

The current consolidated statute (read to July 1, 2026) and updated provincial income-tax page agree on the six 2026 bands. The January payroll page's older five-band presentation and its CAD 142,250 display are superseded by the statute's CAD 142,520 boundary and new top band. Source the actual law before trusting a cached withholding table. Section 31(2) expressly removes surtax for years ending after 2023. No surtax is added to a 2026 return. [Current Act sections 7 and 31](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf); [updated provincial table](https://www.princeedwardisland.ca/en/information/finance-and-affordability/provincial-personal-income-tax).

Ordinary provincial credit bases convert at 9.5%; they are not all equal to the basic personal amount and do not all have the same income test. Section 9's spouse/eligible-dependant base is reduced using the person's income and the CAD 1,274 offset; satisfy the support/status and no-duplicate tests. Age base is reduced by 15% above the stated income threshold, not an unrestricted maximum for every senior. Pension uses the eligible-income limit and disability requires the federal certification/child-supplement conditions incorporated by the Act. [Sections 9 and 12](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

For medical claims under section 11, deduct the lesser of CAD 1,678 or 3% of net income from the eligible self/family amount and use the separate dependant rule; reimbursements and claim periods still matter. Tuition/education carryovers and current-year transfers follow sections 13-18 and the applicable annual schedules, not an assumed transfer of all unused balances. Donation excess uses the year's highest provincial percentage, 20% for 2026, not the old 18% figure. Political contributions have their own statutory receipt and cap, not the charitable-gift formula. [Sections 10-18 and 36.4](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

The low-income reduction uses adjusted family income and the eligible-individual conditions, not a universal single-person cutoff. One family applies; the spouse/eligible-dependant additions are alternatives, and a child counted as the eligible dependant is not also an “other child”. The statute permits an authorised unused-spouse transfer, but unused reduction is not refunded to a single person. Age, support, residence, bankruptcy and prison exclusions must be tested. [Section 32](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

### Volunteer and child wellness claims

The volunteer claim is a **CAD 1,000 refundable tax amount**, linked to federal firefighter/search-rescue eligibility and the no-emergency-services-exemption election. The province's credit is not barred because the federal volunteer amount is claimed; federal eligibility is a condition. It is not CAD 500 times an old provincial rate. Qualifying death-residence cases are included, but specified separate returns are excluded. [Section 36.2](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

The children's wellness base is up to CAD 1,000 per eligible child shared between claimants, not a CAD 1,000 cash payment. The child must be under 18 **at the beginning of the year**. Confirm a qualifying supervised non-school programme and the weekly/camp/mixed-use tests, net reimbursements and duplication rules; integral eligible uniform/equipment costs are not categorically excluded. The credit details are in `pe-tax-credits`. [Section 11.1](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

### Benefits, community equity and other retained topics

The Island Essentials Benefit replaces the former PEI sales tax credit from July 2026. Do not apply the old CAD 110/55/60 and 2% phase-out formula to the new benefit period. The updated provincial page describes the new maxima and minimum; section 36.3 provides the current quarterly formula and the eligible-person/family/payment-month rules. It is a CRA-administered benefit separate from provincial tax and based on the relevant previous-year information. [Updated provincial page](https://www.princeedwardisland.ca/en/information/finance-and-affordability/provincial-personal-income-tax); [section 36.3](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

Community-development equity is a certificate-based, non-refundable investment credit with an annual **CAD 7,000 tax claim** limit, actual registration, ownership/security and holding conditions and authorised carryover. A generic direct investment in any private business does not qualify. Do not use the old guide's contradictory four-year carryforward or four-year holding assertions. For the actual current community-development programme, distinguish the registered CEDB issuer from its underlying investee and check the amended Act, not only the old programme overview. [Income Tax Act section 36.1](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf); [Community Development Equity Tax Credit Act](https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf).

Seasonal employment, EI benefits and multiple T4s require all slips and income reconciliation; withholding by several employers does not necessarily settle annual tax. Workers commuting to NB or NS still need their actual year-end residence and any business-allocation exception. PEI property-transfer tax is a separate transactional tax; no relief follows automatically from this income-tax return and the old blanket “1% of price or value” claim is held until its actual law/exemptions are read. Senior-independence assistance, school-supply credits, labour incentives and business incorporation each need their actual claimant/programme route. General population and “lowest tax in Canada” claims do not establish anyone's tax position.

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Simple 2026 provincial slice, CAD 75,000 taxable income

Assume an ordinary full-year PEI single resident, taxable income CAD 75,000 and no credit other than the sourced basic personal amount, no minimum/split-income/foreign-tax adjustments and no LITR. Apply the six-band law to the portions that actually arise, then the basic-personal credit. Do not apply the highest rate to all income or add the abolished personal surtax. This is only the stated provincial slice; complete all federal and other personal items before giving a balance. [Income Tax Act sections 7, 9 and 31](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

```oa-check
name: PEI basic provincial slice six-band law 2026
inputs:
  income: 75000
  bpa: 15000
steps:
  - band_1: max(0, min(income, 33928) - 0) * .095
  - band_2: max(0, min(income, 65820) - 33928) * .1347
  - band_3: max(0, min(income, 106890) - 65820) * .166
  - band_4: max(0, min(income, 142520) - 106890) * .1762
  - band_5: max(0, min(income, 200000) - 142520) * .19
  - band_6: max(0, income - 200000) * .20
  - gross_tax: band_1 + band_2 + band_3 + band_4 + band_5 + band_6
  - bpa_credit: bpa * 0.095
  - provincial_tax: round(max(0, gross_tax - bpa_credit), 2)
expected:
  gross_tax: 9042.8924
  provincial_tax: 7617.89
```

### Surtax comparison: historical mechanic versus 2026

Retain the old illustrative basic-tax inputs CAD 12,500, CAD 15,000, CAD 20,000 and CAD 30,000. Section 31's old formula would give CAD 0, CAD 250, CAD 750 and CAD 1,750, respectively, only for a year to which that historical provision applies. The statute expressly excludes taxation years ending after 2023, so the surtax addition for **every one of those 2026 scenarios is zero**. The old instruction “never omit surtax” must not produce a 2026 charge. This comparison does not reconstruct the old year's underlying tax calculation. [Section 31(1)-(2)](https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf).

```oa-check
name: PEI retained surtax comparison excluded in 2026
inputs:
  basic_tax: 30000
  historical_threshold: 12500
steps:
  - historical_formula_only: max(0, basic_tax - historical_threshold) * 0.10
  - surtax_2026: 0
  - hypothetical_total_2026: basic_tax + surtax_2026
expected:
  historical_formula_only: 1750
  surtax_2026: 0
  hypothetical_total_2026: 30000
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: PEI Income Tax Act current to July 1, 2026, sections 7-18, 31-32 and 36.1-36.4: six bands, conditional credits, no current surtax, family reduction and benefit/volunteer mechanics | https://www.princeedwardisland.ca/sites/default/files/0432/I-01-Income%20Tax%20Act_1.pdf | 2026-11-14 |
| Read for: PEI updated personal-income-tax page: 2026 enacted rates/credits and July 2026 Essentials Benefit replacement | https://www.princeedwardisland.ca/en/information/finance-and-affordability/provincial-personal-income-tax | 2026-11-14 |
| Read for: CRA January 2026 PE payroll guide: read to identify the superseded five-band/threshold display, not used against the amended law | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032pe-jan/t4032pe-january-general-information.html | 2026-11-14 |
| Read for: CRA 2025 PEI annual guide: explicitly historical Parts A-C and personal-credit/special-return filing map | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/prince-edward-island/5002-pc.html | 2026-11-14 |
| Read for: Community Development Equity Tax Credit Act current May 29, 2026: registered issuer, investment/certificate and holding conditions | https://www.princeedwardisland.ca/sites/default/files/legislation/c-13-01-community_development_equity_tax_credit_act.pdf | 2026-11-14 |
| Read for: CRA current-year rates: federal 2026 bands and corroborating updated PEI six-band table | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | 2026-11-14 |
| Read for: CRA GST/HST rates/place-of-supply opening rules: PEI participating-province rate and classification | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html | 2026-11-14 |
| Read for: ITA section 150(1)(b),(d): ordinary, business and death filing clocks | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return page: assessment prerequisite and correction route | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

Not yet confirmed: Final 2026 annual PE428/other schedules and box mapping; current PEI dividend-credit percentages and federal gross-up/inclusion/LCGE/CPP details before a full combined answer; property-transfer rate/exemptions, housing/POS rebate caps, senior-independence assistance and any purported provincial school-supply credit; exact present investment-certificate entitlement/application restrictions where the old programme overview conflicts with amended law, as explained in pe-tax-credits; current federal instalment interest/penalty amounts rather than the old guide's generic estimates. Prior-year forms are not relabelled 2026.
