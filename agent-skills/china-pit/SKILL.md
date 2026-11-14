---
name: china-pit
description: "Use this skill whenever asked to prepare, review, or classify transactions for China Personal Income Tax (个人所得税 / IIT) in tax year 2026, the annual comprehensive income settlement (汇算清缴), Chinese tax brackets or the special additional deductions (专项附加扣除). Trigger on phrases like \"个人所得税\", \"IIT China\", \"综合所得\", \"汇算清缴\", \"专项附加扣除\", \"China income tax\", or any PRC personal income tax question. It gives the 2026 comprehensive and business income scales, the 60,000 yuan basic deduction, the special additional deduction amounts and the cumulative withholding and annual settlement method, and routes depth to cn-iit. Built from the law, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/china-pit"
  jurisdiction: "CN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# China Personal Income Tax (个人所得税): quick computation for 2026

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in China.

## Scope

This skill computes PRC Individual Income Tax (IIT) for a resident individual for calendar tax year 2026: the comprehensive income scale (wages, labour remuneration, author's remuneration, royalties), the business income scale, the 20% flat categories, the 60,000 yuan basic deduction and the special additional deductions. It is the short computation route. The full 2026 guide, with the 2026 changes (foreign individuals' dividends from 1 September 2026, offshore trusts, the home replacement refund, platform workers), non-residents and foreign income in depth, is `cn-iit`. Social insurance rates are in `cn-social-insurance`; payer withholding mechanics in `cn-withholding`.

**Quick reference**

| Field | Value |
| --- | --- |
| Country | 中华人民共和国 (People's Republic of China), mainland only; Hong Kong, Macao and Taiwan have their own skills |
| Tax | 个人所得税 (Individual Income Tax, IIT) |
| Currency | CNY (人民币, RMB, yuan) |
| Tax year | Calendar year, 1 January to 31 December 2026 |
| Tax authority | 国家税务总局 (State Taxation Administration, STA) |
| Filing app | 个人所得税 APP (IIT APP) |
| Filing portal | https://etax.chinatax.gov.cn (natural person e-tax web) |
| Annual settlement (汇算清缴) for 2026 | 1 March to 30 June 2027 (IIT Law art. 11) |
| Basic deduction | 60,000 yuan a year (5,000 yuan a month) |

## Rates, bands and thresholds

All figures are for tax year 2026. Conditions sit in the third column.

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Comprehensive income, band 1 | 3%, quick deduction 0 | Annual taxable income up to 36,000 yuan | https://guangdong.chinatax.gov.cn/gdsw/fssw_nsrxt_kjxz/2025-10/09/content_b02be06c906e46bca00673beb9e7783a.shtml |
| Comprehensive income, band 2 | 10%, quick deduction 2,520 | Over 36,000 to 144,000 yuan | same |
| Comprehensive income, band 3 | 20%, quick deduction 16,920 | Over 144,000 to 300,000 yuan | same |
| Comprehensive income, band 4 | 25%, quick deduction 31,920 | Over 300,000 to 420,000 yuan | same |
| Comprehensive income, band 5 | 30%, quick deduction 52,920 | Over 420,000 to 660,000 yuan | same |
| Comprehensive income, band 6 | 35%, quick deduction 85,920 | Over 660,000 to 960,000 yuan | same |
| Comprehensive income, band 7 | 45%, quick deduction 181,920 | Over 960,000 yuan | same |
| Business income (经营所得), band 1 | 5% | Annual taxable income up to 30,000 yuan (IIT Law Table 2) | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html |
| Business income, band 2 | 10% | Over 30,000 to 90,000 yuan | same |
| Business income, band 3 | 20% | Over 90,000 to 300,000 yuan | same |
| Business income, band 4 | 30% | Over 300,000 to 500,000 yuan | same |
| Business income, band 5 | 35% | Over 500,000 yuan | same |
| Interest, dividends, rental, property transfer, incidental income | 20% flat | IIT Law art. 3(3) | same |
| Basic deduction (基本减除费用) | 六万元 (sixty thousand yuan) a year | Resident individual, comprehensive income (art. 6(1)) | same |
| Labour remuneration, author's remuneration, royalties: income amount | Receipts less 20% | Annual computation; author's remuneration then counted at 百分之七十 (seventy per cent) (art. 6) | same |
| Property rental expense deduction | 800 yuan, or 20% | 800 yuan if each receipt is 四千元 (four thousand yuan) or less; 20% if more (art. 6(4)) | same |
| Charitable donations | Up to 30% of declared taxable income | Full deduction where the State Council so provides (art. 6) | same |
| Residence test | 183 days | A person without domicile is resident if in China 183 days or more in the tax year (art. 1) | same |
| Children's education (子女教育) | 2,000 yuan a month per child | From 1 January 2023; full-time education from age 3 to doctorate; one parent takes the whole amount or each parent half (split rule from the 2018 Interim Measures, not on this notice) | https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/202308/t20230831_3905100.htm |
| Infant care (3岁以下婴幼儿照护) | 2,000 yuan a month per child | Child under 3; same split options | same |
| Elderly care (赡养老人) | 3,000 yuan a month | Only child takes all 3,000; siblings share 3,000 with at most 1,500 each | same |
| Continuing education, degree (学历继续教育) | 400 yuan a month | During the degree course, at most 48 months | https://hainan.chinatax.gov.cn/xxgk_6_1/22110230.html |
| Continuing education, professional certificate | 3,600 yuan | In the year the certificate is obtained | same |
| Serious illness medical (大病医疗) | Actual cost above 15,000 yuan, up to 80,000 yuan | Self-paid part within the basic medical insurance list, claimed at the annual settlement | same |
| Housing loan interest (住房贷款利息) | 1,000 yuan a month | First home loan, at most 240 months, once per lifetime | same |
| Housing rent (住房租金), tier 1 | 1,500 yuan a month | Municipalities, provincial capitals, cities with separate plans; no own home in the work city | same |
| Housing rent, tier 2 | 1,100 yuan a month | Other cities with registered urban population over 1 million | same |
| Housing rent, tier 3 | 800 yuan a month | Cities with registered urban population of 1 million or less | same |
| Commercial health insurance | 2,400 yuan a year (200 yuan a month) | Qualifying products | https://guangdong.chinatax.gov.cn/gdsw/zjfg/2017-05/03/content_f7a7387e2ba441a995345e7c0d60e44f.shtml |
| Personal pension (个人养老金) | 12,000 yuan a year | Contributions to the personal pension account, nationwide from 1 January 2024 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202412/t474540.html |
| Labour remuneration prepayment, band 1 | 20%, quick deduction 0 | Per-payment taxable amount up to 20,000 yuan | https://guangdong.chinatax.gov.cn/gdsw/fssw_nsrxt_kjxz/2025-10/09/content_b02be06c906e46bca00673beb9e7783a.shtml |
| Labour remuneration prepayment, band 2 | 30%, quick deduction 2,000 | Over 20,000 to 50,000 yuan | same |
| Labour remuneration prepayment, band 3 | 40%, quick deduction 7,000 | Over 50,000 yuan | same |
| Labour, author's, royalty prepayment expense | 800 yuan, or 20% | 800 yuan if each payment is 四千元 (four thousand yuan) or less; 20% if more | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html |
| Settlement exemption | Income up to 12万 yuan (120 thousand) with tax due, or tax due up to 400 yuan | Years 2024 to 2027; not where a withholding agent failed to withhold | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468462.html |
| Late payment surcharge (滞纳金) | 万分之五 (five ten-thousandths, that is 0.05 per cent) a day | From the day the tax is overdue (Tax Collection Law art. 32) | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html |

Business income quick deductions (computed from the Table 2 bands, not printed in the law): 0; 1,500; 10,500; 40,500; 65,500.

## Ask the client first

1. Residence: domicile in China, or days in mainland China in 2026 (183-day test). Non-residents go to `cn-iit`.
2. Each income type and amount for 2026, by the nine categories, and who paid it (withholding agent or not).
3. Social insurance and housing fund actually withheld (专项扣除), from the payslips.
4. Facts for each special additional deduction: children and ages, parents over 60 and siblings, first home loan, rent and city, continuing education, large medical costs, and any split agreed with a spouse or siblings.
5. Tax prepaid or withheld during 2026, from the IIT APP income record.
6. Any foreign income, business income, equity incentive or annual bonus (route to `cn-iit`).

## The method, step by step

1. **Annual income amount (全年收入额).** Wages at the actual amount. Labour remuneration and royalties at 80% of receipts. Author's remuneration at 80% then 70% (56% of receipts).
2. **Less the basic deduction** of 60,000 yuan.
3. **Less special deductions (专项扣除):** the employee's basic pension, medical, unemployment insurance and housing fund contributions actually paid (rates in `cn-social-insurance`).
4. **Less special additional deductions (专项附加扣除)** at the monthly amounts in the rates table, for the months the condition was met.
5. **Less other deductions:** commercial health insurance (2,400 yuan a year cap), personal pension (12,000 yuan a year cap), and other items the law allows.
6. **Less charitable donations,** up to 30% of declared taxable income (or in full where the State Council allows).
7. **Annual taxable income (全年应纳税所得额).**
8. **Tax** = taxable income times the band rate, less the quick deduction (comprehensive income table).
9. **Less tax prepaid or withheld** during the year (已预缴税额).
10. **Tax payable or refund (补税/退税).** Check the settlement exemption before filing.

**Cumulative withholding (累计预扣预缴).** Employers withhold each month on cumulative wages to date, less cumulative basic deduction (5,000 yuan a month), cumulative special and special additional deductions; they apply the comprehensive table to the cumulative amount and subtract tax already withheld in earlier months.

**Labour remuneration prepayment.** Per payment: deduct 800 yuan (payment of 4,000 yuan or less) or 20% (more); apply the 20%/30%/40% prepayment table. The prepayment is credited at the annual settlement.

**Business income** (individual businesses, sole proprietorship and partnership investors): annual profit less allowable costs, losses and, for an individual without comprehensive income, the 60,000 yuan basic deduction and the special and special additional deductions; apply the 5% to 35% table. Preferential halving for individual businesses and filing detail: `cn-iit`.

### Nine categories of taxable income

| # | Chinese | English | Tax treatment |
| --- | --- | --- | --- |
| 1 | 工资、薪金所得 | Wages, salary | Comprehensive (cumulative withholding) |
| 2 | 劳务报酬所得 | Labour remuneration | Comprehensive (20%/30%/40% prepayment, settled annually) |
| 3 | 稿酬所得 | Author's remuneration | Comprehensive (income amount at 70%) |
| 4 | 特许权使用费所得 | Royalties | Comprehensive |
| 5 | 经营所得 | Business income | Separate (5% to 35% bands) |
| 6 | 利息、股息、红利所得 | Interest, dividends | 20% flat |
| 7 | 财产租赁所得 | Property rental | 20% flat |
| 8 | 财产转让所得 | Property transfer | 20% flat on gain (proceeds less cost and reasonable expenses) |
| 9 | 偶然所得 | Incidental income | 20% flat (lottery winnings and the like) |

### Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Income category ambiguous | Classify as the higher-rate category and flag |
| Special additional deduction eligibility unclear | Do not claim; flag for the reviewer |
| Foreign income of a resident | Include; credit foreign tax up to the PRC tax on it (art. 7); declare 1 March to 30 June of the next year; route to `cn-iit` |
| Stock options, RSUs | Treat as wages on exercise or vesting under the equity rules; route to `cn-iit` |
| Crypto gains | No specific STA rule read; conservative position is property transfer at 20% on the gain; flag |
| Annual one-off bonus | A separate-taxation option exists to 2027; route to `cn-iit` |
| Non-resident | Monthly converted table, no annual settlement; route to `cn-iit` |
| Both parents claim the full child deduction | Not allowed: one parent 100% or each 50%, fixed for the year |

## Worked cases

**Case 1: Beijing employee, annual settlement.** Salary 360,000 yuan; one child in school; first home loan; only child caring for a parent over 60. Social insurance and housing fund withheld 4,500 yuan a month. Tax withheld during the year 18,500 yuan.

| Step | Description | Amount (yuan) |
| --- | --- | --- |
| Annual salary | | 360,000 |
| Less basic deduction | 5,000 x 12 | (60,000) |
| Less social insurance and housing fund | 4,500 x 12 | (54,000) |
| Less children's education | 2,000 x 12 | (24,000) |
| Less housing loan interest | 1,000 x 12 | (12,000) |
| Less elderly care | 3,000 x 12 | (36,000) |
| **Taxable income** | | **174,000** |

Tax: 174,000 x 20% less 16,920 = 17,880 yuan. Withheld 18,500, so the refund is 620 yuan.

```oa-check
name: CN 2026 Beijing employee annual settlement, refund
inputs:
  salary: 360000
  basic: 60000
  social: 54000
  child: 24000
  loan: 12000
  elderly: 36000
  withheld: 18500
steps:
  - taxable: salary - basic - social - child - loan - elderly
  - tax: taxable * 0.20 - 16920
  - refund: withheld - tax
expected:
  taxable: 174000
  tax: 17880
  refund: 620
```

**Case 2: decision, which parent claims the child deduction.** Parent A has taxable income of 200,000 yuan before the child deduction (20% band); parent B has 50,000 yuan (10% band). One child: 24,000 yuan a year. Option 1: A claims 100%. Option 2: each claims 50%. Option 1: A pays 176,000 x 20% less 16,920 = 18,280; B pays 50,000 x 10% less 2,520 = 2,480; total 20,760. Option 2: A pays 188,000 x 20% less 16,920 = 20,680; B pays 38,000 x 10% less 2,520 = 1,280; total 21,960. A claiming 100% saves the household 1,200 yuan (12,000 x the 10-point band gap). The deciding figure is the difference in marginal band; if both are in the same band, the split does not matter.

```oa-check
name: CN 2026 child deduction split, higher earner claims all
inputs:
  a: 200000
  b: 50000
  child: 24000
steps:
  - opt1_a: (a - child) * 0.20 - 16920
  - opt1_b: b * 0.10 - 2520
  - opt1: opt1_a + opt1_b
  - opt2_a: (a - child / 2) * 0.20 - 16920
  - opt2_b: (b - child / 2) * 0.10 - 2520
  - opt2: opt2_a + opt2_b
  - saving: opt2 - opt1
expected:
  opt1: 20760
  opt2: 21960
  saving: 1200
```

## When to refuse or refer

- Non-residents, people without domicile in their first six years, treaty claims: refer to `cn-iit` and `cn-cross-border`.
- Equity incentives, offshore trusts, foreign-invested enterprise dividends to foreign individuals (taxed from 1 September 2026): `cn-iit`.
- Business income with audited books, partnerships with several investors, or approved (核定) assessment: refer to an accountant.
- Any request to hide income, back-date a deduction split or claim a deduction the person does not meet: refuse.

## Filing and payment

### Annual settlement (汇算清缴)

| Situation | Action and deadline |
| --- | --- |
| Tax due exceeds prepayments | File and pay between 1 March and 30 June 2027 for tax year 2026, unless the settlement exemption applies |
| Prepayments exceed tax due (退税) | File between 1 March and 30 June 2027 to claim the refund |
| Settlement exemption | Comprehensive income up to 120,000 yuan with tax to pay, or tax to pay up to 400 yuan: no settlement needed (2024 to 2027), unless a withholding agent failed to withhold |
| Single employer, withholding correct, no refund wanted | No settlement needed |
| Foreign income | Declare 1 March to 30 June of the next year |
| Income with no withholding agent | File by the 15th of the month after receipt |
| Business income | Prepay within 15 days after each month or quarter; annual return by 31 March of the next year |

The STA opens an appointment window for early March each year (for the 2025 year: bookings from 25 February for 1 to 20 March 2026, STA notice 2026 No. 1). Correction (old file): the old file said everyone with annual income over 120,000 yuan must file; under the current law the test is whether tax is due or refundable, with the exemption above.

### Key filing methods

- **个人所得税 APP** (official mobile app), the most common route.
- **Web portal:** etax.chinatax.gov.cn.
- **In person:** the local tax service hall (办税服务厅).

### Penalties and interest

Late payment: surcharge of 0.05% a day from the due date (Tax Collection Law art. 32). Late filing, false filing and non-payment carry fines under Tax Collection Law arts. 62 to 64 and 68; route detail to `cn-iit`.

## Completion checklist

- Residence confirmed; income listed by category with payer.
- Social insurance amounts taken from payslips, not computed from rates.
- Each special additional deduction checked against its condition and split.
- Tax computed with the comprehensive table and reconciled to prepayments.
- Settlement exemption checked; deadline 30 June 2027 noted.
- Anything routed to `cn-iit` named.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| PRC Individual Income Tax Law (2018 amendment), STA Shanghai policy library. Read for arts. 1, 3, 6, 7, 11 to 14 and Tables 1 and 2 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html | 2026-11-14 |
| STA Guangdong, IIT rate and prepayment tables. Read for the comprehensive quick deductions and the labour remuneration prepayment table | https://guangdong.chinatax.gov.cn/gdsw/fssw_nsrxt_kjxz/2025-10/09/content_b02be06c906e46bca00673beb9e7783a.shtml | 2026-11-14 |
| State Council 国发〔2023〕13号 on the Ministry of Finance site. Read for the 2,000 yuan child and infant amounts and the 3,000 yuan elderly care amount | https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/202308/t20230831_3905100.htm | 2026-11-14 |
| STA Guangdong, STA announcement 2023 No. 14 implementing the higher amounts. Read for the 1,500 yuan sibling cap | https://guangdong.chinatax.gov.cn/gdsw/gzsw_gkwj/2023-09/15/content_eaad1edc607b4328b494e1a053085a5e.shtml | 2026-11-14 |
| Interim Measures for special additional deductions 国发〔2018〕41号, STA Hainan. Read for continuing education, medical, housing loan and the three rent tiers | https://hainan.chinatax.gov.cn/xxgk_6_1/22110230.html | 2026-11-14 |
| Withholding measures, STA announcement 2018 No. 61. Read for the 800 yuan or 20% prepayment expense rule | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html | 2026-11-14 |
| MOF and STA announcement 2023 No. 32. Read for the settlement exemption to 2027 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202308/t468462.html | 2026-11-14 |
| STA notice 2026 No. 1. Read for the 2025 settlement window and appointment dates | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202602/t479400.html | 2026-11-14 |
| Commercial health insurance notice, STA Guangdong. Read for the 2,400 yuan a year cap | https://guangdong.chinatax.gov.cn/gdsw/zjfg/2017-05/03/content_f7a7387e2ba441a995345e7c0d60e44f.shtml | 2026-11-14 |
| Personal pension, MOF and STA announcement 2024 No. 21. Read for the 12,000 yuan a year cap | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/202412/t474540.html | 2026-11-14 |
| Tax Collection Administration Law, STA Shanghai. Read for art. 32 surcharge and arts. 62 to 64, 68 | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html | 2026-11-14 |

Not yet confirmed: the 2026 settlement window dates and appointment schedule (the STA publishes them in early 2027; the law fixes 1 March to 30 June); a specific STA rule on crypto gains (none read; the 20% property transfer position is a conservative default, not a confirmed rule).

*OpenAccountants: open-source accounting skills for AI. This is not tax advice. All outputs must be reviewed by a qualified professional before filing.*

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `china-pit` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/china-pit. If neither is available, confirm every figure against the official source pages cited above before relying on it.
