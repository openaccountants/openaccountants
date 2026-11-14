---
name: japan-tax-optimization
description: >
  Use this Tier 2 reference when working through LEGAL tax minimization
  strategies for Japanese taxpayers: individuals, sole proprietors (kojin jigyō)
  and small corporations (KK/GK). Trigger on phrases like "reduce my tax Japan",
  "tax planning", "blue return", "ao-iro shinkoku", "furusato nozei", "iDeCo",
  "NISA", "sole proprietor vs corporation", "shakai hoken", "social insurance
  optimization", "consumption tax", or any question about legally minimizing
  Japanese income tax. Covers entity selection, blue return optimization,
  deductions, capital allowances, loss utilization, timing, consumption tax,
  social insurance and red lines, each with its condition and limit, for the
  2026 year, with filing through e-Tax. ALWAYS read this skill before giving
  Japanese tax optimization advice. It has no accountant sign-off and does not
  authorise filing, payment or a tax position.
version: 1.3
jurisdiction: JP
tax_year: 2026
tax_year_notes: "The 2026 year (令和8年分, filed in 2027), read at 6 November 2026. Some enacted 2027 and later changes are recorded, not all of them, and no later year is computed. The 2026 basic deduction was read in text in force from 1 December 2026. The announced food consumption tax cut is a proposal on the text read. No 令和9年度 tax reform outline had been published when the Ministry of Finance page was read on 5 November 2026."
last_updated: 2026-11-14
depends_on:
  - bookkeeping-workflow-base
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: tax-optimization
type: decision
---

# Japan Tax Optimization v1.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals resident in Japan (居住者) other than non-permanent residents (非永住者), sole proprietors (個人事業主) with business income, and owner-managers of a 株式会社 (KK) or 合同会社 (GK) with capital of JPY 100,000,000 or less that is not in a group tax sharing regime (通算法人). Currency is JPY only. The tax authority is the National Tax Agency (国税庁, NTA). Filing is through e-Tax (https://www.e-tax.nta.go.jp/), with individual returns prepared in the 確定申告書等作成コーナー.

**Period label: the 2026 year (令和8年分, filed in 2027), read at 6 November 2026.** Some enacted 2027 and later changes are recorded, not all of them, and no later year is computed. The 2026 basic deduction was read in text in force from 1 December 2026. The announced food consumption tax cut is a proposal on the text read. No 令和9年度 tax reform outline had been published when the Ministry of Finance page was read on 5 November 2026.

Primary legislation: 所得税法 (Income Tax Act), 法人税法 (Corporation Tax Act), 租税特別措置法 (措法), 地方税法 (Local Tax Act), 消費税法, 確定拠出年金法 and 小規模企業共済法. Translations of statutory terms are the author's, not official text.

### What this file is

This is a Tier 2 source-cited draft, pending review, with no accountant sign-off. The prior version named no reviewer, and this version names none. Every output must be reviewed and signed off by a qualified professional, such as a 税理士 (zeirishi) or equivalent licensed practitioner in Japan, before filing or acting on it.

**Each strategy here is a rule with its conditions, not a recommendation.** It becomes advice only when a qualified professional applies it to a named client's facts. Never tell a client that a step is right for them because this file lists it. State the condition, then what the facts show. Every comparison gives arithmetic and leaves the choice to the client and their 税理士.

These sibling guides own their figures. Where one differs from this file, check the primary source before relying on either:

- `jp-income-tax`: the income tax computation, its refusals, deadlines and penalties. This file follows it.
- `jp-estimated-tax`, `jp-etax-filing` and `jp-nonpermanent-resident`: prepayments, e-Tax steps and non-permanent residents.
- `jp-social-insurance` and `japan-payroll`: National Pension, NHI and payroll contributions.
- `jp-consumption-tax` and `japan-consumption-tax`: the consumption tax return.
- `jp-incorporation` and `japan-formation`: forming a company.
- `japan-bookkeeping`: books, charts of accounts and financial statements.
- `japan-transfer-pricing` and `japan-crypto-tax`: their own subjects.

### What the workflow base requires

This file depends on `bookkeeping-workflow-base`, which owns ledger work, its tiers, its question round and its outputs. This file is a planning reference and is not the base's country skill: that is `japan-bookkeeping`.

- **Refusal.** If a request needs a ledger, posting, adjustment or output file and `japan-bookkeeping` is not loaded, stop at base Step 1 and send exactly: "I need a country-specific bookkeeping skill loaded alongside this workflow base. Which jurisdiction are these accounts for?" Do no partial classification.
- **Operational hold.** A text search of `japan-bookkeeping` on 6 November 2026 found no conservative default slot or materiality threshold slot of the kind base Section 7 asks for. Until those are confirmed, do not produce ledger output from this file. Use it as a reference.
- **Question threshold:** JPY 0. No item is filtered on amount, because no text read sets a floor.
- **Order.** Questions come before any output: base Step 5.5 runs before Step 6. Whatever stays unanswered is Needs Input. Do not build a working paper with assumed answers first.

### Refusals

A refusal is a full stop. When a trigger applies, output the message verbatim and end. Do no partial planning. Where a trigger is only suspected, ask the question that resolves it. When a computation is asked for, refusals R-JP-1 to R-JP-10 in `jp-income-tax` also apply.

| Code | Trigger | Exact message |
| --- | --- | --- |
| R-OPT-1 | The client asks to hide income, alter a date or document, pay for work that was not done, or claim a private cost as a business cost | I cannot help with this. It would misstate the facts, which can bring heavy additional tax (重加算税). Please speak to a 税理士 about what the facts support. |
| R-OPT-2 | The person is, or may be, a non-resident (非居住者) or non-permanent resident (非永住者) | This file covers residents who are not non-permanent residents. Please refer this to a 税理士. |
| R-OPT-3 | A computed figure is asked for a year other than 2026 | This file computes the 2026 year only. Read the text in force for that year; the changes recorded here are not a complete list. |
| R-OPT-4 | A company comparison is asked for a company with capital above JPY 100,000,000, in a group tax sharing regime, or excluded by 法人税法 art. 66(5), such as one wholly owned by a company with capital of JPY 500,000,000 or more | The company rates here cover small independent companies only. Please refer this to a 税理士. |

### Rules for every answer

1. Ask the facts in 'Ask the client first' before any figure or comparison.
2. Give each strategy with its condition and its limit. A strategy with an unmet condition is not available. An unknown condition is Needs Input.
3. A proposal is not law. Never use a proposed rate. See 'Enactment position'.
4. Every comparison states what is in it and what is left out, above all social insurance, local rates, professional fees and the cost of taking money out of a company.
5. Label every computed figure 'estimated, not reviewed'.

### How to read the status words

- **Enacted** means the text was read in dated e-Gov consolidated law and is in force at the date shown.
- **Enacted, later start** means the text was read in dated e-Gov law for a later date.
- **Administrative** means an NTA or ministry page gives it. The law read does not print it, or it was not read.
- **Proposal** means a government announced it. It is not law on the text read.
- **Held** means not proved here.

### Defaults

A default stands only where the law read fixes the result of the missing fact.

| Situation | Treatment | Basis |
| --- | --- | --- |
| Blue approval unknown | Needs Input. Show both results, as Example 1 does | 所得税法 arts 143 to 147 |
| Blue tier conditions unproved, blue approval confirmed | JPY 100,000 stands, with the higher tier and its effect disclosed | 措法 art. 25-2(1) |
| Pension category or fund membership unknown | Needs Input. The limit depends on it | 確定拠出年金法施行令 art. 36 |
| Municipality unknown | Needs Input. Standard rates may appear only as a labelled stand-in | 地方税法 arts 35, 314-3 |
| NHI premium or company health rate unknown | Needs Input. Examples use labelled fixtures only | 国民健康保険法施行令 art. 29-7; `jp-social-insurance` |
| Business or private character unclear | Not deducted, and flagged | 所得税法 arts 37, 45 |
| Whether the donation recipient is a designated municipality unknown | Needs Input. Do not assume the special credit | 地方税法 arts 37-2(2), 314-7(2) |
| Consumption tax status unknown | Needs Input | 消費税法 arts 9, 9-2, 12-2, 12-3 |

## Rates, bands and thresholds

Label: the 2026 year (令和8年分, filed in 2027), read at 6 November 2026. All amounts are in yen. e-Gov text is the consolidated text at the dates stated in Sources.

### Reference facts

| Field | Value | Official source |
| --- | --- | --- |
| Tax year | Calendar year for individuals. A company's year is its own business year | 所得税法 art. 120(1): https://laws.e-gov.go.jp/law/340AC0000000033 |
| Final return, 2026 year | 16 February to 15 March 2027 | NTA No. 2020: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2020.htm |
| Top marginal rate, 2026 | 55.945%: 45% × 1.021 + 10% standard inhabitant tax. Own arithmetic. Excludes 個人事業税 and any local rate above standard | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; 地方税法 arts 35, 314-3: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Consumption tax | 10% standard (2.2% local; national part computed as 7.8%); 8% reduced (1.76% local; national part computed as 6.24%) for the items the law names | 消費税法 art. 29: https://laws.e-gov.go.jp/law/363AC0000000108; NTA No. 6101: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6101.htm |

### National income tax

`jp-income-tax` owns this table. Tax = taxable income × rate − deduction amount, on taxable income rounded down to JPY 1,000.

| Taxable income (JPY) | Rate | Deduction amount | Tax year | Official source |
| --- | --- | --- | --- | --- |
| Up to 1,950,000 | 5% | 0 | 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 1,950,000, up to 3,300,000 | 10% | 97,500 | 2026 | same |
| Over 3,300,000, up to 6,950,000 | 20% | 427,500 | 2026 | same |
| Over 6,950,000, up to 9,000,000 | 23% | 636,000 | 2026 | same |
| Over 9,000,000, up to 18,000,000 | 33% | 1,536,000 | 2026 | same |
| Over 18,000,000, up to 40,000,000 | 40% | 2,796,000 | 2026 | same |
| Over 40,000,000 | 45% | 4,796,000 | 2026 | same |

### Surtaxes and enacted 2027 changes to individuals

| Item | Amount | Tax year | Status | Official source |
| --- | --- | --- | --- | --- |
| 復興特別所得税 (reconstruction surtax) | 2.1% of 基準所得税額, rounded down to JPY 1 | 2013 to 2026 | Enacted | 復興財確法 arts 9, 12, 13: https://laws.e-gov.go.jp/law/423AC0000000117 |
| 復興特別所得税 from 2027 | 1.1% of 基準所得税額 | 2027 to 2047 | Enacted, later start | 復興財確法 arts 9, 13 at 1 January 2027: https://laws.e-gov.go.jp/law/423AC0000000117 |
| 防衛特別所得税 (defence surtax) | 1% of 基準所得税額 | 2027 onward, 当分の間 | Enacted, later start | 防衛財確法 art. 5-9 at 1 January 2027: https://laws.e-gov.go.jp/law/505AC0000000069 |
| Very high income | The art. 41-19 threshold falls to JPY 165,000,000 and the rate is 30%, for 2027 onward. See R-JP-8 in `jp-income-tax` | 2027 onward | Enacted, later start | 措法 art. 41-19(1) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |

The 2 surtaxes from 2027 add to the same 2.1%, so the combined figure above does not change on the text read. The prior version's end date of 2037 is the older rule.

### Basic deduction

`jp-income-tax` owns the full table, including 2025 and the tiers above JPY 23,500,000.

| 合計所得金額 (JPY) | 2026 and 2027 | 2028 onward | Status | Official source |
| --- | --- | --- | --- | --- |
| Up to 4,890,000 | 1,040,000 | See `jp-income-tax`, which splits this band for 2028 | Enacted, read at 1 December 2026 | 所得税法 art. 86(1) with 措法 art. 41-16-2(1): https://laws.e-gov.go.jp/law/332AC0000000026 |
| Over 4,890,000, up to 6,550,000 | 670,000 | 620,000 | Enacted, read at 1 December 2026 | same |
| Over 6,550,000, up to 23,500,000 | 620,000 | 620,000 | Enacted, read at 1 December 2026 | 所得税法 art. 86(1): https://laws.e-gov.go.jp/law/340AC0000000033 |
| Inhabitant tax basic deduction | 430,000 where prior-year 合計所得金額 is up to 24,000,000 | Not checked | Enacted | 地方税法 arts 34, 314-2: https://laws.e-gov.go.jp/law/325AC0000000226 |

### Blue return special deduction

`jp-income-tax` owns the tests. The deduction is under 措法 art. 25-2, not Income Tax Act art. 65 as the prior version said.

| Tier | Amount | Tax year | Conditions | Official source |
| --- | --- | --- | --- | --- |
| Base | 10万円 | 2026 | Blue approval. The lesser of 10万円 or the income | 措法 art. 25-2(1): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 2072: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Middle | 550,000 | 2026 | Business, or real-estate income from a business-scale activity; not on the cash basis; 正規の簿記; balance sheet and profit and loss statement attached; return filed by the deadline | 措法 art. 25-2(3): https://laws.e-gov.go.jp/law/332AC0000000026 |
| Upper | 650,000 | 2026 | All Middle conditions, and either e-Tax transmission by the deadline or qualifying electronic books under 電子帳簿保存法 art. 8(4) | 措法 art. 25-2(4): https://laws.e-gov.go.jp/law/332AC0000000026 |
| White return | 0 | 2026 | No special deduction | 措法 art. 25-2 applies to blue filers only: https://laws.e-gov.go.jp/law/332AC0000000026 |
| 2027 upper | 650,000 | 2027 onward | 正規の簿記 and the statements, with e-Tax transmission by the deadline. The JPY 550,000 tier does not continue | 措法 art. 25-2(4) and (7) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |
| 2027 top | 750,000 | 2027 onward | The 650,000 conditions with electronic books and either limb of para. (5). See `jp-income-tax` | 措法 art. 25-2(5) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |
| 2027 base | 100,000 | 2027 onward | Not for a filer outside the cash basis whose 総収入金額 of business or real-estate income in the prior-prior year exceeds 10,000,000, unless para. (4) is met | 措法 art. 25-2(1) and (2) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |

### Retirement contribution limits

小規模企業共済 and iDeCo contributions are 小規模企業共済等掛金控除 (所得税法 art. 75), and 国民年金基金 contributions are social insurance premiums (art. 74(2)(5)). In each case the full amount paid in the year comes off income. The prior version's JPY 84,000 a month for 小規模企業共済 was wrong: the Act's limit is JPY 70,000 a month.

| Scheme and person | Monthly limit | Period | Conditions | Official source |
| --- | --- | --- | --- | --- |
| 小規模企業共済 | 1,000 to 70,000, in steps of 500. So at most 840,000 a year (computed: 70,000 x 12) | Read at 5 November 2026 | A 小規模企業者 under the next row | 小規模企業共済法 art. 4(2): https://laws.e-gov.go.jp/law/340AC0000000102; 中小機構: https://www.smrj.go.jp/kyosai/skyosai/features/index.html |
| Who is a 小規模企業者 | By the main business: 20 or fewer regular employees in 工業, 鉱業, 運送業 and other businesses outside the next 2 groups; 5 or fewer in 商業 or サービス業; 20 or fewer in 宿泊業 or 娯楽業 | Read at 5 November 2026 | The individual who runs the business (items 1 to 3), an individual taking part in running it (item 4), an officer of a company on the same counts (items 5 to 7), or an officer of a 企業組合, 協業組合 or other body the order names (item 8) | 小規模企業共済法 art. 2(1): https://laws.e-gov.go.jp/law/340AC0000000102; 小規模企業共済法施行令 art. 1: https://laws.e-gov.go.jp/law/340CO0000000185 |
| iDeCo, category 1 (自営業者等) or 任意加入 | 68,000, less any 付加保険料 or 国民年金基金 contribution paid for that month, not below nil. Nil for a month with no National Pension premium paid | To 30 November 2026 | Excludes a person exempt from National Pension premiums, in full or in part (確定拠出年金法 art. 62(1)(1)). Tested at each month-end | 確定拠出年金法施行令 art. 36 item 1 at 5 November 2026: https://laws.e-gov.go.jp/law/413CO0000000248 |
| iDeCo, category 1 or 任意加入 | 75,000, on the same reductions | From 1 December 2026 | As above. Enacted by 政令第442号 of 2025 | 確定拠出年金法施行令 art. 36 item 1 at 1 December 2026: https://laws.e-gov.go.jp/law/413CO0000000248 |
| iDeCo, category 2 (employee), no company plan | 23,000 | To 30 November 2026 | Item 2 | 確定拠出年金法施行令 art. 36 at 5 November 2026: https://laws.e-gov.go.jp/law/413CO0000000248 |
| iDeCo, category 2, with 企業型 DC or another plan | 20,000. Reduced by the excess over 35,000 of the 事業主掛金 (item 3), the 他制度掛金相当額 with any 事業主掛金 (item 4), or the 共済掛金相当額 (item 5). Items 4 and 5 not below nil | To 30 November 2026 | Items 3 to 5 | same |
| iDeCo, category 2, no company plan | 62,000 | From 1 December 2026 | Item 2. So the prior version's JPY 23,000 stops for this group | 確定拠出年金法施行令 art. 36 at 1 December 2026: https://laws.e-gov.go.jp/law/413CO0000000248 |
| iDeCo, category 2, with 企業型 DC or another plan | 62,000 less the 事業主掛金 (item 3), the 他制度掛金相当額 with any 事業主掛金 (item 4), or the 共済掛金相当額 (item 5). Items 4 and 5 not below nil | From 1 December 2026 | Items 3 to 5 | same |
| iDeCo, category 3 (dependent spouse) | 23,000 | Both periods | Art. 36 item 6 in both texts | same |
| iDeCo, 第五号加入者 (60 to under 70, on art. 62(1)(5) conditions) | 62,000, with the same reductions for company plans | From 1 December 2026 | Items 7 to 10. A person who has or had an iDeCo old-age benefit right, or has been awarded 老齢基礎年金, cannot join (art. 62(2)) | 確定拠出年金法 art. 62 at 1 December 2026: https://laws.e-gov.go.jp/law/413AC0000000088 |
| 国民年金基金 | 68,000 | To 30 November 2026 | Within the category 1 iDeCo limit. Special cases in art. 35 of the order not reproduced | 国民年金基金令 art. 34 at 5 November 2026: https://laws.e-gov.go.jp/law/402CO0000000304 |
| 国民年金基金 | 75,000 | From 1 December 2026 | As above. A fund member cannot pay 付加保険料 (国民年金法 art. 87-2(1)) | 国民年金基金令 art. 34 at 1 December 2026: https://laws.e-gov.go.jp/law/402CO0000000304 |

The Ministry of Health, Labour and Welfare's iDeCo page still showed JPY 68,000 and JPY 23,000 when read, which is right for dates to 30 November 2026.

### Furusato nozei

| Item | Amount | Period | Status | Official source |
| --- | --- | --- | --- | --- |
| Income tax side | 寄附金控除 of the donation less JPY 2,000. It is an income deduction, not a credit. Donations count up to 40% of 総所得金額等 | 2026 | Enacted | 所得税法 art. 78(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1155: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1155.htm |
| Inhabitant tax, basic credit | (Donations, up to 30% of 総所得金額等, less 2,000) × 10% (prefectural 4% and municipal 6%, or 2% and 8% in a designated city) | 2026 donations | Enacted | 地方税法 arts 37-2(1), 314-7(1): https://laws.e-gov.go.jp/law/325AC0000000226 |
| Inhabitant tax, special credit | (Donation to a designated municipality less 2,000) × the ratio below | 2026 donations | Enacted | 地方税法 arts 37-2(11), 314-7(11): https://laws.e-gov.go.jp/law/325AC0000000226 |
| Ratio, with surtax | 84.895%, 79.79%, 69.58%, 66.517%, 56.307%, 49.16% and 44.055% by band: 90% less the marginal rate × 1.021. 85% to 45% is the ratio before the surtax rule. Items (2) and (3) set a separate ratio where the band test falls below nil or there is no 課税総所得金額; those cases are not reproduced | 2026 donations | Enacted | 地方税法 附則 art. 5-6: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Band test | Local 課税総所得金額 less the art. 37 第一号イ amount and (the national basic deduction − 480,000, not below nil). The second term is new in the text at 5 November 2026 | 2026 donations | Enacted | 地方税法 art. 37-2(11)(1): https://laws.e-gov.go.jp/law/325AC0000000226 |
| Special credit cap | 20% of 所得割 after arts 35 and 37 (arts 314-3 and 314-6 for the municipal part). Above this, the excess is not credited | Fiscal years to 令和9年度, so donations to 2026 | Enacted | 地方税法 arts 37-2(11), 314-7(11) at 5 November 2026: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Special credit cap, added limit | The lower of that 20% and a fixed amount: prefectural 772,000 (386,000 in a designated city), municipal 1,158,000 (1,544,000 in a designated city). Total 1,930,000 | 令和10年度 onward, so donations from 2027 | Enacted, later start | 地方税法 arts 37-2(11), 314-7(11) at 1 January 2027 and 令和8年法律第2号 附則 arts 1(2), 3 and 11: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Return gifts | Procurement cost of each gift up to 30% of the donation, and a local product meeting the Minister's standard. These test the municipality, not the donor | Read at 5 November 2026 | Enacted | 地方税法 art. 37-2(2)(3) and (4): https://laws.e-gov.go.jp/law/325AC0000000226 |
| Use of funds test on municipalities | Donations net of fundraising costs at least 60% of donations. For a designation period starting from the start date of 令和8年法律第2号 附則 art. 1 item 1 to 30 September 2027, 52.5%; 1 October 2027 to 30 September 2028, 55%; 1 October 2028 to 30 September 2029, 57.5% | Read at 5 November 2026 | Enacted | 地方税法 art. 37-2(2)(2) and 令和8年法律第2号 附則 art. 3: https://laws.e-gov.go.jp/law/325AC0000000226 |
| One-Stop | Up to 5 municipalities. Only for a person not expected to need a final return or a local return for other reasons. See 'Furusato nozei' under The base | 当分の間 | Enacted | 地方税法 附則 art. 7: https://laws.e-gov.go.jp/law/325AC0000000226 |

### Other deductions

| Deduction | Amount | Conditions | Tax year | Official source |
| --- | --- | --- | --- | --- |
| Medical (医療費控除) | Paid in the year, net of reimbursement, above the lesser of 10万円 or 5% of 総所得金額等; maximum 200万円 | For the taxpayer or a relative in the same household (生計を一にする). Paid, not merely incurred | 2026 | 所得税法 art. 73: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1120: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1120.htm |
| Self-medication (セルフメディケーション) | An alternative to the medical deduction; the taxpayer takes one or the other and cannot switch later | Payments to 31 December 2026 on the text read, with a health check or similar. Amounts not reproduced | 2026 | 措法 art. 41-17: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1129: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1129.htm |
| Social insurance (社会保険料控除) | Full amount paid, no cap | Includes amounts for a spouse or relative in the same household | 2026 | 所得税法 art. 74: https://laws.e-gov.go.jp/law/340AC0000000033 |
| Life insurance (生命保険料控除) | 40,000 for each of 3 limbs; 120,000 in total. New life limb 60,000 for 2026 and 2027 for a filer with a dependant under 23. Inhabitant tax total 70,000 | Limb detail with `jp-income-tax` | 2026 | 所得税法 art. 76: https://laws.e-gov.go.jp/law/340AC0000000033; 措法 art. 41-15-5(1): https://laws.e-gov.go.jp/law/332AC0000000026; 地方税法 art. 34: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Earthquake insurance (地震保険料控除) | Up to 50,000. Inhabitant tax up to 25,000 | A home usually lived in, or household goods, of the taxpayer or a relative in the same household | 2026 | 所得税法 art. 77: https://laws.e-gov.go.jp/law/340AC0000000033; 地方税法 art. 34: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Casualty loss (雑損控除) | The loss net of insurance, less: (1) 10% of 総所得金額, 退職所得金額 and 山林所得金額 where 災害関連支出 is 50,000 or less; (2) where it is above 50,000, the lower of that 10% and the loss less the 災害関連支出 above 50,000; (3) where the whole loss is 災害関連支出, the lower of 50,000 and that 10% | Disaster, theft or embezzlement only, on assets of the taxpayer or a named relative in the same household. Not assets in art. 62(1) or art. 70(3) | 2026 | 所得税法 art. 72: https://laws.e-gov.go.jp/law/340AC0000000033 |
| Spouse (配偶者控除) | 38万円 (48万円 if 70 or over) with taxpayer's 合計所得金額 up to 900万円; less above; nil above 1,000万円 | Spouse's 合計所得金額 up to 62万円 for 2026. The prior version's 48万円 is the limit for years to 2024 | 2026 | 所得税法 art. 83: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1191: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1191.htm |
| Dependant (扶養控除) | 38万円; 63万円 for those aged 19 to 22; more for those 70 or over | Age 16 or over. 合計所得金額 up to 62万円 for 2026 | 2026 | 所得税法 art. 84: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1180: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1180.htm |
| Home loan credit (住宅借入金等特別控除) | 0.7% of the year-end balance up to the 借入限度額, a credit against tax, rounded down to JPY 100. For move-in from 2026 to 2030, 20,000,000 under art. 41(3)(3), and 20,000,000 to 45,000,000 for a 認定住宅等 by type under art. 41(7). Later paragraphs, including those for small homes with a 10,000,000 income test, were not read in full | Move-in by 31 December 2030; within 6 months; repayment over 10 years or more; 合計所得金額 up to 20,000,000 in the year. 10 years generally. For a 認定住宅等, 13 years with move-in in 2026 to 2030, or in 2022 to 2025 where new or bought resold after renovation (買取再販) | 2026 | 措法 art. 41(1), (2), (3), (4), (6) and (7) at 5 November 2026: https://laws.e-gov.go.jp/law/332AC0000000026 |

The limits in the home loan row depend on facts this file does not test. The NTA page read, No. 1213, covers older 認定住宅 cases, so the row rests on the Act. Do not state a limit for a client without reading art. 41 for that house and year.

### Asset expensing

`jp-income-tax` owns the sole proprietor rows.

| Item | Amount | Conditions | Tax year | Official source |
| --- | --- | --- | --- | --- |
| Immediate expense | Cost under 100,000, or useful life under 1 year | Not assets lent other than as a main business. Rule is in the order, not the Act | 2026 | 所得税法施行令 art. 138: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Pool over 3 years (一括償却資産) | Cost under 200,000; one-third a year | Schedule attached | 2026 | 所得税法施行令 art. 139: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Small business, sole proprietor, acquired to 31 March 2026 | Under 300,000 each; 3,000,000 a year in total | Blue filer who is a 中小事業者 with 500 or fewer regular employees. The prior version's 300 employees has no basis | 2026 | 措法 art. 28-2 at 31 December 2025: https://laws.e-gov.go.jp/law/332AC0000000026; 措法施行令 art. 18-5(1): https://laws.e-gov.go.jp/law/332CO0000000043 |
| Small business, sole proprietor, acquired 1 April 2026 to 31 March 2029 | Under 400,000 each; 3,000,000 a year in total | Blue filer, 400 or fewer regular employees; acquired and put to use in the business; schedule attached | 2026 | 措法 art. 28-2 at 5 November 2026: https://laws.e-gov.go.jp/law/332AC0000000026 |
| Small company | Under 400,000 each to 31 March 2029 | Blue filer; 中小企業者等 in the terms of art. 67-5. Annual total not read | 2026 | 措法 art. 67-5: https://laws.e-gov.go.jp/law/332AC0000000026 |

### Useful lives

| Asset | Useful life | Official source |
| --- | --- | --- |
| Personal computer, not a server | 4 years; other computers 5 | 耐用年数省令 別表第一: https://laws.e-gov.go.jp/law/340M50000040015 |
| Office furniture | 8 years, or 15 if mainly metal | same |
| Ordinary motor vehicle; light vehicle up to 0.66 litres | 6 years; 4 years | same |
| Software | 5 years; 3 for a master for copying and sale | 耐用年数省令 別表第三: https://laws.e-gov.go.jp/law/340M50000040015 |
| Office building, reinforced concrete | 50 years | 耐用年数省令 別表第一: https://laws.e-gov.go.jp/law/340M50000040015 |
| Office building, metal frame | 38 years over 4 mm; 30 years over 3 mm up to 4 mm; 22 years at 3 mm or less | same |

The prior version's 'steel-frame 34 to 47 years' mixes different uses and structures. Use the row for the actual structure and use.

### Company tax layers

For a company outside refusal R-OPT-4. Figures are standard rates, and a prefecture or municipality may charge more. They are for business years starting in the period shown.

| Layer | Amount | Period | Status | Official source |
| --- | --- | --- | --- | --- |
| 法人税, income up to 年800万円 | 15% (17% where the year's income exceeds 10億円). Not for a 適用除外事業者 or 通算法人 | Years starting to 31 March 2027 | Enacted | 措法 art. 42-3-2(1): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 5759: https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5759.htm |
| 法人税, income up to 8,000,000 a year, after that period | 19% | Years starting from 1 April 2027 on the text read | Enacted | 法人税法 art. 66(2): https://laws.e-gov.go.jp/law/340AC0000000034 |
| 法人税, income above 8,000,000 | 23.2% | Current | Enacted | 法人税法 art. 66(1): https://laws.e-gov.go.jp/law/340AC0000000034 |
| 地方法人税 | 10.3% of 法人税 | Current | Enacted | 地方法人税法 art. 10(1): https://laws.e-gov.go.jp/law/426AC0000000011 |
| 防衛特別法人税 | 4% of (基準法人税額 − 5,000,000 a year). Nil where 法人税 is 5,000,000 or less | Years starting from 1 April 2026 | Enacted | 防衛財確法 arts 11, 13, 14: https://laws.e-gov.go.jp/law/505AC0000000069 |
| 法人住民税, 法人税割 | 1% prefectural and 6% municipal of 法人税, standard | Current | Enacted | 地方税法 arts 51(1), 314-4(1): https://laws.e-gov.go.jp/law/325AC0000000226 |
| 法人住民税, 均等割 | 20,000 prefectural and 50,000 municipal, standard, where 資本金等 is up to 10,000,000 and municipal employees are 50 or fewer. Payable even with no profit, on the plain text | Current | Enacted | 地方税法 arts 52(1), 312(1): https://laws.e-gov.go.jp/law/325AC0000000226 |
| 法人事業税 | 3.5% to 4,000,000; 5.3% to 8,000,000; 7% above, standard | Current | Enacted | 地方税法 art. 72-24-7(1)(3): https://laws.e-gov.go.jp/law/325AC0000000226 |
| 特別法人事業税 | 37% of 基準法人所得割額 | Current | Enacted | 特別法人事業税及び特別法人事業譲与税に関する法律 art. 7(3): https://laws.e-gov.go.jp/law/431AC0000000004 |

On income up to JPY 4,000,000 the layers add to 22.39% before any deduction for the business taxes: 15% × 1.173 + 3.5% × 1.37. That is own arithmetic at standard rates, not a published rate. The prior version's 'effective 34 to 35%' for small companies has no support: 34.62% is the Ministry of Finance's national and local rate for 2014, and its current figure is 29.74%, or 30.64% where the defence tax applies, as a rate of general application at standard local rates. Neither is a small company's rate.

### Consumption tax

`jp-consumption-tax` and `japan-consumption-tax` own these.

| Item | Amount | Conditions | Status | Official source |
| --- | --- | --- | --- | --- |
| Exemption | Taxable sales of 10,000,000 or less in the base period (prior-prior year for an individual) | Not where specified-period sales exceed 10,000,000 (art. 9-2, payroll alternative), or the business has registered or elected | Enacted | 消費税法 arts 9, 9-2: https://laws.e-gov.go.jp/law/363AC0000000108 |
| New company | Exempt while it has no base period, if capital at the start of the year is under 10,000,000 | Not at 10,000,000 or more (art. 12-2). Not where a person with over 50% control has base-period-equivalent sales over 500,000,000 (art. 12-3). Art. 9-2 and registration also end it | Enacted | 消費税法 arts 12-2, 12-3: https://laws.e-gov.go.jp/law/363AC0000000108 |
| Simplified method (簡易課税) | Deemed purchase ratios of 90%, 80%, 70%, 60%, 50% and 40% by business type | Base-period sales of 5,000万円 or less; election by the day before the period; generally kept for 2 years | Enacted | 消費税法 art. 37: https://laws.e-gov.go.jp/law/363AC0000000108; 消費税法施行令 art. 57: https://laws.e-gov.go.jp/law/363CO0000000360; NTA No. 6505: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6505.htm |
| 2割特例 | Tax payable = output tax × 2割 (one fifth) | Taxable periods including any day from 1 October 2023 to 30 September 2026, for a business that became taxable only by registering. Base-period and specified-period sales tests apply | Administrative, on NTA pages read | NTA No. 6498: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm |
| 3割特例 | Tax payable = output tax × 30% | Sole proprietors only, 2027 and 2028 periods. Base-period sales of 1,000万円 or less (2025 for 2027; 2026 for 2028). Q&A 問115-2 excludes: a non-resident business without a permanent establishment; base-period sales above 1,000万円; a period caught by art. 9-2; a period taxable under arts 10 to 12; art. 9(7) adjusted fixed assets; art. 12-4 high-value assets; and a shortened period | Administrative, on NTA pages read | NTA invoice-system review page: https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm; 問115-2: https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/qa/115-2.pdf |
| Purchases from unregistered suppliers | 80% credit to 30 September 2026; 70% to 30 September 2028; 50% to 30 September 2030; 30% to 30 September 2031 | Per supplier, the 70%, 50% and 30% rules stop above 1億円 a year, for taxable periods starting from 1 October 2026 | Enacted, read as the 附則 printed in 消費税法 and on the NTA page | 消費税法 printed 附則 of 平成28年法律第15号: https://laws.e-gov.go.jp/law/363AC0000000108; NTA review page: https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm |
| Food rate from 1 April 2027 | 1% on food for 2 years to 31 March 2029 | Never use. The NTA and Ministry of Finance page says its content assumes a bill still to be submitted and passed. 消費税法 art. 29 at 1 April 2027 still prints the current reduced national rate | Proposal | NTA special page: https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/zeiritsuhikisage.htm |

### Social insurance

`jp-social-insurance` and `japan-payroll` own these. They are here because a comparison cannot be read without them.

| Item | Amount | Period | Official source |
| --- | --- | --- | --- |
| NHI cap (per household, standard order limit) | 1,090,000: 660,000 + 260,000 + 170,000 | Fiscal 2025 | 国民健康保険法施行令 art. 29-7 at 31 December 2025: https://laws.e-gov.go.jp/law/333CO0000000362 |
| NHI cap | 1,130,000: 670,000 + 260,000 + 170,000 + 30,000 for the child support levy | Fiscal 2026 | 国民健康保険法施行令 art. 29-7 at 5 November 2026: https://laws.e-gov.go.jp/law/333CO0000000362 |
| National Pension | 17,920 a month | Fiscal 2026 | 日本年金機構: https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html |
| 付加保険料 | 400 a month | Current | 国民年金法 art. 87-2(1): https://laws.e-gov.go.jp/law/334AC0000000141 |
| Employees' pension (厚生年金) rate | 18.3%, split between employer and employee | Current | 厚生年金保険法 art. 81(4): https://laws.e-gov.go.jp/law/329AC0000000115 |
| Employees' pension, cap on standard monthly remuneration | 65万円 now; 68万円 from September 2027, 71万円 from September 2028, 75万円 from September 2029 | Stated dates | Ministry of Health, Labour and Welfare: https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000147284_00024.html |
| Health insurance, cap on standard monthly remuneration | 1,390,000, grade 50 | Current | 健康保険法 art. 40(1): https://laws.e-gov.go.jp/law/211AC0000000070 |

Health insurance rate: not given in this table. Each insurer sets it, and for 協会けんぽ it varies by prefecture; it includes 子ども・子育て支援金 and, for ages 40 to 64, long-term care (健康保険法 arts 160, 160-2: https://laws.e-gov.go.jp/law/211AC0000000070). No rate was read, so it is listed under Not yet confirmed.

The prior version said health insurance has no cap after JPY 1,390,000. It is the reverse: JPY 1,390,000 is the cap. Its '~30%' is unproved and is not used. The 厚生年金保険法 table in art. 20 at 5 November 2026 stops at JPY 620,000, and the JPY 650,000 grade comes from the ministry page; the order that adds it was not read.

### Retirement and investment accounts

| Vehicle | Rule | Period | Official source |
| --- | --- | --- | --- |
| NISA, growth limb | 2,400,000 a year; within 18,000,000 lifetime, of which 12,000,000 at most in this limb | Current | 措法 art. 37-14(5): https://laws.e-gov.go.jp/law/332AC0000000026 |
| NISA, 積立 (tsumitate) limb | 1,200,000 a year, within the 18,000,000 | Current | same |
| NISA holder and losses | Aged 18 or over on 1 January of the year; resident or non-resident with a permanent establishment. A loss inside counts as nil (art. 37-14(2)), so no offset or carry-forward (NTA No. 1474 note 3) | Current | same |
| NISA for minors | An under-18 account from 1 January 2027, with an annual limit of 600,000 in the tsumitate limb. Other limits not read | From 1 January 2027 | 措法 art. 37-14 at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |
| Listed securities | 15% national + 5% inhabitant, separately taxed; with 2.1% surtax on the national part, 20.315% in all (computed: 15% x 1.021 + 5%) | Current | 措法 arts 8-4, 37-11: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1463: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1463.htm |
| Dividend from a company the owner controls | Withholding 20% (20.42% with surtax in 2026). Aggregated with other income, with 配当控除 of 10% of the dividend where 課税総所得金額 is 10,000,000 or less; above that, 5% on the part of the dividend within the excess (art. 92(1)(3)). A payment up to 100,000 × months ÷ 12 from one payer may be left off the return (措法 art. 8-5(1)(1)), and then it earns no credit. Local 配当控除 not read | Current | 所得税法 arts 92, 182(2): https://laws.e-gov.go.jp/law/340AC0000000033; 措法 art. 8-5: https://laws.e-gov.go.jp/law/332AC0000000026 |

### Enactment position

- **Law for 2026.** 所得税法, 租税特別措置法 and related Acts at the dates read, including 所得税法等の一部を改正する法律 (令和8年法律第12号) as consolidated. That Act was not read as a separate document (`jp-income-tax`, Enactment position).
- **Local tax.** 地方税法 as amended by 令和8年法律第2号, read as consolidated, with that Act's 附則 as printed in e-Gov. The JPY 1,930,000 cap comes from there.
- **iDeCo.** 政令第442号 of 2025 under 令和7年法律第74号, in force on 1 December 2026, read as consolidated.
- **Consumption tax on food.** A Cabinet outline of 15 September 2026 and an NTA and Ministry of Finance page describe a 2-year rate of 1%. The page says its content assumes a bill is submitted and passed. Some NTA Tax Answers print it without that condition. Consolidated 消費税法 at 1 April 2027 shows no change. A search for an enacted Act was not complete: the Ministry's bills pages tried returned 404. So it is a proposal here and is not used.
- **Outlines.** A 税制改正大綱 is a proposal. No figure here rests on one. No proposal for a later year is used.
- **Practice.** An NTA Tax Answer or ministry page is administrative text. Where a row rests on one, the row says so.

## The base

Each block gives the rule, the condition and the limit. None is a recommendation. Where a statement is an inference from text read, it says so.

### Sole proprietor or company

- **Sole proprietor.** Business income is taxed at progressive rates, with the blue return deduction if its conditions are met. Health cover is NHI, and pension is National Pension (with a fund or iDeCo option). 個人事業税 falls on business income above JPY 2,900,000 (地方税法 art. 72-49-14) at 5% for most listed businesses, 4% for the second class and 3% to 5% in the third class, or nil for a business not listed (art. 72-49-17). Consulting (コンサルタント業) is a listed third-class business at 5%; whether a given activity is listed is a question of fact.
- **Company.** Profit is taxed under the layers above. The owner's salary is deductible only inside the rules below. The owner and company generally join shakai hoken, with an employer share and an employee share. Money taken out as a dividend is not deductible to the company (法人税法 art. 22(5)) and is taxed again on the owner.
- **The prior version's rule of thumb.** 'Generally beneficial above JPY 8 to 10 million' and 'usually superior below JPY 5 million' have no source and are not rules of law. Its 'advantage appears at about JPY 12 to 15 million' is held too. The result turns on the facts listed in Example 3. Work it through, and do not quote a threshold. `jp-incorporation` prints a breakeven near JPY 8,000,000 with its own assumptions; it is not read here as law.
- **New company and consumption tax.** Exemption in the first years is not automatic. See the 'New company' row. The prior version's 'capital of JPY 10 million or less' was wrong at the limit: capital of exactly JPY 10,000,000 falls under art. 12-2. In the second year the specified-period test in art. 9-2 can end the exemption. Registering as an invoice issuer ends it too.
- **Limit on structure.** Moving a business into a company to change who bears tax must be real. The company must own the contracts, bear the costs and pay under the rules below. 所得税法 art. 157 and 法人税法 art. 132 let the tax office disregard an act or calculation of a 同族会社 that would unfairly reduce tax.

### Salary, dividend or retained profit

This is arithmetic, not a recommendation. Four outcomes differ:

1. **Salary** is deductible to the company inside art. 34, bears shakai hoken on both sides up to the caps, and gets the employment income deduction.
2. **Dividend** is paid from after-tax profit, is not 報酬 for health insurance where it is not paid for work (健康保険法 art. 3(5) defines 報酬 as what is received for labour; this is an inference from the definition), and is taxed on the owner as above.
3. **Retained profit** bears company tax only for now. It is not the owner's money. Compare it only with its exit cost stated.
4. **Very low salary.** The prior version said this triggers NTA scrutiny. No text read says so. Art. 34(2) reaches pay that is too high. A low salary also reduces pension and sickness benefits: state that alongside the premium saved.

The prior version advised setting salary 'to minimise combined' cost. This file gives the method instead: compute each candidate salary with Example 3's steps, list what is left out, and leave the choice to the client and their 税理士.

### Family salary

- **Blue.** Salary to a family employee (青色事業専従者給与) is deductible at the notified amount where it is reasonable for the work. The relative must be in the same household (生計を一にする, not only living together), aged 15 or over at year-end, and working mainly in the business for more than 6 months of the year, or for more than half the possible period where the business did not run all year, or the relative could not work all year because of death, long illness, marriage or similar reason. Time as a student or in another occupation does not count unless it leaves the relative free to do the work (所得税法施行令 art. 165(2)). Notify by 15 March of the first year, or within 2 months where the business starts on or after 16 January (所得税法 art. 57(1) and (2); 所得税法施行令 art. 165(1)).
- **White.** The deduction for each family employee is the lesser of JPY 860,000 for a spouse or JPY 500,000 for another relative, and income before this rule ÷ (family employees + 1) (art. 57(3)). The return must state it (art. 57(5)).
- **Effect.** A relative paid this way is not a spouse or dependant for those deductions (art. 2(1)(33) and (34)). So compare both ways. It shifts income only if the work is real.
- **Limit.** Payment beyond what the work justifies is not deductible. A relative in the household who is paid outside art. 57 is not deductible at all (art. 56).

### Director pay

Under 法人税法 art. 34(1), pay that fits none of the 3 classes below is not deductible. Art. 34(1) leaves out retirement pay that is not 業績連動給与, pay for employee duties of a 使用人兼務役員, and pay under art. 34(3). The prior version said pay must be set at the start of the year. That is too narrow:

- **定期同額給与.** Paid at intervals of 1 month or less, in the same amount in each period (art. 34(1)(1)). Same after tax counts (法人税法施行令 art. 69(2)).
- **Permitted changes.** A change within 3 months of the start of the accounting period; a change for a change of position or duties or similar unavoidable reason; or a reduction for a marked worsening of the business (art. 69(1)(1)イ, ロ and ハ). Each period between changes must be level.
- **事前確定届出給与.** A fixed amount at a fixed time (art. 34(1)(2)), with a notification. NTA No. 5211 gives the date: generally the earlier of 1 month after the resolution (or the start of duties, if later) and 4 months after the start of the accounting period, or 2 months after incorporation for a new company's first duties. The Act does not need a notification for cash pay from a company that is not a 同族会社 to an officer with no 定期給与 (art. 34(1)(2)イ). Share rules are not reproduced. Pay that departs from the notice is outside the class on the plain text.
- **業績連動給与.** Art. 34(1)(3) needs an objective formula, a remuneration committee process and disclosure, and is closed to a 同族会社 unless a company that is not a 同族会社 wholly controls it. For a typical owner-managed company it is not available.
- **Excess.** The part above a reasonable amount is not deductible (art. 34(2)). The order tests duties, the company's profit, staff pay and pay at similar companies, and any ceiling in the articles or a shareholder resolution (法人税法施行令 art. 70(1)).
- **Disguised pay.** Pay accounted for by concealment or false entry is not deductible (art. 34(3)), and economic benefits count as pay (art. 34(4)).

### Deductions most people miss

The table above gives amounts. Conditions that decide whether a planning step works:

- **Blue tier.** A paper return can reach JPY 550,000 for 2026, and only e-Tax transmission or qualifying electronic books reach JPY 650,000. Paper filing loses this for 2027: the JPY 550,000 tier does not continue.
- **Medical.** Payment in the year decides (NTA No. 1120). The prior version's floor is right in effect, but it omitted the JPY 2,000,000 cap on the deduction. Only costs named in art. 73(2) and the order count. Reimbursement reduces it.
- **Social insurance.** Premiums paid for a spouse or relative in the same household count.
- **Cash cost.** Contributions to iDeCo and 小規模企業共済 lock up cash. Compare the tax saved with the money tied up.

### Furusato nozei

The prior version called this a credit on income and residence tax. It is an income deduction on the national side and a credit on the local side.

- **The JPY 2,000 result holds only within the cap.** Above the special credit cap the excess is a donation with no matching credit. Example 4 shows the arithmetic. The prior version's 'no penalty, but non-refundable' stays true.
- **The cap moves with everything else.** Each other deduction lowers 所得割 and with it the cap. So settle iDeCo, 小規模企業共済 and insurance figures first. No simulator is a source: the 所得割 on the actual assessment decides, and the 総務省 page warns that a municipality may be unable to state the limit.
- **Timing.** The 2026 result needs money paid in 2026. For 2026 donations, the fiscal 2027 inhabitant tax takes the credit. For donations from 2027, the JPY 1,930,000 limit also applies.
- **One-Stop does not suit a sole proprietor.** It is for a person not expected to have to file under 所得税法 art. 120(1), or expected to fall within art. 121, with 5 or fewer authorities expected (附則 art. 7(1) and (2)). Requests count as never made if the person leaves art. 121, files a local return, ends up with more than 5 authorities, or (for that request) the municipality differs (附則 art. 7(6)). NTA No. 1155 says filing a final return ends it. A sole proprietor who must file enters every donation on the return.
- **The recipient.** Only a municipality designated by the Minister at the time of donation counts for the special credit (art. 37-2(9)). A donation is outside art. 37-2(1)(1) where the donor gets exclusive use of a facility it funds or another special benefit. How a return gift is taxed in the donor's hands was not read: held.

### Depreciation

- **Method.** For an individual with no election the statutory method is straight-line (定額法) (所得税法 art. 49(1); 所得税法施行令 art. 125). Declining balance (定率法) needs an election (NTA No. 2100). The prior version's default was wrong for individuals. For a company with no election, assets acquired from 1 April 2007 in 法人税法施行令 art. 48-2(1)(1)イ and (2), such as machinery and vehicles, take declining balance (art. 53(2)イ).
- **Buildings.** Buildings, building fittings and structures acquired from 1 April 2016 are straight-line only. Fittings and structures acquired before that date, but not buildings, could use either method (所得税法施行令 art. 120-2(1)(1); 法人税法施行令 art. 48-2(1)(1)).
- **Vehicles.** A JPY 6,000,000 car with a 6-year life depreciates at 0.167 a year straight-line, or from 0.333 declining balance for an individual who elected it or a company. The private share is not deductible (所得税法 art. 45(1)(1); 所得税法施行令 art. 96). No cost cap was found in the texts read: this is a search of those texts only, and the car's business use is the live question.
- **Limit.** Useful lives are a statutory table, not a choice. The prior version's 'useful life adjusted by NTA' is held.

### Losses

`jp-income-tax` owns the ladder. Points that bear on planning:

- **Blue carry-forward.** Net loss carries forward 3 years (art. 70(1)), with a return for the loss year and each year after it (art. 70(4)). Art. 70-2 gives 5 years in the named disaster cases.
- **White.** Only 変動所得 losses and 被災事業用資産 losses carry forward 3 years (art. 70(2)), and 雑損失 under art. 71. The prior version's 'casualty, theft or disaster' was loose, and business losses in general do not carry.
- **Carry-back.** A blue filer who filed blue for the prior year and files on time may claim a refund for the prior year, up to that year's tax (art. 140). Art. 140(5) covers a business wholly transferred or ended.
- **Offset in the year.** Only losses from real estate, business, timber and capital gains income offset other income (art. 69(1)). A loss on an asset not usually needed for living is limited (art. 69(2)). The part of a real-estate loss equal to interest on debt to buy the land is treated as nil (措法 art. 41-4). The prior version's 'high-leverage properties' was not the test.
- **Listed securities.** A loss on listed securities offsets gains on listed securities, and listed dividends under separate taxation, on a final return (措法 art. 37-12-2(1)). What remains carries forward 3 years on those same items (NTA No. 1474). It does not reach business or employment income.
- **Company.** A loss carries forward 10 years (法人税法 art. 57(1)), with returns filed in each year (art. 57(10)). A company with capital of JPY 100,000,000 or less may use it against all income, and others against 50% (art. 57(1) and (11)). The prior version's 50% to 60% was historical. Carry-back is 1 year (art. 80), suspended to 31 March 2028 except for the small companies named in 措法 art. 66-12.

### Timing

| Strategy | Rule | Limit |
| --- | --- | --- |
| Furusato before year-end | Paid in the calendar year | Within the cap; the JPY 2,000 result needs the cap test |
| iDeCo and 小規模企業共済 before year-end | The deduction follows the amount paid in the year (art. 75). An iDeCo month and its debit month can differ, so use the certificate. Processing time for a new iDeCo member is held | Limits above; cash is locked up |
| Asset purchases | Under JPY 400,000, acquired and put to use in the business in the year. Buying without use does not qualify | Blue, small business, JPY 3,000,000 a year. See the table |
| Income timing | Income is what is due in the year (art. 36(1)), and an expense is one whose obligation is fixed in the year (art. 37(1)). Only a blue filer on the art. 67(1) cash basis uses money received and paid | Art. 67(1) needs the JPY 3,000,000 test and a notification. Changing an invoice date does not change the year in which income became due. The prior version's 'delay billing to January' is removed as a general rule. Where work is really done or delivered in January, that is a fact, not a plan. R-OPT-1 applies to any altered date |
| Medical | Paid in the year, so aggregate the family's payments against the floor | A cost counts only if art. 73(2) and the order name it. The prior version's advice to schedule elective procedures is not kept: whether a procedure counts was not read |
| Year-end adjustment | 年末調整 settles many credits for employees (所得税法 art. 190). The self-employed file. See `jp-income-tax` | A deduction not given to the employer needs a return |
| Listed shares | Choosing the year of a sale chooses the year of the gain or loss | 20.315% for 2026. A loss works only within listed securities income, with a final return each year |

### Consumption tax

- **Registration.** A business that registers as an invoice issuer is taxable whatever its sales (NTA No. 6491 note 2). Weigh the customers: a mainly consumer business that stays exempt charges no consumption tax, whilst a business customer's credit for purchases from an unregistered supplier is falling. The prior version's 'non-registered sellers lose B2B competitiveness' is a judgement, not a rule.
- **Simplified method.** The deemed ratio replaces actual input tax. It reduces tax only where actual input tax is lower, so compare both methods for a year with large purchases.
- **2割特例 and 3割特例.** The first ends with periods including 30 September 2026. For a sole proprietor on a calendar year, 2026 is the last year. The second is for 2027 and 2028 only, and for sole proprietors only. A company cannot use it.
- **Input credit.** Needs books and a qualified invoice, or a book-only case in NTA No. 6496.
- **Limit on structure.** The prior version said the NTA may reclassify an artificial structure kept below the threshold. Arts 9-2, 12-2 and 12-3 are specific rules, and no general reclassification rule for consumption tax was found in the parts read. So the point is held, and no one should structure a business only to stay exempt.

### Social insurance

- **NHI cap.** Premiums stop rising at the cap: JPY 1,130,000 for fiscal 2026, per household. Whether income reaches it depends on the municipality's rates. The saving compared with shakai hoken is real only where income is above that level, and benefits differ.
- **Shakai hoken.** Employer and employee each bear half (厚生年金保険法 art. 82(1); 健康保険法 art. 161(1)). Caps apply at the standard monthly remuneration limits above, so high pay bears a lower share. Premiums on bonuses (標準賞与額) were not read: `japan-payroll`.
- **National Pension add-ons.** 付加保険料 of JPY 400 a month or a fund contribution reduces the category 1 iDeCo limit.
- **Limit.** Whether an owner-director must join, including at nil pay, was not read and is held. Low pay also lowers benefits.

### Investment and retirement

- **iDeCo.** Contributions are deductible. The ministry's page says gains are not taxed whilst invested; the Act was not read on this. A lump sum is retirement income (所得税法 art. 31 item 3; 所得税法施行令 art. 72(3)(7)); an annuity is 公的年金等 (所得税法施行令 art. 82-2). Money generally stays in until old age: early withdrawal rules are in 確定拠出年金法 and were not read.
- **Lump sum order, new from 2026.** Where an iDeCo lump sum is taken and a retirement payment follows, the overlap period rule looks back 9 years, for lump sums paid from 1 January 2026 (所得税法施行令 art. 70(1)(2)ロ). The prior rule looked back 4 years. Where a retirement payment comes first and a DC lump sum follows, the look-back is 19 years (ハ). So the order and the gap between them change the 退職所得控除.
- **退職所得.** Receipts less 退職所得控除, then one-half, with exceptions for short service and 特定役員退職手当等 (所得税法 art. 30(2)).
- **小規模企業共済.** Contributions are deductible. 共済金 needs 6 months of contributions (art. 9(1)). A lump sum 共済金 is retirement income (所得税法施行令 art. 72(3)(3)イ). An instalment is 公的年金等 (art. 82-2). The 解約手当金 needs 12 months (art. 12(1)). On a member's own cancellation it is a percentage of contributions set by order, not below 80% (art. 12(3)(1)), so it can be less than was paid. It is retirement income for a member aged 65 or over (art. 72(3)(3)ロ), and the other cases are held (所得税法施行令 art. 183 names it among lump sums, but the result was not worked through).
- **国民年金基金.** Contributions are social insurance premiums (所得税法 art. 74(2)(5)). The prior version says its annuity is pension income. That rests on 所得税法 art. 35(3)(1), an inference from the Act's wording.
- **NISA.** Gains and dividends inside are not taxed (措法 arts 37-14(1), 9-8). The 2024 limbs have no end date for a sale on the text read (art. 37-14(1)(3) and (4)). A loss inside counts as nil. Money invested is after tax. The limits are in the table.
- **Listed securities and real estate.** See the tables and 'Losses'. Rent is taxed at progressive rates, net of depreciation.

### Layering

Order for a sole proprietor. This is a sequence of tests, not advice:

1. Blue return tier, because it comes off income first.
2. 小規模企業共済: up to JPY 840,000 a year if eligible.
3. iDeCo: to JPY 68,000 a month to November 2026, then to JPY 75,000, less any fund contribution or 付加保険料.
4. 国民年金基金: only inside the same limit.
5. NISA: after-tax money.
6. Furusato: after the rest, because the cap depends on them.

The prior version gave a combined deduction of about JPY 1.9 million and a saving of about JPY 820,000. Both were wrong. The largest iDeCo and 小規模企業共済 amounts for a whole year at the rule before 1 December 2026 are JPY 816,000 + JPY 840,000 = JPY 1,656,000. The saving depends on the band: Example 2 gives JPY 583,271 on its fixture. The saving is also partly a deferral, because a later lump sum or annuity is taxed.

## Deadlines and filing

Calendar for the 2026 year. `jp-income-tax` owns return dates.

| When | Action | Basis |
| --- | --- | --- |
| By 31 December 2026 | Money paid for furusato, iDeCo, 小規模企業共済, medical and insurance deductions for 2026. Assets put to use. | Arts 73 to 78 |
| December | Year-end adjustment for employees. National Pension 追納 for exempted periods within the last 10 years, deducted when paid | 所得税法 art. 190; 国民年金法 art. 94(1); 所得税法 art. 74 |
| 1 December 2026 | New iDeCo and fund limits start | 確定拠出年金法施行令 art. 36 |
| 10 January 2027 (Sunday) | One-Stop: 附則 art. 7(4) sets this date for notifying a change of name, address or similar. The request is made when donating (附則 art. 7(1)). The prior version's '10 January' deadline for the request is not in the text read, and municipal practice was not read. 地方税法 art. 20-5(2) moves a date falling on a holiday, apart from dates the order excludes; the order was not read | 地方税法 附則 art. 7(1), (4) |
| 16 February to 15 March 2027 | File the final return. Tax due 15 March | 所得税法 art. 120(1); NTA No. 2020 |
| By 15 March 2027 | Blue application for the 2027 year, or within 2 months where business starts on or after 16 January. Family employee notice on the same pattern | 所得税法 arts 57(2), 144 |
| By 31 March 2027 | Individual consumption tax return | NTA No. 6101 |
| Within 3 months of the start of the accounting period | Company director pay change. The prior version's 'April' fits only a March year-end | 法人税法施行令 art. 69(1)(1)イ |
| Within 2 months of the year-end | Company return | 法人税法 art. 74(1) |
| June, August, October, January | Inhabitant tax instalments, unless the ordinance differs. Check that the notice for the year shows the furusato credit. Timing of the notice was not read | 地方税法 art. 320 |
| 1 to 31 July; 1 to 30 November | Prepayments, where they apply. `jp-estimated-tax` owns these | 所得税法 art. 104(1) |
| Mid-year to November | Estimate income, then re-run the cap and limit tests. Check medical payments and asset purchases. This is practice, not law | None |
| Autumn | The prior version says insurance certificates arrive in October. This is insurer practice; not read | None |

A national tax date on a Saturday, Sunday or public holiday moves to the next day that is none of these (国税通則法 art. 10(2)).

**Portal.** Individuals file on e-Tax, using the 確定申告書等作成コーナー or other software, or on paper. Companies file 法人税 and 消費税 on e-Tax. Local company filings were not read. Forms: 確定申告書 第一表 and 第二表, 第三表 for separately taxed income, 第四表 for losses, with the 青色申告決算書 or 収支内訳書. `jp-etax-filing` owns the steps. After submission keep the reception record, then pay by a route in `jp-income-tax`.

**Evidence.** Keep the 小規模企業共済 and iDeCo payment certificates, the donation receipts (寄附金受領証明書), medical records, insurance certificates and the blue return approval. Blue records are kept 7 years, some 5 years (所得税法 art. 148; NTA No. 2070).

## Penalties and interest

`jp-income-tax` owns the table. In summary:

| Offence | Penalty | Basis |
| --- | --- | --- |
| Under-reporting (過少申告加算税) | 10%, or 5% where a return follows a notice of investigation but the correction was not foreseen; a further 5% on the part above the greater of the timely tax or JPY 500,000. Other cases in `jp-income-tax` | 国税通則法 art. 65 |
| Late filing (無申告加算税) | After investigation, 15% to JPY 500,000, 20% to JPY 3,000,000 and 30% above. Other cases in `jp-income-tax`: 10%, 15% and 25%, 5%, nil and a further 10% | 国税通則法 art. 66 |
| Fraud or concealment (重加算税) | 35% in place of 過少申告加算税; 40% in place of 無申告加算税; a further 10% on a repeat | 国税通則法 art. 68 |
| Late payment interest (延滞税), 2026 | 2.8% and 9.1% | 国税通則法 art. 60(2); 措法 art. 94; NTA 延滞税の割合 |

The prior version's '15% for large amounts' is the 10% plus the further 5%.

### Anti-avoidance limits

No provision of general application to every taxpayer was found in the parts read. This is not a complete search. The prior version's statement that Japan has no statutory GAAR is held on that footing. What was read:

- **同族会社.** 所得税法 art. 157 and 法人税法 art. 132: the tax office may recompute where an act or calculation of a 同族会社 or the named company would, if accepted, unfairly reduce tax. Art. 157 reaches the shareholder's own income tax.
- **Reorganisations.** 所得税法 art. 157(4). 法人税法 art. 132-2 by heading only.
- **Director pay.** 法人税法 art. 34.
- **Transfer pricing.** 措法 art. 66-4 (`japan-transfer-pricing`).
- **Blue approval.** The tax office may revoke it, back to the year concerned, for books not kept as required, failing to follow an instruction on the books, or concealed or false entries or reasonable grounds to doubt the truth of the books as a whole (所得税法 art. 150(1)(1) to (3)). 法人税法 art. 127(1) is the company rule; its limbs are not reproduced.
- **Judicial doctrine.** The prior version's 'substance over form doctrine' is held: no judgment was read.

### Scrutiny points

The prior version's list. Where an entry is a risk rather than a rule, it says so.

| Point | Effect | Status |
| --- | --- | --- |
| Director pay too high | Excess not deductible (art. 34(2)) | Enacted |
| Director pay too low | No text read | Held |
| Family salary with no work | Not deductible; revocation under art. 150 where the books are false | Enacted for the limbs stated |
| Private costs through the business | Not deductible (arts 37, 45); 加算税 | Enacted |
| Structure to stay exempt from consumption tax | See 'Consumption tax' | Held |
| Related-party pricing | 措法 art. 66-4 for companies. `japan-transfer-pricing` | Enacted |
| Crypto gains not reported | The prior version's 'data matching since 2020' was not read. `japan-crypto-tax` owns this | Held |
| Foreign income of a resident not reported | Residents are taxed on all income, wherever it arises (art. 7(1)(1)) | Enacted |
| Depreciation beyond the table | Useful lives are statutory. See 'Depreciation' | Enacted for the table; held for the prior version's wording |
| Mixing private and business accounts | No rule read makes this a ground on its own. Art. 150 turns on books | Held as a ground; a practical risk |
| Furusato above the cap | No penalty; the excess is not credited | Enacted |

### Red lines

Never advise or help with the first 4. R-OPT-1 applies to them.

- Underreporting income or hiding cash transactions.
- Claiming private costs as business deductions.
- Director pay that cannot be justified by the work and the art. 70 factors.
- A structure whose only reason is to keep a consumption tax exemption, with no business substance.
- Filing a white return to avoid bookkeeping. A white return is lawful, so this is a caution, not a refusal. A white filer with business income still keeps books and records (所得税法 art. 232(1)), and the prior version's claim that lost deductions almost always outweigh the effort is a judgement to test with figures, as Example 1 does.

## Cross-border points

- **Scope.** A resident other than a non-permanent resident is taxed on all income wherever it arises (所得税法 art. 7(1)(1)). R-OPT-2 stops others.
- **Foreign tax and treaties.** R-JP-9 in `jp-income-tax` applies. Nothing here is treaty planning.
- **Securities.** Separate-taxation rules and foreign tax are not computed here.
- **NISA and leaving Japan.** The account rules for departure were not read. Ask before relying on the tax-free result.
- **Company.** A foreign company or a related-party cross-border charge goes to `japan-transfer-pricing`.

## Two worked examples that recompute

All names are fixtures. Figures are estimates, labelled 'estimated, not reviewed'. Each example gives arithmetic, not a recommendation. Inhabitant tax uses standard rates of 10% as a labelled stand-in, the JPY 430,000 basic deduction, and the JPY 2,500 調整控除 (5% × JPY 50,000, arts 37(2) and 314-6(2)), for a filer with no dependants. Per-capita levies are left out. Inhabitant tax on 2026 income falls in fiscal 2027.

### Example 1: Which should I file, blue or white? JPY 8,000,000, 2026

Sole proprietor, resident, no other income. Business income before any blue deduction JPY 8,000,000. To isolate the choice, the fixture has no other deduction. Blue case: approval held, 正規の簿記, statements attached, e-Tax by the deadline, so JPY 650,000. Both incomes are above JPY 6,550,000, so the basic deduction is JPY 620,000 either way.

White: taxable JPY 7,380,000; income tax JPY 1,061,400; surtax JPY 22,289. Local levy (JPY 8,000,000 − JPY 430,000) × 10% − JPY 2,500 = JPY 754,500.

Blue: 合計所得金額 JPY 7,350,000; taxable JPY 6,730,000; income tax JPY 918,500; surtax JPY 19,288. Local levy JPY 689,500.

The figure that decides: blue costs JPY 210,901 less tax a year on these facts. That is before bookkeeping cost, and the blue approval must have been applied for. 個人事業税 is left out: its base follows 所得税法 arts 26 and 27 (地方税法 art. 72-49-12(1)), and 措法 art. 25-2 is not named there, so on this reading the blue deduction does not reduce it, and both cases bear the same amount. That reading is an inference. The prior version's JPY 212,126 used 2025 figures.

```oa-check
name: JP 2026 blue or white on JPY 8,000,000
inputs:
  income: 8000000
  blue: 650000
  basic: 620000
  local_basic: 430000
  adjustment: 2500
steps:
  - taxable_white: floor((income - basic) / 1000) * 1000
  - tax_white: taxable_white * 0.23 - 636000
  - surtax_white: floor(tax_white * 0.021)
  - local_white: floor((income - local_basic) / 1000) * 1000 * 0.10 - adjustment
  - total_white: tax_white + surtax_white + local_white
  - income_blue: income - blue
  - taxable_blue: floor((income_blue - basic) / 1000) * 1000
  - tax_blue: taxable_blue * 0.20 - 427500
  - surtax_blue: floor(tax_blue * 0.021)
  - local_blue: floor((income_blue - local_basic) / 1000) * 1000 * 0.10 - adjustment
  - total_blue: tax_blue + surtax_blue + local_blue
  - saving: total_white - total_blue
expected:
  taxable_white: 7380000
  tax_white: 1061400
  surtax_white: 22289
  local_white: 754500
  total_white: 1838189
  taxable_blue: 6730000
  tax_blue: 918500
  surtax_blue: 19288
  local_blue: 689500
  total_blue: 1627288
  saving: 210901
```

### Example 2: Layered deductions on JPY 12,000,000, 2026

Sole proprietor, category 1 pension, business income before blue JPY 12,000,000. JPY 650,000 blue deduction, social insurance JPY 1,200,000 (fixture), furusato JPY 250,000 (寄附金控除 JPY 248,000). The question: what do iDeCo of JPY 816,000 (JPY 68,000 for 12 months paid in 2026, no fund, no 付加保険料) and 小規模企業共済 of JPY 840,000 (JPY 70,000 × 12) do?

With both, taxable income is JPY 7,626,000: 23% band. Without, JPY 9,282,000: 33% band. The first JPY 282,000 of the reduction saves at 33% and the rest at 23%, so a flat '33% + 10%' overstates it. Total reduction JPY 583,271: national JPY 417,671 and local JPY 165,600.

The 12 payment months are a fixture: use the certificate. The furusato credit is left out of both local figures, because the cap in Example 4 changes with the contributions. It is not a like-for-like gain. JPY 1,656,000 of cash is locked in, and a later payment is taxed. The prior version's 'about JPY 1,300,000 against no planning' had no stated baseline and is replaced.

```oa-check
name: JP 2026 iDeCo and mutual aid on JPY 12,000,000
inputs:
  business_income: 12000000
  blue: 650000
  social: 1200000
  donation_deduction: 248000
  basic: 620000
  ideco: 816000
  mutual_aid: 840000
  local_basic: 430000
  adjustment: 2500
steps:
  - total_income: business_income - blue
  - taxable_with: floor((total_income - social - donation_deduction - basic - ideco - mutual_aid) / 1000) * 1000
  - tax_with: taxable_with * 0.23 - 636000
  - national_with: tax_with + floor(tax_with * 0.021)
  - taxable_without: floor((total_income - social - donation_deduction - basic) / 1000) * 1000
  - tax_without: taxable_without * 0.33 - 1536000
  - national_without: tax_without + floor(tax_without * 0.021)
  - local_with: floor((total_income - social - ideco - mutual_aid - local_basic) / 1000) * 1000 * 0.10 - adjustment
  - local_without: floor((total_income - social - local_basic) / 1000) * 1000 * 0.10 - adjustment
  - national_saving: national_without - national_with
  - local_saving: local_without - local_with
  - total_saving: national_saving + local_saving
expected:
  taxable_with: 7626000
  taxable_without: 9282000
  national_with: 1141457
  national_without: 1559128
  local_with: 803900
  local_without: 969500
  national_saving: 417671
  local_saving: 165600
  total_saving: 583271
```

### Example 3: Which should I choose, sole proprietor or company? Profit JPY 10,000,000, 2026

Consultant (第三種, 5% on the listed business), 50, single, profit before owner pay JPY 10,000,000. Capital JPY 3,000,000, one officer, standard local rates, a full year, consumption tax left out of both.

**Fixtures, not sourced rates:** NHI JPY 900,000 and a health rate of 10% all in. Both are stand-ins for a real figure from the municipality and the insurer, and are Needs Input in a real case. Change them and the result changes.

Sole proprietor: blue JPY 650,000, social insurance JPY 900,000 + JPY 215,040 (12 × JPY 17,920, the fiscal 2026 rate, as a fixture for the calendar year). Taxable JPY 7,614,000. Income tax and surtax JPY 1,138,639. Local levy JPY 777,900. 個人事業税 (JPY 10,000,000 − JPY 2,900,000) × 5% = JPY 355,000. Total JPY 3,386,579.

Company: salary JPY 6,000,000 (JPY 500,000 a month, grade JPY 500,000). Shakai hoken JPY 1,698,000, half each. Company profit JPY 10,000,000 − JPY 6,000,000 − JPY 849,000 = JPY 3,151,000. Company layers JPY 775,509, including 均等割 of JPY 70,000. Employment income JPY 4,360,000 (所得税法 別表第五 for 2026). Basic deduction JPY 1,040,000. Taxable JPY 2,471,000. Income tax and surtax JPY 152,741. Local levy JPY 305,600. Total JPY 2,931,850.

The figure that decides: on these fixtures the company route shows JPY 454,729 less in taxes and premiums. The prior version found the company JPY 680,000 dearer because it left out 個人事業税, did not deduct the employer's premium from company profit, and overstated the owner's tax. Its conclusion is withdrawn. So is the opposite conclusion: this figure is not a finding that incorporation is better.

Left out, and each can reverse it:

- **Exit cost.** JPY 2,375,491 stays in the company. The owner has JPY 4,692,659 in hand, against JPY 6,613,421 as a sole proprietor. Taking the rest out as a dividend adds tax and is not computed.
- **Costs.** Formation, annual accounts, a 税理士, payroll, and the employer's 子ども・子育て拠出金.
- **Benefits.** 厚生年金 and health insurance benefits differ from National Pension and NHI.
- **Deductions.** The sole proprietor's next-year deduction for 個人事業税 and the company's for its business taxes.
- **Consumption tax.** A new company may be exempt for a time, on the conditions above.
- **Salary level.** Another salary gives another result. Run several.
- **Law.** The 15% rate is for years starting by 31 March 2027. Basic deduction amounts change for 2028.

```oa-check
name: JP 2026 sole proprietor or company on JPY 10,000,000
inputs:
  profit: 10000000
  blue: 650000
  nhi_fixture: 900000
  pension: 215040
  basic_high: 620000
  local_basic: 430000
  adjustment: 2500
  enterprise_relief: 2900000
  salary: 6000000
  employment_income: 4360000
  basic_low: 1040000
  health_fixture: 0.10
  per_capita: 70000
steps:
  - social_sole: nhi_fixture + pension
  - income_sole: profit - blue
  - taxable_sole: floor((income_sole - social_sole - basic_high) / 1000) * 1000
  - tax_sole: taxable_sole * 0.23 - 636000
  - national_sole: tax_sole + floor(tax_sole * 0.021)
  - local_sole: floor((income_sole - social_sole - local_basic) / 1000) * 1000 * 0.10 - adjustment
  - enterprise_sole: (profit - enterprise_relief) * 0.05
  - total_sole: national_sole + local_sole + enterprise_sole + social_sole
  - shakai: salary * (0.183 + health_fixture)
  - employer_share: shakai / 2
  - company_profit: profit - salary - employer_share
  - corporation_tax: company_profit * 0.15
  - local_corporation: corporation_tax * 0.103
  - resident_levy: corporation_tax * 0.07
  - business_tax: company_profit * 0.035
  - special_business: business_tax * 0.37
  - company_tax: round(corporation_tax + local_corporation + resident_levy + business_tax + special_business + per_capita, 0)
  - taxable_owner: floor((employment_income - employer_share - basic_low) / 1000) * 1000
  - tax_owner: taxable_owner * 0.10 - 97500
  - national_owner: tax_owner + floor(tax_owner * 0.021)
  - local_owner: floor((employment_income - employer_share - local_basic) / 1000) * 1000 * 0.10 - adjustment
  - total_company: company_tax + national_owner + local_owner + shakai
  - gap: total_sole - total_company
  - owner_cash: salary - employer_share - national_owner - local_owner
  - retained: company_profit - company_tax
expected:
  taxable_sole: 7614000
  national_sole: 1138639
  local_sole: 777900
  enterprise_sole: 355000
  total_sole: 3386579
  shakai: 1698000
  company_profit: 3151000
  company_tax: 775509
  taxable_owner: 2471000
  national_owner: 152741
  local_owner: 305600
  total_company: 2931850
  gap: 454729
  owner_cash: 4692659
  retained: 2375491
```

### Example 4: Furusato cap, the Example 2 taxpayer

Same facts, living outside a designated city. The local base after deductions is JPY 8,064,000, so 所得割 after 調整控除 is JPY 803,900 and the 20% cap is JPY 160,780. The band test takes JPY 190,000 off (JPY 50,000 + JPY 620,000 − JPY 480,000), leaving JPY 7,874,000, so the ratio is 66.517%. The largest donation with the full special credit is JPY 160,780 ÷ 0.66517 + JPY 2,000 = about JPY 243,712.

So the JPY 250,000 in the prior version's example passes the cap. Net cost is about JPY 6,182, not JPY 2,000. A JPY 240,000 donation costs about JPY 2,000. This is before the actual municipal rate and assessment. For a filer with these facts, the donation goes on the final return.

```oa-check
name: JP 2026 furusato cap with JPY 250,000 and JPY 240,000
inputs:
  local_base: 8064000
  adjustment: 2500
  ratio: 0.66517
  taxable_before: 7874000
  high_donation: 250000
  low_donation: 240000
steps:
  - levy: local_base * 0.10 - adjustment
  - cap: levy * 0.20
  - largest_donation: floor(cap / ratio + 2000)
  - tax_before: taxable_before * 0.23 - 636000
  - national_before: tax_before + floor(tax_before * 0.021)
  - high_tax: floor((taxable_before - (high_donation - 2000)) / 1000) * 1000 * 0.23 - 636000
  - high_national: high_tax + floor(high_tax * 0.021)
  - high_basic: (high_donation - 2000) * 0.10
  - high_special: min((high_donation - 2000) * ratio, cap)
  - high_net_cost: high_donation - (national_before - high_national) - high_basic - high_special
  - low_tax: floor((taxable_before - (low_donation - 2000)) / 1000) * 1000 * 0.23 - 636000
  - low_national: low_tax + floor(low_tax * 0.021)
  - low_basic: (low_donation - 2000) * 0.10
  - low_special: min((low_donation - 2000) * ratio, cap)
  - low_net_cost: low_donation - (national_before - low_national) - low_basic - low_special
expected:
  levy: 803900
  cap: 160780
  largest_donation: 243712
  national_before: 1199695
  high_national: 1141457
  low_national: 1143805
  high_net_cost: 6182
  low_net_cost: 1999.54
```

## Ask the client first

Ask these before any figure. What stays unanswered is Needs Input.

1. **Status and year.** Resident all year, Japanese national or years in Japan, age, municipality (and whether a designated city), and which year.
2. **Form.** Sole proprietor, KK or GK; capital, year-end, employees (including whether the main business is commerce or services), family members working, and who controls the company.
3. **Return.** 青色申告 or 白色申告, with the approval date; 複式簿記 or 簡易簿記; e-Tax or paper; cash basis; any notification filed.
4. **Income.** Estimated profit, salary, dividends, securities, real estate, crypto, foreign income, and 合計所得金額 this year and the 2 years before.
5. **Pension and premiums.** Pension category, any exemption, 付加保険料, 国民年金基金, iDeCo and 小規模企業共済 amounts with payment certificates; NHI or which health insurer; any company DC or DB plan.
6. **Tax position.** Consumption tax status, invoice registration and base-period sales; losses carried forward with the returns; donations made this year and to whom; home loan details; medical and insurance payments.

### Completion checks

- [ ] No refusal fired, and residence confirmed?
- [ ] Each strategy stated with its condition and limit, and not as advice?
- [ ] 小規模企業共済 limit taken as JPY 70,000 a month?
- [ ] iDeCo limit taken for the right category and month, less any fund contribution or 付加保険料?
- [ ] Surtax added: 2.1% for 2026? Any 2027 figure treated as not computed?
- [ ] Basic deduction band taken after the blue deduction?
- [ ] Furusato cap run after every other deduction, and One-Stop ruled out for a filer?
- [ ] Each comparison states what is left out, including social insurance, 個人事業税 and exit cost?
- [ ] Inhabitant tax labelled as standard rates?
- [ ] No proposal used as law, including the food consumption tax rate?
- [ ] Figures labelled 'estimated, not reviewed' and open items listed?

## Sources

Read on 6 November 2026 unless stated. e-Gov text is the consolidated text from the e-Gov law API at the dates shown; the URL column gives the public e-Gov page. 'Retained' marks a file fetched on 5 November 2026 for `jp-income-tax` and reread here. No English text was treated as law.

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| 所得税法 | https://laws.e-gov.go.jp/law/340AC0000000033 | 2026-11-06 | Retained. Read in part at 5 November 2026 and 1 December 2026: arts 30, 31, 35(3), 36, 69, 72, 73, 75, 77, 78, 86, 92, 140, 150, 157 and 182, with arts 2, 7, 45, 56, 57, 70, 71, 74, 76, 83, 84, 89, 104, 120 and 143 to 148 through `jp-income-tax` |
| 所得税法 別表第五 | https://laws.e-gov.go.jp/law/340AC0000000033 | 2026-11-06 | Retained. The JPY 6,000,000 row at 1 December 2026 only |
| 所得税法施行令 | https://laws.e-gov.go.jp/law/340CO0000000096 | 2026-11-06 | Retained. Read in part at 5 November 2026, with a comparison at 31 December 2025: arts 70, 72(3), 82-2, 120-2 and 183, with arts 96, 125, 138, 139 and 165 through `jp-income-tax` |
| 租税特別措置法 | https://laws.e-gov.go.jp/law/332AC0000000026 | 2026-11-06 | Retained, with text at 1 April 2027 newly fetched. Read in part at 5 November 2026, 1 December 2026 and 1 January 2027: arts 8-4, 8-5, 25-2, 28-2, 37-11, 37-12-2, 37-14, 41, 41-4, 41-16-2, 41-17, 42-3-2, 61-4, 66-12 and 67-5 |
| 租税特別措置法施行令 | https://laws.e-gov.go.jp/law/332CO0000000043 | 2026-11-06 | Through `jp-income-tax`: art. 18-5 |
| 法人税法 | https://laws.e-gov.go.jp/law/340AC0000000034 | 2026-11-06 | Read in part at 5 November 2026: arts 22(5), 34, 57(1), (10) and (11), 66, 74(1), 80(1), 127(1), 132 and 132-2 heading |
| 法人税法施行令 | https://laws.e-gov.go.jp/law/340CO0000000097 | 2026-11-06 | Read in part at 5 November 2026: arts 53, 69(1) and (2) and 70 |
| 地方税法 | https://laws.e-gov.go.jp/law/325AC0000000226 | 2026-11-06 | Retained at 31 December 2025, 5 November 2026 and 1 January 2027; newly fetched at 1 January 2028 and 1 January 2029. Read in part: arts 34, 37, 37-2, 51, 52, 72-24-7, 72-49-12, 72-49-14, 72-49-17, 312, 314-4, 314-6, 314-7, 320, 附則 arts 5-5, 5-6, 7 and 7-2, and the 附則 of 令和8年法律第2号 |
| 地方法人税法 | https://laws.e-gov.go.jp/law/426AC0000000011 | 2026-11-06 | Read in part: art. 10 |
| 特別法人事業税及び特別法人事業譲与税に関する法律 | https://laws.e-gov.go.jp/law/431AC0000000004 | 2026-11-06 | Read in part: art. 7 |
| 防衛財確法 | https://laws.e-gov.go.jp/law/505AC0000000069 | 2026-11-06 | Retained. Read in part at 5 November 2026: arts 9 to 14, with art. 5-9 through `jp-income-tax` |
| 復興財確法 | https://laws.e-gov.go.jp/law/423AC0000000117 | 2026-11-06 | Through `jp-income-tax`: arts 9, 12, 13 |
| 消費税法 | https://laws.e-gov.go.jp/law/363AC0000000108 | 2026-11-06 | Retained at 5 November 2026; newly fetched at 1 April 2027. Read in part: arts 9-2, 12-2, 12-3, 29, 37 and the 附則 of 平成28年法律第15号 as printed |
| 消費税法施行令 | https://laws.e-gov.go.jp/law/363CO0000000360 | 2026-11-06 | Read in part: art. 57 |
| 国税通則法 | https://laws.e-gov.go.jp/law/337AC0000000066 | 2026-11-06 | Retained. Read in part: opening of arts 65 and 68, with arts 10, 60 and 66 through `jp-income-tax` |
| 確定拠出年金法 | https://laws.e-gov.go.jp/law/413AC0000000088 | 2026-11-06 | Read in part at 5 November 2026 and 1 December 2026: art. 62 |
| 確定拠出年金法施行令 | https://laws.e-gov.go.jp/law/413CO0000000248 | 2026-11-06 | Read in part at 5 November 2026, 1 December 2026 and 1 January 2027: art. 36 |
| 小規模企業共済法 | https://laws.e-gov.go.jp/law/340AC0000000102 | 2026-11-06 | Read in part: arts 2, 4, 5, 9 and 12 |
| 小規模企業共済法施行令 | https://laws.e-gov.go.jp/law/340CO0000000185 | 2026-11-06 | Read in part: arts 1 to 3 |
| 国民年金基金令 | https://laws.e-gov.go.jp/law/402CO0000000304 | 2026-11-06 | Read in part at 5 November 2026 and 1 December 2026: art. 34 |
| 国民年金法 | https://laws.e-gov.go.jp/law/334AC0000000141 | 2026-11-06 | Read in part: arts 87-2 and 94(1) |
| 健康保険法 | https://laws.e-gov.go.jp/law/211AC0000000070 | 2026-11-06 | Read in part: arts 3(5) and 40 and the heading of art. 160-2 |
| 厚生年金保険法 | https://laws.e-gov.go.jp/law/329AC0000000115 | 2026-11-06 | Read in part: arts 20 and 81 |
| 国民健康保険法施行令 | https://laws.e-gov.go.jp/law/333CO0000000362 | 2026-11-06 | Read in part at 31 December 2025 and 5 November 2026: the cap items of art. 29-7 |
| 減価償却資産の耐用年数等に関する省令 | https://laws.e-gov.go.jp/law/340M50000040015 | 2026-11-06 | Retained. Read in part: building rows of 別表第一, with other rows through `jp-income-tax` |
| NTA, Tax Answer 所得税 pages | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1155.htm | 2026-11-06 | Read in part. Nos 1120, 1129, 1155, 1213 and 1474 at the same URL pattern, stated at 1 April 2026; Nos 2020, 2070, 2072, 2100, 2260, 1180 and 1191 through `jp-income-tax` |
| NTA, Tax Answer 法人税 pages | https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5759.htm | 2026-11-06 | Read in part. Nos 5211 and 5759. Nos 5209, 5212, 5280 and 5765 returned a not-found page and were not read |
| NTA, Tax Answer 消費税 pages | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm | 2026-11-06 | Read in part. Nos 6101, 6491, 6496, 6498 and 6505. No. 6103 returned a not-found page and was not read |
| NTA, invoice-system review page | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/invoice-review/index.htm | 2026-11-06 | Read in part: 3割特例, simplified method and transitional credit, as HTML text; a table cell of rates was not all in text |
| NTA, Invoice Q&A 問115-2 (PDF) | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/qa/115-2.pdf | 2026-11-06 | Read in part by local text extraction. Administrative text |
| NTA and Ministry of Finance, 消費税率引下げ特設サイト | https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/zeiritsuhikisage.htm | 2026-11-06 | Read in part: the page and its leaflet of September 2026, by local text extraction. A proposal, not law |
| NTA, 延滞税の割合 | https://www.nta.go.jp/taxes/nozei/entaizei/keisan/entai_wariai.htm | 2026-11-06 | Through `jp-income-tax`: 2026 rows |
| 総務省, ふるさと納税 税金の控除について | https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/furusato/mechanism/deduction.html | 2026-11-06 | Read in part: credit formula, One-Stop and filing. Administrative text |
| 厚生労働省, iDeCo | https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/nenkin/kyoshutsu/ideco.html | 2026-11-06 | Read in part: limits table, which shows the rule before 1 December 2026 |
| 厚生労働省, 標準報酬月額の上限 | https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000147284_00024.html | 2026-11-06 | Read in part: the 65万円 cap and its stages |
| 中小機構, 小規模企業共済の特長 | https://www.smrj.go.jp/kyosai/skyosai/features/index.html | 2026-11-06 | Read in part: contribution range and how benefits are taxed |
| 日本年金機構, 国民年金の保険料 | https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html | 2026-11-06 | Retained. Read in part: fiscal 2026 premium and 付加保険料 |
| 財務省, 法人課税に関する基本的な資料 | https://www.mof.go.jp/tax_policy/summary/corporation/c01.htm | 2026-11-06 | Read in part: national and local rate history and note on the defence tax |
| 財務省, 令和9年度 税制改正 | https://www.mof.go.jp/tax_policy/tax_reform/outline/fy2027/index.html | 2026-11-05 | Retained: index page only, as read for `jp-income-tax` |
| e-Tax | https://www.e-tax.nta.go.jp/ | 2026-11-05 | Retained: read for the portal name only |

### Source conflicts

- **Surtax dates on furusato.** The 総務省 page says the surtax-inclusive rate runs to donations of 2037 (令和19年). NTA No. 1155 says 2047 (令和29年分). 地方税法 附則 art. 5-6 reads 令和20年度 at 1 January 2027 and 令和30年度 at 1 January 2029. This file follows the law for the year covered, where all 3 agree.
- **Furusato cap and the 2027 surtax.** The rate in 附則 art. 5-6 stays on a 2.1% footing, and how the 2027 split is treated was not worked through.
- **iDeCo page.** The Ministry's page shows the rule before 1 December 2026. The order read at 1 December 2026 gives the later limits. Both are right for their dates.
- **Consumption tax on food.** Some NTA Tax Answers state the April 2027 cut without qualification. The special page says it assumes a bill is passed. The law read shows no change. This file treats it as a proposal.
- **小規模企業共済.** The prior version's table said JPY 84,000 a month and its own example used JPY 70,000 a month. The Act says JPY 70,000.
- **Sibling guide.** `jp-incorporation` gives enterprise tax rates of 5.665% and 7.48% for its bands, against the standard 5.3% and 7% read here, and a breakeven this file does not adopt. That guide was not changed.

### Other legacy topics

- **Chuo City source.** The prior version cited a municipal page for the local basic deduction. 地方税法 arts 34 and 314-2 are cited instead, through `jp-income-tax`.
- **Vehicle comparison.** 'Unlike Australia or UK' is removed: foreign law was not read.
- **Reconstruction surtax in 20.315%.** The 15% national rate × 1.021 = 15.315%, plus 5% local.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 1.2 | November 2026 | Converted to the upstream template for the 2026 year, against primary text. Corrected the 小規模企業共済 limit to JPY 70,000 a month; dated the iDeCo limits at 1 December 2026; corrected the saving figures, health cap, furusato treatment and cap, One-Stop conditions, depreciation default, small-asset employee limit, loss limits, carry-forward percentages, director pay timing, new company test, company rates and citations. Withdrew the rules of thumb on incorporation and the January billing strategy. Added refusals, defaults, salary and dividend outcomes, anti-avoidance limits and a furusato cap example |
| 1.1 | November 2026 | Prior version |

Not yet confirmed: the Act 令和8年法律第12号 and 令和8年法律第2号 as separate documents; any enacted law for the food consumption tax rate of 1%; any 令和9年度 tax reform outline after 5 November 2026; 2027 computations and forms; company health insurance rates, for which Example 3 uses a fixture; actual NHI premiums and local rates above standard; the order adding the JPY 650,000 厚生年金 grade; National Pension premium for fiscal 2025 (the prior version's JPY 17,510 was not on the page read); the date for filing a One-Stop request in municipal practice; processing time for a new iDeCo member; tax on a return gift in the donor's hands; 解約手当金 taxation below age 65; premiums on bonuses; whether a low director salary draws scrutiny; any general anti-avoidance provision outside the parts read, and the judicial doctrine; any general consumption tax reclassification rule; NTA data matching on crypto; the rule on an owner-director's shakai hoken membership, including at nil pay; NISA rules on departure from Japan and the other limits for minors; the home loan limits for a given house; early withdrawal from iDeCo; Tax Answer pages after the read date; the 調整控除 for a filer with dependants.
