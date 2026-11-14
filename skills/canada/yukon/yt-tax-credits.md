---
name: yt-tax-credits
description: >
  Prepare Yukon individual and corporate credit workpapers for certified investment, qualified research, manufacturing and processing, fitness, fertility and political claims. Distinguish First Nation tax sharing, separate benefits and unsupported current mineral incentives; preserve the actual latest annual form edition and specific unconfirmed issues.
version: 2.0
jurisdiction: CA-YT
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Yukon tax credits and incentives v2.0

## Scope

Prepare and reconcile the supported Yukon personal and corporate credit workpapers for calendar 2026, keeping return type, tax base, refundability, claimant eligibility, tax-sharing transfers and actual claim deadlines separate. The latest personal annual forms actually read are the **2025-2026 filing cycle**. They are identified below rather than relabelled as final 2026 forms. The companion `yt-individual-return` owns the ordinary personal bands and full return handoff. This method does not compute every federal SR&ED, mining, corporate-group or First Nation liability. [Current government measures](https://yukon.ca/yukon-income-tax), [CRA annual instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).

The main statute is the Income Tax Act, R.S.Y. 2002, c.118, as amended. Its current headings read here are individual tax s. 6, fertility s. 7.01, child benefit s. 9, fitness s. 9.01, corporation s. 10, M&P s. 10.1, political s. 11, First Nation s. 12, business investment s. 13 and R&D s. 15. The old section 17/17.1/21 and generic Part 2 anchors were not correct citations for these claims. The consolidation contains application notes and alternative-period text; the separately read 2025 amendment is needed for commencement. [Act](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [2025 amendment](https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf).

## Ask the client first

1. Obtain the actual tax year/return type, Canadian/Yukon residence dates, year-end address and any business permanent establishments or allocation. Obtain federal income/credit workpapers and actual prior assessments/carryovers; T1 line 40427 is not an interchangeable description of all federal tax.
2. For settlement land, obtain the exact residence/land, applicable First Nation and enacted income-tax law/sharing agreement, any departure date and actual exemption determination. Citizenship/status does not replace these facts.
3. For investment, obtain investor age and year-end residence, issuer/active business/PE and eligibility, security terms and payment source, certificate, acquisition date, ownership/relationship, disposal and holding records, past use and carryback/forward tax.
4. For research, obtain actual qualified Yukon SR&ED expenditure, work location, University payee/included amount, assistance/repayments, federal-base/ITC reconciliation, trust/partnership allocations and the claim deadline. Do not treat every technology expense as SR&ED or every college as Yukon University.
5. For corporate work, obtain T2, actual Schedule 5 allocation, federal SBD eligibility and associated-group limit/passive-income/taxable-capital workpapers, investment-income classification and actual M&P profit/base. Use the correct research and M&P forms rather than an invented universal Schedule 443.
6. Obtain fitness child age/disability and eligible activity receipts/reimbursements/shared use; fertility medical/travel receipts, eligible claimant/recipient and health-insured residence; political official receipts; current utility-grant/benefit and historic carbon records. For minerals obtain claim/activity/stage, expenditure, programme/certificate and flow-through documents.

## The method, step by step

### Rates, bands and thresholds

Each amount below belongs to its stated legal or actual annual edition; a refundable credit is not limited by ordinary tax merely because a non-refundable one is.

| Item | Supported amount and limitation | Official source |
|---|---|---|
| Business investment | 25% of a qualifying certified investment; annual credit use at most CAD 25,000, subject also to tax and eligible-investor/security requirements; unused credit window seven preceding/three following years as applied on the claim | [Act s. 13](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [CRA actual annual application](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html) |
| Investor age and holding | Eligible investor at least 19 and Yukon resident at year-end; disposition within four years other than by death can deem the security never acquired; no automatic exception for a different sale | [Act s. 13(1),(5)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf) |
| Investment claim filing | Prescribed income return within 36 months after year-end, with certificate and actual conditions; not an unlimited amendment right | [Act s. 13(2)-(4)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf) |
| R&D base and enhancement | Refundable 15% of the supported eligible base plus 5% of its included Yukon University expenditure portion; not 20% on every payment to a university/college | [Act s. 15](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [T1232](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1232/t1232-fill-25e.pdf) |
| R&D claim deadline | Required written claim/information with return within 12 months after filing-due date; CRA corporation instruction is 18 months after corporate year-end | [Act s. 15(2)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [T1232](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1232/t1232-fill-25e.pdf), [CRA corporate instruction](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-8-page-9-t2-return.html) |
| M&P corporate credit | Non-refundable 9.5% on the statutory eligible large-business M&P base after limits/exclusions; small-business portion has zero deduction, not a universal 2.5% rate applied to all company income | [Act s. 10.1](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [CRA Schedule 440 instruction](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-8-page-9-t2-return.html) |
| Ordinary corporate rates | Yukon 0% eligible small-business income within the applicable CAD 500,000 limit; general 12%. Ordinary federal SBD 9%, ordinary general 15%, each with its own conditions | [Current CRA rate table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html), [Yukon](https://yukon.ca/yukon-income-tax) |
| First Nation territorial percentage | Prescribed 95% applied only to the correct eligible individual's statutory tax-otherwise-payable base and agreement; not 95% of federal abatement or an automatic corporate credit | [Act s. 12](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [prescribed percentage](https://laws.yukon.ca/cms/images/LEGISLATION/SUBORDINATE/1999/1999-0184/1999-0184.pdf) |
| Actual 2025 fitness | Refundable 6.4% of eligible expenses, ordinary maximum CAD 1,000 per qualifying child; qualifying disability additional CAD 500 expense amount requires at least CAD 100 eligible expense | [Actual annual eligibility](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf) |
| Fertility/surrogacy from 2025 | Refundable lesser of CAD 10,000 and 40% of statutory eligible amount; insured residence, receipt, timing and non-duplication requirements apply | [2025 amendment ss.3,6](https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf) |
| Actual 2025 political | Non-refundable maximum CAD 650 using the actual annual worksheet and valid Yukon party/candidate receipt; no flat credit on all contributions | [Actual YT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf), [CRA annual political instruction](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html) |

### First Nation credit, transfer and exemption are different questions

1. Start with the actual individual's taxable income and territorial ordinary/special tax. The statutory s. 12 claimant is an individual meeting settlement-land residence (or the stated departure alternative) and an applicable First Nation final agreement, enacted income-tax law and tax-sharing agreement. It is not an earned-on-land source allocation available only to citizens. Actual CRA instructions say year-end residents on the listed settlement lands complete YT432 even if they are not citizens; citizens living elsewhere do not complete that form solely because of citizenship. [Act s. 12(2)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [YT432](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf).
2. Keep the federal and territorial legs separate. The actual YT432 uses a federal tax/abatement field and a territorial YT428 or T2203 field, computes a transfer and has separate T1 tax-transfer and federal-abatement handoffs. The territorial 95% prescribed percentage is not substituted into the federal leg. The percentage field in the fillable federal text was not readable; do not invent it. [Actual YT432](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf), [regulation](https://laws.yukon.ca/cms/images/LEGISLATION/SUBORDINATE/1999/1999-0184/1999-0184.pdf).
3. Establish the applicable statutory **tax-otherwise-payable base** before multiplication. The consolidation presents application-period alternatives reducing the base by specified investment/refundable amounts, with commencement references. The annual printed form is useful evidence of its own edition; it does not resolve every special-credit/current-period interaction. The correct effective definition and affected-credit interactions remain explicitly unconfirmed here. Do not silently choose the definition that gives the largest credit. [Act s. 12 definitions and application notes](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [YT428/YT432](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf).
4. Do not turn the offset of part of transferred tax into a claim that the taxpayer's overall tax disappears. Reconcile the First Nation income-tax law and actual transfer/abatement. An Indian Act exemption requires its own actual income/Agreement analysis; status and a land address alone are not a final determination. Refer disputes with the law and documents, not a taxpayer choice of rule. [Actual form and instructions](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf), [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).
5. **Corporate FNTC:** the old parallel 95% company abatement is not established by this individual s. 12 or the personal form. Preserve the corporate ownership/control/Agreement investigation, but do not claim a generic corporate credit or put it on Schedule 5 without the controlling legal basis and actual form. A corporation's ownership by a First Nation is not proof of that outcome.

### Business investment: evidence, calculation, use and recapture

6. Confirm the investor is the eligible individual at year-end, rather than assuming residence at purchase is sufficient. Verify that the corporation/security is certified and genuinely eligible: a private/cooperative head office and active-business PE in Yukon, employee work/payroll and asset conditions, excluded professional practices and prescribed conditions are relevant. Check the security definition, arm's-length rules, cash consideration, issuer financing, capital return/redemption windows and permitted use of funds. Mere registration or a purchase of any share is not enough. [Act s. 13(1)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).
7. The statutory security definition includes specified common/cooperative shares and qualifying subordinated debt, subject to the full conditions; do not restrict the method to equity or assume every loan qualifies. A qualifying trust/RRSP holding has specific deeming and no-double-use conditions. Obtain the terms and beneficial ownership before claiming. [Act s. 13 definitions](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).
8. Reconcile qualifying cost, issue/acquisition date, the first-days-of-following-year rule and any already-used credit. Actual 2025 CRA instructions permit eligible acquisition in that year or its first 60 days of 2026 if not already claimed for 2024; do not use the same security twice. The Act supplies the recurring timing rule. Obtain the actual investment certificate; CRA calls it **YBITC-1**, while the government summary uses a different abbreviation. Match the actual issued document, not a guessed label. [Act s. 13(4)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual CRA instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [government summary](https://yukon.ca/yukon-income-tax).
9. Compute current credit and available prior/subsequent-year amounts within the statutory carry window, applying the oldest available credit first and avoiding reuse. Actual 2025 YT428 claims current credit at 63810 and the printed carry balance, then limits use by the tax balance and annual cap. It applies **before** First Nation and political credits; it is not a refundable YT479 entry. Carryback cannot create an unlimited refund beyond the target year's available tax/use limit. [Act s. 13(2)-(4)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual YT428 lines 63-74](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf).
10. Retain the issue/holding/disposal calendar and monitor certificate revocation. Disposal within the statutory holding period other than death can deem the investment never acquired; revocation can deem a certificate never issued and trigger reassessment. Do not merely retain a nominal seven-year unused balance after disqualifying disposal. The actual claim filing window remains separate from the carryover window. [Act s. 13(5),(14)-(15)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).

### Research: qualified Yukon base, correct forms and interactions

11. Establish the eligible taxpayer, actual Yukon SR&ED activity and federal qualified-expenditure definition. An individual needs the statutory year-end residence; a corporation needs a Yukon PE and is subject to the statutory excluded/exempt-control conditions. A generic lesser-of-two-estimates rule is not a substitute for qualifying and allocating the actual expenditures. Obtain federal T661/ITC workpapers, assistance and repayments, and reconcile the provincial/federal base effects rather than blindly adding percentage benefits. [Act s. 15](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).
12. Compute the base and included Yukon University portion separately. Do not double count the enhancement as another full rate on the entire base. Include only supported trust/partnership allocations and repayment adjustments. The provincial own-credit/base rule and federal assistance interactions require their actual statutory workpaper; a bare “in addition to federal SR&ED” statement is insufficient. [Act s. 15(1),(4)-(5)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).
13. For an individual, complete actual **T1232**, including its qualifying base, University portion and supported allocated credits; carry its result to actual YT 47963840. For a corporation, CRA requires **Schedule 442**, with its deadline and Schedule 5 refundable line 698. Schedule 443 is not the Yukon R&D form. Trust/partnership allocations can reach an eligible claimant under the law; this method does not turn itself into a full T3-return method. [Actual T1232](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1232/t1232-fill-25e.pdf), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf), [CRA corporate R&D instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-8-page-9-t2-return.html).
14. Calendar the legal claim deadline and retain the submitted schedules/acknowledgement. A refundable credit can first settle outstanding tax before a cash refund; it is not automatically a cash payment on the day a workpaper is made. [Act s. 15(2)-(3)](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [CRA corporate description](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-8-page-9-t2-return.html).

### Corporation rates and manufacturing/processing

15. Reconcile real Yukon PE and Schedule 5 allocation before applying Yukon rates. A mailbox/incorporation address or resident shareholder does not allocate all Canadian profit to Yukon. Determine SBD eligibility, associated allocation, taxable-capital/passive-income restrictions, year length and actual income character. Retain those federal/group workpapers; this credit guide does not manufacture the available business limit. [CRA rate/business-limit instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html), [Act s. 10](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf).
16. The general rate and small-business rate are different bases. Ordinary eligible small-business income within the available limit is territorially zero, not a deduction that can be claimed on all investment income. Federal ordinary SBD tax is 9%; the old derivation “15% minus 19%=9%” is arithmetically and conceptually wrong. [CRA ordinary federal/territorial rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html).
17. For M&P, compute the actual statutory eligible base under s. 10.1, including the limited excess M&P and taxable-income amounts, allocated exclusions and investment-income restrictions. The 9.5% deduction can produce a simple 2.5% territorial result on a fully qualifying general-rate portion, but that is not a flat statutory rate for every M&P dollar or company. CRA calls this a non-refundable credit; **Schedule 440 is a worksheet not filed**, and the claimed result goes to Schedule 5line 677. The small-business portion's deduction is zero. Do not apply the obsolete small-business M&P percentage. [Act s. 10.1](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [CRA corporate M&P instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-8-page-9-t2-return.html).
18. A simple ordinary federal 15% plus Yukon 2.5% illustration can only apply where both underlying ordinary bases/rates actually qualify. Special federal zero-emission manufacturing and other rules can differ. Do not issue a universal combined M&P or investment-income rate without that analysis. CCPC passive/investment-income, refundable-tax/RDTOH and capital-dividend questions retain their own corporate owner workpapers. [CRA federal special-rate notice](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html).

### Fitness, fertility, political, benefits and resource jobs

19. **Fitness, actual 2025-2026 filing cycle:** eligible child under 16 at the start of the year, or under 18 with disability-credit eligibility; qualifying receipt/activity and total shared eligible expenses are required. The ordinary expense cap is CAD 1,000; the eligible disability additional CAD 500 requires at least CAD 100 of eligible expense. Actual YT 47963800 uses 6.4%. Parent/spouse sharing cannot duplicate the expense. Apply childcare priority, no double use with arts, reimbursements and taxable-benefit exceptions. CRA describes ongoing programmes of at least 8 weeks or camps of at least 5 consecutive days, supervision, physical-activity conditions, and adapted observable movement for disability; motor-vehicle-dominated activity is not automatically eligible. Obtain the actual programme evidence. [CRA full fitness instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).
20. **Fertility/surrogacy:** the separately read 2025 Act applies to 2025 and subsequent years, despite the government summary mentioning a different earlier date. Apply the law's Yukon-insured year-end/death-time claimant and qualifying spouse/dependant requirements. Receipts and eligible specified fertility/surrogacy/qualifying travel expenses are required. The statutory timing is a 12-month period ending in the year, with the stated 24-month death alternative; no duplicate claimant/year use and no expense already used for the specified northern deduction. Do not invent a prohibition on all medical-credit overlap where the statute did not say it. Actual 2025 YT 47961268 computes 40%, capped CAD 10,000. A general medical or travel receipt is not automatically a specified fertility expense. [2025 amending Act s. 3 and commencement s. 6](https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf), [actual form](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).
21. **Political:** obtain the official Yukon registered-party/candidate receipt and subtract advantages as required by the law. Use the actual year's worksheet and tax-use cap; the territorial receipt does not become a federal political receipt. The actual 2025 form limits this non-refundable credit after the other printed reductions. Corporate political claims have the statutory receipt and taxpayer provisions, not an assumed personal form. [Act s. 11](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual YT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf), [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).
22. **Carbon:** keep the actual historical Schedule 14/YT479 fields and payment records for their own years. CRA identifies the final individual payment in April 2025 and excludes business years ending on/after April 1,2025. Do not promise quarterly 2026 payments because an old form still has carbon fields. [CRA changes](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).
23. **Separate programmes:** Pioneer Utility Grant and child benefit are separate eligibility/application/payment jobs, not ordinary YT428 credits. Preserve age, address, income, family/benefit period, programme decision and receipt evidence. The utility grant's current application page is a separate route; do not substitute a fitness or political form. [Pioneer programme](https://yukon.ca/en/pioneer-utility-grant), [CRA benefits](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html).
24. **Mineral exploration/flow-through/royalty:** retain the old research job, including grassroots versus later stage, Yukon work, expenditure/CEE, claim rights, certificate/programme, renunciation and federal T1229/ITC workpapers where applicable. But the old current 25%, non-refundable, ten-year-carry and automatic 15%/30% federal-stacking claims were not established. The official 2006budget describes a historical **refundable**, time-limited programme. That is not proof of a 2026entitlement, nor of every repeal detail. No current mineral field exists in the actual YT479 read. Do not invent one or Schedule 443. Hold the claimed current programme/rate/refundability/carry and federal interaction pending controlling law, preserving the resource/royalty investigation. [Historical budget only](https://open.yukon.ca/information/6e6c5d07-2fa4-4841-b743-96a50e3174e6/resource/8ae49b62-3145-3892-8053-c3d5843486af/download/fin-2006-07-budget-address.pdf), [current measures](https://yukon.ca/yukon-income-tax), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).

## Boundary and exception table

| Original code/default | Correct response |
|---|---|
| R-YT-1, non-resident | Apply actual return/credit-specific residence and source-income scope, not one universal refusal |
| R-YT-2, federal substitution | Keep federal SR&ED, mining and other ITCs separate; reconcile their actual base/assistance effects |
| R-YT-3, First Nation dispute | Obtain controlling land/law/agreement and applicable base/commencement; refer unresolved legal result |
| R-YT-4, trust | No full T3 computation here; preserve eligible trust/partnership-to-claimant allocation pathways actually authorised |
| R-YT-5, associated-group limit | Obtain the real corporate allocation/grind workpaper, do not assume a fresh full business limit per company |
| R-YT-6, part-year/FN change | Separate domestic move, arrival/departure, land residence and actual effective dates; no universal proration or citizen-only conclusion |
| Investment uncertified | Obtain actual issuer/security/investor certificate and conditions before claiming; preserve conditional work |
| Mineral uncertain | Do not treat a historical scheme as current or automatically choose a grassroots classification; isolate the actual unanswered law |
| R&D allocation uncertain | Trace actual qualified expenditures/location/payee and federal assistance interaction, not the lesser of two untested estimates |
| Allocation uncertain | Use actual federal PE/allocation workpaper; no mailbox rate choice |

## Worked cases

### Case 1: the original Whitehorse Tech Ltd. facts

Whitehorse Tech Ltd. retains the original Canadian-controlled private corporation, Yukon owner, CAD 400,000 active business income, no associated companies, no passive-income grind and no M&P facts. For a calendar 2026 ordinary illustration, additionally establish actual Yukon PE/allocation and an available business limit covering all this income, with no other restricting facts. Federal ordinary SBD tax is CAD 36,000 and Yukon tax zero. This is not a full T2 calculation and does not promise a credit based on incorporation or ownership alone. [Current ordinary rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html).

The old cross-province comparison was inconsistent (including its 500,000 example arithmetic) and did not establish current effective-date/limit rules. Preserve the comparison job by obtaining the actual other province's current owner workpaper, year and PE allocation rather than repeating stale Ontario/BC/Saskatchewan totals here. No file outside this Yukon lane is changed.

```oa-check
name: Yukon ordinary qualifying CCPC portion
inputs:
  eligible_income: 400000
steps:
  - federal_ordinary_tax: eligible_income * 0.09
  - yukon_ordinary_tax: eligible_income * 0
  - total_ordinary_tax: federal_ordinary_tax + yukon_ordinary_tax
  - effective_rate: total_ordinary_tax / eligible_income
expected:
  federal_ordinary_tax: 36000
  yukon_ordinary_tax: 0
  total_ordinary_tax: 36000
  effective_rate: 0.09
```

### Case 2: actual 2025 refundable fitness, including disability condition

A resident parent has one otherwise eligible child under 16 with CAD 1,200 qualifying unreimbursed receipts and a second otherwise eligible disabled child under 18 with CAD 400 qualifying receipts. Childcare/arts overlap and other claimant use are zero. The first base caps at CAD 1,000. The second meets the minimum expense condition and adds CAD 500, giving CAD 900. Actual 2025 YT479 expense base totals CAD 1,900 and refundable credit CAD 121.60, even if ordinary territorial tax is zero. This is the expressly dated latest annual edition read, not assumed final 2026 optional amounts. [Actual fitness rules](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [actual YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).

```oa-check
name: Yukon actual 2025 fitness caps and disability supplement
inputs:
  ordinary_child_expense: 1200
  disabled_child_expense: 400
steps:
  - ordinary_base: min(1000, ordinary_child_expense)
  - disabled_base: min(1000, disabled_child_expense) + 500
  - total_expense_base: ordinary_base + disabled_base
  - refundable_credit: round(total_expense_base * 0.064, 2)
expected:
  ordinary_base: 1000
  disabled_base: 900
  total_expense_base: 1900
  refundable_credit: 121.6
```

The disability addition in that case is used only because its stated eligibility and minimum-expense conditions are satisfied; it is not an unconditional function for all receipts. A basic CAD 1,000 ordinary base gives CAD 64, and a supported CAD 1,500 disability base gives CAD 96 under the same actual edition. [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html), [YT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf).

### Case 3: separate research base and included University amount

An eligible claimant has a supported CAD 80,000 statutory qualified Yukon base, of which CAD 20,000 is included eligible Yukon University expenditure; no additional trust/partnership/repayment adjustment applies. The territorial workpaper is CAD 12,000 plus CAD 1,000, or CAD 13,000. It is not 20% of all 80,000 and not a promise of a further unchanged federal ITC. Reconcile assistance and actual federal-base effects separately before signing. [Act s. 15](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual T1232](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1232/t1232-fill-25e.pdf).

```oa-check
name: Yukon research base and included University enhancement
inputs:
  qualified_base: 80000
  included_yukon_university: 20000
steps:
  - general_credit: qualified_base * 0.15
  - university_addition: included_yukon_university * 0.05
  - territorial_credit: general_credit + university_addition
expected:
  general_credit: 12000
  university_addition: 1000
  territorial_credit: 13000
```

### Case 4: certified investment is limited by tax, not refunded

An otherwise eligible certified investment of CAD 120,000 generates CAD 30,000 at 25%. With CAD 20,000 of supported tax available for this credit and no conflicting prior use, the actual use is CAD 20,000, within the annual CAD 25,000 cap. CAD 10,000 remains potentially available subject to the carry window, other years' tax/use, continued qualification and actual filing conditions; it is not automatically refunded or permanently valid after a disqualifying disposal. [Act s. 13](https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf), [actual YT428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf).

```oa-check
name: Yukon certified investment generation and limited use
inputs:
  certified_qualifying_cost: 120000
  available_tax: 20000
steps:
  - generated: certified_qualifying_cost * 0.25
  - used: min(25000, generated, available_tax)
  - potentially_unused: generated - used
expected:
  generated: 30000
  used: 20000
  potentially_unused: 10000
```

## When to refuse or refer

Do not finalise an unsupported material credit, legal tax-sharing result, qualified research/mineral base, PE/group limit or incomplete certificate. Obtain the actual source/claimant evidence and identify the precise missing determination. Continue supported parts of the work, preserving every original refusal and investigation above. An unresolved programme is not a reason to fabricate a replacement rule or ask the taxpayer to choose a tax treatment.

## Completion checklist

- Return year/type, residence/source and PE/group allocation documented.
- Correct ordinary, refundable, non-refundable and tax-transfer mechanisms separated.
- First Nation statute/agreement/base/commencement established before a final claim; no invented corporate 95% route.
- Investment certificate/security/investor, use order, carry windows, holding/recapture and claim deadline reconciled.
- R&D qualified base and University portion separate; federal assistance effects and actual T1232/Schedule 442 deadline checked.
- M&P statutory base/exclusions and worksheet/Schedule 5 handoff correct.
- Fitness/fertility/political claimant, receipts, timing, shared use and actual annual fields checked.
- Separate utility/child-benefit and historical carbon/resource jobs retained without unsupported current claims.
- Prepared schedules, authorised submission, accepted acknowledgement, assessment and actual refund/payment retained distinctly.

## Sources

| Source actually read and scope | Official URL | Read on |
|---|---|---|
| Read for bounded individual/corporate, M&P, political, First Nation definitions and application notes, investment eligibility/use/holding/certificate and R&D provisions; not every administrative provision or every commencement | https://laws.yukon.ca/cms/images/LEGISLATION/PRINCIPAL/2002/2002-0118/2002-0118_6.pdf | 2026-11-14 |
| Read for entire operative 2025 amendment, fertility definition/timing, AMT transition and commencement | https://laws.yukon.ca/cms/images/LEGISLATION/AMENDING/2025/2025-0006A/2025-0006A.pdf | 2026-11-14 |
| Read for current government credit/corporate/benefit summaries; statutory conflicts not silently resolved by the summary | https://yukon.ca/yukon-income-tax | 2026-11-14 |
| Read for actual 2025 annual claimant, investment certificate/timing, fitness detailed conditions, fertility and ended carbon instructions | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/yukon/5011-pc.html | 2026-11-14 |
| Read for all actual 2025 YT428 pages, tax-use, special-tax and investment/First Nation/political sequence | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c/5011-c-fill-25e.pdf | 2026-11-14 |
| Read for entire actual 2025 refundable fitness/R&D/historic carbon/fertility and final transfer form | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-tc/5011-tc-fill-25e.pdf | 2026-11-14 |
| Read for entire actual 2025 YT432 land-residence, separate federal/territorial transfer and abatement fields; unreadable percentage fields not inferred | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5011-c1/5011-c1-fill-25e.pdf | 2026-11-14 |
| Read for prescribed First Nation percentage regulation and its historical section cross-reference | https://laws.yukon.ca/cms/images/LEGISLATION/SUBORDINATE/1999/1999-0184/1999-0184.pdf | 2026-11-14 |
| Read for entire actual 2025 T1232 base, included University portion, allocated credits, deadline and handoff | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1232/t1232-fill-25e.pdf | 2026-11-14 |
| Read for current CRA ordinary federal and territorial corporation rates/business limits and special-rate warning | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html | 2026-11-14 |
| Read for bounded Yukon corporate M&P worksheet and R&D Schedule 442, deadline and Schedule 5 instructions; not the whole federal T2 guide | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4012/t2-corporation-income-tax-guide-chapter-8-page-9-t2-return.html | 2026-11-14 |
| Read for separate current utility-grant programme/application overview only; no live submission or award assumed | https://yukon.ca/en/pioneer-utility-grant | 2026-11-14 |
| Read for historical 2006budget paragraph describing a refundable time-limited mineral programme only; no current entitlement/repeal inferred | https://open.yukon.ca/information/6e6c5d07-2fa4-4841-b743-96a50e3174e6/resource/8ae49b62-3145-3892-8053-c3d5843486af/download/fin-2006-07-budget-address.pdf | 2026-11-14 |

Not yet confirmed: final 2026 personal annual forms, optional indexed credit amounts, field references and rounding; effective application of the alternative First Nation statutory tax-base definitions and all affected refundable-credit interactions, federal percentage unreadable in the fillable YT432 text, and any specific corporate First Nation exemption/credit under its controlling instrument. The government fertility summary's earlier date is not used in place of the separately read 2025 Act's commencement. Current mineral programme/rate/refundability/carry/flow-through eligibility and federal-credit interaction remain unestablished; the historical 25% non-refundable ten-year claim is not usable. Claimant-specific certificates, qualified research/assistance, investment recapture, medical/travel, special tax, allocation and group limits need actual supporting workpapers. Latest annual personal forms above are expressly the 2025-2026 filing cycle.
