---
name: sa-gosi-saudization
description: "Saudi Arabia private-sector employer payroll for 2026: identify existing versus new GOSI cohorts, branch coverage, contributory wages and the July pension-rate change before computing employer contributions and employee deductions. Reconciles GOSI bills, gross-to-net bank pay, Nitaqat entity assessment, independent occupational localization and Mudad WPS reporting. Preserves the IT-consultancy LLC and capped-manager examples with cohort-specific results. Read before Saudi payroll work; missing coverage or wage evidence stops final submission."
jurisdiction: SA
tax_year: 2026
last_updated: "2026-11-16"
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: "payroll"
category: "payroll"
version: "1.1"
type: "computation"
---

# Saudi Arabia employer payroll: GOSI, Saudization and WPS for 2026

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill prepares a private-sector employer compliance workpaper. Calculations are preliminary and require qualified professional review before a payroll, contribution return or employment decision is submitted.

## Scope

Read before Saudi employer registration, social-insurance contributions, Nitaqat monitoring or monthly wage-file work. The three outputs are separate: **GOSI contribution liability**, **the establishment's actual Qiwa/Nitaqat assessment plus occupational localization tests**, and **wages paid and reported through Mudad**. Passing one does not establish compliance with the others.

**2026 quick reference:** existing-law Saudi pension contributions remain 9% each for employer and employee. For the new-law cohort they are **9.5% each through 30 June 2026 and 10% each from 1 July 2026**. Ordinary SANED is **0.75% each**, not 1.5% each; occupational hazards is ordinarily **2% employer-only**. First establish each person's law, branch coverage, contribution history and wage base. [GOSI current employer awareness](https://awareness.gosi.gov.sa/businessJourney.html), [existing-law awareness](https://awareness.gosi.gov.sa/journey1.html), [official phased-rate table, PDF p. 4](https://awareness.gosi.gov.sa/pdf/Contributions.pdf).

Saudi employment remuneration is not subject to an ordinary personal-income-tax/PAYE computation merely because the employee is Saudi or foreign. This does not exempt a person's separate business, non-resident service income or employer tax obligations. Income Tax Law art. 2 concerns the specified business/taxpayer categories; the WHT guide's employee/independent-service distinction must be respected. Use [CIT](sa-corporate-tax.md), [WHT](sa-withholding-tax.md), [Zakat](sa-zakat.md), [VAT](saudi-arabia-vat.md), [e-invoicing](saudi-einvoice.md), [formation](sa-formation.md), [intake](sa-freelance-intake.md) and [return assembly](sa-return-assembly.md) for those separate jobs. [Income Tax Law art. 2](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf); [WHT guide, employment-relationship example](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf).

## Ask the client first

Obtain the following records before calculating or classifying. Do not infer missing coverage from a passport alone.

| Required input | Evidence and decision it controls |
|---|---|
| Employer legal name, CR, unified establishment number, GOSI account, principal/branch accounts and authorised users | Registration reconciliation across GOSI, Qiwa, Mudad and the bank; do not assume each CR is its own Nitaqat entity |
| Payroll month, join/leave dates, paid/unpaid leave, absences and all changes | Relevant rate period, bill, prorating and filing events |
| Each worker's Saudi/GCC/other nationality, ID/iqama, date of birth, residency/work-permit and expiry records | Actual compulsory branches, age conditions, GCC extension and immigration calendar |
| Full GOSI **and civil-pension** contribution history, including withdrawn/compensated periods and current portal cohort/branch classification | Whether there were relevant periods before **3 July 2024**; a recent first entry on this employer's payroll does not prove new-law status |
| Contract and wage breakdown: basic, cash/in-kind housing, commissions, sales/profit percentages, overtime, bonuses and other allowances | Statutory contribution base, not a blanket “include every fixed allowance” default |
| Other simultaneous employers and their registered wages | Aggregate cap and any required allocation; do not give each employer a separate unrestricted SAR 45,000 cap |
| Qiwa entity/activity, workforce averages, counting categories, wages, job codes, current band and dated calculator output | Weighted localization assessment and current thresholds |
| Sector/occupation decisions, actual duties, professional accreditation and phased effective dates | Separate occupation quota and qualifying-worker tests |
| Bank/payroll-card details, contractual due date, gross-to-net workpaper, actual transfers, rejected transfers and original bank wage file | Wage compliance and Mudad upload reconciliation |
| Prior GOSI bills, SADAD receipts, WPS acknowledgements/justifications, notices and exemptions | Arrears, corrections, disputed amounts and special treatment |

If cohort, coverage, base or bank reconciliation is missing, return a missing-evidence schedule and conditional estimate; stop final payroll/contribution sign-off. Never create phantom staff, backdate unsupported employment or count a worker whose substantive role fails the localization decision.

## The method, step by step

### 1. Classify the insured person and the law

The **1445H Social Insurance Law, M/273**, is effective **3 July 2024** for new civilian labour-market entrants without previous relevant civil-pension/social-insurance periods. The Royal Decree preserves earlier laws for existing participants, subject to its specified retirement-age/service changes. Those retirement changes do **not** turn all existing participants into the new contribution-rate cohort. Check the actual contribution-history and GOSI classification, including exceptions for previously compensated periods. [M/273 decree, second/fourth clauses](https://beta.gosi.gov.sa/new-system); [current employer awareness, eligible categories](https://awareness.gosi.gov.sa/businessJourney.html).

For an ordinary Saudi private-sector worker, determine pension, occupational-hazards and SANED eligibility separately. New-law pension coverage is in art. 14; new-law SANED art. 43 has its own entry-age/retirement conditions. Do not deduct SANED merely because someone is Saudi if that branch is not applicable. Occupational-hazards coverage ordinarily extends to non-Saudi workers; excluded or specially introduced categories require their own decision. **GCC extension of protection is a separate home-state scheme calculation**, not permission to charge every GCC national Saudi pension/SANED rates. [New law arts. 5-8, 14, 28-29, 43-44](https://beta.gosi.gov.sa/new-system); [old law arts. 4-5, 18-19](https://beta.gosi.gov.sa/social-insurance).

Public-sector civil staff cannot simply be labelled “PPA, outside GOSI”: the new scheme also covers qualifying civilian public entrants. Their pension/occupational-hazard commencement and salary rules need a public-sector workpaper. Military/security, domestic/Musaned, maritime, agricultural, short temporary/seasonal and other special categories are not automatically ordinary private-sector payroll. The new law's art. 6 expressly leaves listed categories to Board/regulatory decisions. Route these with the exact law/coverage decision rather than assuming either universal coverage or universal exemption.

### 2. Establish the contributory wage and cap

For each covered person/month, reconcile contract, actual pay, registered wage and the law-specific base. New-law IR art. 17 and the employer guidance include basic salary and equivalent commissions/sales or profit percentages, cash housing at the agreed value, and in-kind housing valued at **two months' basic salary annually**, subject to stated exceptions. This is a monthly equivalent of one-sixth of basic when the annual valuation applies; it is not a universal 25% housing default. The monthly maximum is **SAR 45,000**. [New law art. 8](https://beta.gosi.gov.sa/new-system); [new IR art. 17](https://www.uqn.gov.sa/details?p=25240); [current awareness, wage elements](https://awareness.gosi.gov.sa/businessJourney.html).

| Wage component | Treatment and evidence required |
|---|---|
| Basic salary | Included under the applicable statutory definition |
| Cash housing | Include the contractual cash amount under the applicable regulation |
| In-kind housing | New-law annual two-month valuation above; obtain the old-law registration regulation/accepted valuation for old-law staff instead of silently extending the new formula |
| Commissions, sales/profit percentages | Basic-equivalent treatment described by current new-law guidance; determine attributable month and applicable old-law rule separately |
| Transport, mobile, food and other allowances | Analyse their legal character and contract. No blanket inclusion merely because fixed/unconditional; no blanket exclusion of remuneration re-labelled as an allowance |
| Performance/annual bonus | Character and attribution require the applicable wage regulation; recurrence alone does not decide inclusion |
| Overtime and end-of-service accrual | Keep separate from ordinary basic/housing working base; any special contractual reclassification needs the actual regulation. End-of-service liability is a separate calculation |
| Several employers, wage changes, age-related increases, joining/leaving or irregular wage | Apply the relevant registration/contribution rule and portal evidence; do not invent full-month, daily or uncapped treatment |

The old law art. 19 defines the base and empowers regulation for added elements; GOSI's contributor FAQ explains the **aggregate** ceiling and proportional allocation across simultaneous employers. New-law IR art. 19 expressly requires the same **SAR 45,000 aggregate ceiling**, allocating each employer's capped base in proportion to its wage divided by combined wages. [New IR art. 19](https://www.uqn.gov.sa/details?p=25240). Preserve the uncapped wage in the workpaper even when the contribution base is capped. Gross pay, contributory wage and net bank transfer are different amounts. [Old law art. 19](https://beta.gosi.gov.sa/social-insurance); [GOSI contributor FAQ, multiple-employer cap](https://www.gosi.gov.sa/GOSIOnline/FAQ_Contributor?locale=ar_SA).

For new-law irregular/partial periods, IR art. 18 multiplies daily wage by **30**; piece/profit/sales/output wages use the stated previous-year actual monthly average or the comparable-worker rule for a new entrant, while hourly wages require the Governor's specific controls. IR art. 20 uses wages before deductions and charges the joining/leaving months by **actual service days**; specified leave, permitted unpaid absence and secondment rules also apply. Art. 21 limits late wage corrections subject to the statutory exception. Do not force a full month or an ad hoc bonus average. [New IR arts. 18–21](https://www.uqn.gov.sa/details?p=25240).

### 3. Apply the correct 2026 branch rates

These are ordinary rates **only where every listed branch applies** and no special occupational-hazard increase or separate GCC scheme applies.

| Covered worker / contribution period | Pension rate employer / employee | SANED employer / employee | Occupational hazards employer / employee | Derived total employer / employee | Official source |
|---|---|---|---|---|
| Existing-law Saudi worker, 2026 | 9% / 9% | 0.75% / 0.75% | 2% / 0% | **11.75% / 9.75% (derived)** | [Old law art. 18](https://beta.gosi.gov.sa/social-insurance); [current SANED](https://awareness.gosi.gov.sa/journey1.html) |
| New-law Saudi worker, 1 January–30 June 2026 | 9.5% / 9.5% | 0.75% / 0.75% | 2% / 0% | **12.25% / 10.25% (derived)** | [Phase table p. 4](https://awareness.gosi.gov.sa/pdf/Contributions.pdf); [current branches](https://awareness.gosi.gov.sa/businessJourney.html) |
| New-law Saudi worker, 1 July–31 December 2026 | 10% / 10% | 0.75% / 0.75% | 2% / 0% | **12.75% / 10.75% (derived)** | [Phase table p. 4](https://awareness.gosi.gov.sa/pdf/Contributions.pdf); [current branches](https://awareness.gosi.gov.sa/businessJourney.html) |
| Ordinary non-Saudi worker covered only for occupational hazards, outside GCC extension | None / none | None / none | 2% / 0% | **2% / 0%** | [Old law arts. 4, 18](https://beta.gosi.gov.sa/social-insurance); [new law arts. 28–29](https://beta.gosi.gov.sa/new-system) |

Sources: pension existing law art. 18, [old law](https://beta.gosi.gov.sa/social-insurance); new-law decree's phased implementation and [official table, PDF p. 4](https://awareness.gosi.gov.sa/pdf/Contributions.pdf); operational SANED **1.5% total split equally** and hazards rates in [new-law awareness](https://awareness.gosi.gov.sa/businessJourney.html) and [existing-law awareness](https://awareness.gosi.gov.sa/journey1.html). The enabling new-law art. 44 prints a 2% SANED headline and permits variation; do not substitute its unadjusted 1% each or an old FAQ's obsolete SANED text for GOSI's current 0.75% each guidance. The old draft's 1.5% **each** was wrong even though another table in that draft correctly displayed 0.75%.

For historical comparison, new-law pension was 9% each until 30 June 2025 and 9.5% each from 1 July 2025. The published future sequence is 10.5% each from **1 July 2027**, then 11% each from **1 July 2028**. Do not apply either future increase to 2026. [Official phased-rate table](https://awareness.gosi.gov.sa/pdf/Contributions.pdf).

Calculate base × each applicable branch for each worker, using the billing system's required rounding. Aggregate employer liability and employee deductions separately. The employer remits both; employee deductions reduce net pay, whereas employer contributions add to employer cost. Match the generated GOSI bill and investigate every difference rather than adjusting wages to force a match.

### 4. Register changes, pay GOSI and retain the evidence

The old law art. 19(5), (8) requires contribution payment and monthly wage schedules **within the first 15 days of the following month**, not the end of that month. The current employer FAQ describes SADAD/bank channels and that same payment period. GOSI's contributor FAQ says new joiners/leavers should be registered/removed by **the end of the joining/leaving month**; it also contains older, differently worded registration answers. Register promptly on the actual date and retain the current account instruction. Do not delay a join/leave action by choosing the more generous FAQ. [Old law art. 19](https://beta.gosi.gov.sa/social-insurance); [employer FAQ, payment](https://www.gosi.gov.sa/GOSIOnline/FAQ_Employer); [contributor FAQ, joiners/leavers](https://www.gosi.gov.sa/GOSIOnline/FAQ_Contributor?locale=ar_SA).

The **new-law implementing regulation**, published in the official gazette on **5 July 2024**, resolves the timing directly: art. 24 also requires payment **within the first 15 days of the following month**. Art. 6 requires establishment registration within **10 days** of meeting coverage conditions; new worker, leaver and worker-data changes are notified immediately and no later than the **last day of the relevant month**. Changes to employer activity/legal form/data have a **10-day** maximum. New-law registration timing therefore comes from the regulation, not a guess from a legacy FAQ. [New IR arts. 6, 24](https://www.uqn.gov.sa/details?p=25240).

Archive worker coverage/cohort evidence, wage changes, calculation, GOSI bill, submitted schedule, SADAD reference and bank settlement. Check arrears separately from the current month. A portal submission is not payment evidence. There is no confirmed universal separate “annual GOSI reconciliation return” in the sources read; reconcile annually as an accounting control and comply with an actual notice if issued.

### 5. Assess Nitaqat at the correct entity and period

The developed Nitaqat manual defines the entity by all branches of the **same economic activity owned by one firm**. It uses workforce averages and the applicable activity coefficients. Its five bands are **Red, Low Green, Medium Green, High Green and Platinum**. The old Yellow row and giant/big/medium/small/tiny fixed size-band matrix are not the developed method. The manual expressly replaced fixed size categories with a curve based on worker count. [Decision 182495/manual, definitions and §§3-4](https://www.hrsd.gov.sa/sites/default/files/2023-02/E182495.pdf).

For the manual's method, the minimum percentage for each green/platinum range is **R = M × ln(O) + W**, where O is the relevant workforce and M/W are the activity/range/year coefficients. Compare the properly calculated localization rate with all four thresholds; below Low Green is Red. **Do not reuse an unrelated sector's coefficients or assume a 5–75% universal quota range.** Obtain the current Qiwa calculation and applicable updated manual/coefficients, average periods, exclusions and category weights before determining the actual band. A snapshot headcount fraction is not that complete computation.

Check qualifying wage, full/part-time/flexible/student/trainee status, disability/Mowaamah conditions, concurrent employment and any recognized GCC/special-category treatment. The previous “women in male-dominated roles get a multiplier” statement has not been confirmed as a general current rule. Do not count every Saudi as one, every disability as four, or every GCC national on the basis of a general payroll table. [Preceding wage-count decision](https://www.hrsd.gov.sa/sites/default/files/2020-11/61706.pdf); [new prospective decision, p. 1](https://www.hrsd.gov.sa/sites/default/files/2026-11/qrar-wzary-a-tmad-tnzym-ahtsab-alajwr-fy-brnamj-thfyz-almnshat--ly-altwtyn-ntaqat.pdf).

**Future change, not 2026:** HRSD's decision dated **25 October 2026** approves a new wage-count regulation with stage one **25 April 2027–24 April 2028**, and stage two from **25 April 2028**. Its wage definition refers to documented ministry-platform wages. The prospective table must not be applied early to 2026. Re-open the complete applicable column and category when preparing a 2027/2028 workpaper; this skill does not assert a future generic qualifying-wage number. [Decision clauses 2-4](https://www.hrsd.gov.sa/sites/default/files/2026-11/qrar-wzary-a-tmad-tnzym-ahtsab-alajwr-fy-brnamj-thfyz-almnshat--ly-altwtyn-ntaqat.pdf).

| Current band | Operational workpaper action |
|---|---|
| Platinum / High Green | Preserve current eligibility shown for the requested Qiwa service; status alone does not grant unlimited visas, tender priority or an unconditional right to transfer another firm's worker |
| Medium Green / Low Green | Compare the specific visa, work-permit renewal and transfer service's eligibility/limits with the dated account result; do not give both an unconditional “full” entitlement |
| Red | Escalate recruitment, renewal and mobility restrictions shown in the account immediately; a band is not itself proof that every iqama renewal, tender or transfer is legally barred |

The manual has service-by-band tables, but current immigration, worker-mobility and procurement conditions can also apply. Obtain the actual service decision. **Yellow**, blanket free “poaching,” fixed renewal periods, automatic government-tender bans and universal WPS-to-band downgrades from the old draft are not confirmed current entitlements or penalties. Keep their operational topics in the escalation checklist rather than presenting them as law.

### 6. Apply occupational localization independently

A compliant Nitaqat band does not excuse a separate occupation quota. For **accounting**, HRSD decision **103108, 26 January 2025**, as described in the March 2026 procedural guide, applies at entity level to the specified accounting occupations. Entities with **five or more accountants** move from **40% on 27 October 2025** to **50% on 27 October 2026**, then published future stages of 60% on 27 October 2027 and 70% on 27 October 2028. The fifth stage adds entities with **three or four accountants at 30% from 27 October 2029**, while continuing the five-plus stage. Licensed accounting offices use the separate professional-regulation route stated in §3.2. [HRSD accounting guide §§3.1-3.7, 6](https://www.hrsd.gov.sa/sites/default/files/2026-03/aldlyl-alajry-y-lqrar-twtyn-mhn-almhasbyt_-almwjwd-balmwq-.pdf).

For this occupational calculation, the guide requires SOCPA professional accreditation and a registered contributory monthly wage of at least **SAR 6,000 for bachelor's/equivalent** or **SAR 4,500 for diploma/equivalent**. An unaccredited accountant or a wage below the applicable threshold is not counted. These figures are **occupation-specific**, not a Saudi-wide minimum wage or a generic Nitaqat wage threshold. Use the guide's complete job-code list and actual duties, not titles selected to avoid the quota. Its example rounds required headcount to the nearest whole number: **23 × 40% = 9.2 → 9**, and **23 × 50% = 11.5 → 12**. [§§3.3-3.6, FAQs](https://www.hrsd.gov.sa/sites/default/files/2026-03/aldlyl-alajry-y-lqrar-twtyn-mhn-almhasbyt_-almwjwd-balmwq-.pdf).

Preserve the other original sector topics as separate decision lookups: **engineering; dentistry; pharmacy/pharmacy assistants; malls and specified retail; telecom/device retail and communications; real-estate brokerage; project management; customer-service/call centres; driving schools; gold/jewellery; optical; watches; car rental; and electrical-appliance retail**. Their current percentage, worker-count trigger, phase date, wage/accreditation, geography and duties have **not been confirmed** in this workpaper. Do not quote one accounting percentage for them, recycle 2024/2025 figures or ask the client to research the law. The preparer must retrieve the relevant latest official decision and resolve it before a hiring/localization sign-off.

### 7. Pay wages and upload the WPS file through Mudad

Use the contractual wage due date. The Ministry's WPS program follows actual wage payment, amount and time; local bank accounts or payroll cards are part of its published process. The old “every worker must have an IBAN” wording was too narrow because the official program also describes payroll cards. Do not treat cash, a promise, an unexecuted batch or a bounced transfer as a successful bank payroll record. [HRSD WPS program, requirements and file specification](https://www.hrsd.gov.sa/knowledge-centre/initiatives/national-transformation-initiatives-bank/108808).

Prepare the payroll gross-to-net reconciliation, make and verify the wage transfers, obtain the **original electronically sealed bank wage file**, then upload it for the correct entity, wage month and type through Mudad. Do not edit a bank-sealed file to improve its apparent compliance. The Ministry says opening/altering the supplied file, mismatched/missing establishment identifiers or non-SAR payment can cause rejection. Fields include basic, housing, other allowances, deductions, **net transferred amount**, employee/account identifiers and transfer status/date. [WPS program](https://www.hrsd.gov.sa/knowledge-centre/initiatives/national-transformation-initiatives-bank/108808); [current upload service, steps/requirements](https://www.hrsd.gov.sa/ministry-services/services/رفع-ملف-حماية-الأجور).

From **1 March 2025**, the permitted WPS upload period is **30 days instead of 60 days**. This is an upload limit, **not a 30-day permission to pay wages late**. The old instruction to upload proof before salary disbursement reverses the bank-file evidence sequence. Mudad processes the file, matches GOSI data, shows compliance and permits explanations sent to the worker for acceptance/rejection. Archive the original file, bank execution evidence, submission acknowledgement, exceptions and worker responses. An uploaded explanation alone does not prove the wage was timely paid or the worker accepted it. [HRSD announcement, 3 February 2025](https://www.hrsd.gov.sa/media-center/news/وزارة-الموارد-البشرية-والتنمية-الاجتماعية-تعلن-عن-تعديل-المدة-المسموحة-لرفع-ملفات-حماية-الأجور-في); [upload service](https://www.hrsd.gov.sa/ministry-services/services/رفع-ملف-حماية-الأجور).

## Worked cases

### A. Original IT-consultancy LLC: 10 Saudi and 5 expatriate staff

Preserve the original Saudi LLC, IT-consultancy registration, **10 Saudi nationals and five expatriates**, Saudi basic **SAR 8,000 + SAR 2,000 cash housing**, expatriate basic **SAR 12,000 + SAR 3,000 cash housing**. None exceeds the cap. The original example omitted month and contribution histories, so it cannot prove one unconditional total. Assume a full month, all Saudis eligible for all three branches, all five expatriates outside GCC extension and covered only for hazards, no other employers, no other earnings/deductions and no special hazard increase.

Saudi total contributory wages are **SAR 100,000**; expatriate wages **SAR 75,000**; gross wages **SAR 175,000**. These facts produce three different lawful cohort/date scenarios:

| Scenario | Saudi employer | Expatriate employer | Total employer | Employee deductions | GOSI remittance | Net wages | Gross plus employer contributions |
|---|---:|---:|---:|---:|---:|---:|---:|
| All Saudi staff existing-law, 2026 | 11,750 | 1,500 | **13,250** | **9,750** | **23,000** | **165,250** | **188,250** |
| All Saudi staff new-law, Jan–Jun 2026 | 12,250 | 1,500 | **13,750** | **10,250** | **24,000** | **164,750** | **188,750** |
| All Saudi staff new-law, Jul–Dec 2026 | 12,750 | 1,500 | **14,250** | **10,750** | **25,000** | **164,250** | **189,250** |

Amounts are SAR. A mixed-cohort employer must calculate each person instead of selecting a whole-table row. The old **SAR 14,000 employer / SAR 10,500 employee / SAR 24,500 remittance / SAR 189,000 cost** came from 1.5% SANED each and are not the ordinary existing-law result. The bank net is not the SAR 175,000 contractual gross. Report all wage/deduction fields truthfully and reconcile them to the transfer.

```oa-check
name: Original IT consultancy payroll across the two 2026 new-cohort periods and existing cohort
inputs:
  saudi_count: 10
  saudi_basic: 8000
  saudi_housing: 2000
  expat_count: 5
  expat_basic: 12000
  expat_housing: 3000
steps:
  - saudi_base: saudi_count * (saudi_basic + saudi_housing)
  - expat_base: expat_count * (expat_basic + expat_housing)
  - gross: saudi_base + expat_base
  - existing_employer: saudi_base * 0.1175 + expat_base * 0.02
  - existing_employee: saudi_base * 0.0975
  - existing_remittance: existing_employer + existing_employee
  - existing_net: gross - existing_employee
  - existing_cost: gross + existing_employer
  - new_first_half_employer: saudi_base * 0.1225 + expat_base * 0.02
  - new_first_half_employee: saudi_base * 0.1025
  - new_second_half_employer: saudi_base * 0.1275 + expat_base * 0.02
  - new_second_half_employee: saudi_base * 0.1075
  - new_second_half_remittance: new_second_half_employer + new_second_half_employee
  - new_second_half_net: gross - new_second_half_employee
  - new_second_half_cost: gross + new_second_half_employer
expected:
  gross: 175000
  existing_employer: 13250
  existing_employee: 9750
  existing_remittance: 23000
  existing_net: 165250
  existing_cost: 188250
  new_first_half_employer: 13750
  new_first_half_employee: 10250
  new_second_half_employer: 14250
  new_second_half_employee: 10750
  new_second_half_remittance: 25000
  new_second_half_net: 164250
  new_second_half_cost: 189250
```

The raw headcount fraction is **10 ÷ 15 = 66.67%**. It does **not** prove Platinum: current entity/activity, workforce averages, recognized weights, applicable coefficients and independent occupation tests are missing. The old “small size band, IT target typically 30–40%, therefore likely Platinum/tender priority” was unsupported. Obtain the actual Qiwa assessment; preserve 15 correct wage lines and the cohort-dependent gross-to-net bank reconciliation.

### B. Original senior manager above the contribution cap

Preserve basic **SAR 50,000 + cash housing SAR 12,000 = SAR 62,000 monthly gross**. Assume one employer, a full month, all three Saudi branches applicable and no other deductions. Contribution base is **SAR 45,000**, with **SAR 17,000 above the cap**. Under existing-law rates, employer contributions are **SAR 5,287.50**, employee deductions **SAR 4,387.50**, remittance **SAR 9,675**, net wages **SAR 57,612.50** and employer cost **SAR 67,287.50**. Under new-law July–December 2026 rates, these are **SAR 5,737.50 / SAR 4,837.50 / SAR 10,575 / SAR 57,162.50 / SAR 67,737.50**. The old SAR 5,625/SAR 4,725 rates are not the corrected existing-law result.

```oa-check
name: Original capped Saudi manager distinguishes gross wage from GOSI base and net transfer
inputs:
  basic: 50000
  cash_housing: 12000
  monthly_cap: 45000
steps:
  - gross: basic + cash_housing
  - contributory_base: min(gross, monthly_cap)
  - above_cap: gross - contributory_base
  - existing_employer: contributory_base * 0.1175
  - existing_employee: contributory_base * 0.0975
  - existing_net: gross - existing_employee
  - new_july_employer: contributory_base * 0.1275
  - new_july_employee: contributory_base * 0.1075
  - new_july_remittance: new_july_employer + new_july_employee
  - new_july_net: gross - new_july_employee
  - new_july_cost: gross + new_july_employer
expected:
  gross: 62000
  contributory_base: 45000
  above_cap: 17000
  existing_employer: 5287.50
  existing_employee: 4387.50
  existing_net: 57612.50
  new_july_employer: 5737.50
  new_july_employee: 4837.50
  new_july_remittance: 10575
  new_july_net: 57162.50
  new_july_cost: 67737.50
```

WPS carries basic/housing/gross and deductions accurately, with the **net actually transferred**. It must not instruct the bank to transfer SAR 62,000 while also treating GOSI deductions as already withheld. A second employer changes the cap-allocation workpaper.

## When to refuse or refer

| Original scenario retained | Handoff and minimum evidence before proceeding |
|---|---|
| Domestic workers/Musaned | Separate domestic-worker and social-insurance coverage decisions; do not apply this ordinary payroll calculation by analogy |
| Public-sector/PPA and military/security | Separate civil/military workpaper. PPA-only/private-GOSI-only shorthand is superseded by the new civilian entrant scheme |
| End-of-service award, Labour Law arts. 84–88 | Separate termination/service/contract calculation, counsel for contested or senior cases; contribution payment does not settle gratuity |
| Home-country/shadow payroll | Determine real employer, local wage/benefits, immigration and insured coverage; foreign payroll alone is no exemption. Cross-border charging goes to CIT/WHT/TP workpapers |
| Options, RSUs and long-term incentives | Obtain plan, vesting/settlement and wage regulation; do not declare universally included, exempt or legally unsettled without examining the actual instrument |
| GCC extension/treaty or social-security coordination | Obtain home-state coverage certificate, applicable extension rules, bases/rates and employer payment instructions; do not use Saudi national totals by default |
| NEOM, SILZ or another special/free-zone employer | Obtain actual enacted zone/employer coverage exception; a zone name is not evidence that ordinary labour/social-insurance rules are displaced |
| Mixed old/new-law Saudi workforce | Calculate each worker with history and effective month; mixed status is supported, not a reason to abandon all ordinary calculations |
| Small/family businesses, fewer than five staff, claimed occupation exemption | Retrieve the specific current decision; no universal exemption from GOSI, WPS, Nitaqat or occupation localization follows from small size |
| Missing cohort/branch, cap allocation, in-kind valuation, retroactive wages or actual bill | Obtain operative regulation/account evidence; conditional estimates only until resolved |
| Actual wage dispute, sham employment or unexplained bank/GOSI/WPS mismatch | Stop submission and escalate with documents; do not falsify records or treat an unaccepted explanation as settlement |

## Filing calendar, penalties and workpaper sign-off

| Event | Calendar/control |
|---|---|
| Joining/leaving or worker-data change | Immediately, no later than relevant month end under new IR art. 6; preserve actual event and account evidence |
| Old-law monthly contribution/wage schedule | First **15 days of following month**, art. 19; check applicable holiday extension/account notice rather than inventing an end-of-month deadline |
| New-law monthly contribution | First **15 days of following month**, new IR art. 24; reconcile actual bill and settlement |
| Wages | Contractual/legal pay date, with executed transfer evidence |
| WPS upload | Monthly wage file through Mudad, within the current **30-day** upload window; does not extend the wage due date |
| Nitaqat and occupational quota | Review actual Qiwa assessment before recruitment/renewal/transfer and after relevant workforce changes; accounting stage rises on **27 October 2026** |
| Iqama/work permit | Each actual expiry and service's conditions; no universal annual/biennial term assumed |
| Year end/separation | Reconcile wage and contribution control accounts; assess separate gratuity obligations and actual notices |

Old-law art. 19(5) and new-law art. 9(3) impose **2% of unpaid contributions per month or part** after the applicable payment grace period, with regulatory exemption/limit conditions. This is not an instruction to add a flat 2% to every correction irrespective of dates or an approved relief decision. New-law art. 59 provides ordinary violations up to **SAR 50,000**, repeat rules within **three years**, multiple-worker consequences and a separate sham-registration limb. Inspect the relevant limb and actual notice before computing a fine. The base contribution and employee rights remain separate from fines. [Old law](https://beta.gosi.gov.sa/social-insurance); [new law arts. 9, 59](https://beta.gosi.gov.sa/new-system).

GOSI's current new-law awareness also describes suspension when unpaid contribution periods reach **six months**, and insolvency/closure-type events, with statutory/reactivation conditions. Do not infer that paying the latest month alone clears all suspended periods. [Current employer awareness, suspension section](https://awareness.gosi.gov.sa/businessJourney.html).

Wage underpayment, late payment, altered bank files, localization non-compliance and sham employment can produce separate enforcement. **Current quantified WPS/localization fines and automatic visa/iqama/tender outcomes have not been confirmed** from an operative current penalty schedule in this workpaper. Do not quote the old blanket Article 90 fine, old Yellow consequences, automatic band downgrade or automatic cash-equals-legal-nonpayment rule as a measured current penalty. Obtain the applicable violation decision, facts, worker count and notice. A lawful cash settlement question and WPS recognition question must both be resolved; do not manufacture bank payment evidence.

Final workpaper: identify month and law/cohort for every worker; show uncapped and capped wages, branch rates, employer/employee amounts, rounding and bill differences; reconcile gross to deductions and executed net transfers; attach Mudad acknowledgements and exceptions; record the actual Qiwa entity/band and each occupational decision; list deadlines, receipts and unresolved items. Until the listed missing evidence is resolved, label the output **conditional**, not ready to file.

## Not confirmed

Old-law in-kind/irregular remuneration valuations not evidenced by the applicable regulation; client-specific branch coverage/age and multiple-employer allocation; actual Qiwa coefficients, averages, weighting and service entitlements; non-accounting sector decisions listed above; special-zone/GCC/domestic/public-sector exceptions; exact current WPS/localization penalty amounts; universal annual GOSI return and a prescribed retention period. These are work-stopping only for the affected decision: do not replace missing law with a larger charge, an invented exemption or an unverified historical table.

## Sources

Read date: **16 November 2026**. Official Arabic legislation controls; the current awareness material supplies implemented rates where enabling legislation prints a variable headline. A working URL is not accountant verification.

| Source | What was read and used |
|---|---|
| [M/273 new Social Insurance Law and decree](https://beta.gosi.gov.sa/new-system) | Read on 2026-11-16. Read for transition/cohort clauses; arts. 5–9, 14–15, 28–29, 43–44 and 59 coverage, cap, payment/penalty framework. The implementing regulation was read separately from the official gazette below |
| [New-law implementing regulation, official gazette](https://www.uqn.gov.sa/details?p=25240) | Read on 2026-11-16. Read for arts. 6, 17–26: establishment/worker registration, wage elements, multiple employers, partial periods, corrections, payment and relief procedure |
| [Existing Social Insurance Law](https://beta.gosi.gov.sa/social-insurance) | Read on 2026-11-16. Read for arts. 4–5, 18–20 coverage, ordinary rates, ceiling, payer duty and first-15-days payment rule |
| [GOSI new-law employer awareness](https://awareness.gosi.gov.sa/businessJourney.html) | Read on 2026-11-16. Read for cohort, wage elements, cash/in-kind housing, current SANED/hazard rates, phased pension and suspension paragraphs |
| [GOSI existing-law awareness](https://awareness.gosi.gov.sa/journey1.html) | Read on 2026-11-16. Read for existing-law contribution-rate paragraph; retirement coverage is not mistaken for a contribution-rate change |
| [GOSI contribution-increase bulletin](https://awareness.gosi.gov.sa/pdf/Contributions.pdf) | Read on 2026-11-16. Read for cohort explanation and PDF p. 4 table; visually inspected dates/rates, including 1 July 2026 and future stages |
| [GOSI contributor FAQ](https://www.gosi.gov.sa/GOSIOnline/FAQ_Contributor?locale=ar_SA) | Read on 2026-11-16. Read for aggregate multiple-employer ceiling and joiner/leaver registration paragraphs; conflicting/stale answers are not silently treated as current rate authority |
| [GOSI employer FAQ](https://www.gosi.gov.sa/GOSIOnline/FAQ_Employer) | Read on 2026-11-16. Read for SADAD/bank payment and first-15-days period; not a substitute for missing new-law regulation |
| [HRSD developed Nitaqat decision/manual](https://www.hrsd.gov.sa/sites/default/files/2023-02/E182495.pdf) | Read on 2026-11-16. Read for entity/averages definitions, five bands, size-category replacement, logarithmic threshold method and service-table boundary |
| [Preceding HRSD wage-count decision](https://www.hrsd.gov.sa/sites/default/files/2020-11/61706.pdf) | Read on 2026-11-16. Read for preceding wage-count categories; no claim that all historical category rules have been revalidated for a particular 2026 account |
| [HRSD decision dated 25 October 2026](https://www.hrsd.gov.sa/sites/default/files/2026-11/qrar-wzary-a-tmad-tnzym-ahtsab-alajwr-fy-brnamj-thfyz-almnshat--ly-altwtyn-ntaqat.pdf) | Read on 2026-11-16. Read and visually inspected first page for prospective April 2027/April 2028 stages; no premature use of future wage columns |
| [HRSD accounting-localization procedural guide, March 2026](https://www.hrsd.gov.sa/sites/default/files/2026-03/aldlyl-alajry-y-lqrar-twtyn-mhn-almhasbyt_-almwjwd-balmwq-.pdf) | Read on 2026-11-16. Read for §§3.1–3.7 and FAQs: occupational scope, thresholds, accreditation, rounded examples, phase dates and independent operation alongside Nitaqat |
| [HRSD WPS program](https://www.hrsd.gov.sa/knowledge-centre/initiatives/national-transformation-initiatives-bank/108808) | Read on 2026-11-16. Read for bank/payroll-card process, file integrity, payroll fields and wage timing. Historical rollout/sanction paragraphs are not promoted to an unverified current fine schedule |
| [HRSD Mudad upload service](https://www.hrsd.gov.sa/ministry-services/services/رفع-ملف-حماية-الأجور) | Read on 2026-11-16. Read for entity/month/type/upload steps, GOSI matching, explanations/worker response and registration/bank prerequisites |
| [HRSD 30-day upload announcement](https://www.hrsd.gov.sa/media-center/news/وزارة-الموارد-البشرية-والتنمية-الاجتماعية-تعلن-عن-تعديل-المدة-المسموحة-لرفع-ملفات-حماية-الأجور-في) | Read on 2026-11-16. Read for the 1 March 2025 change from 60 to 30 days; this is not a wage-payment extension |
| [Income Tax Law](https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/%D9%86%D8%B8%D8%A7%D9%85%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf) and [ZATCA WHT guide](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) | Read on 2026-11-16. Read for taxpayer/business and employment-versus-independent-service boundary; separate tax computations stay in their owning skills |

**Not yet confirmed:** the items listed under Not confirmed, including actual account/worker evidence, older-law valuations, current Qiwa coefficients/weights and non-accounting occupation decisions. These are excluded from unconditional filing guidance.
