---
name: jp-income-tax
description: "Use this skill whenever asked about Japanese income tax for self-employed individuals filing a final tax return (確定申告 Kakutei Shinkoku). Trigger on phrases like \"how much tax do I pay in Japan\", \"kakutei shinkoku\", \"確定申告\", \"blue return\", \"青色申告\", \"white return\", \"白色申告\", \"business income Japan\", \"事業所得\", \"necessary expenses\", \"必要経費\", \"basic deduction\", \"基礎控除\", \"reconstruction tax\", \"resident tax\", \"住民税\", \"self-employed tax Japan\", \"e-Tax\", \"Rakuten Bank\", \"Japan Post Bank\", \"freee Japan\", \"Misoca\", or any question about filing or computing income tax for a self-employed individual in Japan. It covers the 2025 and 2026 years: brackets, blue and white returns, special deductions, reconstruction surtax, resident tax, necessary expenses and filing deadlines. ALWAYS read this skill before touching any Japan income tax work. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/jp-income-tax"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan income tax for self-employed individuals v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Coverage: the 2025 year (令和7年分, filed in 2026) and the 2026 year (令和8年分). Some enacted 2027 changes are recorded, not all of them, and no 2027 computation is supported. The law was read at 5 November 2026. The 2026 basic deduction and employment income rules were enacted by 令和8年法律第12号, read only as consolidated e-Gov text, and are in force on 1 December 2026, so they were read in the text dated from that day. No 令和9年度 tax reform outline had been published at the read date.

## Who this applies to

An individual resident in Japan (居住者) other than a non-permanent resident (非永住者) who has business income (事業所得, 所得税法 art. 27), with or without employment income, and files a final return (確定申告) on a calendar-year basis. Currency is JPY only. The filing unit is the individual: art. 120(1) places the return on each resident.

A resident is an individual with a domicile (住所) in Japan, or a residence (居所) there for a continuous year or more up to the present (所得税法 art. 2(1)(3)). A non-permanent resident is a resident who is not a Japanese national and whose domicile or residence in Japan in the past 10 years totals 5 years or less (art. 2(1)(4)). Everyone else is a non-resident (art. 2(1)(5)).

The tax authority is the National Tax Agency (国税庁, NTA). Primary legislation is the Income Tax Act (所得税法, Act No. 33 of 1965) with the Special Taxation Measures Act (租税特別措置法). The filing portal is e-Tax (国税電子申告・納税システム, https://www.e-tax.nta.go.jp/), with returns prepared in the NTA's 確定申告書等作成コーナー (https://www.keisan.nta.go.jp/kyoutu/ky/sm/top).

### What this file is

This file is a Tier 2 reference with review pending. It holds the rate tables, the base, classification patterns, deadlines and reviewer questions. Treat every computed figure as an estimate for review by a 税理士 (zeirishi) or equivalent licensed practitioner in Japan.

**Operational hold.** This file does not fill the complete country companion contract in `income-tax-workflow-base`, so it does not support unattended preparation:

- The transaction pattern library and bank formats below are carried from the prior version. Their narrations and file layouts were not tested against bank files.
- The employee and mixed fixtures below stop at the national balance due. Employment receipts below JPY 6,600,000 need the table in 所得税法 別表第五, which this file does not reproduce, or for 2026 and 2027 措法 art. 29-4(2) for receipts of JPY 691,000 to under JPY 2,200,000.
- Inhabitant tax (住民税) is described but not computed: its base, its deductions and any local rate differ from the national computation. Individual enterprise tax (個人事業税) and social insurance are not computed here. `jp-social-insurance` owns social insurance and supplies only the amount paid.
- Other Japanese guides in this repository state some of the same facts differently. See 'Source conflicts' below; those guides were not changed.

**Reviewer warning.** Any working paper produced under this file is a working paper only. It must show which inputs were confirmed and which are Needs Input, and it must carry the label 'estimated, not reviewed'.

### Question threshold

Tier 2 question threshold: JPY 0. No row is filtered on amount: a material question goes to the client or the reviewer whatever its size, because no text read sets a floor.

### Refusals

A refusal is a full stop. When a trigger applies, output the message verbatim and end. Do not classify part of the file first. Where a trigger is only suspected, ask the client the question that resolves it.

- **R-JP-1, non-resident.** Trigger: the person is, or may be, a non-resident (非居住者) at any time in the year. Message: 'Non-resident taxation has different sourcing rules and treaty interactions, and this file covers residents only. Refer it to a 税理士. This workflow cannot continue.'
- **R-JP-2, corporate entity.** Trigger: the income belongs to a corporation (法人). Message: 'Corporations file corporate tax (法人税), not income tax. This workflow cannot continue.'
- **R-JP-3, real estate gains or inherited property.** Trigger: the year includes a gain on real estate or the disposal or valuation of inherited property. Message: 'Real estate gains and inherited property need a separate computation that this file does not contain. Refer it to a 税理士. This workflow cannot continue.'
- **R-JP-4, cryptocurrency.** Trigger: the year includes a gain, payment or income in crypto assets (暗号資産). Message: 'Crypto income needs classification rules that this file does not contain. Check `japan-crypto-tax` and refer it to a 税理士. This workflow cannot continue.'
- **R-JP-5, non-permanent resident.** Trigger: the person is, or may be, a non-permanent resident (非永住者). Message: 'Non-permanent residents are taxed on a limited scope of foreign income, which this file does not compute. Check `jp-nonpermanent-resident` and refer it to a 税理士. This workflow cannot continue.'
- **R-JP-6, other income in the aggregate.** Trigger: the year includes income, other than business or employment income, that must or may enter the return: real estate (不動産所得), dividends (配当所得), capital gains (譲渡所得), retirement (退職所得), timber (山林所得), occasional (一時所得) or miscellaneous income (雑所得), including public pensions. Message: 'This year includes income that this file does not compute, and total income (合計所得金額) cannot be stated without it. Refer it to a 税理士. This workflow cannot continue.'
- **R-JP-7, year not covered.** Trigger: a computation is asked for a year other than 2025 or 2026. Message: 'This file computes 2025 and 2026 only. Read the text in force and the return form for that year. This workflow cannot continue for that year.'
- **R-JP-8, very high income.** Trigger: for 2025 or 2026, 基準所得金額 may exceed JPY 330,000,000, so that 租税特別措置法 art. 41-19 may apply. Message: 'The minimum tax on very high income needs a computation that this file does not contain. Refer it to a 税理士. This workflow cannot continue.'
- **R-JP-9, foreign tax or treaty claim.** Trigger: foreign tax was paid or withheld, or a treaty position is claimed. Message: 'The foreign tax credit (所得税法 art. 95) and any treaty need an analysis that this file does not contain. Refer it to a 税理士. This workflow cannot continue.'
- **R-JP-10, death or departure.** Trigger: the taxpayer died or left Japan in the year, or the return is a 準確定申告. Message: 'A return for a year ending in death or departure has timing rules that this file does not contain, and the 2026 amounts depend on the filing date. Refer it to a 税理士. This workflow cannot continue.'

### Required inputs

- **Minimum viable.** Bank statement for the full calendar year (January to December) in CSV, PDF or pasted text, and confirmation of return type (blue or white) and bookkeeping method.
- **Recommended.** All invoices issued (Misoca, freee, MF Cloud), payment notices or 支払調書 copies from clients who withheld tax, the 源泉徴収票 from any employer, national pension payment certificates (国民年金), national health insurance receipts (国民健康保険) and the blue return approval.
- **Ideal.** Complete double-entry general ledger, asset register, prior year return (申告書 copy), e-Tax receipt, iDeCo and small enterprise mutual aid (小規模企業共済) contribution statements.

### Prohibitions

- Never omit the surtax: 2.1% of 基準所得税額 for 2025 and 2026.
- Never apply the JPY 650,000 blue return deduction without confirming blue approval, 正規の簿記, attached statements, filing by the deadline and one of the 2 routes: e-Tax transmission or qualifying electronic books.
- Never allow national pension or health insurance as 必要経費: they are 所得控除.
- Never allow income tax or inhabitant tax as a deduction (所得税法 art. 45(1)(2) and (4)).
- Never treat loss carry-forward as blue only: blue filers carry net losses 3 years, and white filers carry only the 2 kinds in art. 70(2).
- Never skip rounding taxable income down to JPY 1,000 before applying rates.
- Never skip rounding a positive amount of tax payable down to JPY 100. A refund is not rounded to JPY 100.
- Never present a calculation as definitive: label it estimated and direct the client to their 税理士.

## Rates, bands and thresholds

All amounts are in yen. e-Gov consolidated text was read at the dates stated in Sources.

### National income tax

Taxable income is total income after 所得控除 (art. 89(2)), rounded down to JPY 1,000 (国税通則法 art. 118(1)). Tax = taxable income × rate − deduction amount. The table form is NTA No. 2260; the statute states marginal bands.

| Taxable income (JPY) | Rate | Deduction amount (控除額) | Tax year | Official source |
| --- | --- | --- | --- | --- |
| Up to 1,950,000 | 5% | 0 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 1,950,000, up to 3,300,000 | 10% | 97,500 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 3,300,000, up to 6,950,000 | 20% | 427,500 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 6,950,000, up to 9,000,000 | 23% | 636,000 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 9,000,000, up to 18,000,000 | 33% | 1,536,000 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 18,000,000, up to 40,000,000 | 40% | 2,796,000 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| Over 40,000,000 | 45% | 4,796,000 | 2025, 2026 | 所得税法 art. 89(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 2260: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |

### Surtaxes

基準所得税額 is the income tax after tax credits, before withholding. The surtax is rounded down to JPY 1: 令和7年分 手引き p. 27 for 2025. No 令和8年分 手引き was read, so the 2026 rounding is carried from the 2025 手引き, an extrapolation for the reviewer to confirm.

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| 復興特別所得税 (reconstruction surtax) | 2.1% of 基準所得税額 | 2013 to 2026 | 復興財確法 arts 8, 9(1), 12, 13 read at 31 December 2025 and 1 December 2026: https://laws.e-gov.go.jp/law/423AC0000000117 |
| 復興特別所得税 from 2027 | 1.1% of 基準所得税額 | 2027 to 2047 | 復興財確法 arts 9 and 13 read at 1 January 2027: https://laws.e-gov.go.jp/law/423AC0000000117 |
| 防衛特別所得税 (defence surtax) | 1% of 基準所得税額 | 2027 onward, 当分の間 | 防衛財確法 art. 5-9 read at 1 January 2027: https://laws.e-gov.go.jp/law/505AC0000000069 |

The prior version's end date of 2037 was right for the law as it stood in 2025 and 2026. From 2027 the 2 surtaxes above add to the same 2.1% (NTA No. 2260 notes), and the reconstruction surtax runs to 2047 on the enacted text.

### Basic deduction (基礎控除)

The test is on 合計所得金額: income before loss carry-forwards under arts 70 and 71 (art. 2(1)(30)), and after the blue return deduction. Residents only: non-residents are refused by R-JP-1.

| 合計所得金額 (JPY) | 2025 | 2026 and 2027 | 2028 onward | Official source |
| --- | --- | --- | --- | --- |
| Up to 1,320,000 | 950,000 | 1,040,000 | 990,000 | 所得税法 art. 86(1) with 措法 art. 41-16-2: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 1,320,000, up to 3,360,000 | 880,000 | 1,040,000 | 620,000 | 所得税法 art. 86(1) with 措法 art. 41-16-2: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 3,360,000, up to 4,890,000 | 680,000 | 1,040,000 | 620,000 | 所得税法 art. 86(1) with 措法 art. 41-16-2: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 4,890,000, up to 6,550,000 | 630,000 | 670,000 | 620,000 | 所得税法 art. 86(1) with 措法 art. 41-16-2: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 6,550,000, up to 23,500,000 | 580,000 | 620,000 | 620,000 | 所得税法 art. 86(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 23,500,000, up to 24,000,000 | 480,000 | 480,000 | 480,000 | 所得税法 art. 86(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 24,000,000, up to 24,500,000 | 320,000 | 320,000 | 320,000 | 所得税法 art. 86(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 24,500,000, up to 25,000,000 | 160,000 | 160,000 | 160,000 | 所得税法 art. 86(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over 25,000,000 | 0 | 0 | 0 | 所得税法 art. 86(1): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1199: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |

**Timing.** The 2026 column comes from text in force on 1 December 2026 and applies to the 2026 year. Year-end adjustment picks it up in December 2026, unless the last 2026 pay fell on or before 30 November, when the new amounts need a return (NTA Q&A of May 2026, Q1-3). Payroll tables change for pay due from 1 January 2027 (Q1-1). The 2025 year stays under the old rule. Prepayments (予定納税) for 2026 do not reflect the change; it is settled on the final return (NTA No. 2040).

### Employment income deduction (給与所得控除)

| Employment receipts (JPY) | 2025 | 2026 and 2027 | Official source |
| --- | --- | --- | --- |
| Up to 1,900,000 | 650,000 | 740,000, or the receipts if less | 所得税法 art. 28(3): https://laws.e-gov.go.jp/law/340AC0000000033; 措法 art. 29-4 at 1 December 2026: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| Over 1,900,000, up to 2,200,000 | receipts × 30% + 80,000 | 740,000 | 所得税法 art. 28(3): https://laws.e-gov.go.jp/law/340AC0000000033; 措法 art. 29-4 at 1 December 2026: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| Over 2,200,000, up to 3,600,000 | receipts × 30% + 80,000 | same | 所得税法 art. 28(3): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| Over 3,600,000, up to 6,600,000 | receipts × 20% + 440,000 | same | 所得税法 art. 28(3): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| Over 6,600,000, up to 8,500,000 | receipts × 10% + 1,100,000 | same | 所得税法 art. 28(3): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |
| Over 8,500,000 | 1,950,000 | same | 所得税法 art. 28(3): https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1410: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm |

Below JPY 6,600,000, income comes from 所得税法 別表第五, not the formula (art. 28(4); NTA No. 1410). For 2026 and 2027, receipts of JPY 691,000 to under JPY 2,200,000 follow 措法 art. 29-4(2), not 別表第五. Use the figure on the 源泉徴収票. Where receipts exceed JPY 8,500,000 and the taxpayer is a special disabled person or has a dependant under 23 or a special disabled spouse or dependant, the 所得金額調整控除 in 措法 art. 41-3-11(1) applies. Art. 41-3-11(2) has a separate rule for pensions, which R-JP-6 stops.

### Blue return special deduction (青色申告特別控除)

The deduction comes off real-estate, business and timber income in the order NTA No. 2072 sets, and cannot exceed that income before loss offset. Failing the Upper limb leaves JPY 550,000; failing a Middle condition leaves JPY 100,000 (NTA No. 2072).

| Tier | Amount | Tax year | Conditions | Official source |
| --- | --- | --- | --- | --- |
| Base | 100,000 | 2025, 2026 | Blue approval, with no further tier condition. The lesser of 100,000 or the income | 措法 art. 25-2(1): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 2072: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Middle | 550,000 | 2025, 2026 | Business, or real-estate income from a business-scale activity; not on the cash basis of art. 67(1); 正規の簿記; balance sheet and profit and loss statement attached; return filed by the deadline. The lesser of 550,000 or the income | 措法 art. 25-2(3) and (6): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 2072: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| Upper | 650,000 | 2025, 2026 | All Middle conditions, and either limb: (1) qualifying electronic books (優良な電子帳簿) under 電子帳簿保存法 art. 8(4); or (2) e-Tax transmission of the return and statements by the deadline. Limb 1 needs the notification filed by the deadline (NTA No. 2072). The lesser of 650,000 or the income | 措法 art. 25-2(4): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 2072: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2072.htm |
| White return | 0 | 2025, 2026 | No special deduction | 措法 art. 25-2 applies to blue filers only: https://laws.e-gov.go.jp/law/332AC0000000026 |
| 2027 base | 100,000 | 2027 onward | As Base, but not for a filer, other than one on the cash basis of art. 67(1), whose 総収入金額 of business or real-estate income in the prior-prior year exceeds 10,000,000, unless the filer meets para. (4) | 措法 art. 25-2(1) and (2) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |
| 2027 upper | 650,000 | 2027 onward | 正規の簿記 and the statements as before, and e-Tax transmission by the deadline. The paper JPY 550,000 tier does not continue | 措法 art. 25-2(4) and (7) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |
| 2027 top | 750,000 | 2027 onward | The 650,000 conditions with electronic books, and either the 優良 requirement in para. (5)(1) or the electronic transaction conditions in para. (5)(2), which are not summarised here | 措法 art. 25-2(5) at 1 January 2027: https://laws.e-gov.go.jp/law/332AC0000000026 |

The cash basis (art. 67(1)) is open to a blue filer whose real-estate and business income for the prior-prior year, before art. 57, totals JPY 3,000,000 or less, on notification (所得税法施行令 art. 195; NTA No. 2072).

### Deductions other than the basic deduction

| Deduction | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Social insurance (社会保険料控除) | Full amount paid in the year, including for a spouse or relative in the same household | 2025, 2026 | 所得税法 art. 74: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1130: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1130.htm |
| Small enterprise mutual aid and iDeCo (小規模企業共済等掛金控除) | Full amount paid in the year | 2025, 2026 | 所得税法 art. 75: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1135: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1135.htm |
| Life insurance (生命保険料控除) | Up to 120,000 in total. New-contract limb cap 40,000, or for 2026 and 2027 60,000 for new life insurance of a filer with a dependant under 23 | 2025, 2026 | 所得税法 art. 76: https://laws.e-gov.go.jp/law/340AC0000000033; 措法 art. 41-15-5(1): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1140: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1140.htm |
| Spouse (配偶者控除) | 380,000 (480,000 if 70 or over) where the taxpayer's 合計所得金額 is up to 9,000,000; 260,000 (320,000) up to 9,500,000; 130,000 (160,000) up to 10,000,000; nil above | 2025, 2026 | 所得税法 art. 83: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1191: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1191.htm |
| Spouse income limit | 合計所得金額 up to 580,000 for 2025; up to 620,000 for 2026. Employment-only spouse: receipts up to 1,230,000 for 2025; up to 1,360,000 for 2026 | 2025, 2026 | NTA No. 1191: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1191.htm |
| Special spouse (配偶者特別控除) | Taxpayer's 合計所得金額 up to 10,000,000. Spouse income over 580,000 up to 1,330,000 for 2025; over 620,000 up to 1,330,000 for 2026. Amount table not reproduced | 2025, 2026 | 所得税法 art. 83-2: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1195: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1195.htm |
| Dependant (扶養控除) | General 380,000; aged 19 to 22 at 630,000; aged 70 or over 480,000, or 580,000 for a lineal ascendant of the taxpayer or spouse who usually lives with either. Age 16 or over. 合計所得金額 up to 580,000 for 2025; up to 620,000 for 2026 | 2025, 2026 | 所得税法 art. 84: https://laws.e-gov.go.jp/law/340AC0000000033; 措法 art. 41-16(1): https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 1180: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1180.htm |
| Specified relative (特定親族特別控除) | Up to 630,000, tapering by the relative's income up to 1,230,000; aged 19 to 22 | 2025, 2026 | 所得税法 art. 84-2: https://laws.e-gov.go.jp/law/340AC0000000033; NTA No. 1177: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1177.htm |

NTA No. 1100 also names 雑損, 医療費, 地震保険料, 寄附金, 障害者, 寡婦, ひとり親 and 勤労学生 deductions. This file gives no amounts for them: Needs Input with the reviewer.

### Inhabitant tax (住民税), for information only

Do not compute this from the national figures. The base differs: for example the basic deduction is JPY 430,000 at the top band, not the national amount, and the tax falls on prior-year income (地方税法 art. 32).

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Prefectural income levy (所得割), standard rate | 4%, or 2% in a designated city | Read at 31 December 2025, 5 November 2026 and 1 January 2027 | 地方税法 art. 35(1): https://laws.e-gov.go.jp/law/325AC0000000226 |
| Municipal income levy, standard rate | 6%, or 8% in a designated city | Same | 地方税法 art. 314-3: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Per-capita levy (均等割), standard rate | 1,000 prefectural and 3,000 municipal | Same | 地方税法 arts 38 and 310: https://laws.e-gov.go.jp/law/325AC0000000226 |
| Forest environment tax (森林環境税) | 1,000 | From fiscal 2024 (令和6年度) | 森林環境税及び森林環境譲与税に関する法律 art. 5: https://laws.e-gov.go.jp/law/431AC0000000003 |
| Basic deduction | 430,000 where prior-year 合計所得金額 is up to 24,000,000 | Same | 地方税法 arts 34 and 314-2: https://laws.e-gov.go.jp/law/325AC0000000226 |

These are standard rates. A local rate above standard was not surveyed, so the charge for any municipality is Needs Input. The upper tiers of the local basic deduction and the 調整控除 in arts 37 and 314-6 were not read in full.

### Asset expensing

| Item | Amount | Tax year | Official source |
| --- | --- | --- | --- |
| Immediate expense | Cost under 100,000, or useful life under 1 year; not assets lent other than as a main business | 2025, 2026 | 所得税法施行令 art. 138: https://laws.e-gov.go.jp/law/340CO0000000096; NTA No. 2100: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2100.htm |
| Pool over 3 years (一括償却資産) | Cost under 200,000; one-third a year; same lending exclusion; a statement of the pooled cost attached to the return for the year of first use and the computation kept (art. 139(2)); a computation schedule attached to the return for each year a third is deducted (art. 139(3)) | 2025, 2026 | 所得税法施行令 art. 139: https://laws.e-gov.go.jp/law/340CO0000000096; NTA No. 2100: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2100.htm |
| Small business immediate expense, acquired to 31 March 2026 | Under 300,000 each; total 3,000,000 a year, scaled by months in a start or cease year | 2025, 2026 | 措法 art. 28-2 read at 31 December 2025: https://laws.e-gov.go.jp/law/332AC0000000026 |
| Small business immediate expense, acquired 1 April 2026 to 31 March 2029 | Under 400,000 each; same annual total | 2026 | 措法 art. 28-2 read at 5 November 2026: https://laws.e-gov.go.jp/law/332AC0000000026; NTA No. 2100: https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2100.htm |
| Small business test | Blue filer who is a 中小事業者 with 500 or fewer regular employees for an acquisition before 1 April 2026, or 400 or fewer for one on or after that date | 2025, 2026 | 措法施行令 art. 18-5(1), and 附則 of 政令第98号 of 2026 (in force 1 April 2026): https://laws.e-gov.go.jp/law/332CO0000000043 |

The small business limb needs a schedule attached to the return (措法 art. 28-2). It excludes assets taken under arts 138 and 139 of the order and assets lent other than as a main business; 措法施行令 art. 18-5(2) lists further exclusions under special depreciation rules, which are not reproduced here. The cost is tax-inclusive or tax-exclusive according to the taxpayer's consumption tax accounting method (NTA No. 2100).

### Depreciation

Art. 49(1) and 所得税法施行令 art. 125 make the straight-line method (定額法) the statutory method for an individual with no election. The declining-balance method (定率法) needs an election notified by 15 March of the year after the business starts (NTA No. 2100). The prior version's table showed declining-balance rates only.

| Asset | Useful life | 定額法 rate | 200% 定率法 rate, acquired from 1 April 2012 | Official source |
| --- | --- | --- | --- | --- |
| Personal computer, not a server | 4 | 0.250 | 0.500 | 耐用年数省令 別表第一, 第八, 第十: https://laws.e-gov.go.jp/law/340M50000040015 |
| Other computer, including a server | 5 | 0.200 | 0.400 | 耐用年数省令 別表第一, 第八, 第十: https://laws.e-gov.go.jp/law/340M50000040015 |
| Office furniture, mainly metal | 15 | Not read | Not read | 耐用年数省令 別表第一: https://laws.e-gov.go.jp/law/340M50000040015 |
| Office furniture, other (including wood) | 8 | 0.125 | 0.250 | 耐用年数省令 別表第一, 第八, 第十: https://laws.e-gov.go.jp/law/340M50000040015 |
| Ordinary motor vehicle, other than the special classes | 6 | 0.167 | 0.333 | 耐用年数省令 別表第一, 第八, 第十: https://laws.e-gov.go.jp/law/340M50000040015 |
| Light vehicle, up to 0.66 litres | 4 | 0.250 | 0.500 | 耐用年数省令 別表第一, 第八, 第十: https://laws.e-gov.go.jp/law/340M50000040015 |
| Software, master for copying and sale | 3 | Not read | Straight-line only | 耐用年数省令 別表第三: https://laws.e-gov.go.jp/law/340M50000040015; 所得税法施行令 art. 120-2: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Software, other | 5 | 0.200 | Straight-line only | 耐用年数省令 別表第三, 第八: https://laws.e-gov.go.jp/law/340M50000040015; 所得税法施行令 art. 120-2: https://laws.e-gov.go.jp/law/340CO0000000096 |

The 200% 定率法 switch rates also matter: use 別表第十 for 改定償却率 and 保証率 rather than the rate above alone.

### Enactment position

- **Law for 2025.** 所得税法, 租税特別措置法 and related Acts as they stood at 31 December 2025.
- **Enacted changes.** 所得税法等の一部を改正する法律 (令和8年法律第12号), promulgated on 31 March 2026, enacted the 2026 basic deduction, the JPY 740,000 employment floor, the income limits for spouses and dependants, the JPY 400,000 expensing limit, the 2027 blue return tiers and the 2027 surtax split. It was read only as consolidated into dated e-Gov text and through its 附則 as abridged there. The Act itself could not be retrieved by its id. The Ministry of Finance's bill as submitted on 20 February 2026 was read for 附則 art. 1 only; a bill is not the Act, and whether the Diet amended it was not checked.
- **Very high income from 2027.** Text from 1 January 2027 lowers the threshold in 措法 art. 41-19(1) to JPY 165,000,000 and sets 30%, for 2027 onward. R-JP-7 stops any 2027 computation.
- **Outlines.** A 税制改正大綱 is a proposal, not law. The 令和8年度 大綱 is listed on the Ministry of Finance page; no figure here rests on it. For 令和9年度 the Ministry's page showed only departmental requests. No proposal for a later year is used here.
- **Practice.** The 手引き and NTA pages are administrative texts. Where a row rests on one, the row says so.

## The base

### Income

**Category.** Business income (事業所得) is income from the businesses named by order (art. 27(1)), and is revenue less necessary expenses (art. 27(2)). Whether side work is business income or miscellaneous income (art. 35) is a question of fact, and R-JP-6 stops the file if it is miscellaneous. Keep each receipt in its own category:

| Receipt | Category | Treatment here |
| --- | --- | --- |
| Professional fees, contract income, product sales | 事業所得, art. 27 | Revenue, at the gross amount before withholding |
| Salary | 給与所得, art. 28 | Employment receipts, from the 源泉徴収票 |
| Deposit interest | 利子所得, art. 23 | General interest paid in Japan is taxed separately at 15% national rate (措法 art. 3(1)). Not in business revenue. Exceptions in art. 3(1) were not listed here: Needs Input |
| Dividends | 配当所得, art. 24 | Not in business revenue. R-JP-6 |
| Public pension, other 雑所得 | Art. 35 | R-JP-6 |

**Consumption tax.** Revenue is net or gross of consumption tax according to the method used, not according to registration alone: a business may choose 税抜経理 or 税込経理 (NTA No. 6901; 平元直所3-8 para. 2). Under 税込経理 the tax collected is revenue and the tax payable is a necessary expense. A business exempt under 消費税法 art. 9(1) uses 税込経理 even if its books separate the tax (平元直所3-8 para. 5; NTA No. 2100 注5).

**Timing.** Necessary expenses are the amounts for which the obligation was fixed in the year (NTA No. 2210). A payment in the year with no fixed obligation is not an expense of that year, and the reverse also holds. A blue filer on the art. 67(1) cash basis is the exception. A prepayment for continuing services is not an expense of the year paid to the extent the services fall after 31 December. 所得税基本通達 37-30の2 accepts deduction in the year paid where the services fall within 1 year of payment and the filer treats such payments that way consistently. So the part after 31 December is Needs Input until that practice is confirmed.

### Expenses

Necessary expenses are the cost of sales and other costs directly required to earn the revenue, and the selling, general administrative and other business costs of the year. Costs other than depreciation whose obligation is not fixed in the year are left out (art. 37(1)).

**Mixed use.** Household expenses and related costs are not deductible (art. 45(1)(1)), except under 所得税法施行令 art. 96: (1) the main part of the cost is necessary for the business and that part is clearly separable; or (2) for a blue filer, the part shown by records to be directly necessary for the business. NTA No. 2210 states the test as a clear split on the basis of transaction records. Apply this to home rent, electricity, internet, phone and vehicle running costs. No text read sets a percentage: the prior version's 20% to 50% range has no source, and floor-area or time methods are not stated in any text read. Hold those as reviewer questions, and state the record relied on.

**Vehicles.** The same test applies to fuel, insurance, vehicle taxes and depreciation. A mileage log is one way to meet it; no text read makes it the only way.

**Entertainment.** No cap on an individual's entertainment costs was found. 措法 art. 61-4 limits 法人 only; a word search of the consolidated 所得税法, its order and 措法 found no such limit on an individual. That search covers those 3 texts only. The art. 37 and art. 45 tests still apply: record date, venue, attendees and purpose as a working standard, not a legal list.

**Family.** Payments to a relative in the same household are generally not necessary expenses (art. 56). Exceptions:

- **Blue:** salaries to a family employee aged 15 or over at year-end, working mainly in the business for more than 6 months of the year, are deductible at the notified amount where reasonable. Where the business did not run all year, or death, long illness, marriage or a similar reason meant the relative could not work in it all year, more than half the period they could work is enough (所得税法施行令 art. 165(1) proviso, which is limited to art. 57(1)). Notify by 15 March, or within 2 months of the business starting or of the relative becoming a family employee, where that falls on or after 16 January (art. 57(1) and (2); NTA No. 2075).
- **White:** for a relative in the same household, aged 15 or over at year-end, working mainly in the business for more than 6 months of the year: the lesser of JPY 860,000 for a spouse or JPY 500,000 for another relative, or income before this deduction ÷ (number of family employees + 1) (art. 57(3)). The return must state the claim (art. 57(5)). The half-period test in the Blue bullet does not apply (所得税法施行令 art. 165(1)). The prior version had the 2 amounts reversed.
- **Both:** a relative paid as a family employee is not counted as a spouse or dependant for those deductions (art. 2(1)(33) and (34)). 所得税法施行令 art. 165(2) leaves out of the period any time as a student or in another occupation, unless it does not stop the relative working mainly in the business (as with an evening student working by day, or short hours in the other job), and any time when age or disability seriously impairs the ability to work. Real-estate income qualifies only where the letting is a business (NTA No. 2075 注2).

**Not deductible.** Income tax (art. 45(1)(2), which excepts certain 利子税) and the 加算税 on it, which 国税通則法 art. 69 treats as the same tax; 延滞税 and the 加算税 on other national taxes (art. 45(1)(3)); inhabitant tax (art. 45(1)(4)); and the forest environment tax (art. 45(1)(3-2)). 延滞税 on income tax follows item 2 on inference: item 3 covers only other taxes and 所得税基本通達 files item 2 under 附帯税, but no text read names it. A reviewer should confirm.

**Assets.** Use the Asset expensing and Depreciation tables. Land is outside depreciation. Subscriptions are not depreciable assets where the contract grants access for the period only; a perpetual licence is an intangible asset to test against the expensing limits.

### Allowances, ladder and ordering

Follow this ladder (arts 89 and 120; 手引き p. 27):

1. Business income = before-deduction income − `min(tier amount, max(before-deduction income, 0))`, where before-deduction income = revenue − necessary expenses.
2. Employment income = receipts − employment income deduction − any 所得金額調整控除.
3. 合計所得金額 = business income + employment income (losses are offset under art. 69 first).
4. Carried loss used = `min(eligible carried loss, max(合計所得金額, 0))`, under arts 70 and 71. See Losses for what is eligible.
5. Taxable income = `floor(max(合計所得金額 − carried loss used − all 所得控除, 0) / 1,000) × 1,000`.
6. Income tax = taxable income × rate − deduction amount.
7. Surtax = `floor(基準所得税額 × 2.1%)`. For 2026 the rounding is carried from the 2025 手引き (see Surtaxes).
8. Tax after withholding = income tax + surtax − withholding credits. If positive, round down to JPY 100; if negative, keep the exact amount.
9. Balance = line 8 − prepayments. Positive: pay. Negative: refund.

Step 3 sets the basic deduction band and every other 合計所得金額 test, so the blue return deduction can change them and a carried loss cannot (art. 2(1)(30)). Examples 1 and 7 show this.

### Losses

- **Offset in the year.** Business losses offset other income under art. 69 (NTA No. 2250).
- **Blue carry-forward.** Net loss of a year with a blue return carries forward 3 years (art. 70(1)). Art. 70(4) needs a return for the loss year and a return for every year after it; those later returns need not be blue.
- **White carry-forward.** Limited to 変動所得 losses and 被災事業用資産 losses, also 3 years (art. 70(2)). The prior version said white filers could carry nothing.
- **Specified disasters.** Art. 70-2 gives 5 years for the cases it names (NTA No. 2070).
- **Using a carried loss.** Step 4 takes only a loss that meets all of these: it arose in the 3 years before this one, or 5 under art. 70-2; it falls under art. 70(1) or (2); the art. 70(4) returns exist; it has not been deducted already or used for a carry-back refund; and a return is filed for this year (art. 70(1) and (2)). Art. 71 carries 雑損失 3 years on the same return condition (art. 71(1) and (2)), or 5 under art. 71-2. Losses go by year, oldest first, across both kinds, so an older 雑損失 comes before a newer net loss (所得税法施行令 arts 201(1) and 204(2)). Within one year, the art. 70 loss comes before the art. 71 loss (art. 204(2)). An ordinary loss from the year of a 5-year loss under art. 70-2 or 71-2, or from the year after it, counts as older than that 5-year loss (arts 201(2) and 204(3)). The amount left over carries on until its period ends.
- **Reporting it.** 手引き p. 29 puts a carried loss used up this year in 第一表 本年分で差し引く繰越損失額, and tells 第四表 users to leave that box blank.
- **Other measures.** 総所得金額等 is after these losses (手引き p. 39), unlike 合計所得金額. The 40% limit in art. 78 is one test measured on the later figure.
- **Carry-back.** A blue filer who filed blue for the prior year and files on time may claim a refund for the prior year (art. 140(1) and (4)). Art. 140(5) covers the year a business is wholly transferred or ended, and art. 142 the claim procedure. Not computed here.

### Withholding

**Which fees.** Tax is withheld by a payer of the fees listed in art. 204(1), paid to a resident in Japan. There is no JPY 1,000 threshold, and the fact that the payer is a corporation does not decide it. The test is the type of payment and the payer:

| Limb of art. 204(1) | Payment |
| --- | --- |
| 1 | Manuscripts, illustrations, composition, record recording, design, broadcast fees, copyright and industrial property royalties, lecture fees and others named by order |
| 2 | Lawyers, 司法書士, 土地家屋調査士, certified public accountants, tax accountants, 社会保険労務士, patent attorneys, 海事代理士, surveyors, architects, real estate appraisers, professional engineers (技術士) and others named by order |
| 3 | 診療報酬 paid under 昭和23年法律第129号, named 社会保険診療報酬支払基金法 in the text at 31 December 2025 and 医療情報基盤・診療報酬審査支払機構法 in the text at 5 November 2026 |
| 4 | Professional baseball players, professional boxers, jockeys, models, sales agents (外交員), collectors, meter readers and others named by order |
| 5 | Appearance, direction or planning fees for film, theatre, other entertainment named by order, radio and television, and fees for entertainers' services through a business, unless received from unspecified members of the public |
| 6 | Hostesses and others whose work is attending customers in the cabarets, night clubs and bars the limb describes |
| 7 | Lump-sum contract money for promising services, as named by order |
| 8 | Advertising prizes and racehorse owners' prizes, as named by order |

Art. 204(2)(1) excludes payments that are employment income or retirement allowances. Art. 204(2)(2) excludes limbs 1 to 5, 7 and 8 where the payer is an individual who is not a payroll withholding agent under art. 183. Art. 204(2)(3) limits limb 6 to bar operators and payments through them. Prizes for submitted works and contribution fees need no withholding at JPY 50,000 or less per payment to one person (NTA Nos. 2792 and 2795). The further lists in 所得税法施行令 art. 320 were read for its heading only and are not reproduced: test a fee outside the plain words against that article.

**Rate.** Art. 205 has 2 items. The 10.21% and 20.42% below are the 10% and 20% in art. 205 with the surtax. Tax is rounded down to JPY 1. The base includes consumption tax unless the invoice separates it (NTA Nos. 2792 and 2798).

- **Item 1:** limbs 1, 2, 4, 5 and 7, other than the payments in item 2. Fee up to JPY 1,000,000 per payment: fee × 10.21%. Above: (fee − 1,000,000) × 20.42% + 102,100 (art. 205 item 1; NTA Nos. 2792, 2795 and 2798).
- **Item 2:** the payments in the table below. `max(payment − amount deducted, 0)` × 10.21%, with no higher band. A payment at or below the amount deducted leaves no 残額, so nothing is withheld (art. 205 item 2; 所得税法施行令 art. 322; NTA No. 2801).

| Item 2 payment | Measured on | Amount deducted | Source |
| --- | --- | --- | --- |
| 司法書士, 土地家屋調査士, 海事代理士 (limb 2) | Each payment to one person | 10,000 | 所得税法施行令 art. 322: https://laws.e-gov.go.jp/law/340CO0000000096 |
| 診療報酬 (limb 3) | The month's amount to one person | 200,000 | 所得税法施行令 art. 322: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Professional boxers (limb 4) | Each payment to one person | 50,000 | 所得税法施行令 art. 322: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Sales agents (外交員), collectors, meter readers (limb 4) | The month's payments to one person | 120,000, less any salary the same payer pays that person in the month | 所得税法施行令 art. 322: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Limb 6 fees | Each payment to one person | 5,000 × days in the payment's calculation period, less any salary the same payer pays for that period | 所得税法施行令 art. 322: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Advertising prizes (limb 8) | Each payment to one person | 500,000 | 所得税法施行令 art. 322: https://laws.e-gov.go.jp/law/340CO0000000096 |
| Racehorse owners' prizes (limb 8) | Each payment to one person | 20% of the prize + 600,000 | 所得税法施行令 arts 298(1) and 322: https://laws.e-gov.go.jp/law/340CO0000000096 |

So a 外交員 paid JPY 300,000 in a month, with no salary from that payer, has (300,000 − 120,000) × 10.21% = JPY 18,378 withheld. A 司法書士 paid JPY 12,000 in one payment has (12,000 − 10,000) × 10.21% = JPY 204 withheld. For a 司法書士, 土地家屋調査士 or 海事代理士, one payment means the amount payable under one 委託契約, or the amount paid together where the contract pays a period's 委託契約 as one sum. It is not necessarily each bank transfer (所得税基本通達 205-1 and 205-2(1)). This file treats the salary reductions in the table as stopping at nil, so salary above the limit does not add to the payment. That is an inference: 所得税基本通達 205-5 withholds on the fee above the 残額 of JPY 120,000 after salary, but no text read states the nil case.

**Credit.** Tax withheld or required to be withheld is credited on the return (art. 120(1)(4)) and refunded if it exceeds the tax (art. 138).

**Evidence.** Art. 225 has the payer file a 支払調書 with the tax office. No duty to give the payee a copy was found in the parts read. So accept any of: a 支払調書 copy, a client payment notice, the invoice showing the withheld line, or another record stating gross, tax and net. A bank line alone does not prove the gross. The prior version also called this a 源泉徴収票, which is the employment slip.

### Defaults

A default stands only where the law read fixes the result of the missing fact. Everything else is Needs Input.

| Situation | Treatment | Basis |
| --- | --- | --- |
| Return type unknown | Needs Input. Blue needs approval, so do not assume white or blue; show both results as Example 1 does | Arts 143 to 147 |
| No blue approval on the facts | Default stands: white return, no deduction | Art. 143; 措法 art. 25-2 |
| Blue approval confirmed, books or filing conditions unproved | Default stands at JPY 100,000 for 2025 or 2026, with the higher tier and its effect disclosed | 措法 art. 25-2(1); NTA No. 2072 |
| Mixed-use cost with no record or split | Default stands: not deducted until a limb of the order is shown. Flag as Needs Input | Art. 45(1)(1); 所得税法施行令 art. 96 |
| Business or personal character unclear | Default stands: not deducted. Flag as Needs Input | Arts 37 and 45 |
| Withholding credit not evidenced | Needs Input. Leave the credit out of the computed figure, and ask for a document listed under Evidence | Art. 120(1)(4) |
| Receipt of unclear nature | Needs Input, in a suspense line | Art. 27 |
| Family, age or disability deduction unclear | Needs Input | Arts 79 to 84-2 |
| Carried loss with any test under Losses unproved, including one from an unseen year | Needs Input, and the dependent calculation is held. Step 4 may appear only as 2 provisional scenarios, as Cases A and B in Example 7 do: nil, and the claimed loss. Label each 'estimated, not reviewed'. Neither is settled until the loss-year return and each return since are seen | Arts 70(1), (2) and (4) and 71 |
| Prepayment without a notice or payment record | Needs Input | Arts 104 and 120(2) |
| Asset cost, life or date unknown | Needs Input | Asset expensing table |
| Local rate of inhabitant tax unknown | Needs Input | 地方税法 arts 35 and 314-3 |

### Reviewer attention thresholds

Each row is a flag, not a rule of law, unless a source is shown.

| Flag | Threshold | Action |
| --- | --- | --- |
| Consumption tax liability | Base-period taxable sales (the year before last, 消費税法 art. 2(1)(14)) above JPY 10,000,000; or specified-period sales above JPY 10,000,000, with the payroll alternative in 消費税法 art. 9-2; or a registered 適格請求書発行事業者, whatever the sales (消費税法 art. 9(1)) | Check status; use `jp-consumption-tax` |
| Withholding on fees | Any amount within art. 204(1) | Check gross, tax and evidence |
| Blue return application | The art. 144 date in Deadlines and filing | Check approval |
| Deemed blue approval | No refusal or approval by 31 December of the year, or 15 February next where the business started on or after 1 November (art. 147) | Check the date |
| Prior-prior year revenue | Above JPY 10,000,000 | The 2027 JPY 100,000 rule; note it for 2027 planning only |
| Loss carry-forward | Any | Check return history |
| Asset expensing | Each item at or above JPY 100,000; the total of JPY 3,000,000 | Test the limb |
| Entertainment | High against revenue; no text read sets a level | Reviewer judgement |
| Family salaries in bank data | Any | Check the notification |
| Large iDeCo or mutual aid amounts | Any | Confirm from contribution statements |

### Classifying a bank line

Use this as a pre-classifier. If no pattern fits, apply the rules above. Each row assumes the item is confirmed as the taxpayer's own. A Stripe, PayPal, Amazon Pay, BASE or Mercari payout can be net of fees: use the platform statement for gross revenue and fees.

**Credits (入金)**

| Pattern | Tax line | Treatment | Notes |
| --- | --- | --- | --- |
| 振込 [client name] / 入金 [client company] | 事業収入 | Gross revenue | Professional fee from client |
| 銀行振込 [sender] / 普通振込 | 事業収入 | Revenue | Standard bank transfer from client |
| STRIPE PAYOUT / STRIPE TRANSFER | 事業収入 | Revenue | Stripe Japan or international clients; match to invoices |
| PAYPAL TRANSFER / ペイパル | 事業収入 | Revenue | International client payments |
| freee PAYMENT / フリー支払 | 事業収入 | Revenue | freee Payments platform settlement |
| Amazon Pay 振込 / Amazonペイ | 事業収入 | Revenue | E-commerce platform payout |
| BASE SETTLEMENT / BASE振込 | 事業収入 | Revenue | BASE (JP e-commerce) settlement |
| メルカリ振込 / MERCARI | 事業収入 | Revenue if business | Mercari business seller payout; personal goods sales are a question for the reviewer |
| 報酬振込 [client] | 事業収入 | Revenue | Honorarium or professional fee |
| 源泉徴収後振込 [amount] | 事業収入 | Revenue at gross | Client withheld tax. Use the document for the gross: see Withholding |
| 給与振込 [employer] | 給与所得 | Not business income | Use the 源泉徴収票 |
| 利子 / 利息 [bank] | 利子所得 | Not business income | See Income |
| 配当金 [company] | 配当所得 | Not business income | R-JP-6 |
| 還付金 国税局 / 税金還付 | Exclude | Not income | Refund of non-deductible tax. A consumption tax refund under 税込経理 is revenue (NTA No. 6901) |
| 贈与 / 振込 PERSONAL | Exclude | Personal transfer | Gifts and personal transfers; gift tax is out of scope |

**Debits (出金)**

| Pattern | Tax line (必要経費) | Treatment | Notes |
| --- | --- | --- | --- |
| 事務所賃料 / オフィス家賃 [landlord] | 地代家賃 | Deductible if dedicated business premises | Rent to a relative in the same household falls under art. 56 |
| 電気料金 [TEPCO/関西電力/中部電力/九州電力] | 水道光熱費 | Business part only | Art. 96 of the order |
| 水道料金 / 水道局 | 水道光熱費 | Business part only | Art. 96 of the order |
| インターネット [NURO/フレッツ/au/ドコモ光] | 通信費 | Business part only | Ask the client for the split and its record |
| 携帯電話 [ドコモ/au/SoftBank/楽天モバイル] | 通信費 | Business part only | Mixed use: art. 96 of the order |
| 交通費 [JR/東京メトロ/新幹線/バス] | 旅費交通費 | Deductible if business | IC card statements are a practical record; no text read names them |
| 航空券 [ANA/JAL/LCC] | 旅費交通費 | Deductible if business purpose | Keep the booking confirmation |
| 接待 [restaurant] / 飲食 | 接待交際費 | Deductible if the art. 37 test is met | See Entertainment |
| 書籍 [Amazon Japan/紀伊國屋/丸善] | 新聞図書費 | Deductible if professional | Art. 37 |
| セミナー [event] / 研修費 | 研修費 | Deductible if for the business | Art. 37 |
| ソフトウェア [Adobe/Microsoft/Figma/Notion] | 消耗品費 or 減価償却費 | Purchased licence under JPY 100,000: expense. At or above: test the limits | Subscription and perpetual licence differ |
| 広告費 [Google Ads/Meta Ads] | 広告宣伝費 | Deductible | Art. 37 |
| 税理士報酬 / 会計士報酬 | 税理士・弁護士費用 | Deductible if for the business | Personal matters are not. The payer may have to withhold |
| 損害保険 [business] | 損害保険料 | Deductible | Business liability only |
| 外注費 / フリーランス費用 | 外注工賃 | Deductible | The payer may have to withhold |
| 銀行手数料 / 振込手数料 | 雑費 | Deductible | Business account only |
| 国民年金 / 国民年金保険料 | 社会保険料控除, not 必要経費 | Exclude | 所得控除 |
| 国民健康保険 / 国保料 | 社会保険料控除, not 必要経費 | Exclude | 所得控除 |
| 所得税 振替 / 住民税 口座振替 | Exclude | Tax payments | Not deductible |
| 消費税 振替 | 租税公課 under 税込経理 only | Depends on the method | NTA No. 6901 |
| 生命保険 [Nippon Life/Dai-ichi/明治安田] | 生命保険料控除, not 必要経費 | Exclude | Personal insurance is a 所得控除 |
| プライベート引き出し / ATM出金 | Exclude | Personal withdrawal | Drawings; ask what it was for |

**SaaS and cloud services.** Each is carried from the prior version as 消耗品費 and deductible if for the business, subject to the mixed-use and timing rules above: Adobe Systems / Adobe Creative Cloud (check whether annual or monthly), Microsoft / Office 365 / M365, Google Workspace / G Suite, freee / Money Forward Cloud / Yayoi (accounting software), Slack / Notion / Figma and AWS Japan / Amazon Web Services (cloud hosting). The account name is a bookkeeping choice, not a rule of law.

### Bank formats

Carried from the prior version; not checked against bank files.

| Bank | Format | Key fields |
| --- | --- | --- |
| 三菱UFJ (MUFG) | CSV / PDF | 日付, 摘要, お引出し, お預入れ, 残高 |
| みずほ銀行 (Mizuho) | CSV | 取引年月日, 摘要, お支払金額, お預り金額, 差引残高 |
| 三井住友銀行 (SMBC) | CSV / PDF | 年月日, 摘要, 支払金額, 預入金額, 残高 |
| 楽天銀行 (Rakuten Bank) | CSV | 取引日, 入出金(円), 残高(円), 取引名称, 利用先 |
| ゆうちょ銀行 (Japan Post Bank) | CSV | 年月日, 摘要, 支払金額, 預入金額, 差引残高 |
| 住信SBIネット銀行 (SBI Sumishin) | CSV | 取引日, 内容, 出金金額, 入金金額, 残高 |

| Japanese term | English | Classification hint |
| --- | --- | --- |
| 振込入金 | Wire transfer in | Potential income |
| 振込出金 / 振込手数料 | Wire transfer out / fee | Potential expense or bank fee |
| 自動振替 | Auto debit | Regular expense (utilities, insurance) |
| カード利用 | Card payment | Identify payee |
| ATM出金 | ATM withdrawal | Personal; ask purpose |
| 利息 / 利子 | Interest | Other income |
| 税金 口座振替 | Tax payment auto-debit | Exclude (tax payment) |
| 国民年金 振替 | Pension auto-debit | Income deduction (not expense) |
| 国保 振替 | Health insurance auto-debit | Income deduction (not expense) |

### Excel working paper

```
確定申告 WORKING PAPER -- Tax Year ____ -- estimated, not reviewed
Taxpayer: _______________  My Number: not recorded in this paper
Return type: Blue (正規の簿記 / simplified) / White [circle one]
Filing method: e-Tax / Paper [circle one]

A. 事業収入 (BUSINESS REVENUE)
  A1. Total invoiced, at gross before withholding  ___________
  A2. Less: consumption tax, under 税抜経理 only   ___________
  A3. Net business revenue                    ___________

B. 必要経費 (NECESSARY EXPENSES)
  B1. 地代家賃 (rent / office costs)          ___________
  B2. 水道光熱費 (utilities, business part)   ___________
  B3. 通信費 (phone/internet, business part)  ___________
  B4. 旅費交通費 (travel)                    ___________
  B5. 接待交際費 (entertainment)             ___________
  B6. 広告宣伝費 (advertising)              ___________
  B7. 消耗品費 (consumables / SaaS)         ___________
  B8. 減価償却費 (depreciation)             ___________
  B9. 外注工賃 (subcontracting)             ___________
  B10. 税理士費用 (adviser fees)            ___________
  B11. 雑費 (bank charges, misc)            ___________
  B12. Total 必要経費                        ___________

C. 事業所得 BEFORE DEDUCTION (A3 - B12)      ___________

D. 青色申告特別控除 (Blue return deduction, at most C)  ___________

E. 事業所得 (C - D)                          ___________

E2. 給与所得 (from the 源泉徴収票)            ___________

E3. 合計所得金額 (E + E2, for the basic deduction band)  ___________

E4. 繰越損失 used (arts 70 and 71, at most E3 if positive)  ___________

F. 所得控除 (INCOME DEDUCTIONS)
  F1. 基礎控除 (basic deduction)            ___________
  F2. 社会保険料控除 (NHI + pension)        ___________
  F3. 小規模企業共済等 (iDeCo, etc.)       ___________
  F4. 生命保険料控除                        ___________
  F5. 配偶者控除 / 扶養控除               ___________
  F6. Total 所得控除                        ___________

G. 課税所得 (E3 - E4 - F6, at least 0) -- round down to 1,000  ___________

H. 所得税 (apply rate table)                 ___________

I. 復興特別所得税 (H x 2.1%, round down to 1)  ___________

J. TOTAL NATIONAL TAX (H + I)               ___________

K. 源泉徴収税額 (withholding credits)       ___________

K2. J - K: if positive, round down to 100; if negative, keep exactly  ___________

L. 予定納税 (estimated tax credits)         ___________

M. NET TAX DUE / REFUND (K2 - L)           ___________

REVIEWER FLAGS:
  [ ] Blue approval evidenced?
  [ ] Bookkeeping method and tier conditions confirmed?
  [ ] Mixed-use split supported by records?
  [ ] Withholding credits checked against a document stating gross, tax and net?
  [ ] National pension / NHI certificates confirmed?
```

## Deadlines and filing

| Item | Deadline | Basis |
| --- | --- | --- |
| Final return, 2025 year | 16 February to 16 March 2026 (15 March was a Sunday). A refund return may be filed earlier | 所得税法 art. 120(1); 国税通則法 art. 10(2); 手引き |
| Tax payment, 2025 year | 16 March 2026 | 手引き p. 2 |
| Direct debit (振替納税), 2025 year | Debit on 23 April 2026, if the return was filed by the deadline; application by 16 March 2026 | 手引き p. 2 |
| Final return and payment, 2026 year | 16 February to 15 March 2027. The date set for 振替納税 for that year was not read | 所得税法 art. 120(1); NTA No. 2020 |
| Blue return application | By 15 March of the first blue year, or within 2 months where the business started on or after 16 January | Art. 144 |
| Family employee notification | By 15 March of the year, or within 2 months of the business starting or of the relative becoming a family employee, where that falls on or after 16 January | Art. 57(2); NTA No. 2075 |
| Prepayment (予定納税), 1st instalment | 1 to 31 July | Art. 104(1) |
| Prepayment, 2nd instalment | 1 to 30 November | Art. 104(1) |
| Inhabitant tax (普通徴収) | June, August, October and January, unless the municipality's ordinance differs | 地方税法 art. 320 |

A date on a Saturday, Sunday or public holiday moves to the next day that is none of these (国税通則法 art. 10(2); NTA No. 2040). So the blue application for 2026 was due on 16 March 2026, and the 2nd prepayment for 2025 on 1 December 2025.

**Must file.** Whether the taxpayer must file turns on art. 120(1): tax on income after deductions exceeds the dividend credit, together with any home loan credit taken at year-end adjustment (NTA No. 2020). A salaried person is usually settled by year-end adjustment but must file in the listed cases, including: employment receipts above JPY 20,000,000; one employer, fully withheld, and other income above JPY 200,000; 2 or more employers on the stated test (NTA No. 2020; 手引き p. 3). A 同族会社 director limb also appears in the 手引き; it was not read in full.

**Forms.** 確定申告書 第一表 and 第二表; 第三表 for separately taxed income; 第四表 for losses (NTA forms page for 令和7年分). Blue filers attach the 青色申告決算書. White filers attach the document stating revenue and expenses, the 収支内訳書 (art. 120(6); NTA No. 2080). Identity documents for My Number are required as the 手引き states (手引き 4-1).

**Filing routes.** e-Tax, on the 確定申告書等作成コーナー or other software, or on paper at the tax office. The route matters for the blue return tier.

**Payment.** 振替納税; ダイレクト納付; internet banking or ATM; credit card (under JPY 10,000,000, with a fee); smartphone app (up to JPY 300,000); convenience store QR (up to JPY 300,000); cash at a bank or tax office (手引き p. 2).

**Prepayment amount.** Applies where the 予定納税基準額 is JPY 150,000 or more; the prior version said 'exceeded'. Each instalment is one-third of that base, rounded down to JPY 100 (art. 104(1) and (3)). The base is the prior year's tax on a recurring-income footing, fixed at 15 May (art. 105), and the NTA gives notice by 15 June (NTA No. 2040). It is not simply one-third of last year's total tax. `jp-estimated-tax` owns the computation.

**Amendments.** A 修正申告 raises the tax; 更正の請求 lowers it, generally within 5 years of the statutory deadline (NTA No. 2026).

**Blue records.** 所得税法 art. 148 and NTA No. 2070: books kept in the required form, retained 7 years, some documents 5 years. Inherited-business timing is in NTA No. 2070 and was not reproduced.

## Penalties and interest

| Offence | Penalty | Basis |
| --- | --- | --- |
| Under-reporting (過少申告加算税) | 10% of the additional tax; 5% in place of 10% where the amended return follows a notice of investigation but the correction was not foreseen (art. 65(1)); a further 5% on the part above the greater of the timely tax or JPY 500,000 (art. 65(2)). Nil if amended voluntarily before the notice of investigation (art. 65(6)) | 国税通則法 art. 65 |
| Late filing (無申告加算税), after investigation or assessment | 15% to JPY 500,000, 20% to JPY 3,000,000 and 30% above, for returns due from 1 January 2024 | 国税通則法 art. 66(1) to (3); NTA No. 2024 |
| Late filing, after notice of investigation but not foreseen | 10%, 15% and 25% on the same bands | 国税通則法 art. 66(1) to (3); NTA No. 2024 |
| Late filing, voluntary before notice of investigation | 5% | 国税通則法 art. 66(8) |
| Late filing within 1 month of the deadline | Nil if art. 66(9) is met: filed within 1 month, not foreseen, and intent to file on time shown as the order sets. NTA No. 2024 lists full payment by the deadline and no recent penalty or use of this rule | 国税通則法 art. 66(9); NTA No. 2024 |
| Repeat late filing | A further 10% of the tax for repeats named in art. 66(6) | 国税通則法 art. 66(6) |
| Records not produced | Further 5% or 10% rates under arts 65(4) and 66(5) | 国税通則法 arts 65(4), 66(5) |
| Fraud or concealment (重加算税) | 35% in place of 過少申告加算税; 40% in place of 無申告加算税; a further 10% on a repeat | 国税通則法 art. 68(1), (2), (4) |
| Late payment interest (延滞税), 2025 | 2.4% for the first 2 months, 8.7% thereafter | 国税通則法 art. 60(2); 措法 art. 94; NTA 延滞税の割合 |
| Late payment interest, 2026 | 2.8% and 9.1% | Same |

Penalty and interest bases round down under 国税通則法 art. 118(3): to JPY 10,000. Final amounts round down to JPY 100 and drop to nil under JPY 1,000, or JPY 5,000 for 加算税 (art. 119(4)). 延滞税 runs from the day after the statutory due date until the tax is paid in full (art. 60(2)). The lower rate covers the period to the 納期限 and 2 months after it (art. 60(2)); confirm the 納期限 of a late or amended return with the reviewer.

## Cross-border points

- **Scope.** A resident other than a non-permanent resident is taxed on all income wherever arising (art. 7(1)(1); NTA No. 2010). R-JP-5 stops non-permanent residents.
- **Treaties.** A person resident in 2 countries needs the treaty tie-breaker (NTA No. 2875). R-JP-9 applies.
- **Foreign clients.** Fees from clients abroad are business revenue in yen. Art. 57-3(1) converts at the exchange rate at the time of the transaction. 所得税基本通達 57の3-2 uses the mid rate (仲値) on the transaction date or, if applied consistently for business income, the buying rate for income and the selling rate for expenses. Confirm the rate used with the reviewer.
- **Foreign withholding.** R-JP-9 applies.
- **Excluded jurisdictions.** The prior version names no fixed excluded jurisdiction, and this file adds none.

## Two worked examples that recompute

All names are fixtures. Each example shows a decision. Figures are estimates, labelled 'estimated, not reviewed'. Examples use only amounts confirmed in the fixture.

### Example 1: self-employed, 2025, with blue status tested both ways

Designer, resident, one client group, no other income. Revenue JPY 8,200,000 and necessary expenses JPY 1,300,000. Social insurance paid JPY 900,000, mutual aid and iDeCo paid JPY 840,000. Tax withheld by clients JPY 102,100, shown on payment notices. Prepayments JPY 60,000.

The decision: the client says 'blue' but has not shown the approval. Do not default. Run both cases and ask for the approval. The deduction also moves the basic deduction band: JPY 6,900,000 sits above JPY 6,550,000, whereas JPY 6,250,000 sits below it.

Case A has blue approval, 正規の簿記, attached statements and e-Tax filing by the deadline, so the Upper tier applies through limb 2.

```oa-check
name: JP 2025 self-employed with blue approval and e-Tax
inputs:
  revenue: 8200000
  expenses: 1300000
  blue_deduction: 650000
  basic_deduction: 630000
  social_insurance: 900000
  mutual_aid: 840000
  withheld: 102100
  prepaid: 60000
steps:
  - before_blue: revenue - expenses
  - business_income: before_blue - min(blue_deduction, max(before_blue, 0))
  - deductions: basic_deduction + social_insurance + mutual_aid
  - taxable: floor(max(business_income - deductions, 0) / 1000) * 1000
  - income_tax: taxable * 0.20 - 427500
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - after_withholding: floor(max(total_tax - withheld, 0) / 100) * 100
  - due: after_withholding - prepaid
expected:
  business_income: 6250000
  taxable: 3880000
  income_tax: 348500
  surtax: 7318
  total_tax: 355818
  due: 193700
```

Case B has no approval. The white return carries no deduction, the band moves up and the basic deduction falls to JPY 580,000.

```oa-check
name: JP 2025 self-employed on a white return
inputs:
  revenue: 8200000
  expenses: 1300000
  basic_deduction: 580000
  social_insurance: 900000
  mutual_aid: 840000
  withheld: 102100
  prepaid: 60000
steps:
  - business_income: revenue - expenses
  - deductions: basic_deduction + social_insurance + mutual_aid
  - taxable: floor(max(business_income - deductions, 0) / 1000) * 1000
  - income_tax: taxable * 0.20 - 427500
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - after_withholding: floor(max(total_tax - withheld, 0) / 100) * 100
  - due: after_withholding - prepaid
expected:
  business_income: 6900000
  taxable: 4580000
  income_tax: 488500
  surtax: 10258
  total_tax: 498758
  due: 336600
```

The difference is JPY 142,900 of tax due for the year. The reviewer sees both until the approval is shown.

### Example 2: mixed income, 2026, with the tier deciding the band

Employee, resident, with a confirmed side business. Employment receipts JPY 7,000,000, so the deduction is 7,000,000 × 10% + 1,100,000 = JPY 1,800,000. Business income before the blue deduction JPY 1,500,000. Social insurance JPY 1,000,000. Tax withheld JPY 361,260: JPY 300,000 on salary, per the 源泉徴収票, and JPY 61,260 on fees of JPY 600,000, per payment notices. No prepayments. Blue approval is confirmed.

The decision: does the JPY 650,000 tier apply? Case A keeps simplified books, so the deduction is JPY 100,000 and 合計所得金額 is JPY 6,600,000, above JPY 6,550,000: the 2026 basic deduction is JPY 620,000.

```oa-check
name: JP 2026 mixed income on the JPY 100000 tier
inputs:
  receipts: 7000000
  before_blue: 1500000
  blue_deduction: 100000
  basic_deduction: 620000
  social_insurance: 1000000
  withheld: 361260
steps:
  - employment_income: receipts - (receipts * 0.10 + 1100000)
  - business_income: before_blue - min(blue_deduction, max(before_blue, 0))
  - total_income: employment_income + business_income
  - taxable: floor(max(total_income - basic_deduction - social_insurance, 0) / 1000) * 1000
  - income_tax: taxable * 0.20 - 427500
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - due: floor(max(total_tax - withheld, 0) / 100) * 100
expected:
  employment_income: 5200000
  total_income: 6600000
  taxable: 4980000
  income_tax: 568500
  surtax: 11938
  due: 219100
```

Case B meets the Upper tier through e-Tax. 合計所得金額 falls to JPY 6,050,000, inside the JPY 6,550,000 band, and the 2026 basic deduction rises to JPY 670,000.

```oa-check
name: JP 2026 mixed income on the JPY 650000 tier
inputs:
  receipts: 7000000
  before_blue: 1500000
  blue_deduction: 650000
  basic_deduction: 670000
  social_insurance: 1000000
  withheld: 361260
steps:
  - employment_income: receipts - (receipts * 0.10 + 1100000)
  - business_income: before_blue - min(blue_deduction, max(before_blue, 0))
  - total_income: employment_income + business_income
  - taxable: floor(max(total_income - basic_deduction - social_insurance, 0) / 1000) * 1000
  - income_tax: taxable * 0.20 - 427500
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - due: floor(max(total_tax - withheld, 0) / 100) * 100
expected:
  total_income: 6050000
  taxable: 4380000
  income_tax: 448500
  surtax: 9418
  due: 96600
```

### Example 3: employee, 2025, who must file

Boundary case: this employee has no business income, so the file's main scope does not cover the person; the example only tests the employment limb of the must-file rule. Resident employee, one employer, receipts JPY 22,000,000, so a return is due: receipts exceed JPY 20,000,000. The deduction is the cap of JPY 1,950,000. No spouse, dependant or special disability, so the 所得金額調整控除 does not apply. Social insurance JPY 1,800,000. Tax withheld JPY 4,300,000 per the 源泉徴収票.

The decision is which band applies to the basic deduction: employment income of JPY 20,050,000 stays within the JPY 23,500,000 band, so JPY 580,000.

```oa-check
name: JP 2025 employee above JPY 20 million
inputs:
  receipts: 22000000
  employment_deduction: 1950000
  basic_deduction: 580000
  social_insurance: 1800000
  withheld: 4300000
steps:
  - employment_income: receipts - employment_deduction
  - taxable: floor(max(employment_income - basic_deduction - social_insurance, 0) / 1000) * 1000
  - income_tax: taxable * 0.33 - 1536000
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - due: floor(max(total_tax - withheld, 0) / 100) * 100
expected:
  employment_income: 20050000
  taxable: 17670000
  income_tax: 4295100
  surtax: 90197
  total_tax: 4385297
  due: 85200
```

### Example 4: refund, not rounded to JPY 100

Resident, 2025, taxable income JPY 3,480,000, withholding JPY 300,000 on fees, no prepayment. The decision is whether to round: the tax after withholding is negative, so it stays exact.

```oa-check
name: JP 2025 refund kept exact
inputs:
  taxable: 3480000
  withheld: 300000
steps:
  - income_tax: taxable * 0.20 - 427500
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - refund: max(withheld - total_tax, 0)
  - due: floor(max(total_tax - withheld, 0) / 100) * 100
expected:
  income_tax: 268500
  surtax: 5638
  total_tax: 274138
  refund: 25862
  due: 0
```

### Example 5: withholding on a large fee

A client pays a design fee of JPY 1,500,000 in one payment, with consumption tax shown separately on the invoice. The part above JPY 1,000,000 is at 20.42%.

```oa-check
name: JP withholding above JPY 1 million
inputs:
  fee: 1500000
steps:
  - tax: floor(min(fee, 1000000) * 0.1021 + max(fee - 1000000, 0) * 0.2042)
  - net: fee - tax
expected:
  tax: 204200
  net: 1295800
```

A 司法書士 paid JPY 8,000 or JPY 10,000 in one payment has nothing withheld.

```oa-check
name: JP item 2 withholding around the amount deducted
inputs:
  amount_deducted: 10000
  payment_low: 8000
  payment_equal: 10000
  payment_high: 12000
steps:
  - tax_low: floor(max(payment_low - amount_deducted, 0) * 0.1021)
  - tax_equal: floor(max(payment_equal - amount_deducted, 0) * 0.1021)
  - tax_high: floor(max(payment_high - amount_deducted, 0) * 0.1021)
expected:
  tax_low: 0
  tax_equal: 0
  tax_high: 204
```

### Example 6: late filing, 3 positions on the same tax

Tax on a late 2025 return JPY 4,000,000. The decision is when the return was filed. Filed voluntarily before notice of investigation: 5%. Filed after notice but not foreseen: the 10%, 15% and 25% row. Filed after the investigation: the 15%, 20% and 30% row. The 1-month nil rule is not tested here, as it needs facts the fixture does not give.

```oa-check
name: JP late filing penalty by position
inputs:
  tax: 4000000
steps:
  - low: min(tax, 500000)
  - mid: max(min(tax, 3000000) - 500000, 0)
  - high: max(tax - 3000000, 0)
  - voluntary: tax * 0.05
  - after_notice: low * 0.10 + mid * 0.15 + high * 0.25
  - after_investigation: low * 0.15 + mid * 0.20 + high * 0.30
expected:
  voluntary: 200000
  after_notice: 675000
  after_investigation: 875000
```

### Example 7: carried loss, with the band held on 合計所得金額

Blue filer, resident, 2025, no other income. Revenue JPY 4,600,000, necessary expenses JPY 450,000, and the Upper tier met through limb 2. Social insurance paid JPY 500,000. No withholding or prepayment. A blue return for 2023 showed a net loss of JPY 500,000, none of it used.

The decision: is the loss eligible? With the 2023 and 2024 returns both shown, it is (Case A). Without a 2024 return, art. 70(4) fails and the loss is nil (Case B). Either way 合計所得金額 is JPY 3,500,000, so the basic deduction is JPY 680,000. Testing the band on JPY 3,000,000, after the loss, would wrongly give JPY 880,000.

```oa-check
name: JP 2025 blue filer with an eligible carried loss
inputs:
  revenue: 4600000
  expenses: 450000
  blue_deduction: 650000
  carried_loss: 500000
  basic_deduction: 680000
  social_insurance: 500000
steps:
  - before_blue: revenue - expenses
  - total_income: before_blue - min(blue_deduction, max(before_blue, 0))
  - loss_used: min(carried_loss, max(total_income, 0))
  - deductions: basic_deduction + social_insurance
  - taxable: floor(max(total_income - loss_used - deductions, 0) / 1000) * 1000
  - income_tax: taxable * 0.05
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - due: floor(max(total_tax, 0) / 100) * 100
expected:
  total_income: 3500000
  loss_used: 500000
  taxable: 1820000
  income_tax: 91000
  surtax: 1911
  total_tax: 92911
  due: 92900
```

```oa-check
name: JP 2025 blue filer with no eligible carried loss
inputs:
  revenue: 4600000
  expenses: 450000
  blue_deduction: 650000
  carried_loss: 0
  basic_deduction: 680000
  social_insurance: 500000
steps:
  - before_blue: revenue - expenses
  - total_income: before_blue - min(blue_deduction, max(before_blue, 0))
  - loss_used: min(carried_loss, max(total_income, 0))
  - deductions: basic_deduction + social_insurance
  - taxable: floor(max(total_income - loss_used - deductions, 0) / 1000) * 1000
  - income_tax: taxable * 0.10 - 97500
  - surtax: floor(income_tax * 0.021)
  - total_tax: income_tax + surtax
  - due: floor(max(total_tax, 0) / 100) * 100
expected:
  total_income: 3500000
  loss_used: 0
  taxable: 2320000
  income_tax: 134500
  surtax: 2824
  total_tax: 137324
  due: 137300
```

The difference is JPY 44,400 of tax due. In Case C the filer's 合計所得金額 is JPY 2,000,000 and the eligible loss JPY 2,500,000. The loss comes off income before 所得控除, so JPY 2,000,000 of it is used and JPY 500,000 is left to carry.

```oa-check
name: JP 2025 carried loss above income
inputs:
  total_income: 2000000
  carried_loss: 2500000
  basic_deduction: 880000
  social_insurance: 500000
steps:
  - loss_used: min(carried_loss, max(total_income, 0))
  - loss_left: carried_loss - loss_used
  - deductions: basic_deduction + social_insurance
  - taxable: floor(max(total_income - loss_used - deductions, 0) / 1000) * 1000
expected:
  loss_used: 2000000
  loss_left: 500000
  taxable: 0
```

### Example 8: family employee for 4 months

A business starts on 1 September 2025. A spouse in the same household works in it full time to 31 December, a period of 4 months. On a blue return, 4 months is more than half the period the spouse could work, so art. 57(1) can apply, given the notification. On a white return, 4 months does not exceed 6, so art. 57(3) cannot. If the spouse was a daytime student working by day, or held another job with normal hours, in those 4 months, that time does not count on either return (所得税法施行令 art. 165(2)).

### Bank line fixtures

Each line is a fixture, carried from the prior version unless stated.

**1. 三菱UFJ, design fee.** `2025/03/15 | 振込入金 デザインスタジオABC | +350,000 | 残高 1,240,500`. Design fees fall in limb 1 of art. 204(1), so check whether JPY 350,000 is net of withholding. If the invoice was JPY 390,000 and the client withheld JPY 39,819 (10.21%), the bank line would show JPY 350,181, not JPY 350,000, so these figures do not fit. Classification: 事業収入, gross Needs Input until the invoice or payment notice is seen.

**2. 楽天銀行, fee net of withholding.** `2025/05/20 | 振込 株式会社マーケティングXYZ 源泉後 | +107,748 | Ref: 202505-0234`. Corrected fixture: the prior version showed JPY 107,892, which does not equal JPY 120,000 less JPY 12,252. With an invoice of JPY 120,000, tax is JPY 12,252, so revenue is JPY 120,000 and the credit is JPY 12,252, if a document states them.

**3. ゆうちょ銀行, pension.** `2025/04/30 | 国民年金保険料 振替 | -16,590 | 残高 852,410`. Excluded from 必要経費 and recorded as 社会保険料控除 under art. 74, not section 79 as the prior version said. The amount is the prior fixture's; the fiscal 2025 premium in `jp-social-insurance` is JPY 17,510 a month, so check the line.

**4. 住信SBIネット銀行, home internet.** `2025/07/10 | NURO光 利用料 | -5,500 | 残高 423,800`. Mixed use. With a record supporting 70% business use, JPY 3,850 is deductible. Without one, nothing is deducted. Classification: 通信費, pending. Flag for the reviewer.

**5. 三井住友銀行, annual subscription.** `2025/09/01 | ADOBE SYSTEMS | -72,600 | 残高 1,540,200`. A subscription, not a perpetual licence, so the JPY 100,000 asset test does not apply. The 4 months to December relate to 2025; the 8 months to August 2026 are Needs Input under Timing, until the filer's consistent practice is confirmed. Classification: 消耗品費.

**6. みずほ銀行, client dinner.** `2025/11/12 | デビットカード 銀座レストランXX | -48,000 | 残高 3,210,500`. Deductible if the art. 37 test is met. Record date, venue, attendees and purpose. Classification: 接待交際費, pending evidence. Flag if aggregate entertainment is high.

## Ask the client first

1. **Status.** Resident for the whole year, Japanese national or years in Japan (for 非永住者), any death or departure, and any income outside business and employment. 'Are you registered for consumption tax (消費税)?'
2. **Return type.** 青色申告 or 白色申告, with the approval document and its date; 複式簿記 or 簡易簿記; e-Tax or paper; statements attached or not.
3. **Withholding.** Do any clients deduct tax before paying (源泉徴収)? Which clients, and do you have a 支払調書, payment notice or invoice from each? Any 源泉徴収票?
4. **Deductions.** National pension and health insurance paid; iDeCo or 小規模企業共済; life insurance; spouse, dependants and their income.
5. **Mixed use.** Home office: what share is used for business, and what record supports it? Vehicle use, and the same question. Family members paid, with any notification.
6. **Prior year.** 予定納税 notices and amounts paid; prior return; any loss carried forward, with the loss-year return and each return since.

**If the client has only a bank statement.** Do not produce a figure. Mark 振込入金 credits from non-bank entities as potential 事業収入. Mark 国民年金 and 国保 debits as 社会保険料控除. List restaurant and entertainment debits as pending, and mixed-use debits as undeducted. Leave blue status as Needs Input. Generate a working paper with clear pending flags, and ask the questions above.

### Completion checks

- [ ] No refusal fired, and residence confirmed?
- [ ] Surtax added: 2.1% for 2025 and 2026?
- [ ] Taxable income rounded down to JPY 1,000 before applying rates?
- [ ] Positive tax rounded down to JPY 100, and any refund left exact?
- [ ] National pension and health insurance excluded from 必要経費?
- [ ] Blue tier matched to approval, books, statements, deadline and route?
- [ ] Basic deduction band taken after the blue deduction and before any carried loss?
- [ ] Carried loss tested under Losses, or Needs Input?
- [ ] Withholding credits checked against a document, not just the bank statement?
- [ ] Blue approval evidenced (the art. 144 application; there is no 'Form 144')?
- [ ] Figures labelled estimated and open items listed?

## Sources

Read on 5 November 2026 unless stated. e-Gov text is the consolidated text from the e-Gov law API at the dates shown; the URL column gives the public e-Gov page. Translations of statutory terms in this file are the author's, not official text, and no English text was treated as law.

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| 所得税法 | https://laws.e-gov.go.jp/law/340AC0000000033 | 2026-11-05 | Read in part at 31 December 2025, 5 November 2026, 1 December 2026 and 1 January 2027: arts 2, 7, 23, 24, 27, 28, 34, 35, 37, 45, 49, 56, 57, 57-3, 67, 69, 70, 70-2, 71, 71-2, 74 to 84-2, 86, 89, 95, 104, 105, 120, 138, 140, 142 to 148, 183, 204, 205 and 225, the heading of art. 149, and 別表第五 at 31 December 2025 and 1 December 2026 for its headings and sample rows |
| 所得税法施行令 | https://laws.e-gov.go.jp/law/340CO0000000096 | 2026-11-05 | Read in part at 31 December 2025 and 5 November 2026: arts 96, 120-2, 125, 138, 139, 165, 195, 201, 202, 204, 298(1) and 322, and the heading of art. 320 |
| 租税特別措置法 | https://laws.e-gov.go.jp/law/332AC0000000026 | 2026-11-05 | Read in part at 31 December 2025, 5 November 2026, 1 December 2026, 1 January 2027 and 1 January 2028: arts 3, 25-2, 28-2, 29-4, 41-3-11, 41-15-5, 41-16, 41-16-2, 41-19, 61-4, the heading of art. 94 and the 附則 of 令和8年法律第12号 printed there |
| 租税特別措置法施行令 | https://laws.e-gov.go.jp/law/332CO0000000043 | 2026-11-05 | Read in part at 31 December 2025 and 5 November 2026: art. 18-5 and its 附則 |
| 国税通則法 | https://laws.e-gov.go.jp/law/337AC0000000066 | 2026-11-05 | Read in part at 31 December 2025 and 5 November 2026: arts 10, 60, 65, 66, 68, 69, 118, 119 |
| 復興財確法 | https://laws.e-gov.go.jp/law/423AC0000000117 | 2026-11-05 | Read in part at 31 December 2025, 5 November 2026, 1 December 2026, 1 January 2027 and 1 January 2028: arts 8, 9, 12, 13 |
| 防衛財確法 | https://laws.e-gov.go.jp/law/505AC0000000069 | 2026-11-05 | Read in part at 5 November 2026 and 1 January 2027: arts 5-3, 5-9, 5-11, 5-13 |
| 電子帳簿保存法 (電子計算機を使用して作成する国税関係帳簿書類の保存方法等の特例に関する法律) | https://laws.e-gov.go.jp/law/410AC0000000025 | 2026-11-05 | Read in part at 31 December 2025: art. 8(4) |
| 森林環境税及び森林環境譲与税に関する法律 | https://laws.e-gov.go.jp/law/431AC0000000003 | 2026-11-05 | Read in part: arts 4 to 7 and the start year |
| 減価償却資産の耐用年数等に関する省令 | https://laws.e-gov.go.jp/law/340M50000040015 | 2026-11-05 | Read in part: rows of 別表第一, 第三, 第八 and 第十 used here |
| 消費税法 | https://laws.e-gov.go.jp/law/363AC0000000108 | 2026-11-05 | Read in part: arts 2(1)(14), 9, 9-2 |
| 地方税法 | https://laws.e-gov.go.jp/law/325AC0000000226 | 2026-11-05 | Read in part at 3 dates: arts 32, 34, 35, 37, 38, 41, 310, 314-2, 314-3, 314-6, 320 |
| NTA, Tax Answer 所得税 pages | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm | 2026-11-05 | Read in part. Nos 1100, 1130, 1135, 1140, 1177, 1180, 1182, 1191, 1195, 1199, 1200, 1300, 1350, 1410, 2010, 2020, 2024, 2026, 2040, 2070, 2072, 2075, 2080, 2100, 2106, 2210, 2220, 2250, 2260 and 2270, at the same URL pattern; each stated at 1 April 2026 |
| NTA, Tax Answer 源泉所得税 pages | https://www.nta.go.jp/taxes/shiraberu/taxanswer/gensen/2798.htm | 2026-11-05 | Read in part. Nos 2502, 2792, 2795, 2798, 2801 and 2875, at the same URL pattern |
| NTA, 消費税 No. 6901 | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6901.htm | 2026-11-05 | Read in part: 税抜 and 税込 accounting |
| NTA, 延滞税の割合 | https://www.nta.go.jp/taxes/nozei/entaizei/keisan/entai_wariai.htm | 2026-11-05 | Read in part: 2025 and 2026 rows |
| NTA, 令和7年分 手引き (PDF) | https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2025/pdf/001.pdf | 2026-11-05 | Read in part: printed pp. 2, 3, 27, 29 and 39 by local text extraction. Administrative guide, not law |
| NTA, 手引き 申告書の提出方法 | https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2025/02/2_02.htm | 2026-11-05 | Read in part: filing dates |
| NTA, 手引き 添付書類 | https://www.nta.go.jp/taxes/shiraberu/shinkoku/tebiki/2025/04/4_01.htm | 2026-11-05 | Read in part: attachments and identity documents |
| NTA, 令和7年分 forms | https://www.nta.go.jp/taxes/shiraberu/shinkoku/syotoku/r07.htm | 2026-11-05 | Read in part: form list |
| NTA, 令和8年度 基礎控除 Q&A (May 2026, PDF) | https://www.nta.go.jp/users/gensen/2026kiso/pdf/0026005-024.pdf | 2026-11-05 | Read in part: Q1-1, Q1-3 and Q4-1 by local text extraction. Administrative guide at 1 May 2026 |
| 所得税基本通達 37-30の2 | https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/05/09.htm | 2026-11-05 | Read in part: 37-30の2. Administrative text, not law |
| 所得税基本通達 法第45条関係 | https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/07/01.htm | 2026-11-05 | Read in part: the 附帯税 heading. Administrative text, not law |
| 所得税基本通達 57の3-2 | https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/11a/01.htm | 2026-11-05 | Read in part: 57の3-2 and its notes. Administrative text, not law |
| 所得税基本通達 法第205条関係 | https://www.nta.go.jp/law/tsutatsu/kihon/shotoku/36/07.htm | 2026-11-05 | Read in part: 205-1, 205-2 and 205-5. Administrative text, not law |
| 消費税法等の施行に伴う所得税の取扱いについて (平元直所3-8) | https://www.nta.go.jp/law/tsutatsu/kobetsu/shotoku/shinkoku/890329/01.htm | 2026-11-05 | Read in part: paras 2 and 5. Administrative text, not law |
| Ministry of Finance, 所得税法等の一部を改正する法律案 (PDF) | https://www.mof.go.jp/about_mof/bills/221diet/st080220h.pdf | 2026-11-05 | Read in part: 附則 art. 1, printed pp. 558 and 559, as page images. A bill as submitted, not the Act |
| e-Tax | https://www.e-tax.nta.go.jp/ | 2026-11-05 | Read for the portal name only |
| 確定申告書等作成コーナー | https://www.keisan.nta.go.jp/kyoutu/ky/sm/top | 2026-11-05 | Read for the address only, by HEAD |
| Ministry of Finance, 令和8年度 税制改正 | https://www.mof.go.jp/tax_policy/tax_reform/outline/fy2026/index.html | 2026-11-05 | Read in part: index page listing the 大綱 and the Acts. The 大綱 itself not opened |
| Ministry of Finance, 令和9年度 税制改正 | https://www.mof.go.jp/tax_policy/tax_reform/outline/fy2027/index.html | 2026-11-05 | Read in part: index page showing requests at 31 August 2026 |
| 日本年金機構, 国民年金の保険料 | https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html | 2026-11-05 | Read in part: 令和8年度 premium only |

### Source conflicts

- **NTA No. 2260 worked figure.** The page's example computes JPY 974,000 of tax, then applies 2.1% to JPY 947,000 for JPY 19,887. 2.1% of JPY 974,000 is JPY 20,454. This file follows the statute and treats the printed line as a page error; it is not resolved with the NTA.
- **End date for the surtax.** The 2025 手引き and `japan-crypto-tax`, `jp-incorporation` and `japan-tax-optimization` print 2037 for the surtax. The law read for years to 2026 agrees, but the text from 1 January 2027 runs the lower rate to 2047.
- **Blue return conditions.** `jp-etax-filing` and `japan-bookkeeping` state the JPY 650,000 tier as double-entry and e-Tax only, and omit the electronic-books limb. `japan-tax-optimization` cites Income Tax Act art. 65 for it; the article read is 措法 art. 25-2.
- **Loss carry-forward.** `jp-etax-filing` says blue return only. Art. 70(2) gives white filers 2 kinds.
- **Spouse income limit.** `japan-tax-optimization` prints JPY 480,000, which is the limit for years to 2024.
- **Prepayment threshold.** `jp-etax-filing` says above JPY 150,000. Art. 104(1) says JPY 150,000 or more, as `jp-estimated-tax` states.
- **Filing date.** `jp-etax-filing` and `japan-tax-optimization` print 15 March without the Sunday rule for 2025.
- **Inhabitant tax.** `jp-nonpermanent-resident` lists a 2.1% surtax beside the resident tax row. No such surtax on inhabitant tax was read. `jp-incorporation` gives about JPY 5,000 per capita, which fits JPY 4,000 plus the forest tax of JPY 1,000 as standard rates.
- **Life insurance years.** NTA No. 1140 says 令和8年分以降. 措法 art. 41-15-5(1), at 5 November 2026 and 1 January 2027, says 令和八年分又は令和九年分. This file follows the statute for 2026 and makes no statement about later years.
- **Family employee cap.** `japan-bookkeeping` prints 'max ¥500,000/860,000' with no order. Art. 57(3) gives spouse JPY 860,000.

### Other legacy topics

- **Crypto.** The prior version said up to 55% including resident tax. No rate was read here, so R-JP-4 carries no figure.
- **Known gaps.** Non-resident taxation; cryptocurrency; real estate capital gains; inheritance tax; consumption tax return (`jp-consumption-tax` covers this).
- **Key legislation.** Business income art. 27; necessary expenses art. 37; blue return arts 143 to 148; blue deduction 措法 art. 25-2; depreciation art. 49; income deductions arts 72 to 86; surtax 復興財確法; prepayment arts 104 to 109, as the prior version listed them.

Not yet confirmed: 令和9年分 forms and any 2027 computation; rounding of the 2027 defence surtax; any 令和9年度 tax reform outline; the 令和8年分 手引き, for the surtax rounding carried from the 2025 one; whether the salary reductions in 所得税法施行令 art. 322 stop at nil; whether a filer's practice meets the consistency conditions in 所得税基本通達 37-30の2 and 57の3-2; local inhabitant tax rates above standard and the upper local basic deduction tiers; the 振替納税 date for the 2026 year; the Act 令和8年法律第12号 as a separate document; 別表第五 rows, which are not reproduced; home-office percentages and methods; any statutory duty to give a payee a 支払調書; the Tax Answer pages after the read date; bank file layouts.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the upstream template. Primary-source check against the 2025 and enacted 2026 and 2027 texts. Corrected the surtax end date, per-capita double count, withholding test, 'Form 144', white family employee amounts, white loss rule, spouse income limit, depreciation method, expensing limit, blue tier conditions, consumption tax test, penalty labels, art. 74 citation and fixture arithmetic. Added refusals, an operational hold, the carried-loss step and defaults tied to the law read |
| 2.1 | November 2026 | Basic deduction column for 2026 and 2027 (NTA No. 1199) |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Japanese bank format guide; local platform patterns; worked examples |
| 1.0 | 2025 | Initial version |

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `jp-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/jp-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
