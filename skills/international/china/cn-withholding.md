---
name: cn-withholding
description: 当用户咨询、计算、审核或申报中国预提所得税（源泉扣缴）相关事项时，必须始终先阅读本技能文档。触发关键词包括："中国预提所得税"、"非居民企业税收"、"10% 股息预提税"、"特许权使用费预提税"、"代扣代缴"、"源泉扣缴"、"中国DTA税收协定"、"非居民企业所得税"、"间接转让"、"698号文"、"7号公告"、"受益所有人"、"协定优惠"、"China WHT"、"China withholding tax"、"non-resident enterprise tax"、"China dividend WHT 10%"、"China DTA tax treaty"、"PRC withholding tax"、"China royalty withholding"、"China interest withholding"、"China indirect transfer"、"SAT Bulletin 9"、"SAT Bulletin 35"。本技能涵盖《中华人民共和国企业所得税法》第三章及第五章项下非居民企业（无机构场所）取得的中国境内来源所得的源泉扣缴（股息 10%、利息 10%、特许权使用费 10%、财产转让 10%、租金 10%），并涵盖《中华人民共和国个人所得税法》第九条项下扣缴义务人对工资薪金、劳务报酬、稿酬、特许权使用费、利息股息红利的代扣代缴义务，以及境外服务进口情形下境内购买方作为增值税扣缴义务人的代扣代缴义务（财税〔2016〕36号文附件1第六条）。同时涵盖税收协定（DTA）适用、受益所有人判定（《国家税务总局公告2018年第9号》）、协定优惠"自行判定、事后管理"程序（《国家税务总局公告2019年第35号》），以及非居民企业间接转让中国境内财产的征税规则（《国家税务总局公告2015年第7号》及国税函〔2009〕698号文）。不适用于：居民企业之间股息免税、合伙企业税收处理、特别纳税调整（转让定价）、CRS信息交换、外汇管制实务（SAFE）。**任何中国预提所得税相关工作动手之前，必须始终阅读本技能。**
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

# China withholding: payroll, individual fees, non-resident enterprises and imported services

## Who this applies to

Mainland China payers withholding individual income tax (IIT), enterprise income tax (EIT) from specified Chinese-source non-resident income, or VAT from an overseas seller. These are three separate liabilities: a treaty EIT exemption does not automatically exempt VAT, and a foreign company is not an individual. Establish the recipient, tax residence, income character, source and connection to a China establishment before selecting a rule ([IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) arts. 9–13; [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 3,19,37–40; [2026 VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) art. 15).

This 2026 Guide replaces the old 2025 tables and unsafe defaults. Unknown residence, a service/royalty distinction, place of consumption or treaty entitlement is a question to resolve with records, not permission to declare an invented classification. Ordinary resident enterprise dividends, partnership transparency, TP margins, CRS, SAFE remittance mechanics and foreign-country taxation need their own rules. Use `cn-iit`, `cn-corporate-tax`, `cn-vat`, `cn-transfer-pricing` and `cn-cross-border` at those boundaries.

## Rates, bands and thresholds

All figures are CNY unless an example expressly assumes a currency conversion.

| Income / test | Domestic rule | Official provision |
| --- | --- | --- |
| Specified Chinese-source non-resident enterprise income, no relevant China establishment connection |Statutory 20%, reduced to 10% under Regulations art. 91; treaty claim separately tested | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 3(3),4,27(5); [EIT Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html) art. 91 |
| Dividends, interest, rent, royalties in that scope |Gross income base, subject to the actual rule, exemptions and treaty; no assumed service-cost deduction | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 19; [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §3 |
| Property transfer |Gain: income less net property value; actual records and special indirect-transfer rules | [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) art. 19; [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §3; [STA 2015 No.7](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n1465977/201502/c1676726/content.html) |
| Resident salary monthly basic reduction |5000 per month in cumulative payroll calculation, with eligible additional/special deductions and any applicable special collection measures | [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 6; `cn-iit` |
| Resident labour/author/royalty fees |Per receipt: up to 4000, deduct 800; above 4000, deduct 20%. Author's income amount then×70% | [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 8 |
| Resident labour-fee withholding |20% to 20000;30%/quick deduction 2000 above 20000 to 50000;40%/7000 above 50000 | [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 8/attached table 2 |
| Resident author/royalty withholding |20% of the respective income amount; author's fee is **not** a universal 14% of gross | [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 8 |
| Individual interest/dividend/bonus classified income |20%, subject to specifically verified exemptions/reliefs | [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 3; [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 10 |
| Public-market listed-share dividends: holding≤1 month |Full base×20% | [Caishui 2015 No.101](https://www.chinatax.gov.cn/n810341/n810755/c1797427/content.html) §1 |
| Holding>1 month and≤1 year |50% base×20%=10% effective | [Caishui 2015 No.101](https://www.chinatax.gov.cn/n810341/n810755/c1797427/content.html) §1 |
| Holding>1 year |Temporary exemption, within the notice's actual scope | [Caishui 2015 No.101](https://www.chinatax.gov.cn/n810341/n810755/c1797427/content.html) §1 |
| Ordinary qualifying imported royalty/service consumed in China |6% VAT category for the stated example; classification/territoriality and collection method must be confirmed | [2026 VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) arts. 3–4,10,15; [2026 VAT Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html) art. 4 |

| Cumulative resident salary taxable base |Rate|Quick deduction|Official source|
| --- | --- | --- | --- |
| Up to 36000 |3%|0|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|
| Over 36000 to 144000 |10%|2520|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|
| Over 144000 to 300000 |20%|16920|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|
| Over 300000 to 420000 |25%|31920|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|
| Over 420000 to 660000 |30%|52920|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|
| Over 660000 to 960000 |35%|85920|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|
| Over 960000 |45%|181920|[STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html),table 1|

The individual wage table is cumulative annual withholding, not a monthly non-resident table. Non-resident wages deduct 5000 monthly and use the separate monthly table; non-resident labour/author/royalty income uses the corresponding income amount and that table. The foreign workday allocation,90/183-day or treaty conditions and annual residence change are addressed in `cn-iit`; do not blindly apply cumulative resident deductions ([STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 9).

## The base

### Non-resident enterprise income

Determine Chinese source under EIT Regulations art. 7: dividends depend on the distributing enterprise's location; interest/rent/royalties on the payer/burden rules; immovable property on location; equity transfer on the invested enterprise's location. Service and establishment profits are not automatically royalties taxable on gross receipts. Establishments and effective connection follow EIT Law art. 3; use `cn-corporate-tax` for an actual establishment's net-profit assessment.

For a taxable payment, identify its gross tax base, legal payee and withholding obligor. If the Chinese payer bears the recipient's EIT, gross up the recipient's EIT-exclusive income to the tax-inclusive EIT base under [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §6. Keep VAT **out** of the VAT-exclusive consideration; the contractual promise determines which taxes the payer bears. Do not divide by(1−VAT rate) as though VAT were an income tax. For instalment property transfers, apply the notice's permitted recovery of the investment cost before computing/withholding the gain (§7).

Translate foreign-currency amounts under the actual withholding-obligation rule and applicable central parity; an example's 7.20 is only an assumed input. Retain the contract, conversion date/rate, invoices, payment/accrual records, property cost and prior instalments ([STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §§3–7).

### Resident individual payments

For wages, cumulative taxable base=cumulative salary less exempt income,5000×eligible months and the person's actual allowable social/housing, additional and other deductions. Cumulative tax=base×rate−quick deduction−applicable tax relief; current withholding subtracts prior withholding. A negative current balance is not immediately refunded through this formula; reconcile through the prescribed annual route ([STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 6). Actual eligible deductions and newer special withholding measures remain governed by `cn-iit`, including platform-worker rules; ordinary non-platform labour-fee treatment is not universal.

For labour fees, use the per-receipt expense reduction and progressive withholding table above. For author's fees, apply the expense reduction, then 70%, then 20%; a 10000fee gives 5600 income amount and 1120 withheld, not 1400. Royalties use the expense reduction then 20%. These resident comprehensive categories enter the annual calculation; withholding is not necessarily final tax ([STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) arts. 8,11; [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 11). Define a receipt correctly: one-off income is per occurrence; continuing receipts for one project are grouped within the month (art. 11).

For listed-share dividends under No.101, the company **does not temporarily withhold** for an individual's holdings of 1 year or less at distribution. Upon later sale, the securities registration/settlement and custody chain calculates and collects the actual holding-period tax and passes it to the listed company. This corrects the former “withhold 20% then automatically refund” instruction. Shares held more than 1 year receive the specified exemption; restricted shares, employee-equity programmes and other shareholder types require their own scope analysis ([Caishui 2015 No.101](https://www.chinatax.gov.cn/n810341/n810755/c1797427/content.html) §§1–3).

### Imported services and intangibles

Under the 2026 VAT Law, first establish a taxable transaction in China and its actual category. If an overseas unit/individual makes a taxable transaction in China, the domestic buyer withholds **unless a domestic agent is entrusted to file/pay under the statutory rule**. A service consumed on site abroad can fall outside the China-consumption rule; uncertainty is not proof that it was partly consumed in China ([2026 VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) arts. 3–4,15; [2026 VAT Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html) art. 4).

VAT base excludes VAT. With VAT-inclusive consideration, divide by(1+applicable rate); with a price expressly exclusive of VAT, multiply that base by the rate. A general taxpayer's input claim on paid withholding VAT requires the legal payment voucher and other supporting contract/payment/foreign document conditions, and eligible taxable use; see `cn-vat`. Do not claim it merely because the payer remitted a tax ([2026 VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) arts. 17,21–22; [2026 VAT Implementation Regulations](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html) art. 11).

The import VAT described here is excluded from the urban maintenance/construction tax base. Education and local education surcharge use the same excluded base. The old example's 7%+3%+2% addition on imported royalty/service VAT is therefore removed, rather than treated as a Chinese city-rate assumption ([MOF/STA 2021 No.28](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5194989/content.html) §§1–3).

## Deadlines and filing

| Liability / information | Rule | Official provision |
| --- | --- | --- |
| Non-resident enterprise withholding |Declare/remit within 7 days of the withholding obligation; dividend obligation is actual payment; other payments apply the payment/due-and-payable rule | [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §7; [EIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html) arts. 37,40 |
| EIT withholding report |Submit current withholding enterprise-income-tax report and actual supporting data | [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §8 |
| Non-resident recipient where withholding failed |Recipient has a separate filing/payment duty; the notice governs filing before/after an authority order | [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §§9–10 |
| IIT payroll/fee withholding |Remit and file within 15 days after the following month's start, subject to lawful filing-calendar adjustments | [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 14 |
| IIT resident comprehensive reconciliation |If required,1 March–30 June following income year; distinguish withheld tax from final liability | [IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 11; `cn-iit` |
| IIT salary information |Provide annual income/tax information within 2 months after year end; supply required interim information when requested | [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 13 |
| Treaty documents | Self-assessment/claim plus retained evidence; the ordinary retention period is 10 years under the linked collection rules | [Treaty measures 2019 No. 35 Arts. 3,7–9,11](https://tianjin.chinatax.gov.cn/11200000000/0300/030004/03000418/20191024101530609.shtml); [Tax Collection Detailed Rules Art. 29](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200402/t284445.html) |
| VAT withholding |Same tax periods as the statutory taxpayer rule; use the competent authority's assigned period/calendar, not the EIT 7 day rule | [2026 VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) arts. 30–31 |

Do not apply one “payment date” to every levy. EIT dividend payment, accrued/due non-dividend income, IIT receipt and VAT tax point/filing periods require their actual provisions. Complete the treaty information report and current domestic form where required; no future screen/box identifier is invented. Keep all-recipient/full-income IIT information and the actual recipient's identification ([IIT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html) art. 10; [STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) arts. 2–5).

## Penalties and interest

Tax Collection Administration Law art. 69 distinguishes **failure to withhold**: the authority recovers tax from the taxpayer and can fine the withholding agent **50%–3times** the unwithheld amount. Art.68 addresses tax that remains unpaid/unremitted after the ordered period and permits **50%–5times**; concealment/fraud has its own art. 63 conditions. Art.32 provides the **daily 0.05%** late surcharge for the statutory overdue situations; do not assert that every failure to withhold automatically has identical surcharge mechanics. Reporting failures are separately addressed in arts. 60/62 ([Tax Collection Administration Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html)).

Overpayment and treaty-refund applications follow their actual legal procedure and limitation facts; a future refund is not a justification for knowingly applying the wrong classification. TP adjustments use the separate special-adjustment interest rules in `cn-transfer-pricing`, not this ordinary late-charge table.

## Cross-border points

Treaty entitlement is **self-assessed, claimed and supported by retained evidence**, subject to later authority checks. Collect the actual treaty version/protocol, residence proof, payment/ownership/holding-period records, contracts and beneficial-ownership/substance facts. A registration certificate or a Hong Kong address alone is not tax-residence proof. Missing treaty information does not itself convert an unknown payment into a royalty ([STA 2019 No.35 treaty-claim measures](https://tianjin.chinatax.gov.cn/11200000000/0300/030004/03000418/20191024101530609.shtml) arts. 3–8,11).

For dividends/interest/royalties, beneficial ownership considers ownership and control of the income/right and the actual facts. The adverse onward-payment factor includes an obligation or established practice to pass **50% or more within 12 months** to a third jurisdiction. Other factors concern substantial business activity, taxation and linked financing/licensing; specified dividend safe cases and look-through rules require their full conditions. Do not turn any single adverse factor into an automatic conclusion ([STA 2018 No.9 beneficial-owner rules](https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194781/content.html) §§1–4,8).

For indirect transfers, No.7 applies where a non-resident's arrangement lacks reasonable commercial purpose and avoids EIT on China taxable property. Analyse the actual asset/income/substance/holding/tax facts and listed exceptions; uncertainty is not a universal instruction to tax through the holding company. Report/withhold under the actual current procedure. No.37 §17's repeals mean the old 698circular is not a substitute for current procedural rules ([STA 2015 No.7](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n1465977/201502/c1676726/content.html); [STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html)).

The former Hong Kong, Singapore, US, UK, Japan, Germany, Netherlands, France, South Korea, Australia, Canada, Luxembourg and Ireland treaty-rate examples are retained as **named treaty determinations requiring their exact current instrument**; no unsourced consolidated rate table is carried forward. Hong Kong taxation of foreign dividends is not presumed zero, and China withholding is not asserted to be the recipient's final worldwide burden. Social-security treaties and currency-control/bank requirements are separate from income-tax treaties.

## Two worked examples that recompute

**Example 1: corrected foreign software-royalty gross-up.** Retain the former USD 1000000 scenario with an expressly assumed 7.20CNY/USD, so the foreign recipient is promised net 7200000 after Chinese EIT. Assume a genuine taxable royalty, no relevant China establishment or treaty relief, domestic 10% EIT,6% VAT, no entrusted domestic VAT agent, all Chinese taxes borne by the payer and no other levies. EIT/VAT-exclusive royalty base=7200000/(1−10%)=8000000; EIT=800000; VAT=480000; recipient gets 7200000 and payer cash outflow=8480000. Imported-service/intangible VAT creates no urban/education/local education surcharge base. If input VAT is actually deductible, economic royalty cost is 8000000, not the full cash total. This replaces the old internally inconsistent VAT gross-up and unsupported surcharge calculation ([STA 2017 No.37](https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html) §6; [2026 VAT Law](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html) arts. 10,15,17; [MOF/STA 2021 No.28](https://fgk.chinatax.gov.cn/zcfgk/c102416/c5194989/content.html)).

```oa-check
name: China2026 foreign royalty, payer bears EIT and VAT
inputs:
  usd_net: 1000000
  assumed_cny_per_usd: 7.20
  eit_rate: 0.10
  vat_rate: 0.06
steps:
  cny_net: usd_net * assumed_cny_per_usd
  vat_exclusive_eit_gross_base: cny_net / (1 - eit_rate)
  eit_withheld: vat_exclusive_eit_gross_base * eit_rate
  vat_withheld: vat_exclusive_eit_gross_base * vat_rate
  payer_cash: cny_net + eit_withheld + vat_withheld
expected:
  cny_net: 7200000
  vat_exclusive_eit_gross_base: 8000000
  eit_withheld: 800000
  vat_withheld: 480000
  payer_cash: 8480000
```

**Example 2: preserved cumulative wage scenario with actual deduction assumptions.** Assume 2026 January–May salary 150000, cumulative basic deduction 25000, actual allowable social/housing 15000 and actual eligible additional deductions 10000. The 10000 is an assumed verified aggregate, not the old unsupported 1000/month child/parent standard. Cumulative base 100000; tax 100000×10%−2520=7480; already withheld 4140, current withholding 3340 ([STA 2018 No.61 withholding measures](https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html) art. 6/table 1).

```oa-check
name: China2026 May cumulative resident wage withholding
inputs:
  cumulative_salary: 150000
  basic_deduction: 25000
  actual_social_housing: 15000
  actual_additional_deductions: 10000
  already_withheld: 4140
steps:
  cumulative_base: cumulative_salary - basic_deduction - actual_social_housing - actual_additional_deductions
  cumulative_tax: cumulative_base * 0.10 - 2520
  current_withholding: cumulative_tax - already_withheld
expected:
  cumulative_base: 100000
  cumulative_tax: 7480
  current_withholding: 3340
```

### Other original scenarios retained with their boundaries

**Hong Kong parent dividend.** The former 100000000 dividend,100% ownership and residence-certificate scenario remains a treaty-verification task. **If** the actual current instrument, beneficial ownership, holding period and other conditions independently establish 5%, withholding arithmetic is 5000000 and China net 95000000. At domestic 10%, it is 10000000 and 90000000. This conditional comparison does not verify the current Hong Kong treaty entitlement; no approximate HKD 102 million conversion or Hong Kong exemption/final 5% worldwide burden is asserted.

**Listed-share 5000dividend.** Retain the former acquisition 1 April 2025/distribution 15 June 2025/sale 20 June 2025 scenario: the holding is over 1 month and within 1 year, so the eligible No.101 tax is 5000×50%×20%=500. At distribution the company temporarily does **not** withhold; collection follows the sale, not a refund of a blanket 1000. With sale 10 May 2026 after a holding above 1 year, the specified temporary exemption gives zero. The case's 2025dates are historical facts, not a change of the 2026 Guide's scope ([Caishui 2015 No.101](https://www.chinatax.gov.cn/n810341/n810755/c1797427/content.html)).

## Ask the client first

- Who legally receives the payment: individual/company, tax residence, beneficial owner and actual establishment? Obtain actual evidence before classifying.
- What does the contract buy, where is the activity/consumption/property, and who bears EIT/VAT? Is the price net or VAT-inclusive? What are the payment/accrual and invoice dates?
- Which currency/conversion rule and central-parity date apply? Do property cost and prior instalments support the gain?
- Which treaty/protocol, shareholding/holding period and residence documents support a claim? Was the information report completed and evidence retained?
- For payroll, what are cumulative wages, eligible months, exemptions, actual deductions, prior withholding and the person's residence status? Is a special platform/other withholding measure applicable?
- Is the seller represented by an entrusted domestic VAT agent? Are payment vouchers and input-deduction/use conditions satisfied?
- Is this an original return, omission, authority notice, refund or indirect-transfer investigation? Obtain all dated records and notices.

## Sources

| Source | Official URL | Read on |
| --- | --- | --- |
| EIT Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286573.html | 2026-10-29 |
| EIT Regulations | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/qysds/200801/t286574.html | 2026-10-29 |
| IIT Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201809/t441789.html | 2026-10-29 |
| STA 2018 No.61 withholding measures | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/grsds/201812/t443216.html | 2026-10-29 |
| STA 2017 No.37 | https://www.chinatax.gov.cn/chinatax/n810341/n810765/n2511651/201710/c3289550/content.html | 2026-10-29 |
| Treaty measures 2019 No. 35 Arts. 3,7–9,11 | https://tianjin.chinatax.gov.cn/11200000000/0300/030004/03000418/20191024101530609.shtml | 2026-10-29 |
| STA 2018 No.9 beneficial-owner rules | https://fgk.chinatax.gov.cn/zcfgk/c100012/c5194781/content.html | 2026-10-29 |
| Caishui 2015 No.101 | https://www.chinatax.gov.cn/n810341/n810755/c1797427/content.html | 2026-10-29 |
| STA 2015 No.7 | https://www.chinatax.gov.cn/chinatax/n810341/n810765/n1465977/201502/c1676726/content.html | 2026-10-29 |
| MOF/STA 2021 No.28 | https://fgk.chinatax.gov.cn/zcfgk/c102416/c5194989/content.html | 2026-10-29 |
| Tax Collection Administration Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200609/t284229.html | 2026-10-29 |
| 2026 VAT Law | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202412/t474694.html | 2026-10-29 |
| 2026 VAT Implementation Regulations | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/202601/t478908.html | 2026-10-29 |

| Additional operative source | https://guangdong.chinatax.gov.cn/gdsw/fssw_nsrxt_kjxz/2025-10/09/content_b02be06c906e46bca00673beb9e7783a.shtml | 2026-10-29 |
| Additional operative source | https://shanghai.chinatax.gov.cn/zcfw/zcfgk/swzsgl/200402/t284445.html | 2026-10-29 |

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. A qualified professional in the relevant jurisdiction must review the work before filing, paying or taking a tax position.

**Not yet confirmed:** the exact current Hong Kong/Singapore/US/UK/Japan/Germany treaty rates and protocol/MLI holding-period conditions; Hong Kong/other destination-country taxation; indirect-transfer safe-harbour application to a particular restructuring; special equity/restricted-share treatment; general currency-control/remittance procedures; cross-period gross-up complications where the actual tax-bearing contract differs; Pillar Two effects; case-specific treaty-refund limitation periods and future electronic-form coordinates. These do not authorise the former blanket “when unsure, call it a royalty” or “withhold 20% then refund” defaults. Additional original topics retained as explicit unconfirmed/referral limits: Netherlands, France, South Korea, Australia, Canada, Luxembourg and Ireland treaty rates/conditions; guarantee-fee classification; digital services/cross-border ecommerce; private funds/QFLP/QDLP; FATCA referrals.

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
