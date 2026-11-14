---
name: il-employee-tax-refund
description: "Use this skill when advising salaried Israeli employees on voluntary tax refund claims. Trigger on phrases like \"tax refund Israel employee\", \"החזר מס לשכירים\", \"Form 135\", \"טופס 135\", \"Form 106\", \"טופס 106\", \"miluim refund\", \"מילואים החזר מס\", \"nekudot zikui missed\", \"yishuv mezakeh\", \"ישוב מזכה\", \"Section 46 donations\", \"תרומות\", \"oleh chadash credit points\", \"maternity tax refund Israel\", or any Israeli employee tax refund query. ALWAYS read this skill before advising on Israeli employee tax refunds."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/il-employee-tax-refund"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Israel: employee tax refund working paper

> **Based on work by [Skills IL](https://github.com/skills-il/tax-and-finance)**, licensed under MIT. Adapted for the OpenAccountants format.

> **General reference only.** Compute the whole year's position before recommending a claim. A change of job, leave or a missed credit does not itself establish a refund.

## Scope

Voluntary refund claims in 2026 for employees who are not required to file a full annual return. The Tax Authority's Form 135 service excludes business/company owners and those obliged to file the annual return. Such taxpayers use [il-income-tax-returns](il-income-tax-returns.md). Confirm spouse treatment and include all required income; a refund request may expose an underpayment.

| Quick reference | Rate or threshold and conditions | Official source |
|---|---|---|
| Refund claim period | Return filed no later than the end of 6 years after the tax year (period expressed in words in statute) | ITO s.160(a), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Open years during 2026 | 2020-2025; 2020 claim by 31 December 2026; later endpoints in table below are derived | ITA Form 135 service, https://www.gov.il/en/service/itc135 |
| Resident points | 2 under s.34 plus 0.25 under s.36 = 2.25 (derived); woman additional 0.5 under s.36A = 2.75 (derived), subject to actual eligibility | ITO ss.34, 36, 36A, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Combat reserve credits for 2026/2027 | Based on qualifying combat service in the preceding tax year; day bands below; maximum 4 points | ITO s.39B, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Donation credit for individual | 35% for qualifying total donations above NIS 207; eligible amount capped at lower of 30% taxable income and NIS 10,354,816 | ITO s.46(a), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

The current annual value per point and income-tax bands have one home in [il-income-tax-returns](il-income-tax-returns.md). Use each claim year's own figures; do not apply the wider 2026 bands to a 2024 or 2025 claim.

## Ask the client first

Obtain the claim year; residence and personal status; spouse's income and filing duty; all Form 106s; National Insurance annual income/withholding certificates; pension/life-insurance certificates and Form 161 if relevant; bank ownership confirmation; prior claims/assessments; credits already used; and the specific eligibility evidence below. Check ongoing credit changes for the current Form 101 as well as the historic claim.

## The method, step by step

### Check the window and return route

| Tax year | Last claim date (derived under s.160) | Official source |
|---|---|---|
| 2020 | 31 December 2026 | ITO s.160; ITA service expressly gives this date, https://www.gov.il/en/service/itc135 |
| 2021 | 31 December 2027 | Same service expressly gives this date, https://www.gov.il/en/service/itc135 |
| 2022 | 31 December 2028 (derived: year plus 6) | ITO s.160, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| 2023 | 31 December 2029 (derived: year plus 6) | ITO s.160, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| 2024 | 31 December 2030 (derived: year plus 6) | ITO s.160, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| 2025 | 31 December 2031 (derived: year plus 6) | ITO s.160, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

Earlier years are outside this ordinary 2026 claim window. Special disputes or relief do not follow from this table. A required full return is not replaced by Form 135. The official service supports fully online refund applications from tax year 2019, or the relevant year's paper form with documents. Opening a refund file is for the application, not a determination that a business registration is needed ([official service](https://www.gov.il/en/service/itc135)).

### Reconcile Form 106 and National Insurance income

Collect every employer certificate and sum tax withheld without counting the same pay twice. Read taxable pay, pension/study-fund deposits, work months and tax withheld using the **actual year's form labels**. The old field mapping (042 withheld, 158/172 salary, 218/219 study-fund deposits) needs checking against the year's issued form before entry. Form 106 from a job change does not prove over-withholding.

Obtain National Insurance annual certificates for maternity/paternity, unemployment, work injury, pregnancy-preservation and reserve-duty payments. Identify taxable amounts and tax withheld from the certificate and applicable rules, and avoid adding reserve pay again where the employer already included it. The official refund-service document list includes the relevant benefit confirmations. Do not assume every benefit is fully taxable merely from the benefit name or the old “up to 91 days” description ([official document list](https://www.gov.il/en/service/itc135)).

### Review every refund trigger and its evidence

| Trigger | What to verify before calculating |
|---|---|
| Mid-year job change, multiple employers or partial-year work | All employer/benefit certificates, months worked, tax coordination and total annual income |
| Maternity/paternity leave or unemployment | Actual annual National Insurance amounts and withholding, employer overlap |
| Combat reserve service | Prior-year qualifying combat days and the IDF eligibility certificate, not a generic service-days total |
| Donation | Qualifying institution's approval in the donation year and valid receipts; aggregate and cap test |
| Eligible locality (Yishuv Mezakeh) | Center of life, residence continuity and current locality-specific list; local authority confirmation/Form 1312A |
| New immigrant | Certificate and actual Aliyah date, correct pre/post-2022 schedule, any allowable interruption |
| Degree or professional certificate | Completion year, recognized course/institution, study length, specialization timing and prior use |
| Single parent, alimony or child/custody change | Court judgment, payments, family/custody and benefit facts; no automatic single-parent credit merely from a label |
| Disability/blindness | Applicable medical determination and tax-assessor approval, duration and income type |
| Personal pension/life-insurance deposits | Eligible certificates, insured income, s.45A/s.47 interaction and relief already used |
| Early study-fund withdrawal | Actual withholding and account history; compare final tax rather than treating the old 47% as a universal rule |
| One-time bonus/13th salary | Whole-year computation, withholding method and credits already used |

### Combat reserve points: keep the service and credit years separate

These bands apply for **tax years 2026 and 2027**, based on qualifying service **as a combatant in the previous year**. Obtain the IDF confirmation of qualifying combat service. They are not the schedule from 2028 onward.

| Prior-year qualifying days | Points | Official source |
|---|---|---|
| 30-39 | 0.5 | ITO s.39B(a)(1), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| 40-49 | 0.75 | ITO s.39B(a)(2), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| 50-54 | 1 | ITO s.39B(a)(3)-(4), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Each additional complete 5 days after 50 | Add 0.25, capped at 4 total | ITO s.39B(a)(4), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| From 110 days | 4 maximum (derived from band formula) | ITO s.39B; ITA directive full table, https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info161225-1/he/IncomeTax_employers-info161225-1.pdf |

From 2028 the statute's transition changes the starting test to 20 qualifying days for 0.75 point, plus 0.25 per further complete 5 days, capped at 4. Keep that future schedule out of 2026 calculations ([ITO s.39B transition footnote](https://www.btl.gov.il/Laws1/00_0103_000000.pdf); [directive](https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info161225-1/he/IncomeTax_employers-info161225-1.pdf)). Points reduce otherwise payable tax subject to the person's use limits; their cash value is not automatically a refund.

### New immigrant points, distinct from foreign-income exemption

| Aliyah timing and period | Fraction of annual point per month (law uses words for fractions) | Official source |
|---|---|---|
| First Aliyah from 1 January 2022: first 12 months | 1/12 | ITO s.35(a)(1), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Next 18 months (months 13-30) | 1/4 | ITO s.35(a)(1a), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Next 12 months (months 31-42) | 1/6 | ITO s.35(a)(2), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| Next 12 months (months 43-54) | 1/12 | ITO s.35(a)(3), https://www.btl.gov.il/Laws1/00_0103_000000.pdf |
| First Aliyah before 1 January 2022 | 1/4 for first 18 months, 1/6 for next 12, 1/12 for next 12 | ITO s.35 transition footnote, https://www.btl.gov.il/Laws1/00_0103_000000.pdf |

Post-2022 totals are 1 + 4.5 + 2 + 1 = **8.5 annual-point equivalents over 54 months** (derived), rather than a fixed point count for every calendar year. Earlier schedule totals 7.5 over 42 months (derived). Prorate by eligible months resident; requested exclusion of an uninterrupted absence may apply where it is at least 6 months and at most 3 years, under s.35(c). A returning resident's foreign-income exemption does not automatically qualify them for this credit: s.35 has its own historical qualifying definition. **Section 35 does not create a mortgage-interest deduction.** Foreign-income and gain relief belongs in [il-new-immigrant](il-new-immigrant.md).

### Donation, degree and other relief

For s.46, the qualifying aggregate must be **above** NIS 207, not merely equal. The individual credit is 35% of the eligible amount; annual amount cap is the lower of 30% of taxable income and NIS 10,354,816. Excess over the cap may be carried into the next 3 tax years subject to each year's cap. Verify approved institution and donation year before claiming ([ITO s.46](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)). Combined donation and qualifying R&D claims need the separate s.46A ceiling review: the combined s.46 qualifying amount and specified R&D deductions cannot exceed 50% of taxable income before that R&D deduction. Refer those combined cases rather than using the standalone cap alone. Receipt-format requirements need current instructions; do not invent that only original paper receipts work.

Under s.40C, a qualifying resident's recognized BA generally gives 1 point for the number of study years, capped at 3 tax years; MA gives 0.5, capped at 2 years, beginning in the following year. Only one BA and one MA qualify, with completion/entitlement proof supplied to the assessing officer. Required-specialization timing can permit an alternative start only where specialization begins no later than the year following degree completion. Under s.40D, a qualifying professional certificate gives 1 point for the study-year count, capped at 3 years, from the following year, where the course is at least equivalent to 1,700 academic hours and the professional certificate is recognized by a government ministry, with completion/entitlement proof supplied to the assessing officer. Section 40E requires choosing academic or professional relief where both apply. Historical completion-year transitions need checking before using these for an older refund ([ITO ss.40C-40D](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

Child/custody credits, single-parent/alimony rules, locality relief, disability/blindness and pension relief are fact-sensitive. The old universal child-age table and disability ceiling table are not used as entitlement rules here. Get the exact claim-year provisions and evidence. Locality relief is linked to qualifying income and the locality-specific ceiling, not simply a percentage discount on all tax. Maintain the disability medical-duration distinctions and applicable income type as open computation inputs.

### Calculate the result before submitting

Refund = all tax paid/withheld for the year minus the correct annual liability after eligible reliefs. Positive means an estimated refund; negative means a balance due. Show the computation and missing facts, not a guaranteed amount. A range is appropriate where factual inputs remain unresolved; do not invent a range after every input has been established.

## Worked cases

### Combatant: service in 2025, tax relief in 2026

Retain the teacher's 65-day prior-year service case, now expressly assuming an IDF certificate confirms **combatant** status and all 65 qualifying days in 2025. In 2026: 1 point for the first 50 days plus 3 complete 5-day increments x 0.25 = 1.75 points. At the annual-return skill's NIS 2,904/point, credit is NIS 5,082. Assume tax before this credit and withholding are both NIS 6,000, with no other changes and enough liability to absorb it. Liability becomes NIS 918 and estimated refund NIS 5,082. Without those assumptions the credit's value is not a promised refund.

```oa-check
name: Prior-year combat service credit and refund reconciliation
inputs:
  days: 65
  tax_before: 6000
  withheld: 6000
steps:
  - points: min(1+floor((days-50)/5)*0.25,4)
  - credit: points*2904
  - liability: max(tax_before-credit,0)
  - refund: withheld-liability
expected:
  points: 1.75
  credit: 5082
  liability: 918
  refund: 5082
```

### Donation: cap comparison before refund

Assume eligible 2026 donations of NIS 6,000 to approved institutions, taxable income NIS 100,000, tax before the donation credit NIS 10,000 and withholding NIS 11,000. The income-based cap is NIS 30,000, below the absolute cap but above the donations, so all NIS 6,000 is eligible. Credit is NIS 2,100; final tax NIS 7,900; estimated refund NIS 3,100. Approval, receipts and sufficient remaining liability are assumed established.

```oa-check
name: Donation cap and actual prepayments
inputs:
  donation: 6000
  income: 100000
  tax_before: 10000
  withheld: 11000
steps:
  - amount_cap: min(income*0.30,10354816)
  - eligible: min(donation,amount_cap)
  - credit: eligible*0.35
  - liability: max(tax_before-credit,0)
  - refund: withheld-liability
expected:
  amount_cap: 30000
  eligible: 6000
  credit: 2100
  liability: 7900
  refund: 3100
```

Retain the earlier historical negative-refund example as a conditional check: 6 months at NIS 25,000 and 6 at NIS 22,000 give NIS 282,000 income; withholding NIS 24,800 + NIS 22,400 = NIS 47,200. **If** the correct 2024 calculation establishes rounded gross tax NIS 56,003 and 2.75 eligible points at NIS 2,904, liability is NIS 48,017 and balance due is NIS 817. Those old 2024 band inputs require their year's source; the case illustrates why a job change is not proof of refund. The old 2022 donation scenario likewise assumes approved NIS 6,000 donations and a 35% applicable credit, giving NIS 2,100; its ordinary claim window ends 31 December 2028, but actual 2022 credit eligibility requires the historical year's rules.

## When to refuse or refer

Refer a compulsory annual-return case, missing spouse or benefit income, disputed eligibility, expired-window disputes, insufficient medical/residence/IDF evidence, historical rates not established, or a claim producing tax owed. Do not submit a refund merely to test whether it succeeds. Do not add the same reserve benefit from both employer and National Insurance records.

## Filing and payment

Prepare the relevant year's Form 135 or full return, attach the official service's supporting documents and bank confirmation, submit through the stated online/paper channel and retain acknowledgment. Respond to additional-document requests by the stated deadline. The authority checks the application and issues an assessment/outcome; a refund goes to the documented account if approved ([official service](https://www.gov.il/en/service/itc135)).

Under s.160(a), qualifying overpayment is refundable within 1 year of the assessment establishing it or 2 years after the tax year in which paid, whichever is later, with the statutory linkage/interest calculation. These are not a guaranteed portal turnaround. Section 160 contains fraud/non-filing and appeal qualifications; s.160A permits withholding refunds in assessment circumstances. Obtain the current interest provision rather than promising the old flat 4% on every case ([ITO ss.159A,160,160A](https://www.btl.gov.il/Laws1/00_0103_000000.pdf)).

For an ongoing credit, update Form 101 with the employer and supporting documents for the current year; retrospective refund and prospective withholding correction are separate tasks. Coordinate multiple payers as appropriate. No actual filing, payment or contact is authorized by this working paper.

## Completion checklist

Check full-return eligibility and window; collect all spouse/employer/benefit income; remove duplicate amounts; apply the actual year's bands and substantiated points; compute all reliefs and caps; reconcile payments; explain refund or balance due; obtain CPA review; submit only the correct route and keep receipts; update ongoing payroll data.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated Income Tax Ordinance; Read for ss.33A-36A, 35 schedule/transition/absence conditions, 39B current/future service-year rules, 40C-40E education criteria/election, 46/46A donation amount/rate/carryforward and combined R&D ceiling and 160 refund conditions | https://www.btl.gov.il/Laws1/00_0103_000000.pdf | 2026-11-14 |
| ITA Form 135 service; Read for eligible claimants, 6-year examples, online/paper route, income/spouse/benefit documents, bank details and outcome | https://www.gov.il/en/service/itc135 | 2026-11-14 |
| ITA s.39B employer directive; Read for 2026-2027 and 2028 schedules, preceding-year combat service and IDF confirmation requirement | https://www.gov.il/BlobFolder/dynamiccollectorresultitem/employers-info161225-1/he/IncomeTax_employers-info161225-1.pdf | 2026-11-14 |

Not yet confirmed: current Form 106 issue deadline and exact field identifiers 042/158/172/218/219; full tax treatment/return field placement of each National Insurance benefit and the old 91-day description; receipt-format instructions; detailed child/custody/single-parent/alimony credits, locality-specific list (including the old 12-month continuity condition) and medical exemption calculation. The old disability ceilings (NIS 445,200 for 365+ days, NIS 81,960 for 185-364 days, NIS 684,000 for specified pension categories) and 100%/90% qualifying tests require the actual s.9(5) branches and cannot be used just from this table's former labels. The old universal early-withdrawal 47% and pension-relief formulas remain unconfirmed. The 2024 NIS 56,003 gross-tax example and 2022 donation claim require historical rates/eligibility before filing; both cases are preserved above with explicit assumptions. The old 31 March 2027 Form 106 date for the reserve-duty example is not asserted as a verified deadline. Refund interest is not quoted as a universal 4%. Section 35 is credit relief, not a mortgage deduction; ordinary-returner status under s.14 does not automatically establish s.35 eligibility.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `il-employee-tax-refund` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/il-employee-tax-refund. If neither is available, confirm every figure against the official source pages cited above before relying on it.
