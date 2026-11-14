---
name: japan-payroll
description: Use this skill whenever asked about Japanese payroll, income tax withholding (源泉徴収 gensen chōshū), social insurance (社会保険 shakai hoken), labour insurance (労働保険 rōdō hoken), or employer obligations in Japan. Trigger on phrases like "gensen choshu", "源泉徴収", "shakai hoken", "社会保険", "厚生年金", "kosei nenkin", "kenko hoken", "健康保険", "雇用保険", "koyou hoken", "労災保険", "rosai hoken", "年末調整", "nenmatsu chousei", "year-end adjustment", "standard monthly remuneration", "hyōjun hōshū getsugaku", "payslip Japan", "給与明細", "kyūyo meisai", "minimum wage Japan", "overtime Japan", "36 agreement", "子ども・子育て支援金", or any question about running payroll in Japan. ALWAYS read this skill before processing any Japanese payroll work.
version: 2.0
jurisdiction: JP
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
status: needs_sources
domain: payroll
type: computation
---

# Japan payroll v2.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Run a Japanese resident employee's payroll: classify pay, establish withholding and insurance status, use the correct remuneration grades, reconcile gross to net, remit and report. Currency is JPY. Income tax uses the calendar year; FY2026 labour-insurance rates cover April 2026-March 2027. Health premium changes and the new child-support charge have their own effective months. NTA handles withholding, Japan Pension Service (JPS)/the insurer handles employee health and pension, and Hello Work/Labour Bureau handles labour insurance. Self-employed municipal NHI/National Pension belongs in `jp-social-insurance`.

| Quick reference | Current rule | Official source |
| --- | --- | --- |
| Withholding | Use the actual 2026 monthly/daily or bonus table, after deductible employee social insurance; tables already include reconstruction tax | Income Tax Act arts. 183/185/186; NTA 2026 tables, cover and pp. 19-22: https://www.nta.go.jp/publication/pamph/gensen/zeigakuhyo2026/data/all.pdf |
| Ordinary national withholding remittance | By the 10th of the following month; next business day if a stated holiday/weekend | Income Tax Act art. 183; NTA: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2502.htm |
| Approved small-payroll exception | Regularly fewer than 10 payees, approval required: January-June withheld tax due July 10; July-December due following January 20 | Income Tax Act arts. 216/217; NTA: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2505.htm |
| Tokyo employee insurance | Separate health/pension remuneration grades, wages and bonus caps; never a single percentage of gross pay | Official FY2026 Tokyo schedule: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf |

## Ask the client first

Obtain the pay date and wage period, employer establishment/industry and insurer/prefecture, actual enrolment and coverage dates, age and care-insurance status, residence/treaty position, employment contract/work rules, attendance/overtime, base and each allowance, commuting route and evidence, current health and pension SMR notices, prior remuneration changes, bonus history by month/fiscal year/insurer, approved leave/exemption notices, primary-employer declaration and table-dependent count, previous-month post-insurance pay for bonuses, current municipality special-collection notice, and year-end declarations/prior-employer slips.

Ask whether the employer has the national withholding payment exception; it is not automatic for a small business. Register the payroll office with the tax office, and establish the separate JPS/insurer and labour-insurance registrations. NTA 2502 gives a payroll-office opening notification within 1 month, subject to the actual applicable filing route. Do not assume that a tax registration also enrolls staff in insurance.

## The method, step by step

### Classify gross pay and establish coverage

Pay ordinary wages at least monthly on a fixed date, directly and in full, subject to lawful deductions or the necessary labour-management agreement (Labour Standards Act art. 24). The old examples of paying on the 25th or month-end are possible contractual dates, not nationwide mandatory paydays.

Keep three bases separate: taxable salary, social-insurance remuneration grades, and labour-insurance wages. A qualifying economical/reasonable rail/bus commuting allowance can be income-tax exempt up to JPY 150,000 per month; an excess is taxable. Car/bicycle and mixed travel require their own limits and evidence, not a blanket exemption. Non-taxable commuting is nevertheless included in SMR remuneration and labour-insurance wages. See NTA 2582, JPS commuting FAQ and Labour Bureau wage guidance in Sources.

Confirm employee coverage rather than substituting freelancer NHI. From **October 1, 2026**, the JPY 88,000 monthly scheduled-wage test for short-time employee health/pension coverage was abolished. The JPS notice retains the 20-hour weekly, employer-size 51+ and non-student conditions; establish the complete coverage record and duration requirements before enrolment. A worker under the special minimum-wage reduction permission with pay below JPY 88,000 is generally excluded but may request inclusion. Do not back-apply the October change to earlier payroll months.

### Calculate employee and employer insurance separately

The table is **Kyokai Kenpo Tokyo**, not every insurer. Health and care rates apply from March 2026 premium month (April remittance); new child-support premiums start April 2026 premium month (May remittance). General employment-insurance rates below apply April 2026-March 2027. Earlier payroll needs its own dated schedule.

| Component | Employee | Employer | Basis and condition | Official source |
| --- | --- | --- | --- | --- |
| Tokyo health | 4.925% | 4.925% | Derived halves of 9.85%; health SMR ceiling JPY 1,390,000/month | Tokyo official schedule: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf |
| Care | 0.810% | 0.810% | Derived halves of 1.62%; ages 40-64, health SMR basis | Same: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf |
| Employees' pension | 9.150% | 9.150% | Derived halves of 18.300%; pension SMR ceiling JPY 650,000/month; pension-fund arrangements require their own schedule | Same: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf |
| New child-rearing support, 子ども・子育て支援金 | 0.115% | 0.115% | Derived halves of 0.23%; health SMR/bonus basis; April premium month onward | Same: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf |
| Existing child allowance contribution, 子ども・子育て拠出金 | 0% | 0.360% | Employer only, **pension** SMR/standard bonus basis; this did not become an employee charge | Same, footer: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf |
| General-business employment insurance | 0.50% | 0.85% | Actual labour-insurance wages, not SMR; source prints 5/1,000 and 8.5/1,000 | Employment Insurance Act/contribution schedule: https://www.mhlw.go.jp/content/001692566.pdf |
| Agriculture/forestry/fishery and sake employment insurance | 0.60% | 0.95% | Actual covered wages; specified horticulture, livestock, inland fishery and seafarer operations instead use general-business rates | Same: https://www.mhlw.go.jp/content/001692566.pdf |
| Construction employment insurance | 0.60% | 1.05% | Actual covered wages; source prints 6/1,000 and 10.5/1,000 | Same: https://www.mhlw.go.jp/content/001692566.pdf |
| Workers' compensation | 0% | Industry-specific; 0.30% for category 94 other businesses | Entirely employer-funded. Do not assign an office rate without industry classification; FY2026 schedule spans 0.25%-8.8%, derived from 2.5/1,000-88/1,000 | MHLW FY2026 rate table: https://www.mhlw.go.jp/content/roumuhiritu_r05.pdf |

For illustration only, if all bases happen to be identical and uncapped, the Tokyo category-94/general-business employer rates sum to **15.70%** without care or **16.51%** with care (derived from the linked schedules). These are not usable flat payroll deductions or universal employer-cost percentages. Actual SMR grades, different ceilings and rounding change the cost.

**SMR:** annual determination uses April-June qualifying remuneration for July 1 insured employees, normally effective September-August. Read the JPS exclusions and qualifying days: normally 17 days in a month, 11 for the specified short-time group; ordinary part-time exceptions differ. Current notices control; do not re-grade every monthly wage fluctuation.

A mid-year revision normally requires a fixed-pay change, a qualifying average of the following 3 months and a change of at least 2 grades in the same direction; all 3 months must meet the 17-day/short-time 11-day test. Revision starts in the 4th month counted from the first changed payment. Upper/lower-bound cases can qualify with 1 grade. A fixed-pay rise with an overall average falling, or the reverse, does not qualify under the ordinary rule. JPS annual and mid-year pages give the detailed exceptions.

**Bonuses:** round the gross bonus down to JPY 1,000 to obtain the standard bonus. Health, care and new child-support use the **JPY 5,730,000 fiscal-year cumulative** cap, by insurer; pension and the existing employer contribution use **JPY 1,500,000 per month**, aggregating multiple payments in that month, not per payment. Bonuses paid 4+ times a year can instead be remuneration. Enrolment/loss months, exempt leave months and movement between insurers need the JPS bonus rules, including amounts counted toward the health cumulative limit even when no premium is charged. Submit the bonus notification within 5 days, with same-month payments reconciled as directed by JPS.

For employee premiums deducted through payroll, the Tokyo schedule rounds fractions of JPY 0.50 or less down and fractions above JPY 0.50 up, unless an agreed rule applies. Cash payment by the employee has a different half-yen rule. Reconcile the employer's total bill independently; multiplying one rounded employee deduction by 2 is not a universal reconciliation.

### Withhold national and local tax

Use the 2026 table for the actual payment. **甲 (Ko)** requires the primary-employer dependency declaration; **乙 (Otsu)** is the other column. The old phrase “3.063% minimum” is misleading: in the monthly table that percentage is the Otsu rule below JPY 105,000 after social insurance; higher pay uses its proper row. Daily payments/day labour have separate tables. Count the statutory table dependants, including applicable status additions, not every person in a household. A qualifying secondary-employer declaration can reduce Otsu withholding under NTA 2520; it does not turn the pay into primary-employer Ko pay.

Deduct eligible employee social-insurance amounts from taxable pay and use the actual table row. The reconstruction tax is already in the table: do not multiply the table answer again by 1.021. For an ordinary bonus, use previous-month post-insurance ordinary salary and the table-dependent count to choose the rate, then apply it to the bonus after employee social insurance. If there was no previous-month ordinary salary or the bonus exceeds 10 times the relevant salary, use the table's special monthly-table method; do not invent a bonus rate.

Annual national tax reference, for the correctly rounded taxable base, is retained below. These rates do not replace monthly withholding tables. JPY 0 taxable income produces no tax.

| Annual taxable income JPY | Rate | Quick deduction JPY | Official source |
| --- | --- | --- | --- |
| 1,000-1,949,000 | 5% | 0 | Income Tax Act art. 89; NTA 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 1,950,000-3,299,000 | 10% | 97,500 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 3,300,000-6,949,000 | 20% | 427,500 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 6,950,000-8,999,000 | 23% | 636,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 9,000,000-17,999,000 | 33% | 1,536,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 18,000,000-39,999,000 | 40% | 2,796,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| 40,000,000+ | 45% | 4,796,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Reconstruction supplement | 2.1% of national base tax, through 2037 under the 2026 regime | Separate from local tax; annual computation/rounding required | NTA 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |

For **2026 annual year-end adjustment**, NTA 1410 now gives the following deduction, effective December 1, 2026 and applying to 2026/2027 income. It does not retrospectively replace the published 2026 monthly table. Salary below JPY 6,600,000 must use the statutory employment-income table, including NTA's low-income adjustment notes, rather than this overview alone. Aggregate multiple employment slips.

| Annual gross employment income JPY | Annual deduction overview | Official source |
| --- | --- | --- |
| Up to 2,200,000 | 740,000, subject to no negative employment income and NTA special low-income/table notes | Income Tax Act art. 28/Appendix 5, NTA: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| 2,200,001-3,600,000 | Gross × 30% + 80,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| 3,600,001-6,600,000 | Gross × 20% + 440,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| 6,600,001-8,500,000 | Gross × 10% + 1,100,000 | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| 8,500,001+ | 1,950,000 cap | Same: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |

Year-end adjustment is not for every Ko employee. NTA 2665 covers continuing/year-end employees with the declaration, excluding annual pay over JPY 20,000,000 and specified disaster-relief cases. Mid-year departures qualify only in specified cases such as becoming non-resident, death, serious disability without expected further employment, or retirement after the final December pay; the NTA's low-pay part-time departure case has its own current conditions. Secondary-employer salary normally needs the individual's final return. Collect dependency, spouse, insurance and housing-credit evidence before reconciling annual tax against withholding; housing relief and deductions require actual eligibility. Do not assume all credits can first be granted through payroll. Route unresolved annual computation to `jp-income-tax` and the current NTA year-end instructions.

For **resident tax**, deduct the municipality's notified monthly special-collection amount for June-May, based on the prior year's assessed position. It is not a current-pay percentage, and no new resident-tax percentage is charged on each bonus. The old approximate 10% explanation is not a complete local liability calculation: equal levies, forest-environment tax, exemptions and local variations need the actual municipality. NTA withholding and municipal resident-tax deadlines are different obligations.

### Check minimum wages, hours and leave

Check both the applicable prefectural and specified-industry minimum; the higher applicable minimum controls. Compare the legally includible hourly wage, not gross pay divided blindly by hours. Revisions do not all start in October.

| Prefecture | Hourly minimum JPY, as of November 14, 2026 | Effective date/condition | Official source |
| --- | --- | --- | --- |
| Tokyo | 1,280 | October 1, 2026 | Minimum Wage Act; MHLW current list: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html |
| Kanagawa | 1,279 | October 1, 2026 | Same: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html |
| Osaka | 1,231 | October 1, 2026 | Same: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html |
| Aichi | 1,195 | October 1, 2026 | Same: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html |
| Fukuoka | 1,114 | October 4, 2026 | Same: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html |
| Okinawa | 1,023 currently; 1,086 only from December 2, 2026 | Current rate since December 1, 2025; keep the future rate separate | Same: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html |

Ordinary statutory hours are 8 per day and 40 per week; special working-time systems/industries need their own rule. An art. 36 agreement must be concluded and filed before ordinary overtime/holiday work. Standard overtime limits are 45 hours/month and 360/year. An exceptional special clause is not a routine permission: annual overtime must not exceed 720 hours, overtime plus statutory holiday work must be **below 100 hours** in a month and at most 80/month on every 2-6-month average, and exceeding 45 hours is limited to 6 months/year. Different limits/exceptions, including certain variable-hour arrangements, research/development and special occupations, need specific review. Source: Labour Standards Act arts. 32/36; MHLW overtime page in Sources.

| Work | Minimum premium above ordinary pay | Condition/source |
| --- | --- | --- |
| Ordinary statutory overtime | 25% (125% total, derived) | Art. 37; MHLW: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| Monthly overtime beyond 60 hours | 50% (150% total, derived) | Same; applies to SMEs too: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| Night 22:00-05:00 | Additional 25% | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| Ordinary overtime plus night | 50% (150% total), derived | Sum applicable premiums; overtime beyond 60 hours plus night is 75% (175% total), derived: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| Statutory holiday | 35% (135% total) | Not every contractual day off is a statutory holiday: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| Statutory holiday plus night | 60% (160% total), derived | Holiday 35% + night 25%: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |

Annual paid leave needs 80% attendance in the relevant preceding period. The ordinary grant schedule is preserved below; lower-hours/days part-time staff have proportionate grants, not automatically this table. For employees granted at least 10 days, ensure 5 days are taken within the grant year, counting qualifying employee-selected/planned days toward that duty. Unused entitlement generally expires after 2 years (art. 115). Source: Labour Standards Act art. 39 and MHLW working-rules explanation.

| Service years | Ordinary grant days | Official source |
| --- | --- | --- |
| 0.5 | 10 | Labour Standards Act art. 39; MHLW: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| 1.5 | 11 | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| 2.5 | 12 | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| 3.5 | 14 | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| 4.5 | 16 | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| 5.5 | 18 | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |
| 6.5+ | 20 | Same: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html |

**Maternity:** requested prenatal leave is 6 weeks, or 14 for multiple pregnancy; postnatal leave is 8 weeks, except return after 6 weeks on request and medical clearance for the work (art. 65). Health-insurance maternity allowance is based on average covered SMR over the preceding 12 months ÷ 30 × 2/3, not 67% of actual wage. It generally covers unpaid eligible days from 42 days before birth (98 multiple) through 56 after; late birth adds the qualifying overdue days. Paid salary reduces/eliminates benefit; shorter insurance histories use the insurer's special lower-base test. Qualifying childbirth at a compensation-scheme institution at 22+ gestational weeks receives JPY 500,000 per child; otherwise the stated category is JPY 488,000. The underlying childbirth definition includes pregnancy from 85 days; verify the actual category and claim. These are insurance benefits, not employer salary. Sources: Kyokai maternity/birth pages.

**Childcare:** qualifying employees can generally take leave for a child under 1, extending through the statutory stages up to age 2 for conditions such as inability to obtain childcare. Fixed-term contracts and labour-agreement exclusions need eligibility review. Benefit eligibility is separate from leave entitlement: normally 12 qualifying insured months in the preceding 2 years, with 11 wage-base days or the applicable 80-hour alternative, plus the benefit-period work limits. MHLW Q11-Q18 covers exceptions, extension evidence and the 2025-onward genuine return-to-work childcare application requirement. Ordinary benefit is 67% for the first 180 days, then 50%, subject to wage-payment reductions and caps. Use the official pre-leave wage base and Hello Work decision, not gross salary times a rate alone. A separate birth-support supplement can apply: refer to MHLW Q35-Q40 for the 13%/maximum 28-day calculation, required qualifying leave, spouse rule/exceptions and benefit caps; do not automatically add it for everyone.

Employer and employee health/pension premiums are exempt only for qualifying leave months after the employer's notification. The ordinary period runs from the starting month through the month before the month containing the day after leave ends; a same-month leave can qualify with 14+ days. Bonus exemption requires leave **longer than 1 continuous month including the bonus month's last day**. Do not exempt every bonus merely because some leave occurred. No employment-insurance wage premium arises on a zero-wage month. Paid wages and benefit caps still need review. Sources: JPS childcare exemption FAQ and MHLW benefit Q&A.

**Sickness:** there is no universal employer-paid sickness allowance in this computation; consult the actual contract/work rules for paid sick leave. Do not assume the old “typically 3-10 days” claim. For covered non-work/non-commuting illness/injury, health-insurance sickness allowance requires inability to work, 3 consecutive waiting days, payment from day 4 and no salary or only the benefit difference. It uses average covered SMR over the preceding 12 months ÷ 30 × 2/3, with the shorter-history test and insurer rounding, for an aggregate maximum of 18 months. Occupational injury and post-coverage claims require separate review. Source: Kyokai sickness page.

**Retirement:** a universal retirement allowance is not imposed merely by employing someone, but contractual/work-rule promises can create payment duties. Review lump sum, DB or DC arrangements separately; do not assume statutory rates or deductibility of a reserve. The former employer-prevalence percentages are held below. Source: Saitama government labour explanation.

### Reconcile, issue statements, remit and report

Give the employee a pay statement at payment (Income Tax Act art. 231). As a payroll control show identity, period/pay date, base, itemised allowances/overtime, gross, each employee insurance deduction, national withholding, notified resident tax and net; retain hours and the relevant tax/insurance notices. This list is a practical complete reconciliation, not a claim that every item is mandated by the same statutory payslip article. Separately retain required wage/attendance records.

Reconcile gross to bank transfer, employee deductions to liabilities, and employer contributions to their bills. Post salaries and employer contributions to the relevant expense accounts and net-pay/withholding/insurance payables to the balance sheet (`japan-bookkeeping`). Salary remuneration is outside consumption-tax consideration; commuting payment and its expense evidence need their own consumption-tax classification (`japan-consumption-tax`). No business-tax deduction for a retirement provision is assumed here; refer corporate tax accounting to the applicable sourced corporate rules.

| Obligation | Deadline/process | Official source |
| --- | --- | --- |
| National withholding | Ordinary next-month 10th; approved fewer-than-10 exception July 10/following January 20; holiday adjustment | NTA: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2505.htm |
| Year-end reconciliation | Final qualifying year-end salary, after obtaining required declarations; no blanket November-December statutory declaration deadline | NTA art. 190 scope: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2665.htm |
| Employee withholding slip | Following January 31; mid-year leaver within 1 month; recipient copy omits My Number | Income Tax Act art. 226; NTA: https://www.nta.go.jp/taxes/shiraberu/taxanswer/hotei/7411.htm |
| Salary payment report/statutory reporting | Following January 31 statutory date, with applicable holiday procedure. For submissions due January 1, 2027 onward, municipal salary reporting can constitute deemed submission to NTA under the new rule; do not blindly apply the older separate-report thresholds | NTA 7411: https://www.nta.go.jp/taxes/shiraberu/taxanswer/hotei/7411.htm |
| Annual SMR determination | File July 1-10, with holiday adjustment as directed; annual covered population/exclusions apply | JPS: https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20121017.html |
| Mid-year SMR | Promptly once qualifying change established; revised premium month and payroll collection month must be reconciled | JPS: https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20150515-02.html |
| Bonus notification | Within 5 days; same-month multiple bonuses reconciled under JPS directions | JPS: https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20141203.html |
| FY2026 labour-insurance annual update | June 1-July 10, 2026; reconcile prior-year final and current-year estimated premiums | MHLW annual-update notice: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/hoken/roudouhoken21/index.html |

National withholding can be paid through e-Tax or the approved financial-institution/tax-office route; keep the receipt and liability reconciliation. Municipal remittances and social/labour insurance are separate payees and procedures. The approved national small-payroll exception applies only to its specified payment categories and starts under the NTA approval rules; apply promptly for loss of status if the regular population reaches 10 or more.

**Penalties:** General Tax Act art. 67 sets ordinary nonpayment additional tax at 10%, reduced to 5% for qualifying voluntary payment before notice/investigation foreknowledge; justifiable-reason and qualifying timely-cure exceptions can eliminate it. Separate delinquency tax depends on the actual dates/rates (`jp-estimated-tax` explains the 2026 rate method; do not import a late-filing penalty indiscriminately). The employer remains responsible for proper withholding/remittance. Labour Standards Act art. 119 provides up to 6 months detention or JPY 300,000 for listed hours/premium/leave offences; art. 120 provides up to JPY 300,000 for the art. 39(7) annual 5-day leave duty. Classify the actual offence before quoting a sanction. The old generic social-insurance penalty is not certified as a universal failure-to-enrol consequence; see Not yet confirmed.

## Worked cases

### Pattern 1: standard monthly employee, Tokyo, age 35

Preserved salary JPY 350,000 plus qualifying rail commuting JPY 15,000. Assume confirmed current health/pension SMR **JPY 360,000**, consistent with remuneration JPY 365,000 in the table's JPY 350,000-369,999 grade; no care, general employment insurance, Ko with 0 table dependants, after April 2026 rates. Resident-tax notice supplies JPY 18,000 (example input). Health 17,730 + pension 32,940 + new child support 414 + employment 1,825 = employee insurance **52,909**, derived. Taxable pay after insurance is 297,091, so the 2026 monthly table's 296,000-298,999 row gives Ko/0 **7,820**. Net is **286,271**. This corrects the old non-existent JPY 350,000 SMR and approximate withholding/net.

Employer counterparts before bill-level fraction settlement are health 17,730, pension 32,940, new child support 414, existing employer contribution 1,296, employment insurance 3,102.50, category-94 workers' compensation 1,095: **56,577.50**, derived. The employment/compensation bases are 365,000; health/pension contribution bases are the confirmed 360,000 SMR. Source rates: Tokyo PDF, MHLW employment and compensation schedules; tax: 2026 NTA monthly table p. 2.

```oa-check
name: Tokyo age 35 monthly pay with distinct remuneration and wage bases
inputs:
  salary: 350000
  commuting: 15000
  smr: 360000
  resident_notice: 18000
  monthly_table_tax: 7820
steps:
  gross: salary + commuting
  health: smr * 0.04925
  pension: smr * 0.0915
  child_support: smr * 0.00115
  employment: gross * 0.005
  employee_insurance: health + pension + child_support + employment
  taxable_after_insurance: salary - employee_insurance
  net: gross - employee_insurance - monthly_table_tax - resident_notice
  employer_before_settlement: health + pension + child_support + smr * 0.0036 + gross * 0.0085 + gross * 0.003
expected:
  employee_insurance: 52909
  taxable_after_insurance: 297091
  net: 286271
  employer_before_settlement: 56577.50
```

### Pattern 2: JPY 700,000 bonus

Same age/coverage/rates, previous-month post-insurance ordinary salary 297,091, Ko/0 dependants, no other bonus that month and no health annual cap used. Standard bonus is 700,000. Employee health 34,475 + pension 64,050 + new child support 805 + employment 3,500 = **102,830**, derived. Previous-month salary falls in the 2026 bonus-table Ko/0 band 260,000 to below 309,000, rate **6.126%**. Bonus after insurance 597,170 × 6.126%, truncate below yen = **36,582** withholding; net **560,588**. No extra resident-tax percentage is imposed on this bonus; the current monthly notice still governs collection. Employer insurance before settlement totals **109,900**, derived including the existing employer-only contribution and category-94 compensation rate.

```oa-check
name: Tokyo bonus with child-support premium and previous-month withholding band
inputs:
  bonus: 700000
steps:
  standard_bonus: floor(bonus / 1000) * 1000
  health_base: min(standard_bonus, 5730000)
  pension_base: min(standard_bonus, 1500000)
  health: health_base * 0.04925
  pension: pension_base * 0.0915
  child_support: health_base * 0.00115
  employment: bonus * 0.005
  employee_insurance: health + pension + child_support + employment
  withholding: floor((bonus - employee_insurance) * 0.06126)
  net: bonus - employee_insurance - withholding
  employer: health + pension + child_support + pension_base * 0.0036 + bonus * 0.0085 + bonus * 0.003
expected:
  employee_insurance: 102830
  withholding: 36582
  net: 560588
  employer: 109900
```

**Pattern 3, mid-year change:** retain the original base-pay rise from 300,000 to 350,000 first paid in April. If April-June qualifying average and the existing SMR satisfy all mid-year tests, the new SMR applies to July premium month. This does not necessarily mean deduction in July's wage payment: reconcile the actual premium collection cycle. Include allowances in the average and use the actual grade, not base pay itself.

**Pattern 4, childcare leave:** for a qualifying full exempt month with zero wages and the employer's accepted notification, employee/employer health and pension premiums are exempt and employment-insurance wage premium is zero. Use the actual benefit award at 67%/50% and applicable caps; partial-month or bonus exemption must pass its separate test. Preserve the employee's resident-tax liability and arrange collection/payment rather than treating zero wages as zero local tax.

## When to refuse or refer

Stop an executable payroll result if insurer/rate period, enrolment, SMR, table declaration/dependants, taxable allowances or municipal notice is missing. Do not fabricate a tax-table result. Refer non-residents/treaty relief, expatriate shadow payroll, pension funds, high-age coverage, work-injury benefits, specialised hours systems, disputed leave or penalties, and corporate deduction/provision questions for case-specific professional review. The generic `payroll-workflow-base` supplies workflow controls, not Japan's rates.

## Sources

Every page below was opened and its stated operative material read on **2026-11-14**. The Tokyo PDF's full extracted table and footnotes were read; a text extraction is not claimed as a visual inspection. e-Gov's ordinary law API recovered the current main provisions when the interactive law page did not expose them.

| Official source | Read for | Read date |
| --- | --- | --- |
| NTA 2026 withholding tables: https://www.nta.go.jp/publication/pamph/gensen/zeigakuhyo2026/data/all.pdf | Read for cover/remittance, monthly row used in Pattern 1, bonus band in Pattern 2 and table-use instructions/exception methods pp. 19-22; not every unrelated retirement-table entry | 2026-11-14 |
| NTA 2502: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2502.htm | Read for withholding obligation, payroll-office notification and domestic-service exception | 2026-11-14 |
| NTA 2505: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2505.htm | Read for fewer-than-10 approval, July/January due dates, covered categories, commencement and loss | 2026-11-14 |
| NTA 2520: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2520.htm | Read for primary/secondary declaration, Otsu dependent reduction and no ordinary secondary-pay year-end adjustment | 2026-11-14 |
| NTA 2665: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2665.htm | Read for year-end population/exclusions and specified mid-year departures | 2026-11-14 |
| NTA 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm | Read for annual bands, rounded base, quick deductions and reconstruction supplement | 2026-11-14 |
| NTA 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm | Read for 2026/2027 deduction, December effective date, low-income notes and statutory table below 6,600,000 | 2026-11-14 |
| NTA 2582: https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2582.htm | Read for reasonable rail/bus route, monthly cap, mixed transport and excess taxation | 2026-11-14 |
| NTA 7411: https://www.nta.go.jp/taxes/shiraberu/taxanswer/hotei/7411.htm | Read for employee slip, mid-year leaver, municipality/NTA reporting and January 2027 deemed-submission change | 2026-11-14 |
| Tokyo insurance table: https://www.kyoukaikenpo.or.jp/assets/R8_13tokyo.pdf | Read for full remuneration table, rates/effective months, split, caps, rounding and both distinct child charges | 2026-11-14 |
| MHLW employment premiums: https://www.mhlw.go.jp/content/001692566.pdf | Read for FY2026 general/special sectors, employee/employer split and sector footnote | 2026-11-14 |
| MHLW compensation premiums: https://www.mhlw.go.jp/content/roumuhiritu_r05.pdf | Read for FY2026 ordinary industry rate schedule, including category 94 and range | 2026-11-14 |
| JPS annual SMR: https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20121017.html | Read for qualifying days/population, April-June, July filing, September application and exclusions | 2026-11-14 |
| JPS mid-year SMR: https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20150515-02.html | Read for fixed pay, direction, 3 months/days/grades, 4th-month effective date and boundary exceptions | 2026-11-14 |
| JPS bonus: https://www.nenkin.go.jp/service/kounen/hokenryo/hoshu/20141203.html | Read for standard bonus, caps, multiple payments, frequency, insurer/year accumulation and filing/loss-month exceptions | 2026-11-14 |
| JPS commuting FAQ: https://www.nenkin.go.jp/section/faq/kounen/hyoujunhoushu/20140602-03.html | Read for inclusion of commuting allowance in remuneration | 2026-11-14 |
| JPS October coverage: https://www.nenkin.go.jp/oshirase/taisetu/jigyosho/2026/202610/100104.html | Read for abolition of wage condition and remaining/permission exceptions | 2026-11-14 |
| Labour Bureau wage base: https://jsite.mhlw.go.jp/kanagawa-roudoukyoku/hourei_seido_tetsuzuki/roudou_hoken/hourei_seido/2024_00001.html | Read for salary/allowance/bonus wage inclusion including non-taxable commuting | 2026-11-14 |
| MHLW annual update: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/hoken/roudouhoken21/index.html | Read for FY2026 June-July filing/payment period and electronic filing | 2026-11-14 |
| MHLW minimum wages: https://saiteichingin.mhlw.go.jp/table/page_list_nationallist.html | Read for the six retained prefectures and separate actual/future Okinawa dates | 2026-11-14 |
| MHLW working rules: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudouseisaku/chushoukigyou/joken_kankyou_rule.html | Read for wage payment/payslip, hours/premiums, annual leave table and maternity entitlement; not the page's older childcare limit | 2026-11-14 |
| MHLW overtime: https://hatarakikatakaikaku.mhlw.go.jp/overtime.html | Read for standard/special limits, monthly strict boundary and multi-month/annual tests | 2026-11-14 |
| Current Labour Standards Act: https://laws.e-gov.go.jp/api/2/law_data/322AC0000000049 | Read for main arts. 24/32/36/37/39/65/115/119/120, including current penalty wording; figures are in words on the page | 2026-11-14 |
| Current General Tax Act: https://laws.e-gov.go.jp/api/2/law_data/337AC0000000066 | Read for main art. 67 additional tax and neighboring collection/rounding framework; figures are in words on the page | 2026-11-14 |
| Kyokai maternity: https://www.kyoukaikenpo.or.jp/benefit/childbirth/001/ | Read for covered days, unpaid/difference condition, SMR formula, short coverage, rounding and late birth | 2026-11-14 |
| Kyokai childbirth lump sum: https://www.kyoukaikenpo.or.jp/benefit/childbirth/002/ | Read for covered childbirth, 500,000/488,000 categories, weeks and application/direct payment | 2026-11-14 |
| Kyokai sickness: https://www.kyoukaikenpo.or.jp/benefit/injury_and_sickness_allowance/index.html | Read for eligibility, 3-day wait, pay difference, aggregate duration and SMR formula | 2026-11-14 |
| MHLW childcare Q&A: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000158500.html | Read for Q11-Q18, Q33-Q40: eligibility, wage base/rates/caps, work/pay limits, extension evidence and supplement/spouse exceptions | 2026-11-14 |
| MHLW childcare entitlement: https://www.mhlw.go.jp/seisakunitsuite/bunya/koyou_roudou/koyoukintou/ryouritsu/ikuji/childcare/ | Read for employee eligibility, contract/agreement exceptions, leave periods and distinct economic support | 2026-11-14 |
| JPS childcare exemption: https://www.nenkin.go.jp/section/faq/kounen/hokenryo/20140912.html | Read for application, monthly period/same-month 14 days, bonus longer-than-month test and maternity overlap | 2026-11-14 |
| Shinjuku tax collection: https://www.city.shinjuku.lg.jp/hoken/file04_04_00001.html | Read for notification, June-May salary collection and separate next-month municipal remittance | 2026-11-14 |
| Saitama retirement explanation: https://www.pref.saitama.lg.jp/a0816/rodo/912-2009-1207-176.html | Read for no universal statutory retirement allowance and contractual/work-rule duties | 2026-11-14 |
| MHLW working-time/leave policy: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/jikan/index.html | Read for employer adoption of paid sick-leave rules; no universal contractual day allowance inferred | 2026-11-14 |

**Not yet confirmed:** executable payroll for other insurers/prefectures, pre-change 2026 months or special coverage; exact benefit caps and shorter-history benefit amounts for an individual; local tax liability without the current notice; exact January 2027 operational reporting/holiday route for the employer; generic “failure to enroll = 6 months/JPY 500,000” sanction without identifying the breached provision (old claim held, not usable); old national weighted minimum-wage average JPY 1,121 and JPY 1,500 policy target, which are not wage floors; old “typically 3-10” employer-paid sick days and “80% large/70% SME” retirement prevalence, unsupported as current facts; old approximate net JPY 287,259/employer JPY 55,124, superseded by the recomputed cases; former minimum wages Tokyo 1,163/Kanagawa 1,162/Osaka 1,114/Aichi 1,077/Fukuoka 1,004/Okinawa 952 were not current October 2025 rates, much less November 2026 floors; old JPY 650,000 minimum with JPY 1,625,000/1,800,000 bands blended different years and is not the 2026 annual schedule; corporate deduction of employer contributions/retirement provisions requires separately sourced tax analysis. These topics remain explicit boundaries, not silently deleted advice.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
