---
name: cn-social-insurance
description: 处理中国大陆员工社会保险与住房公积金（五险一金）相关工作时必读本技能。涉及"中国社保"、"五险一金"、"养老保险"、"医疗保险"、"失业保险"、"生育保险"、"工伤保险"、"住房公积金"、"社保基数"、"缴费比例"、"社保申报"、"公积金缴存"、"社保税务征收"、"金税四期"、"外籍员工社保"、"延迟退休"等中文表述时触发；同时在英文场景下出现 "China social insurance"、"five insurances and one fund"、"Chinese pension"、"housing fund"、"China shebao gongjijin"、"China payroll statutory deductions"、"PRC social security"、"China provident fund" 等表述时也应触发。本技能为编排器（orchestrator），按月编制中国员工五险一金的缴费基数、单位与个人缴费金额、申报与缴纳节奏，并给出与个人所得税专项扣除的衔接口径。涵盖《社会保险法》《住房公积金管理条例》及各省/直辖市/计划单列市实施细则的通用框架；具体比例与基数上下限以"参保地"最新文件为准。
jurisdiction: CN
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.1
category: international
---

# China social insurance and housing provident fund: 2026 national method and dated local calculations

## Who this applies to

Mainland China employers and employees calculating the five social insurances and housing provident fund (五险一金). Employee pension and medical insurance are jointly funded; employers fund work injury and maternity, and unemployment follows the statutory employer/employee rules. Flexible workers and self-employed people without employees have separate participation routes. Do not apply an employer payroll table to them automatically ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html), arts. 10,12,23,33–34,44,53).

This is a **national framework with verified Shanghai illustrations**, not one national rate table. Contribution locality, scheme, worker category and contribution month determine the actual schedule. **Never use Shanghai as a provisional default for Beijing, Shenzhen, Guangzhou, Hangzhou, Chengdu or another locality.** Obtain each applicable local authority notice before computing. The earlier six-city overview is preserved as a list of required local determinations below, not as current rates without proof.

The housing fund is separate from social insurance. The consolidated regulation was amended in 2026, effective **20 September 2026**. It retains separate payroll-based contribution and remittance rules; do not use a social-insurance floor or monthly tax deadline for the housing fund ([Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html), amendment commencement; arts. 16–20).

## Rates, bands and thresholds

| Item | Verified figure / period | Official provision |
| --- | --- | --- |
| Shanghai employer pension / employee pension |16% /8%; locality-specific application | [Shanghai employer-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20250120/t0035_1430072.html); [Shanghai employee-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20200828/t0035_1393484.html) |
| Shanghai employer medical including maternity / employee medical |9% /2%;2026-03-01 to 2027-02-28. Employer 9%=8.5% basic including maternity+0.5% local addition | [Shanghai medical notice 2026 No.2](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/sbf/202603/t479836.html) items 1,3 |
| Earlier 2026 medical period |9% /2% for January–February under prior policy covering 2025-03 to 2026-02 | [Shanghai 2025 policy explanation](https://ybj.sh.gov.cn/zcjd/20250225/6ad4b3deb233457298f65fbc287a125e.html) |
| Shanghai unemployment employer / employee |0.5% /0.5% | [Shanghai employer-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20250120/t0035_1430072.html); [Shanghai employee-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20200828/t0035_1393484.html) |
| Shanghai work injury |Employer base rate 0.2%–1.9%; employee 0. Use the employer's notified risk class/floating rate | [Shanghai employer-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20250120/t0035_1430072.html); [Shanghai employee-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20200828/t0035_1393484.html); [Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 33–34 |
| Shanghai social-insurance base, January–June 2026 |Floor 7460/month; ceiling 37302/month, from the 2025-07-01 schedule | [Shanghai 2025 base notice](https://tyjr.sh.gov.cn/shtyjrswj/tzgg/20250919/557388ff0c4c4492ad11a3ae8863fb67.html) |
| Shanghai social-insurance base, from 2026-07-01 |Floor 7546/month; ceiling 37731/month; prior-year full-calibre average 12577/month | [Shanghai 2026 base notice](https://shanghai.chinatax.gov.cn/bsfw/nszx/hdfk/202609/t481435.html); [Shanghai base Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202608/t481376.html) |
| Shanghai ordinary housing fund,2026 fund year from 1 July |Employer and employee **each 5%–7%**, integer percentage; base 2740–37731/month | [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435) parts 1–2 |
| Shanghai supplementary housing fund |Each 1%–5%, integer percentage, voluntary scheme participation | [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435) part 2 |
| Shanghai housing fund at 7% |Published combined monthly minimum 384,maximum 5282; use official amount table and scheme rounding | [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435) part 4/table 1 |
| Shanghai flexible-worker housing fund |Total 10%–24%; separate participation/base rules; not an employer 7%+employee 7% default | [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435) part 5 |
| Employer social-insurance registration |Within 30 days of establishment; employment registration within 30 days of hiring | [Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 57–58 |
| Housing-fund employment registration / termination transfer or sealing |Within 30 days of hiring / termination | [Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html) art. 15 |
| Housing-fund payroll remittance |Within 5 days after monthly wage payment, not a universal next-month 15th | [Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html) art. 19 |

The Shanghai industry base range is not an instruction to select the lowest rate. The old 0.16%–1.52% injury range and 9.5% employer medical example are not used as current rates. Ordinary housing-fund 5%–7% and supplementary 1%–5% are separate; the old statement that Shanghai ordinary rates can be 12% is not carried forward. Other cities'5%–12% ranges require their actual current notices.

## The base

1. **Identify the actual schemes and locality.** Record social-insurance registration and housing-fund account separately, worker identity and category, employment start/end dates, any secondment and any agreement exemption. The five insurances are statutory schemes; housing-fund accounts have separate administration ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 2,57–60; [Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html) arts. 2,15).
2. **Establish the correct wage measure.** Shanghai's 2026 declaration uses the employee's prior natural-year average monthly wage. If employed for less than the full prior year, divide by actual working months. A 2026 new hire uses the full month's wage in the starting month. An employee with assessed grade 1–4 work disability receiving an allowance uses that allowance. Apply the statutory wage-total composition; do not use net pay ([Shanghai annual declaration notice 2026 No.1](https://shanghai.chinatax.gov.cn/tax/zcfw/zcfgk/sbf/202604/t480144.html) part 3).
3. **Apply each scheme's own floor and ceiling.** From July 2026 the Shanghai social base is `min(max(relevant_wage,7546),37731)`. Its housing fund instead uses the fund's 2740–37731 bounds and its own new-hire/new-transfer rules. Housing contributions for a newly employed worker start in the second month, while a transferred employee contributes from the new unit's wage-payment date. The July annual adjustment uses 2025 wages; the fund notice provides alternative actual-paid averages for specified new entrants. Do not presume that equal ceilings mean equal floors or identical new-hire timing ([Shanghai base Q&A](https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202608/t481376.html); [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435) part 1; [Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html) arts. 16–17).
4. **Compute separately by payer and scheme.** For the verified Shanghai employee illustration, employer pension=`social_base×16%`, employee pension=`social_base×8%`; medical=`×9%` and `×2%`; unemployment=`×0.5%` each. Injury is employer-only at its actual assigned rate. Apply the chosen lawful housing percentage separately to the fund base. Reconcile the assessment's rounding and all six scheme lines before paying ([Shanghai employer-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20250120/t0035_1430072.html); [Shanghai employee-rate guidance](https://rsj.sh.gov.cn/tdjjf_17554/20200828/t0035_1393484.html); [Shanghai medical notice 2026 No.2](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/sbf/202603/t479836.html); [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435)).
5. **Keep employer cost and employee deductions apart.** Employee deduction=employee social contributions+employee housing contributions. Employer payroll cost=gross wages+employer social contributions+employer housing contributions. Use `cn-iit` for the actual cumulative salary withholding; do not use the old illustrative 1290 yuan as a universal monthly IIT amount. The employee's allowable social/housing contributions are a separate IIT deduction determination under that Guide; do not net employer contributions against employee taxable pay.
6. **Reconcile and retain evidence.** Tie the registered wage, scheme base, current local notice, employer's injury-rate assessment, employee withholding, authority assessment and bank payment. Base adjustments can create back-payments; use the actual local catch-up notice rather than inventing a nationwide automatic grace period ([Shanghai annual declaration notice 2026 No.1](https://shanghai.chinatax.gov.cn/tax/zcfw/zcfgk/sbf/202604/t480144.html) part 5; [Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) art. 60).

### Benefits, retirement and non-payroll decisions retained from the earlier Guide

- **Pension accounts and entitlement:** employer/employee allocations are governed by Social Insurance Law art. 12. In 2026 the statutory minimum contribution period is 15 years; from 2030 it rises by 6 months per year to 20 years under the retirement decision. Starting 2025 the retirement ages rise gradually: men 60→63; the former 55 female group→58; the former 50 female group→55. Use the birth-date schedule and actual worker category, not the final target age as every person's current retirement age. Arrears/lump-sum eligibility and pension-benefit amounts need their applicable scheme rules ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 12,16; [2024 retirement-age decision and implementing measures](https://www.hmo.gov.cn/2026/08/21/ARTI6kpLUW6qilBUClmQ6bio260821.shtml) arts. 1–3).
- **Medical and maternity:** employee medical participation, medical benefits, employer-funded maternity and maternity medical allowance/benefit rights remain in arts. 23,28–30,53–56. Maternity allowance follows the employer's prior-year average wage under art. 56. The old 98-day plus local 60/80-day examples, an automatic divisor 30, specific local leave supplements, and current medical personal-account allocation percentages are **not computed here without their current separate authority rules**. They do not change the verified payroll contribution rates.
- **Unemployment:** statutory eligibility includes at least 1 year contributions, involuntary unemployment and registration/job-seeking. Statutory duration bands reach at most 24 months; benefit standards follow local rules. Do not assume that every city pays 70%–90% of its minimum wage ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 45–47).
- **Work injury:** employer-only funding and the authority's risk-based classification are separate from injury recognition, work-capacity assessment, medical/leave/disability/death awards. Those benefit calculations remain referrals rather than assumptions derived from the payroll contribution rate ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 33–42).
- **Housing-fund accounts:** registration, transfer/sealing, employee ownership and permitted withdrawals remain separate topics. Current 2026 art. 24 lists rent, purchase/construction/renovation/major repair of own housing, loan repayment, decoration, property charges, retirement, specified disability/termination, settlement abroad and other approved housing consumption. Withdrawal eligibility, loan limits and local implementation are not computed by this contribution Guide ([Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html) arts. 3,15,24–27).
- **Self-employed and flexible workers:** the national pension/medical participation routes are retained. Shanghai's current flexible-worker medical rate is 10% under the medical notice. Other flexible-worker pension rates, worker-category eligibility and regional benefit amounts require their own current source; do not substitute the employer/employee split ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html) arts. 10,23; [Shanghai medical notice 2026 No.2](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/sbf/202603/t479836.html) item 2).

## Deadlines and filing

| Task | Rule and period | Official provision |
| --- | --- | --- |
| Shanghai social insurance |Published normal payment timing is by the 15th **of the relevant month**; automatic deduction normally 10th–15th, subject to the actual published collection calendar | [Shanghai payment guidance](https://shanghai.chinatax.gov.cn/bsfw/nszx/hdfk/202301/t465801.html) |
| Shanghai 2026 annual wage declaration |1 May–25 June 2026 for the social-insurance year July 2026–June 2027; employee signature, employer seal and retained evidence | [Shanghai annual declaration notice 2026 No.1](https://shanghai.chinatax.gov.cn/tax/zcfw/zcfgk/sbf/202604/t480144.html) parts 1,5 |
| Shanghai housing-fund annual adjustment |New 2026 fund base from 1 July, with notification to the employee within 1 month of monthly-amount determination | [Shanghai housing-fund notice 2026 No.3](https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435) part 1 |
| Housing-fund monthly remittance |Within 5 days of wage payment; hardship reduction/deferral needs the prescribed employee representation/authority approval | [Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html) arts. 19–20 |
| IIT payroll withholding and annual reconciliation |Use the distinct dates and actual liability in `cn-iit`; social/housing payment dates do not determine IIT dates | `cn-iit` |

Do not turn Shanghai's guidance into a nationwide next-month 15th rule. Check the actual month and official holiday/collection-calendar adjustments. Shanghai's 2026 annual declaration can be made through the electronic tax bureau, social-fee management client or competent tax service hall; current screen names are in the cited notice ([Shanghai annual declaration notice 2026 No.1](https://shanghai.chinatax.gov.cn/tax/zcfw/zcfgk/sbf/202604/t480144.html) part 4).

## Penalties and interest

Social Insurance Law art. 86 requires an order to pay/make good arrears and a **daily 0.05%** late charge from the overdue date. If payment still is not made within the ordered time, the further fine is **1–3times** the arrears. This is not a discretionary universal interest estimate ([Social Insurance Law (2018 amended text)](https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html)).

Housing-fund sanctions changed during 2026. Under the consolidated text effective 20 September 2026, art. 39 addresses failure to register/open accounts: an order to rectify, then **50000–300000 yuan** if still not done. Art.40 addresses late/short contributions: an order to pay and possible court enforcement if unpaid; do not copy the social-insurance 0.05% charge into it. Historical violations before the amendment need the then-applicable text and transitional analysis; the current amounts are not retroactively asserted ([Housing Provident Fund Regulations, 2026 amended text](https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html), amendment commencement,arts. 39–40).

## Cross-border points

The 2024-revised foreign-worker measures cover lawfully employed foreign nationals, including relevant employment/residence documentation and foreign permanent residents. Local employers and inward secondment host units must arrange the five insurances and pay the prescribed contributions. Registration is within 30 days after the employment-document formalities. On departure before pension age, the individual account can be retained and contribution periods accumulate on return; written termination can permit payment of the individual-account balance. A bilateral/multilateral social-security agreement changes participation only within its actual scope and documentary conditions. Do not assume a passport exempts all five schemes ([Foreign-worker social-insurance measures,2024 revision](https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/202509/t20250908_4194428.html) arts. 2–5,9).

Housing-fund participation for foreign nationals and for Hong Kong/Macao/Taiwan residents is a separate local/category determination, not an automatic consequence of foreign-worker social insurance. The former Guide's general waiver and city examples remain unconfirmed pending those specific rules. Cross-border social-security certificates, validity periods, renewals and covered branches require the actual agreement; no exhaustive treaty-country list or fixed maximum assignment period is asserted here.

## Two worked examples that recompute

**Example 1: corrected Shanghai 30000 yuan employee.** Assume an established employee with prior-year average monthly wage and current monthly gross pay both 30000, a July–December 2026 contribution month, ordinary housing-fund rate 7% each, employer injury assessment 0.2%, no supplementary fund, and no category exemption. Both actual bases are 30000. Employee social contributions 3150 plus housing 2100 give 5250 deductions and 24750 before IIT. Employer social contributions 7710 plus housing 2100 give 9810 contributions; total payroll cost 39810. The old 9.5% medical and 0.16% injury assumptions are replaced by the cited current rates; IIT is computed separately, not fixed at 1290.

```oa-check
name: Shanghai July2026 established employee, separate payer totals
inputs:
  social_base: 30000
  housing_base: 30000
  gross_pay: 30000
steps:
  employee_social: social_base * (0.08 + 0.02 + 0.005)
  employee_housing: housing_base * 0.07
  employee_total: employee_social + employee_housing
  pay_before_iit: gross_pay - employee_total
  employer_social: social_base * (0.16 + 0.09 + 0.005 + 0.002)
  employer_housing: housing_base * 0.07
  employer_total: employer_social + employer_housing
  payroll_cost: gross_pay + employer_total
expected:
  employee_social: 3150
  employee_total: 5250
  pay_before_iit: 24750
  employer_social: 7710
  employer_total: 9810
  payroll_cost: 39810
```

**Example 2: distinct social/housing floors.** Assume an established employee with prior-year average and gross 6000, the same month/category/rates as example 1 and no exemption. Social base=max(6000,7546)=7546; housing base=max(6000,2740)=6000. Round each social-insurance line to cents for this illustration and reconcile actual assessment rounding. Employee social:603.68+150.92+37.73=792.33; housing 420; total 1212.33. Employer social:1207.36+679.14+37.73+15.09=1939.32; housing 420; total 2359.32; employer payroll cost 8359.32. Do not apply 7546 as the housing-fund floor.

```oa-check
name: Shanghai July2026 distinct contribution floors
inputs:
  prior_average: 6000
  gross_pay: 6000
steps:
  social_base: min(max(prior_average, 7546), 37731)
  housing_base: min(max(prior_average, 2740), 37731)
  employee_social: round(social_base * 0.08, 2) + round(social_base * 0.02, 2) + round(social_base * 0.005, 2)
  employee_total: employee_social + housing_base * 0.07
  employer_social: round(social_base * 0.16, 2) + round(social_base * 0.09, 2) + round(social_base * 0.005, 2) + round(social_base * 0.002, 2)
  employer_total: employer_social + housing_base * 0.07
  payroll_cost: gross_pay + employer_total
expected:
  social_base: 7546
  housing_base: 6000
  employee_social: 792.33
  employee_total: 1212.33
  employer_social: 1939.32
  employer_total: 2359.32
  payroll_cost: 8359.32
```

## Ask the client first

- Which city, contribution month, registered schemes and worker category apply? Provide the current local notices and employer's actual injury assessment.
- Is the worker established, a first-time new hire or transferred from another unit? What are the start, payroll and termination dates?
- What was the prior-year wage total and actual working months? Which bonuses/allowances form part of wages? Do we have an approved wage-base declaration?
- Which ordinary and supplementary housing percentages were actually registered? Are housing and social bases different?
- Is there lawful foreign employment/secondment, a Hong Kong/Macao/Taiwan category or a valid agreement certificate? Which branches and periods does it cover?
- Are we correcting a prior period, making a current payment, resolving arrears or computing benefits/retirement? Provide notices and the authority's deadlines.
- Are employee social/housing deductions already included in the cumulative IIT working paper? Reconcile them once, using `cn-iit`.

## Sources

| Source | Official URL | Read on |
| --- | --- | --- |
| Social Insurance Law (2018 amended text) | https://fgk.chinatax.gov.cn/zcfgk/c100009/c5192937/content.html | 2026-10-29 |
| Housing Provident Fund Regulations, 2026 amended text | https://legalinfo.moj.gov.cn/zhfxfzzx/fzzxyw/202608/t20260819_538654.html | 2026-10-29 |
| Shanghai employer-rate guidance | https://rsj.sh.gov.cn/tdjjf_17554/20250120/t0035_1430072.html | 2026-10-29 |
| Shanghai employee-rate guidance | https://rsj.sh.gov.cn/tdjjf_17554/20200828/t0035_1393484.html | 2026-10-29 |
| Shanghai 2025 policy explanation | https://ybj.sh.gov.cn/zcjd/20250225/6ad4b3deb233457298f65fbc287a125e.html | 2026-10-29 |
| Shanghai medical notice 2026 No.2 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/sbf/202603/t479836.html | 2026-10-29 |
| Shanghai 2025 base notice | https://tyjr.sh.gov.cn/shtyjrswj/tzgg/20250919/557388ff0c4c4492ad11a3ae8863fb67.html | 2026-10-29 |
| Shanghai 2026 base notice | https://shanghai.chinatax.gov.cn/bsfw/nszx/hdfk/202609/t481435.html | 2026-10-29 |
| Shanghai base Q&A | https://shanghai.chinatax.gov.cn/tax/zcfw/rdwd/202608/t481376.html | 2026-10-29 |
| Shanghai housing-fund notice 2026 No.3 | https://www.shanghai.gov.cn/gwk/affairs/content/0064%40f3d788ec72e9404ebcbf3d27fda98435 | 2026-10-29 |
| Shanghai annual declaration notice 2026 No.1 | https://shanghai.chinatax.gov.cn/tax/zcfw/zcfgk/sbf/202604/t480144.html | 2026-10-29 |
| Shanghai payment guidance | https://shanghai.chinatax.gov.cn/bsfw/nszx/hdfk/202301/t465801.html | 2026-10-29 |
| 2024 retirement-age decision and implementing measures | https://www.hmo.gov.cn/2026/08/21/ARTI6kpLUW6qilBUClmQ6bio260821.shtml | 2026-10-29 |
| Foreign-worker social-insurance measures,2024 revision | https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/202509/t20250908_4194428.html | 2026-10-29 |

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. A qualified professional in the relevant jurisdiction must review the work before filing, paying or taking a tax position.

**Not yet confirmed:** current city/category tables for Beijing, Shenzhen, Guangzhou, Hangzhou and Chengdu; pre-July 2026 Shanghai housing-fund bounds; non-Shanghai collection calendars and rounding; the previous blanket 5%–12% housing range; city-specific medical-account allocations and supplementary medical fees; precise maternity leave days/local supplements/divisor; local unemployment-benefit percentages; current flexible-worker pension rates and non-Shanghai voluntary-fund rules; foreign/Hong Kong/Macao/Taiwan housing-fund participation; branch-specific social-security agreements/certificates; pre 20 September 2026 housing-fund violation transitions; retirement-benefit and lump-sum eligibility computations. The earlier illustrative tax 1290 yuan is not verified as a current payroll result. These named limits replace unsupported defaults; they do not authorise estimating with another city's table. Additional original topics retained as explicit unconfirmed/referral limits: resident rural/urban schemes; retiree rehires; intern/student work; dispatch/outsourcing; cross-province employer registration; enterprise/occupational annuities; commercial supplementary medical/employer-liability insurance; the former eight work-injury industry classes, industry examples and floating coefficients.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
