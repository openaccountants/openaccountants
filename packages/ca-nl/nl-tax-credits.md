---
name: nl-tax-credits
description: "Newfoundland and Labrador 2026 credit and insurance-tax decisions: geographically correct DETC, benefit periods, volunteer coordination, film/IDM and manufacturing/green incentives, certificate routes and consumer insurance RST."
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

# Newfoundland and Labrador tax credits v2.0

## Scope

Select and compute Newfoundland and Labrador credits for the **2026 tax year**, in CAD. This skill separates personal provincial tax reductions, investment credits, quarterly CRA benefits, corporate incentives and retail sales tax on insurance. It complements `nl-individual-return`; a personal T1 must not absorb a corporation's film, media or manufacturing claim. This version has no accountant approval.

### Quick reference

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

| Item | Figure and conditions | Official source |
|---|---|---|
| Direct equity, North East Avalon business | 20% of qualifying investment; investor location does not decide rate | https://www.gov.nl.ca/fin/faq/tax-program/ |
| Direct equity, rest of province | 35%; mixed qualifying activities need reasonable geographic apportionment, not a “priority sector” uplift | https://www.gov.nl.ca/fin/faq/tax-program/ |
| Annual use limit | CAD 50,000 CREDIT including carryovers used that year; non-refundable; carry forward seven years/back three years with year restrictions | https://www.gov.nl.ca/fin/faq/tax-program/ |
| Issuer holding condition | No redemption of eligible shares for five years after issue; breach can require the issuer to repay credit plus interest | https://www.gov.nl.ca/fin/faq/tax-program/ |
| Issuer size/funding tests | Group assets below CAD 20 million; no more than 50 full-time-equivalent positions; prior equity/shareholder loans at least CAD 25,000; programme fundraising cap CAD 3 million | https://www.gov.nl.ca/fin/faq/tax-program/ |

| Item | Figure and conditions | Official source |
|---|---|---|
| Film/video labour-based credit | Lesser of 40% of eligible resident salaries and 25% of total eligible-project production costs; credit ceiling CAD 5 million for associated group / productions begun in a 12-month period; CAD 4 million applies to productions begun before 1 July 2021; refundable after taxes | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/newfoundland-labrador-provincial-corporation-tax/newfoundland-labrador-film-video-industry-tax-credit.html |
| Interactive digital media | 40% of qualifying expenditure; eligible salaries plus 65% of eligible remuneration; credit caps CAD 40,000 per eligible employee/calendar year and CAD 2 million per company/associated group/year; assistance can reduce it | https://www.gov.nl.ca/fin/tax-programs-incentives/business/idmtc/ |
| Manufacturing/processing investment credit | 10% of qualified investment; non-refundable current use plus, for eligible CCPCs, refund limited to the lesser of unused credit and 40% of the credit; remaining eligible balance may carry three years back/twenty forward; not fully refundable | https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm |
| Green technology credit | 20% of eligible qualified investment, subject to allocated CAD 1 million tax-credit limit and short-year rules; eligible CCPC, Classes 43.1/43.2 property in NL; refund fraction is 40% of the credit, not full automatic refund | https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm |

## Ask the client first

1. Which tax year and benefit-payment period, and which province on the last day of the year? Obtain arrival, departure, death and interprovincial moving dates, Canadian residence status and every business permanent establishment.
2. What are taxable income, net income and adjusted family net income, separately? Obtain all slips, foreign income, deductions, CPP/EI details and the spouse's return. Do not default an unknown marital status to single.
3. Which age, dependant, disability, pension, tuition, medical, donation, volunteer and investment facts apply? Obtain certificates, receipts, shared claims and carryover assessments before using a credit.
4. Is this an individual, an unincorporated business or a corporation? Identify self-employment, farming/fishing, instalments and prior assessments. A corporate credit cannot be placed on a personal return.
5. What is the requested output: a planning estimate, the actual annual filing or a separate CRA-administered benefit calculation? Do not call a partial provincial computation a final refund.

Also obtain investment certificates, issuer registration, business geography, investor age/residence/arm's-length status, issue/payment/redemption dates, assistance and past use. Corporate work needs PE, corporate status, approved project/product, local workers and costs, dates, group caps, assistance and actual certificate deadlines. Insurance work needs policy type, insured risks and values by place, charges, exemptions, seller registration and payments.

## The method, step by step

### Basic credits and low-income tax reduction

Use the enacted 2026 personal/volunteer amounts rather than the January payroll page's superseded BPA. A credit base is not the tax saving: apply the provincial credit percentage and the specific cap/phase-out. The maximum age, spouse, dependant, disability and adoption figures need their full eligibility and income tests. Political contributions use the statutory receipt and graduated formula in section 47, capped at CAD 500; do not treat them as charitable gifts. [Act sections 9-18 and 47](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm); [2026 commencement](https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm).

For the LITR, establish adjusted family income under section 21.1, select the sole family claimant, apply the current-year prescribed components and phase-out, limit current use to tax and transfer only the authorised unused amount to the eligible spouse. Regulation 18/26 sets the **2026 components at CAD 842 basic plus CAD 563 for spouse OR eligible dependant**, in contrast to **2025 CAD 997 plus CAD 557**. The phase-out rate is 16%, but its statutory dollar thresholds are indexed: the nominal base-year statute figures are not an actual 2026 indexed table. The 2025 NL428 thresholds are CAD 23,928 single/CAD 40,460 spouse-or-eligible-dependant; those are historical, not current. Hold the 2026 final LITR calculation until its actual indexed thresholds are sourced. Apply the reduction last, not as a refund. [Regulation 18/26](https://www.assembly.nl.ca/Legislation/sr/Regulations/rc260018.htm); [Act section 21.1](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm); [2025 NL428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5001-c/5001-c-25e.pdf).

The provincial volunteer base is CAD 6,000 from 2026; firefighter and search/rescue are alternatives. At least 200 eligible combined hours, the services and requested certificates matter. It is not a CAD 500 tax-credit base. Do not refuse a provincial claim merely because the federal volunteer amount is claimed: the actual annual instructions use federal eligibility as a route to the provincial claim. Check the separate federal volunteer amount versus emergency-services-income exemption election and exclude paid/ineligible hours as required by that rule. [Act sections 17.3-17.4](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm); [CRA historical 2025 coordination](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html).

### Income supplement, seniors and disability payments

These are CRA-administered cash benefits based on the benefit period and previous-year family information, not amounts placed on NL428 to reduce current tax. The current CRA maxima are in the table. The provincial Income Supplement page's detailed CAD 254 base/CAD 266 phase-in, CAD 69 spouse, CAD 231 child/disability, 5.32% phase-in and 9% phase-out above CAD 40,000 are expressly a **2025 benefit-year** table. Do not call those phase mechanics a fully confirmed 2026 computation just because the current CRA maxima match. The old CAD 200 child/CAD 240 disability/8% phase-out set was not supported by that actual table. [Provincial benefit-year distinction](https://www.gov.nl.ca/fin/tax-programs-incentives/personal/income-supplement/).

For July 2026 to June 2027 the seniors' benefit rises to CAD 1,882 per eligible family; the relevant age is at least 64 on 31 December 2025, with full benefit through AFNI CAD 30,409. Payments are quarterly with the federal consumption-tax benefit, not an October-only payment contingent on GIS and not income at line 14600. The provincial page describes phase-out at 11.66% through CAD 46,550, while CRA presents partial eligibility through CAD 46,549. Before computing an amount at that rounding boundary, read the benefit regulation or use the actual determination; do not manufacture a contradiction resolution by rounding an estimate. [Province](https://www.gov.nl.ca/fin/tax-programs-incentives/personal/income-supplement/); [CRA](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html).

The separate NL disability amount depends on DTC and benefit eligibility. The monthly NL disability benefit is a different programme and must not be substituted for it. File the required annual returns, maintain marital/custody/address information and valid DTC evidence, then reconcile CRA's benefit notice/payment schedule. Death, separation, new arrival and prison rules are programme-specific; do not infer eligibility solely from having no income tax payable. Child benefit and early-childhood nutrition are separate monthly programmes. [CRA current NL benefits](https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html).

### Direct equity: certificate and geography before the percentage

The rate follows the eligible **business**, not the investor or a technology label: 20% inside the North East Avalon and 35% elsewhere, with reasonable apportionment for qualifying activity in both. St. John's and Mount Pearl are in North East Avalon. There is no third DETC 10% venture-capital rate in the programme read. Venture funds and labour-sponsored funds have separate statutory regimes and certificates. [Official FAQ questions 4-5, 21](https://www.gov.nl.ca/fin/faq/tax-program/).

An eligible individual is at least 19 and resident in/paying tax to NL; eligible arm's-length corporate investors need their own NL operation/tax status. The issuer must be Canadian-controlled, not publicly traded, have a provincial PE, meet the group asset/employee/equity tests above, use raised capital in NL for qualifying growth activities, and obtain certification. Excluded activities include ordinary wholesale/retail, food/beverage, personal/business/professional services and trades, real-estate development, oil/gas production, mineral exploration, finance and specified fishing/processing, subject to the actual designated exceptions. Never approve a business by sector alone. [FAQ questions 6-8](https://www.gov.nl.ca/fin/faq/tax-program/).

Specified-issue shares must satisfy the new common-voting, fully cash-paid, non-redeemable/non-convertible and unrestricted-participation conditions. In-kind subscriptions, shareholder cash-outs, retiring old debt and buying an existing company are not automatically eligible uses. Prior disposals and related-party rules matter. The programme has an RRSP exception to its otherwise overlapping-credit/deduction restriction, so a blanket “RRSP means ineligible” is wrong. Securities-law compliance and investment risk remain separate from tax certification. [FAQ questions 9-12, 18-21](https://www.gov.nl.ca/fin/faq/tax-program/).

Apply for issuer certification before using the registered issue. The province issues receipts after investor documentation is submitted. Calculate the individual's T1272 using the correct rate, current tax available, annual CREDIT limit including carryovers and the certificate; the 2025 map places it on NL428 line 78. Eligible first-60-days subscriptions have a prior-year option, without double use. Carryovers are seven years forward/three back with the programme's starting-year restrictions. The issuer must not redeem within five years after issue; breach can require credit repayment plus interest. Maintain shareholding/compliance records and check any proposed disposal or reorganisation separately. [FAQ questions 14-18](https://www.gov.nl.ca/fin/faq/tax-program/); [CRA 2025 investment instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html).

### Resort-property and venture-fund credits

Do not merge these into DETC. The 2025 CRA instructions require T1297 and the resort certificate, an annual credit ceiling CAD 50,000 and lifetime CAD 150,000, with permitted seven-year carryforward/three-year carryback. Venture capital uses the NL VCTC certificate and its own aggregate limits/carryovers; the historical 2025 guide states a lifetime CAD 75,000 ceiling. Any 45% resort rate, investment/security qualification, disposition/holding rule or new-year cap must be checked in its own current legislation before recommending an investment. [2025 CRA instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html).

### Corporate film and interactive media

For the labour-based film/video programme, obtain the Minister's certificate and identify the production-start period before using the table. Current maximum is CAD 5 million for the associated group/productions begun in a twelve-month period; the old CAD 4 million applies to the pre-July-2021 cohort. The current CRA route is T2 Schedule 5 line 521; one certificate number at line 821, or Schedule 302 for multiple certificates, with certificates filed and copies retained. The credit offsets tax first and then is refundable. Do not sum this formula with a separate all-spend film regime or the IDM credit on the same cost; Act sections 45(3.1) and 46.3(7) require the prescribed allocation. [CRA labour-based credit](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/newfoundland-labrador-provincial-corporation-tax/newfoundland-labrador-film-video-industry-tax-credit.html); [Act](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm).

IDM uses qualifying salaries plus 65% of eligible remuneration, with the table's employee and associated-group credit caps and government-assistance reduction. The taxable Canadian corporation must primarily carry on IDM development, have an NL PE and hold registration. The product must educate/inform/entertain through at least two of text/sound/images, be interactive and not primarily communication or promotional material. Exclusions include adult-rated/gambling products, content aggregators, search engines, specified news/commentary/current-affairs content and most ordinary websites. Registration and project eligibility are not inferred from being a software company. Apply for the tax-credit certificate within **18 months after each expenditure-year end**; the official page gives a different completion-year treatment for specified government-oriented pre-November-2019 expenditure. Use the actual receipt's T2 destination. No same expenditure can support IDM and section 42 R&D; allocate overlapping film costs as prescribed. [Current provincial IDM page](https://www.gov.nl.ca/fin/tax-programs-incentives/business/idmtc/); [Act section 46.3](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm).

### Manufacturing/processing and green technology

Classify property and verify acquisition, location, business use, PE, capital cost, assistance, associated group and CCPC status where relevant. Section 41.1 is not a wholly refundable 10% cheque for every corporation: current credit use is limited by tax, eligible CCPC refund is capped at 40% of the credit and the unused balance has statutory three-year carryback/twenty-year carryforward rules. Section 41.2's green credit uses qualifying Classes 43.1/43.2 property, a 20% rate and allocated credit limit; its refund fraction is likewise 40% of the credit. Associated-group allocation, short years, multiple year ends, amalgamation/wind-up continuity and the statutory start-year restrictions must be checked before applying a limit. Do not assume federal CCA and other assistance can be stacked without their base adjustments. [Act sections 41.1-41.2](https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm).

### Insurance: consumer RST is not the insurer's separate tax

Revenue Administration Act section 91.1 imposes 15% RST on the premium for a taxable contract relating to NL property, risk, peril or events. The official RST FAQ exempts accident/sickness, life, automobile, commercial marine, guarantee/surety/fidelity, mortgage-default, crop/livestock and non-commercial personal-property insurance. Classify the actual cover before calculating. The old “life 15%, automobile 5%” table and default “4% for an unlicensed insurer” do not describe this consumer tax. The insurer's own separate Insurance Companies Tax has a different base and obligor; do not add that rate to the customer's RST computation. [RST FAQ](https://www.gov.nl.ca/fin/faq/faq-retail-sales-tax-on-inspremiums/); [Act section 91.1](https://www.assembly.nl.ca/legislation/sr/statutes/r15-01.htm).

For a contract covering risks inside and outside NL, section 91.1(3) allocates the premium by the supported NL risk value over total risk value, multiplied by the full premium; the 15% rate is applied to that taxable portion. Obtain the insured values/underwriting allocation and preserve it. A “national policy” label does not remove the NL part or make the whole premium taxable. For a travel/bundled policy split taxable cover from exempt accident/sickness cover with the actual breakdown; the FAQ addresses the result when no breakdown is available. Do not assume every amount called reinsurance, marine or excess/surplus cover has the same exemption without reading its category.

Premium and related service charges can form the taxable base; separately identified financing interest, NSF and the other specifically excluded charges in the FAQ require their own treatment. Collectors levy tax when premiums are paid, subject to the statutory full-payment case. The premium payer remains liable even if a seller is unregistered; obtain instructions for remitting the actual RST rather than using an unsupported default rate. Cancellation/premium refunds can have proportionate tax-refund rules and a statutory time condition. Do not offset the charge as an HST ITC. For income tax, an actual business premium and its non-recoverable tax need the ordinary purpose/current-versus-capital rules and documentary support, not a universal deduction and not a US Schedule C. Retain invoice, policy, endorsements, payment, exemption classification and allocation evidence. [Act sections 91.1(4)-(11)](https://www.assembly.nl.ca/legislation/sr/statutes/r15-01.htm).

### Return workflow and follow-up

Use CRA-certified T1 software/NETFILE for the individual, the correct year/province and the actual generated NL428/other schedules; obtain approval, save the confirmation and compare the assessment/carryovers. The **2025 annual map** is Parts A/B/C, T1272 DETC, T1297 resort and certificates for venture funds; it does not authorise invented NB/PE forms or treat every benefit as NL479. Corporate certificates/T2 schedules and provincial programme applications are separate. Wait for the assessment before a permitted return adjustment; a general amendment facility does not extend certificate deadlines. [2025 CRA map](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html); [CRA change-return steps](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

### Filing dates and the actual form year

For ordinary 2026 individual returns, ITA section 150(1)(d) gives the following-year filing rule: 30 April 2027 ordinarily; 15 June 2027 where the individual or their spouse/common-law partner carried on a qualifying business, subject to the statutory exceptions. Deaths and other special returns have different clocks. The later business filing date does not itself extend the balance-payment deadline. [ITA section 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html).

The annual provincial instructions read for this rewrite are the **2025 tax year, 2025-2026 filing cycle**, not final 2026 annual forms. Those instructions are used below only for the explicitly dated filing map and historical credit details. Do not put a 2026 figure on a 2025 return or assume a 2025 line number is final for 2026. Verify the released 2026 package before filing. For payments, current interest, instalment requirements and penalties, load the current federal filing/payment rules and the taxpayer's CRA account notices; the old guide's unsupported penalty/interest estimate is not a payment instruction.

## Worked cases

### Maya, CodCloud and Brendan: St. John's rate is 20%

Retain the original fictional parties. Maya's St. John's early-stage SaaS company CodCloud Inc. receives Brendan's CAD 50,000 newly-issued-share subscription on 15 June 2025. The original case records an asserted EBC registration on 1 February 2025, an arm's-length NL-resident investor and no prior Brendan holding; those assertions still require the actual programme evidence, not only an industry registration label. Assume the province confirms the issuer, specified shares and arm's-length investor are eligible and issues the certificate; the location is wholly North East Avalon. Brendan has CAD 14,200 NL tax before DETC and no other use of the annual limit. Credit is CAD 10,000 at 20%, leaving CAD 4,200 tax and no unused current credit. The old 35%/CAD 17,500 credit and CAD 3,300 carryforward were wrong for those location facts. A qualifying business wholly outside North East Avalon would produce CAD 17,500 on the same investment: current use CAD 14,200 and unused CAD 3,300, not a refund. Do not manufacture that second location for the actual St. John's company. [Official geography and carryover rules](https://www.gov.nl.ca/fin/faq/tax-program/).

```oa-check
name: Brendan North East Avalon versus other NL location decision
inputs:
  investment: 50000
  tax_before: 14200
steps:
  - nea_credit: investment * 0.20
  - other_credit: investment * 0.35
  - nea_tax_after: max(0, tax_before - nea_credit)
  - other_unused: max(0, other_credit - tax_before)
expected:
  nea_credit: 10000
  other_credit: 17500
  nea_tax_after: 4200
  other_unused: 3300
```

### Maya's CodCloud insurance: taxable NL business cover

Retain CodCloud Inc.'s CAD 12,000 cyber/errors-and-omissions premium for the policy effective 1 July 2025, and assume evidence shows it is wholly taxable NL business cover, with no exempt portion, no extra charges and no other province's risk. Consumer RST is CAD 1,800 and cash premium cost CAD 13,800. It is not insurer tax or HST; no HST ITC arises from that charge. If the actual contract instead covers exempt automobile or life risk, that taxable-base assumption fails and this computation cannot be reused. Maya's separate CAD 48,000 personal-income fact does not by itself prove the amount or absence of all family benefits: obtain the household and benefit-year facts. [RST FAQ](https://www.gov.nl.ca/fin/faq/faq-retail-sales-tax-on-inspremiums/); [section 91.1](https://www.assembly.nl.ca/legislation/sr/statutes/r15-01.htm).

```oa-check
name: CodCloud taxable insurance RST classification 2026
inputs:
  taxable_nl_premium: 12000
steps:
  - rst: taxable_nl_premium * 0.15
  - cash_cost: taxable_nl_premium + rst
expected:
  rst: 1800
  cash_cost: 13800
```

## When to refuse or refer

- Stop the final calculation when residence, year, taxable income, family status, credit evidence or a current source needed for the answer is missing. State the exact missing fact; do not invent a conservative numeric default or relabel a prior-year amount as current.
- Refer special returns, disputed residence, multiple-province business allocation, treaty income, minimum tax, tax on split income, Indigenous tax exemptions, trusts and corporate claims to the relevant specialist workflow. Do not turn “outside this ordinary computation” into an unsupported statement that no relief exists.
- Do not substitute payroll withholding for annual tax, cash benefits for non-refundable credits, a provincial label for a federal credit, or a corporation's incentive for its shareholder's personal credit.
- Do not promise a refund, investment eligibility, programme funding, investment value or professional approval. Obtain the relevant certificate and calculate tax and cash payments separately. Keep records supporting shared claims, carryovers, amendments and recapture.

Additional stops: no valid investment/corporate certificate, unknown geography, related-party funding, replacement shares, disposal during a restricted period, unallocated policy risks or missing statutory programme criteria means hold that claim. A federal volunteer claim does not alone bar the provincial claim. Death/bankruptcy/non-resident/part-year cases require their actual provisions, not an invented general refusal.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for: NL Finance current-year table: personal/volunteer/medical/adoption maxima and donation rates | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/personalincometax/ | 2026-11-14 |
| Read for: NL Income Tax Act sections 9-23, 41.1-41.2, 45-47: conditional credits, carryovers, partial refundability and overlapping expenditure restrictions | https://www.assembly.nl.ca/legislation/sr/statutes/i01-1.htm | 2026-11-14 |
| Read for: 2026 chapter 14 sections 1-5: current BPA/volunteer increases and actual commencement | https://www.assembly.nl.ca/Legislation/sr/Annualstatutes/2026/2614.chp.htm | 2026-11-14 |
| Read for: Regulation 18/26: exact distinct annual LITR components | https://www.assembly.nl.ca/Legislation/sr/Regulations/rc260018.htm | 2026-11-14 |
| Read for: CRA 2025 NL guide: historical tax-form mapping, volunteer coordination and separate investment forms | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/newfoundland-labrador/5001-pc.html | 2026-11-14 |
| Read for: CRA 2025 NL428 four pages: old-year LITR components, thresholds, credit order and spouse transfer | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5001-c/5001-c-25e.pdf | 2026-11-14 |
| Read for: CRA current NL benefit page: dated July 2026-June 2027 seniors, income/disability supplements and separate disability programme | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-newfoundland-labrador.html | 2026-11-14 |
| Read for: Province income-supplement page: explicitly 2025 phase-in table and July 2026 seniors increase/rounding endpoint | https://www.gov.nl.ca/fin/tax-programs-incentives/personal/income-supplement/ | 2026-11-14 |
| Read for: Official DETC FAQ, questions 4-21: location, all investor/issuer/security tests, application, caps, carryovers and redemption | https://www.gov.nl.ca/fin/faq/tax-program/ | 2026-11-14 |
| Read for: CRA film/video labour-based credit: formula, start-period group cap, refundability and certificate filing route | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax/newfoundland-labrador-provincial-corporation-tax/newfoundland-labrador-film-video-industry-tax-credit.html | 2026-11-14 |
| Read for: NL current IDM page: formula/base, caps, exclusions, assistance and certificate deadlines | https://www.gov.nl.ca/fin/tax-programs-incentives/business/idmtc/ | 2026-11-14 |
| Read for: NL insurance RST FAQ: exemptions, taxable premium/fee components, multi-place and unregistered-seller treatment | https://www.gov.nl.ca/fin/faq/faq-retail-sales-tax-on-inspremiums/ | 2026-11-14 |
| Read for: Revenue Administration Act section 91.1: 15% insured-premium tax, allocation, collector, insured liability and refunds | https://www.assembly.nl.ca/legislation/sr/statutes/r15-01.htm | 2026-11-14 |
| Read for: ITA section 150(1)(b),(d): filing dates and exceptions | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html | 2026-11-14 |
| Read for: CRA change-return page: actual correction procedure | https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html | 2026-11-14 |

Not yet confirmed: Final 2026 annual forms/lines and actual indexed 2026 LITR thresholds; detailed 2026 NLIS phase-in/out regulation (the provincial detailed table is explicitly 2025); exact senior-benefit endpoint rounding between the provincial CAD 46,550 and CRA CAD 46,549 presentation; current resort/venture eligibility and rates beyond the expressly historical filing map; detailed prescribed film/IDM cost-allocation and stacking rules and the separate all-spend-film regime before computing overlapping projects; manufacturing/green programme forms, acquisition-date transition and detailed assistance rules beyond the statutory provisions read; insurer-level tax rates, captive/reinsurance exemptions and uninsured/unlicensed arrangements beyond the sourced consumer RST. The old 4%/5%/life-15% consumer table is not usable guidance.
