---
name: kr-social-insurance
description: "South Korean social insurance for a sole trader or freelancer: National Pension (NPS), community National Health Insurance (NHIS), Long-Term Care Insurance, voluntary self-employed employment insurance and accident-insurance boundaries. Use for Korean self-employed contribution estimates, NPS floors and ceilings, health premiums, payment classification and tax deductions. Covers 2026 with separately dated 2025 regression cases. Obtain the actual insured status and assessment notice before calculating; employing staff can change the owner's own status. Foreign-insured exceptions and disputes require individual review."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kr-social-insurance"
  jurisdiction: "KR"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# South Korea Social Insurance Contributions for the Self-Employed v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Estimate a community-insured sole trader's Korean pension and health contributions in KRW for 2026, reconcile insurance bank entries and distinguish contribution payments from income-tax relief. Contributor: Open Accountants. This version has no accountant approval.

Quick reference: an NPS regional subscriber pays the full **9.5%** in 2026; the income floor and ceiling change in July. NHIS uses **income plus property**, with no vehicle charge. LTCI uses the **month-specific statutory ratio**: the exact rate ratio for January-October 2026; the enacted amendment rounds that ratio for November premiums onward, with statutory commencement on 27 November 2026. The ordinary monthly payment deadline is the **10th of the following month**; special foreign community-insured persons can instead have advance payment by the **25th of the preceding month**. Sources: [NPS premium rules](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do), [NHIS 2026 formula](https://edi.nhis.or.kr/portal/images/popup/20251204_pop01longdesc.html), [LTCI Amendment Act No. 21690, art. 9 and addenda arts. 1 and 3](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=010436&lsRvsGubun=all), National Health Insurance Act arts. 78 and 109(8), [operative Act PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20261008&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=285273&mokChaChk=N).

This is not employee payroll, a benefits calculation, a disability decision, a treaty determination or an arrears-dispute service. Employment/accident cover is classified below, not priced without the relevant registration and occupation. Do not present limited computation coverage as a complete assessment of every insurance regime.

## Ask the client first

Read available records and assessment notices before asking for missing facts. Require:

1. Date of birth, nationality, Korean residence/visa status, coverage dates and any treaty certificate.
2. Actual NPS and NHIS category: regional/community, workplace, dependent, voluntarily continued or excluded. Identify employment alongside business income, and whether the business employs staff.
3. Contribution month, NPS reported/assessed monthly income, and any accepted contribution-exception, adjustment or subsidy decision. Unknown income means **stop**, not substitution of the minimum base.
4. NHIS household membership, assessed monthly income, income categories and reference year; property-tax bases, lease deposits/rent, property deductions and the NHIS property score. Vehicles are not a premium input after abolition.
5. NHIS/LTCI notice, reductions/exemptions, actual payments/refunds and whose premiums they are. A percentage of turnover is not an assessment base.
6. Employment/accident insurance registration, staff count, business/occupation, elected earnings grade and approval notice.
7. For tax relief, business versus employment income, actual contributions paid, reimbursements/refunds and any relief already claimed. Prevent double deduction.

Do not assume age, insured status, eligibility for an exemption or a zero property score from silence. Unknown property/income classifications prevent a complete NHIS estimate even when an NPS estimate is possible.

## The method, step by step

### 1. Establish which insurance category applies

| Insurance | Treatment and conditions | Official source |
|---|---|---|
| NPS | Domestic residents aged 18 to under 60 are generally covered; regional subscribers are people outside workplace coverage, subject to statutory exclusions. Regional subscribers bear the full contribution. No-income spouses and certain students/military members have distinct exclusion/exception rules. | [NPS eligibility and regional coverage FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do) |
| NHIS | Community membership excludes workplace-insured persons and dependants; coverage also has Medical Aid and other statutory exclusions. Community premiums are household based. | National Health Insurance Act arts. 5, 6 and 69(5), [operative Act PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20261008&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=285273&mokChaChk=N) |
| LTCI | Collected with health insurance, subject to its own reductions/exemptions; not a separate voluntary enrolment decision for an ordinary NHIS subscriber. | [Long-Term Care Insurance Act arts. 7-9 and 11, official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260526&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=286217&mokChaChk=N) |
| Employment insurance | The ordinary self-employed-owner scheme is voluntary, including a solo owner or an owner with fewer than 50 workers, subject to registration and exclusions. A contractor may instead fall within mandatory employee, artist or labour-provider coverage. | [MOEL self-employed scheme, membership and applications](https://ei.work24.go.kr/ei/eim/eg/ei/eiEminsr/retrievePb0206Info.do) |
| Industrial accident insurance | Do not classify solely from the word self-employed. Voluntary small-business-owner cover can extend to insured employers with fewer than 300 workers and persons with no workers; the latter route excludes statutory labour providers, who have a separate regime. | Industrial Accident Compensation Insurance Act art. 124; [Enforcement Decree art. 122](https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lspttninfSeq=75327) |

### 2. Select the month and NPS standard income base

NPS standard monthly income discards amounts below KRW 1,000, then applies that month's floor and ceiling. Calculate the **full** regional contribution, before any approved support: `base = clamp(floor(income / 1000) * 1000, floor_base, ceiling_base)`, then `contribution = floor(base * annual_rate / 10) * 10`. Discard the contribution's amount below KRW 10 under National Pension Act art. 117 and the Treasury rule. Match the issued notice; do not apply the employee half-share to a regional subscriber. Sources: [NPS, premium amount, standard income and regional rate sections](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do), [National Pension Act art. 117, operative PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20261020&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=291347&mokChaChk=N).

| Period and subscriber | Full rate | Monthly income floor | Monthly income ceiling | Official source |
|---|---:|---:|---:|---|
| 1 January to 30 June 2026, regional subscriber | 9.5% | KRW 400,000 | KRW 6,370,000 | [NPS current premium rules and dated base table](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) |
| 1 July to 31 December 2026, regional subscriber; these bases continue through 30 June 2027 | 9.5% in 2026 | KRW 410,000 | KRW 6,590,000 | [NPS dated base table](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) |
| Historical: 1 January to 30 June 2025 | 9% | KRW 390,000 | KRW 6,170,000 | [NPS historical base and rate sections](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) |
| Historical: 1 July to 31 December 2025 | 9% | KRW 400,000 | KRW 6,370,000 | [NPS historical base and rate sections](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) |

The legislated schedule increases the full rate by 0.5 percentage points each year from 2026 to 13% in 2033. A base period crossing January does not freeze the previous year's rate. Do not extrapolate unannounced future July bases. Source: [NPS regional rate explanation](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do).

### 3. Calculate community NHIS, then LTCI

| Item | Applicable figure/condition | Official source |
|---|---|---|
| 2026 community income component | Assessed monthly income x 7.19%; add the property component | [NHIS 2026 operative formula](https://edi.nhis.or.kr/portal/images/popup/20251204_pop01longdesc.html), Act art. 69(5) |
| 2026 property component | Assessed property score x KRW 211.5 | [NHIS 2026 operative formula](https://edi.nhis.or.kr/portal/images/popup/20251204_pop01longdesc.html) |
| Community property assessment | Basic property deduction increased to KRW 100 million from February 2024; this is an assessment deduction, not an exemption for every property worth that sale price | [NHIS implementation explanation, March 2024](https://www.nhis.or.kr/static/alim/paper/oldpaper/202403/sub/section4_0.html) |
| Vehicles | Vehicle premium abolished from February 2024; do not add a vehicle score in 2025 or 2026 | [NHIS implementation explanation](https://www.nhis.or.kr/static/alim/paper/oldpaper/202403/sub/section4_0.html) |
| 2026 community monthly NHIS limits | General lower KRW 20,160; upper KRW 4,591,740, before LTCI; individual reductions and foreign-insured rules can alter the payable bill | [NHIS 2026 leaflet, qualification/collection section](https://www.nhis.or.kr/renewal_popup/poster/20260204_poster_longdesc_1.html) |
| January-October 2026 LTCI premiums | NHIS premium after applicable relief x 0.9448% / 7.19%; computed approximation 13.14%, but use the exact ratio for these months | [NHIS 2026 formula](https://edi.nhis.or.kr/portal/images/popup/20251204_pop01longdesc.html); [LTCI Act art. 9](https://law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031056547) |
| November-December 2026 LTCI premiums, enacted amendment commencing 27 November | Round the ratio 0.9448% / 7.19% at its fifth decimal place, giving the computed multiplier 0.1314; then apply monetary truncation. Addenda apply this to the premium for the whole commencement month, not just days after commencement | [Act No. 21690, art. 9 and addenda arts. 1 and 3](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=010436&lsRvsGubun=all) |
| Historical 2025 health and LTCI rates | NHIS 7.09%, property point KRW 208.4; LTCI = NHIS x 0.9182% / 7.09%, computed approximation 12.95% | [NHIS official booklet p. 48, explicitly labelled 2025](https://www.nhis.or.kr/upload/e-book/promotion/files/basic-html/page48.html) |
| Ordinary monetary truncation | Discard amounts below KRW 10; apply the statutory basis rather than rounding a headline rate first | NHIS Act art. 107; [National Treasury Funds Management Act art. 47](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031453575) |

The old formula `(income score + property score + vehicle score) x point value` is not the current method. Use NHIS-assessed income and property data, not a raw accounting profit substituted into every income category. The original September 2022 reform topic is retained as background only: the current authority explicitly separates income and property, and the February 2024 abolition removes vehicle assessment. Missing a property assessment does not mean property is zero.

For LTCI, use the health premium base to which the relevant reductions apply. For January-October 2026, retain the exact rate ratio until monetary truncation. Act No. 21690 commences on 27 November 2026 and its addenda art. 3 applies the revised ratio-rounding rule from the November 2026 premium: round at the fifth decimal place, retaining four decimal places in the ratio (computed multiplier 0.1314), then truncate the premium below KRW 10. Do not apportion the November premium by days. Source: [enacted amendment and commencement/application provisions](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=010436&lsRvsGubun=all). Special LTCI relief can differ from health relief under art. 9(3); refer such a case rather than assuming an identical reduction. The examples assume no reduction and an ordinary domestic regional household.

### 4. Classify payments and tax relief separately

Bank-name matching is a preliminary bookkeeping instruction, not proof of eligibility or tax deductibility. Match case-insensitive substrings, then obtain the notice and allocate any combined bill:

| Bank description/pattern | Preliminary classification | Verification |
|---|---|---|
| NPS, NATIONAL PENSION, 국민연금, 국민연금공단, PENSION SERVICE | NPS contribution | Period, subscriber and notice; ordinary due date below |
| NPS REFUND, 연금환급 | Pension refund | Link to original payment and reassess relief; do not book as another contribution |
| NHIS, 국민건강보험, 건강보험공단, HEALTH INSURANCE, 건강보험료 | Health and possibly LTCI | Split the components from the notice; a combined debit is not a second LTCI payment |
| 장기요양, LONG-TERM CARE | LTCI component | Verify whether already included in the health debit |
| 고용보험, EMPLOYMENT INSURANCE | Employment premium | Verify self-employed voluntary approval versus employee/artist/labour-provider category |
| 근로복지공단 | Employment or accident insurance | Identify insurance and insured person; the agency name does not decide |
| NTS, 국세청, NATIONAL TAX SERVICE | Possible tax payment | Reconcile with NTS/Hometax records; not a social insurance premium merely because tax data later affects assessment |
| HOMETAX, 홈택스 | Tax-portal-related entry | Determine whether payment, refund or reference text; a description alone proves neither filing nor payment |

| Contribution | Tax treatment, subject to the taxpayer's facts | Official source |
|---|---|---|
| Own qualifying public pension contributions paid by a resident with comprehensive income | Pension income deduction; subject to the aggregate-income limitation. Do not deduct employer contributions as the individual's own payments | Income Tax Act art. 51-3(1), (3), [operative Act PDF, p. 39](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260701&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=280405&mokChaChk=N) |
| Own NHIS/LTCI paid as community insured in calculating business income | Necessary business expense under the statutory expense rules; **not a 12% premium tax credit** | Income Tax Act Enforcement Decree art. 55(1)(11-3), [operative Decree PDF, p. 49](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260701&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=286211&mokChaChk=N) |
| Employment-income earner's qualifying employee-borne NHIS/EI/LTCI | Special income deduction against employment income; classification differs from the business-expense route. No double claim | Income Tax Act art. 52(1), [operative Act PDF, p. 39](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260701&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=280405&mokChaChk=N) |
| Employer's statutory health/EI/LTCI amounts; own qualifying workplace health/LTCI; qualifying self-employed EI and small-business-owner accident premiums | Potential business expenses in the respective statutory categories, not an automatic personal premium tax credit | Decree art. 55(1)(11) to (11-5), [operative Decree PDF, p. 49](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260701&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=286211&mokChaChk=N) |

Tax relief reduces a relevant income base; its tax saving depends on the full return. Do not invent a fixed saving for all income levels, deduct NPS twice or claim relief on amounts refunded or paid by somebody else without reviewing the entitlement.

## Boundary and exception table

| Case retained from the earlier version | Treatment | Official source |
|---|---|---|
| EC1: employed plus self-employed | A person already covered by a workplace generally does not become a separate NPS regional subscriber merely for side income. NHIS workplace non-pay income can trigger a separate assessment above KRW 20 million annually; it is the statutory non-pay income total, not a business-turnover threshold | [NPS regional/workplace conversion FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do); Act art. 71(1), Decree art. 41(4), [official law-service explanation](https://www.easylaw.go.kr/CSP/CnpClsMainPreview.laf?ccfNo=4&cciNo=1&cnpClsNo=1&csmSeq=1063&popMenu=ov) |
| EC2: no or low income | Low positive NPS income is floored; no income can support an application for contribution exception, not automatic nonpayment. Some groups are excluded instead. NHIS does not disappear just because NPS accepts an exception; use the health notice and applicable minimum/relief | [NPS eligibility/no-income FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do); [NHIS 2026 limits](https://www.nhis.or.kr/renewal_popup/poster/20260204_poster_longdesc_1.html) |
| EC3: turning 60 | Mandatory NPS category ends under the statutory loss-of-status rule. For a regional subscriber turning 60 with no other status event, loss is the following day and contributions run through the month in which age 60 is reached. For mixed status events, determine the final insured month from the exact loss date; contributions run through the month containing the day before that date. Eligible former contributors may apply for voluntary continuation before 65, subject to exclusions; NHIS/LTCI do not cease merely because NPS age coverage ends | [NPS Act arts. 12-13](https://www.law.go.kr/LSW/lsLawLinkInfo.do?chrClsCd=010202&lsJoLnkSeq=1000829747); [NPS contribution-period rules](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do); NHIS Act arts. 5-6 |
| EC4: new business/no prior tax return | Establish coverage and report actual income to NPS; obtain the initial assessed base. NHIS assesses from available qualifying information. Do not make up an income estimate, assume the floor, or promise a particular later adjustment date | [NPS income-reporting FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do); NHIS Act arts. 69-72 |
| EC5: foreign owner | NPS generally uses equal treatment subject to reciprocity, residence/status exclusions and any applicable agreement; a treaty is not the only route into coverage. Foreign NHIS has residence/status/registration and exclusion rules, and potentially a special minimum and advance due date. Refer for an individual determination | [NPS reciprocity/agreement explanation](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0110P0.do); NHIS Act art. 109(2)-(9), [official foreign-coverage guidance](https://www.nhis.or.kr/english/wbheaa02900m01.do) |
| EC6: owner employs staff | Recheck the owner's own workplace-insured status as well as registering employees. Do not continue treating the owner as community insured automatically. Employee payroll calculations are outside this computation | [NPS workplace registration FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do); NHIS Act art. 6(2) |
| EC7: July base transition | Split January-June and July-December using that period's bases; the January rate change is separate. Never use the July ceiling for the entire year | [NPS dated base table and annual rate schedule](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) |
| EC8: health-premium dispute | Distinguish an adjustment request from formal objection. Formal objection normally requires writing within 90 days of learning of the disposition and within 180 days of disposition, with a justified-delay exception. Do not use 90 days from a bill as the only rule | [NHIS Act art. 87(1)-(3)](https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1026290197) |

Self-employed employment insurance uses seven elected reference-earnings grades, not a premium rate changing merely because a different grade is selected. An approved owner can qualify for unemployment benefits after at least one year of paid self-employed coverage during the preceding 24 months, qualifying involuntary closure and active re-employment efforts; arrears and other restrictions matter. The original construction, transport, delivery and insurance-sales examples remain classification warnings: occupation-specific mandatory labour-provider coverage must be checked before assuming voluntary accident insurance. Sources: [MOEL scheme](https://ei.work24.go.kr/ei/eim/eg/ei/eiEminsr/retrievePb0206Info.do), [current Work24 benefit conditions](https://www.work24.go.kr/cm/c/f/1100/selecSystInfo.do?systClId=SC00000258&systId=SI00000347), [accident Decree art. 122](https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lspttninfSeq=75327). No benefit amount is promised from staff count alone.

## Worked cases

All amounts are KRW. Examples assume the stated insured category remains valid, no accepted NPS contribution exception/support and no health/LTCI reduction. The current cases cover 2026 and its enacted November premium transition. The eight original tests retain every original input below as historical/regression cases; `Jul 2025+` is bounded to July-December 2025, not permission to use 2025 rates indefinitely.

### Current example A: high-income regional subscriber across July 2026

Assessed monthly income KRW 8,000,000. Apply each period's ceiling and the full 9.5% rate, rather than the employee share. Source: [NPS dated base/rate rules](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do).

```oa-check
name: Regional NPS ceiling transition in 2026
inputs:
  monthly_income: 8000000
steps:
  - jan_jun_base: clamp(monthly_income, 400000, 6370000)
  - jan_jun_monthly: jan_jun_base * 0.095
  - jul_dec_base: clamp(monthly_income, 410000, 6590000)
  - jul_dec_monthly: jul_dec_base * 0.095
  - annual_nps: jan_jun_monthly * 6 + jul_dec_monthly * 6
expected:
  jan_jun_base: 6370000
  jan_jun_monthly: 605150
  jul_dec_base: 6590000
  jul_dec_monthly: 626050
  annual_nps: 7387200
```

### Current example B: supplied 2026 health notice

The NHIS health premium is KRW 350,000 before LTCI, with no relief. The LTCI estimate is KRW 45,990 and combined health/LTCI KRW 395,990 after truncation, under both the January-October exact-ratio rule and the November-December rounded-ratio rule. That coincidence does not make the methods interchangeable. Do not round a headline rate in the earlier period or round the resulting premium to the nearest won. Sources: [NHIS exact formula](https://edi.nhis.or.kr/portal/images/popup/20251204_pop01longdesc.html), LTCI Act art. 9 and NHIS Act art. 107.

```oa-check
name: Health notice and exact LTCI ratio in 2026
inputs:
  nhis: 350000
steps:
  - ltci: floor(nhis * 0.9448 / 7.19 / 10) * 10
  - total_health: nhis + ltci
  - november_ratio: round(0.9448 / 7.19, 4)
  - november_ltci: floor(nhis * november_ratio / 10) * 10
  - november_total_health: nhis + november_ltci
expected:
  ltci: 45990
  total_health: 395990
  november_ratio: 0.1314
  november_ltci: 45990
  november_total_health: 395990
```

### Current example C: November 2026 ratio transition changes the result

For an NHIS health premium of KRW 3,000,000 with no relief, the January-October exact-ratio rule produces LTCI KRW 394,210; the enacted November-December rounded-ratio rule produces KRW 394,200. The KRW 10 difference demonstrates why the applicable contribution month matters. Source: [Act No. 21690, art. 9 and addenda arts. 1 and 3](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=010436&lsRvsGubun=all).

```oa-check
name: LTCI November 2026 premium transition
inputs:
  nhis: 3000000
steps:
  - january_october_ltci: floor(nhis * 0.9448 / 7.19 / 10) * 10
  - november_ratio: round(0.9448 / 7.19, 4)
  - november_december_ltci: floor(nhis * november_ratio / 10) * 10
  - difference: january_october_ltci - november_december_ltci
expected:
  january_october_ltci: 394210
  november_ratio: 0.1314
  november_december_ltci: 394200
  difference: 10
```

### Original tests 1-3: ordinary income, ceiling and floor in 2025

Keep original inputs: test 1 age 35/income 3,000,000; test 2 age 40/income 8,000,000; test 3 age 25/income 300,000, each originally labelled `Jul 2025+`. NPS is 270,000, 573,300 and 36,000 respectively for July-December 2025. Test 1 still cannot yield total NHIS without household income/property data; vehicles are not required. Its LTCI uses the exact 2025 ratio. Test 3 may require a no-income/exception inquiry, but low positive income alone does not confer exemption. Sources: [NPS historical bases and rate](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do), [NHIS 2025 formula](https://www.nhis.or.kr/upload/e-book/promotion/files/basic-html/page48.html).

```oa-check
name: Original tests 1-3 bounded to July-December 2025
inputs:
  age_1: 35
  income_1: 3000000
  age_2: 40
  income_2: 8000000
  age_3: 25
  income_3: 300000
steps:
  - nps_1: clamp(income_1, 400000, 6370000) * 0.09
  - base_2: clamp(income_2, 400000, 6370000)
  - nps_2: base_2 * 0.09
  - base_3: clamp(income_3, 400000, 6370000)
  - nps_3: base_3 * 0.09
expected:
  nps_1: 270000
  base_2: 6370000
  nps_2: 573300
  base_3: 400000
  nps_3: 36000
```

### Original test 4: turning 60 in March 2025

Original inputs: age 60, turned 60 in March 2025, monthly income KRW 4,000,000. Assuming no other status event and no contribution exception, March 2025 is the final mandatory contribution month, at KRW 360,000 (4,000,000 x 9%); no mandatory NPS is due for April 2025. Regional status ends on the day after age 60 is reached, and the contribution-period rule therefore includes March. Obtain exact dates where another status event may affect this result. Voluntary continuation requires application and eligibility; NHIS/LTCI continue if still insured. Sources: [NPS Act arts. 12-13](https://www.law.go.kr/LSW/lsLawLinkInfo.do?chrClsCd=010202&lsJoLnkSeq=1000829747), [NPS contribution-period rules](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do).

### Original test 5: correct the premium tax-credit error

Original inputs: annual own NPS paid KRW 3,240,000 and annual own community NHIS/LTCI paid KRW 2,400,000. For a qualifying resident sole trader with sufficient comprehensive income and actual-expense accounts, NPS is a pension income deduction and health/LTCI a business expense. The old fixed KRW 288,000 tax-credit result is wrong. These facts do not determine the tax saving. Sources: Income Tax Act art. 51-3 and Decree art. 55(1)(11-3), linked in the relief table.

```oa-check
name: Original test 5 correct relief categories without invented tax saving
inputs:
  own_nps_paid: 3240000
  own_community_health_paid: 2400000
steps:
  - pension_income_deduction: own_nps_paid
  - health_business_expense: own_community_health_paid
expected:
  pension_income_deduction: 3240000
  health_business_expense: 2400000
```

### Original test 6: owner with three employees

Original input: a self-employed owner with three employees wants unemployment coverage. Three is below the voluntary self-employed scheme's staff ceiling; obtain registration, occupation, age and approval rather than declaring unconditional eligibility. Business closure does not itself prove benefit entitlement. Recheck the owner's NPS/NHIS workplace status separately. Sources: [MOEL self-employed entry requirements](https://ei.work24.go.kr/ei/eim/eg/ei/eiEminsr/retrievePb0206Info.do), [Work24 benefit conditions](https://www.work24.go.kr/cm/c/f/1100/selecSystInfo.do?systClId=SC00000258&systId=SI00000347).

### Original test 7: ceiling change in the full 2025 year

Original inputs: age 45, monthly income KRW 6,300,000, full year 2025. January-June is capped at 6,170,000; July-December uses actual 6,300,000. Source: [NPS historical base/rate table](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do).

```oa-check
name: Original test 7 full 2025 contribution year
inputs:
  age: 45
  monthly_income: 6300000
steps:
  - first_half_base: clamp(monthly_income, 390000, 6170000)
  - first_half_monthly: first_half_base * 0.09
  - second_half_base: clamp(monthly_income, 400000, 6370000)
  - second_half_monthly: second_half_base * 0.09
  - annual_nps: 6 * first_half_monthly + 6 * second_half_monthly
expected:
  first_half_base: 6170000
  first_half_monthly: 555300
  second_half_base: 6300000
  second_half_monthly: 567000
  annual_nps: 6733800
```

### Original test 8: historical health/LTCI notice

Original input: NHIS monthly premium KRW 350,000 under the old 2025 guide. Use the 2025 exact ratio and KRW 10 truncation: LTCI KRW 45,320 and combined health/LTCI KRW 395,320. The old KRW 45,325/395,325 output used rounded 12.95% and omitted truncation. The 2026 result for the same input is in current example B. Sources: [NHIS 2025 formula](https://www.nhis.or.kr/upload/e-book/promotion/files/basic-html/page48.html), [Treasury Act art. 47](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031453575), NHIS Act art. 107.

```oa-check
name: Original test 8 health premium in 2025
inputs:
  nhis: 350000
steps:
  - ltci: floor(nhis * 0.9182 / 7.09 / 10) * 10
  - total_health: nhis + ltci
expected:
  ltci: 45320
  total_health: 395320
```

## When to refuse or refer

Preserve these refusal identifiers and record the documents needed:

- **R-KR-SI-1, disability exemption:** disability status does not by itself establish a contribution exemption. Do not decide eligibility from this guide; refer with NPS status and disability documents to a licensed Korean practitioner/NPS.
- **R-KR-SI-2, international social security agreement:** obtain nationality, actual insured work and the relevant agreement/certificate. Do not assert exemption or entitlement from nationality alone. Refer for the specific agreement determination.
- **R-KR-SI-3, arrears disputes:** obtain the assessment, service dates and payment history; refer for direct NPS/NHIS engagement. Do not calculate disputed arrears, late charges or litigation advice here.

For an unresolved assessment classification, produce a reviewer flag recording the person, coverage period, situation, ambiguous fact, possible treatments, source and required determination. For a matter outside scope, produce an escalation record with the issue and documents, and stop the disputed calculation. These are workflow flags, not claims that any rate or person has accountant approval.

Never compute NPS without the assessed income and month; use an employee half-rate for regional coverage; add a vehicle premium; calculate community NHIS from income alone without establishing the property treatment; treat exception applications as approved; ignore a July base change; assume every contractor's employment/accident insurance is voluntary; invent the old NHIS/LTCI 12% tax credit; or advise on treaty exemptions, disputed arrears or penalties without individual review. Label calculations as estimates and reconcile to the issued notices before action.

## Filing and payment

| Obligation | Deadline/procedure | Official source |
|---|---|---|
| Ordinary monthly NPS | Next month's 10th; if Saturday, Sunday or public holiday, next business day. NHIS collects the premiums. Pay using the issued notice/payment reference and keep receipt | [NPS premium payment deadline and collection sections](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) |
| Ordinary monthly community NHIS/LTCI | Next month's 10th, not the current month's 25th. Check the actual notice and calendar; approved quarterly payment has separate procedures | [NHIS Act art. 78](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lsJoLnkSeq=1001733644); [LTCI Act arts. 8 and 11, official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260526&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=286217&mokChaChk=N) |
| Special foreign community NHIS | For persons within art. 109(9)'s proviso, preceding month's 25th; initial/late-month acquisition has NHIS-set exceptions. Identify the actual category before setting a calendar | Act art. 109(8)-(9), [operative Act PDF, pp. 51-52](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20261008&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=285273&mokChaChk=N) |
| NPS income/coverage report or exception request | Report through NPS branch/available electronic service; keep the acknowledged decision and resulting notice. Income changes require a supported request, not unilateral reduced payments | [NPS registration, income and no-income FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do) |
| Voluntary owner employment insurance | Submit the self-employed employment-insurance application and supporting registration/identity documents to Korea Workers' Compensation and Welfare Service; retain approval/refusal notice and selected grade. This guide does not submit live forms | [MOEL application procedure](https://ei.work24.go.kr/ei/eim/eg/ei/eiEminsr/retrievePb0206Info.do) |

For payment reconciliation, use the agency's notice and the available bank transfer, automatic debit or permitted card/bank/post-office route shown there; retain payment evidence. A successful debit does not prove a coverage adjustment has been accepted. Reconcile tax-data-driven reassessments with the income year and property base on the notice. The earlier blanket claim that every regional NPS income assessment resets in July is not confirmed and must not drive a payment calendar; the published floor/ceiling transition is confirmed independently.

## Completion checklist

- Coverage category, exact period, NPS income and household/property data documented; no invented defaults.
- Rate year and July bases selected separately; regional full-share computation and the applicable monthly LTCI ratio rule recomputed.
- NHIS ordinary/foreign due-date classification established; payment and refunds matched to the notice.
- All original cases and refusals considered; employment/accident mandatory boundaries escalated where applicable.
- Tax deductions/expenses mapped to their proper income category, supported by paid amounts, with no double relief.
- Outstanding facts and source limitations recorded with a clear handoff. No statement of accountant approval.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Official source | Actual reading scope | Read for this guide: date |
|---|---|---|
| [NPS, pension premiums](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0038M0.do) | Read for this guide: income truncation, 2024-27 base table, regional/workplace rate schedule, collection, due-date, contribution-period and own-payment deduction paragraphs. Future support-program content is not used | 2026-11-16 |
| [NPS lifecycle FAQ](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0097M0.do) | Read for this guide: no-income/student/military exclusions, regional/workplace conversion, workplace registration, foreign coverage and reporting/adjustment Q&As. An isolated stale 9% workplace answer is superseded by the explicit 2026 rate section | 2026-11-16 |
| [National Pension Act official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20261020&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=291347&mokChaChk=N) | Read for this guide: art. 117 monetary truncation and neighboring record provisions, plus arts. 88 and 88-2 collection/notice paragraphs. The final art. 88 rate is phased by transitional law; current-year rates follow the explicit NPS authority schedule above | 2026-11-16 |
| [NPS terms, reciprocity and agreements](https://www.nps.or.kr/pnsinfo/ntpsklg/getOHAF0110P0.do) | Read for this guide: reciprocity, treaty precedence and contribution-period entries; no country-specific agreement conclusion | 2026-11-16 |
| [National Pension Act arts. 11-13](https://www.law.go.kr/LSW/lsLawLinkInfo.do?chrClsCd=010202&lsJoLnkSeq=1000829747) | Read for this guide: acquisition, loss and voluntary continuation including exclusions; operative text labelled 20 October 2026 | 2026-11-16 |
| [NHIS 2026 premium notice](https://edi.nhis.or.kr/portal/images/popup/20251204_pop01longdesc.html) | Read for this guide: all displayed formulas and qualification labels: income, property and exact LTCI ratio | 2026-11-16 |
| [NHIS 2026 changes leaflet](https://www.nhis.or.kr/renewal_popup/poster/20260204_poster_longdesc_1.html) | Read for this guide: qualification/collection section only, including effective January 2026 rates and community upper/lower premium limits | 2026-11-16 |
| [NHIS March 2024 implementation explanation](https://www.nhis.or.kr/static/alim/paper/oldpaper/202403/sub/section4_0.html) | Read for this guide: property deduction and vehicle abolition paragraph; identifies February implementation, not merely a proposal | 2026-11-16 |
| [NHIS official booklet p. 48](https://www.nhis.or.kr/upload/e-book/promotion/files/basic-html/page48.html) | Read for this guide: insured categories and formulas explicitly labelled 2025; used only for historical cases | 2026-11-16 |
| [National Health Insurance Act, operative official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20261008&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=285273&mokChaChk=N) | Read for this guide: arts. 5-6, 69-73, 78, 87, 107 and 109. Selected text effective 8 October 2026; separately marked future 27 November 2026/2027 clauses are not treated as operative | 2026-11-16 |
| [LTCI Act art. 9](https://law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031056547) | Read for this guide: formula, statutory rate setting and differing-relief exception; operative 26 May 2026 text | 2026-11-16 |
| [LTCI Act official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260526&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=286217&mokChaChk=N) and [enacted Act No. 21690](https://law.go.kr/LSW/lsRvsDocListP.do?chrClsCd=010202&lsId=010436&lsRvsGubun=all) | Read for this guide: arts. 7-9 and 11, pp. 3-4, including ordinary membership, foreign exclusion, combined collection/separate bill components, and the two art. 9 texts. Read the enacted amendment art. 9 and addenda arts. 1 and 3: commencement 27 November 2026, revised rounding applies from the November premium | 2026-11-16 |
| [National Treasury Funds Management Act art. 47](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031453575) | Read for this guide: truncation rule and delegated exception; ordinary standalone premium examples only | 2026-11-16 |
| [Income Tax Act official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260701&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=280405&mokChaChk=N) | Read for this guide: p. 39, arts. 51-3(1), (3) and 52(1), pension limitation and employee special deduction; not the full income-tax return | 2026-11-16 |
| [Income Tax Act Enforcement Decree official PDF](https://www.law.go.kr/LSW/lsPdfPrint.do?ancYnChk=0&bylChaChk=N&efGubun=Y&efYd=20260701&joAllCheck=Y&joEfOutPutYn=on&lsiSeq=286211&mokChaChk=N) | Read for this guide: art. 55 opening and insurance categories (11) to (11-5), pp. 47-49, including regional NHIS/LTCI business expense | 2026-11-16 |
| [MOEL self-employed employment scheme](https://ei.work24.go.kr/ei/eim/eg/ei/eiEminsr/retrievePb0206Info.do) | Read for this guide: entry, voluntary application/approval, seven-grade structure and benefit conditions in the rendered official page. Local direct response is a redirect shell, not the reading evidence | 2026-11-16 |
| [Work24 current self-employed benefit guidance](https://www.work24.go.kr/cm/c/f/1100/selecSystInfo.do?systClId=SC00000258&systId=SI00000347) | Read for this guide: participation/payment period, closure, re-employment and restriction sections; no blanket entitlement from closure alone | 2026-11-16 |
| [Industrial Accident Compensation Insurance Enforcement Decree art. 122](https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lspttninfSeq=75327) | Read for this guide: owner categories, fewer-than-300 limit, no-worker route and labour-provider exclusion; effective 1 July 2026 | 2026-11-16 |
| [NHIS official foreign guidance](https://www.nhis.or.kr/english/wbheaa02900m01.do) | Read for this guide: registration/status conditions and foreign calculation warning. Its score-based English formula is stale; current Korean 2026 formula governs | 2026-11-16 |
| [Official legal-information service: employee premiums](https://www.easylaw.go.kr/CSP/CnpClsMainPreview.laf?ccfNo=4&cciNo=1&cnpClsNo=1&csmSeq=1063&popMenu=ov) | Read for this guide: art. 71/Decree art. 41(4) non-pay-income threshold and assessed base explanation; not a universal turnover test | 2026-11-16 |

**Not yet confirmed:** the earlier guide's approximate KRW 19,780 historical 2025 health minimum has not been reconfirmed and is superseded for current guidance by the sourced 2026 minimum above; the full current property-score bands, low-income health-income assessment cut-offs, all occupation-specific mandatory employment/accident classifications, disability-specific NPS exceptions, individual nationality/visa/treaty results, subsidy amounts, disputed arrears/late charges, the final insured month in mixed status events without the relevant dates, and regional NPS/NHIS income-reassessment timing and adjustment documentation in every category. The old general assertions of July regional NPS reassessment, November NHIS reassessment, universal six-month foreign NHIS entry and automatic acceptance of a new owner's declared estimate are not usable rules here. Current health coverage must be confirmed from the applicable residence/status rules and notice. Ordinary due dates, the NPS July floor/ceiling change and the tax-treatment correction are confirmed above.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kr-social-insurance` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kr-social-insurance. If neither is available, confirm every figure against the official source pages cited above before relying on it.
