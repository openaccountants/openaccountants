---
name: kr-income-tax
description: >
  Use this skill whenever asked about South Korean income tax for self-employed
  individuals. Trigger on phrases like "comprehensive income tax", "종합소득세",
  "global income tax Korea", "사업소득", "business income Korea", "간편장부",
  "simplified bookkeeping", "복식부기", "double-entry Korea", "local income tax
  surtax", "estimated tax Korea", "Korean income tax return", "Hometax Korea",
  "Kakao Pay income", "Naver Pay settlement", "KakaoBank statement", or any
  question about filing or computing income tax for a Korean freelancer or
  self-employed person. It covers the 2025 and 2026 years: progressive brackets
  (6% to 45%), local income tax, bookkeeping methods, simplified and standard
  expense rates, personal deductions, estimated tax, filing deadlines and
  penalties. ALWAYS read this skill before touching any Korean income tax work.
  This Tier 2 draft supports source checking and reviewer questions; it does not
  authorise filing, payment or a tax position.
version: 2.2
jurisdiction: KR
tax_year: 2025
tax_year_notes: "Coverage starts with the 2025 year (2025년 귀속, filed in 2026) and includes the 2026 year (2026년 귀속, filed in 2027). The law was read at 5 November 2026. Expense rates are those of 국세청고시 제2026-14호, which applies to 2025 only; no rate notice for 2026 was read, so a 2026 computation on 단순경비율 or 기준경비율 is Needs Input. The 2026 revision bills before the National Assembly are not treated as law. The local credit rule in 지방세특례제한법 art. 167의2 has a stated end date of 31 December 2026, and its effect on a 2026 return filed in 2027 is held."
last_updated: 2026-11-05
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# South Korea income tax for self-employed individuals v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Coverage: the 2025 year (2025년 귀속, filed in 2026) and the 2026 year (2026년 귀속, filed in 2027). The law was read at 5 November 2026. Expense rates are those of 국세청고시 제2026-14호, which applies to 2025 only; no rate notice for 2026 was read, so a 2026 computation on 단순경비율 or 기준경비율 is Needs Input. The 2026 revision bills before the National Assembly are not treated as law. The local credit rule in 지방세특례제한법 art. 167의2 has a stated end date of 31 December 2026, and its effect on a 2026 return filed in 2027 is held.

## Who this applies to

An individual resident in Korea (거주자) with business income (사업소득, 소득세법 art. 19), with or without employment income (근로소득), who files a final return of comprehensive income tax (종합소득세) for a calendar year. Currency is KRW only. The filing unit is the individual: each resident files for themselves, with no joint return in the articles read. Example 3 has no business income: it tests the credit rules for employment income and does not widen this scope.

The tax year is 1 January to 31 December (소득세법 art. 5(1)). A resident is an individual with an address (주소) in Korea or a place of abode (거소) there for 183 days or more; everyone else is a non-resident (art. 1의2(1)). Decree rules on the test are referred to in art. 1의2(2) and are not reproduced here. A resident is taxed on all income in the Act (art. 3(1)), subject to the limited foreign income rule for the foreign residents in R-KR-6. A non-resident is taxed on Korean-source income only (art. 3(2)). The place of tax is the address, or the place of abode where there is no address (art. 6(1)).

The tax authority is the National Tax Service (국세청, NTS). Primary legislation is the Income Tax Act (소득세법) with its Enforcement Decree (시행령) and Enforcement Rules (시행규칙), the Framework Act on National Taxes (국세기본법), the Restriction of Special Taxation Act (조세특례제한법), the Local Tax Act (지방세법), the Framework Act on Local Taxes (지방세기본법) and the Restriction of Special Local Taxation Act (지방세특례제한법). The filing portal is Hometax (홈택스, https://www.hometax.go.kr). Local income tax is filed with the local government, by the one-click link from Hometax to Wetax (위택스, https://www.wetax.go.kr). English names of statutes are the author's working translations; no English text was treated as law.

The prior version called 국세기본법 the 'Tax Procedures Act'. That was wrong: it is the Framework Act on National Taxes.

### What this file is

This file is a Tier 2 reference with review pending. It holds the rate tables, the base, classification patterns, deadlines and reviewer questions. Treat every computed figure as an estimate for review by a 세무사, 공인회계사 or equivalent licensed practitioner in South Korea.

**Operational hold.** This file does not fill the complete country companion contract in `income-tax-workflow-base`, so it does not support unattended preparation:

- The transaction pattern library and bank formats below are carried from the prior version. Their narrations and file layouts were not tested against bank files.
- 2026 expense rates were not read. A 2026 estimate route (단순경비율 or 기준경비율) cannot be computed from this file.
- 개인지방소득세 credits for a 2026 return depend on a held point (art. 167의2, see Enactment position). Example 2 shows both results.
- Small and medium business relief (조세특례제한법 art. 7), minimum tax (최저한세, art. 132), 농어촌특별세, depreciation schedules and the local e-filing credit amount are not computed here. Each is a reviewer item.
- `kr-social-insurance` owns social insurance and supplies only the amount paid. `south-korea-vat` owns VAT. `south-korea-crypto-tax` owns crypto. Their text was not changed, and one conflict is recorded under Source conflicts.

**Reviewer warning.** Any working paper produced under this file is a working paper only. It must show which inputs were confirmed and which are Needs Input, and it must carry the label 'estimated, not reviewed'. Direct the client to their 세무사 for confirmation.

### Question threshold

Tier 2 question threshold: KRW 0. No row is filtered on amount: a material question goes to the client or the reviewer whatever its size, because no text read sets a floor.

### Refusals

A refusal is a full stop. When a trigger applies, output the message verbatim and end. Do not classify part of the file first. Where a trigger is only suspected, ask the client the question that resolves it.

- **R-KR-1, non-resident.** Trigger: the person is, or may be, a non-resident (비거주자) at any time in the year. Message: 'Non-resident taxation of Korean-source income has different rules, and this file covers residents only. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-2, corporation.** Trigger: the income belongs to a corporation (법인). Message: 'Corporations file corporate tax (법인세), not income tax. This workflow cannot continue.'
- **R-KR-3, financial income.** Trigger: interest and dividends within 소득세법 art. 14(3)(6) total more than KRW 20,000,000, or any of them was not withheld under art. 127. Message: 'Interest and dividends above the KRW 20,000,000 test, or not withheld, enter comprehensive income and need a computation that this file does not contain. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-4, real estate income or capital gains.** Trigger: the year includes real estate rental income, or a gain within capital gains tax (양도소득세). Message: 'Real estate rental income and capital gains need separate computations that this file does not contain. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-5, foreign income or treaty claim.** Trigger: the year includes foreign-source income, foreign tax paid or withheld, or a treaty position. Message: 'Cross-border income needs tax treaty and foreign tax analysis that this file does not contain. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-6, short-stay foreign resident.** Trigger: a foreign resident whose address or place of abode in Korea totals 5 years or less in the 10 years before the end of the year (소득세법 art. 3(1) proviso). Message: 'A foreign resident within the 5 year rule is taxed on foreign income only where paid in or remitted to Korea, which this file does not compute. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-7, year not covered.** Trigger: a computation is asked for a year other than 2025 or 2026. Message: 'This file computes 2025 and 2026 only. Read the text in force and the return form for that year. This workflow cannot continue for that year.'
- **R-KR-8, death or departure.** Trigger: the taxpayer died or left Korea in the year (소득세법 arts 5(2), 5(3) and 74). Message: 'A year ending in death or departure has its own period and filing dates, which this file does not compute. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-9, joint business.** Trigger: the business is run jointly and shares profit (공동사업, 소득세법 art. 43). Message: 'A joint business computes income at the business and allocates it, which this file does not compute. Refer it to a 세무사. This workflow cannot continue.'
- **R-KR-10, crypto.** Trigger: the year includes income, payment or gain in virtual assets (가상자산). Message: 'Virtual asset income needs rules that this file does not contain. Check `south-korea-crypto-tax` and refer it to a 세무사. This workflow cannot continue.'
- **R-KR-11, other income in the aggregate.** Trigger: pension income (연금소득) or other income (기타소득) must or may enter the return. Message: 'This year needs income heads that this file does not compute. Refer it to a 세무사. This workflow cannot continue.'

### Required inputs

**Minimum viable:** a bank statement for the full calendar year (January to December) in CSV, PDF or pasted text, plus confirmation of the business type (업종코드) and the bookkeeping method.

**Recommended:** withholding receipts (원천징수영수증) or payment statements from clients, the prior year return, estimated tax (중간예납) receipts, national health insurance (국민건강보험) and national pension (국민연금) receipts.

**Ideal:** complete books (간편장부 or 복식부기), all client invoices, expense evidence, an asset register and the prior year assessment (납세고지서).

### Prohibitions

- Never compute income without confirming the business type (업종): expense rates and thresholds differ by industry.
- Never treat a net receipt as the income where tax was withheld: report the gross amount and the tax evidenced.
- Never gross up a receipt on assumption. Only the supplies in Withholding carry the 3% rate, and each needs a document.
- Never put national pension in 필요경비: it is a deduction from total income (소득세법 art. 51의3).
- Never treat a self-employed person's own health premium as a 소득공제: under the decree limbs in Expenses it is 필요경비 on a books route, and an estimate route is Needs Input (see Expenses). Keep the employee's own premium under art. 52.
- Never omit 개인지방소득세, and never treat it as a simple 10% of national tax due. It has its own table, its own credits and its own filing.
- Never allow income tax or local income tax as an expense (소득세법 art. 33(1)(1)).
- Never advise on non-resident taxation.
- Never present a calculation as definitive: label it estimated and direct the client to their 세무사 for confirmation.

## Rates, bands and thresholds

All amounts are in won. Statutory text was read on law.go.kr at the version dates stated in Sources. 2025 links open the text in force at 31 December 2025; 2026 links open the text in force at the read date.

### National income tax

Tax = taxable income (과세표준) × rate − deduction amount (누진공제). 소득세법 art. 55(1) states the bands as a base amount plus a marginal rate; the deduction column is the NTS presentation and gives the same result. The band figures were read from the statute image, because the page's alternative text is cut off. Rates were the same in the text at 31 December 2025, the text in force on 5 November 2026 and the text dated 1 January 2027.

| Taxable income (KRW) | Rate | Art. 55(1) base amount | Deduction (누진공제) | Tax year | Official source |
| --- | --- | --- | --- | --- | --- |
| Up to 14,000,000 | 6% | 0 | 0 | 2025, 2026 | 소득세법 art. 55(1), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0; NTS table labelled 2023 to 2025: https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&cntntsId=7667 |
| Over 14,000,000, up to 50,000,000 | 15% | 840,000 | 1,260,000 | 2025, 2026 | same |
| Over 50,000,000, up to 88,000,000 | 24% | 6,240,000 | 5,760,000 | 2025, 2026 | same |
| Over 88,000,000, up to 150,000,000 | 35% | 15,360,000 | 15,440,000 | 2025, 2026 | same |
| Over 150,000,000, up to 300,000,000 | 38% | 37,060,000 | 19,940,000 | 2025, 2026 | same |
| Over 300,000,000, up to 500,000,000 | 40% | 94,060,000 | 25,940,000 | 2025, 2026 | same |
| Over 500,000,000, up to 1,000,000,000 | 42% | 174,060,000 | 35,940,000 | 2025, 2026 | same |
| Over 1,000,000,000 | 45% | 384,060,000 | 65,940,000 | 2025, 2026 | same |

The NTS table carries no 2026 label, so the 2026 year rests on the statute alone.

### Local income tax (개인지방소득세)

The prior version called this a 10% surtax on national tax. It is a separate tax. Its base is the income tax 과세표준 (지방세법 art. 91), and art. 92(1) gives its own table, which is one tenth of the national table. The result equals 10% of national tax only where every credit also carries across at one tenth. A local government may vary the standard rate by up to 50% (art. 92(2)). Whether any has done so was not checked: a rate above or below standard is Needs Input.

| Taxable income (KRW) | Local tax | Tax year | Official source |
| --- | --- | --- | --- |
| Up to 14,000,000 | 6/1000 | 2025, 2026 | 지방세법 art. 92(1), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276349&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| Over 14,000,000, up to 50,000,000 | 84,000 + 15/1000 of the excess | 2025, 2026 | same |
| Over 50,000,000, up to 88,000,000 | 624,000 + 24/1000 of the excess | 2025, 2026 | same |
| Over 88,000,000, up to 150,000,000 | 1,536,000 + 35/1000 of the excess | 2025, 2026 | same |
| Over 150,000,000, up to 300,000,000 | 3,706,000 + 38/1000 of the excess | 2025, 2026 | same |
| Over 300,000,000, up to 500,000,000 | 9,406,000 + 40/1000 of the excess | 2025, 2026 | same |
| Over 500,000,000, up to 1,000,000,000 | 17,406,000 + 42/1000 of the excess | 2025, 2026 | same |
| Over 1,000,000,000 | 38,406,000 + 45/1000 of the excess | 2025, 2026 | same |

Local credits: 지방세법 art. 94 applies credits under 지방세특례제한법, and any excess over the local computed tax is lost. Art. 167의2(1) of that Act, which has the end date in Coverage, gives 10% of each national credit or relief, except the national e-filing credit in 조세특례제한법 art. 104의8(1). Art. 167의3 gives a separate local e-filing credit; its amount is set by a decree not read, so it is left out of every figure here.

### Employment income deduction (근로소득공제)

Used only for mixed and employee cases. Limit KRW 20,000,000 (소득세법 art. 47(1)). A daily worker's deduction is KRW 150,000 per day (art. 47(2)), and daily workers' pay stays outside the aggregate (art. 14(3)(2)).

| Total pay, 총급여액 (KRW) | Deduction | Tax year | Official source |
| --- | --- | --- | --- |
| Up to 5,000,000 | 70% | 2025, 2026 | 소득세법 art. 47(1), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| Over 5,000,000, up to 15,000,000 | 3,500,000 + 40% of the excess | 2025, 2026 | same |
| Over 15,000,000, up to 45,000,000 | 7,500,000 + 15% of the excess | 2025, 2026 | same |
| Over 45,000,000, up to 100,000,000 | 12,000,000 + 5% of the excess | 2025, 2026 | same |
| Over 100,000,000 | 14,750,000 + 2% of the excess | 2025, 2026 | same |

### Deductions from total income

| Item | Amount and conditions | Tax year | Official source |
| --- | --- | --- | --- |
| Basic deduction (기본공제) | KRW 1,500,000 per person: self; spouse; and each dependant who lives with the resident or spouse and meets the art. 50 age test, claimed by one resident only (art. 50(3)). Living together is not needed for a descendant or adoptee, and covers temporary absence on decree grounds and an ascendant apart for housing reasons (art. 53(1) to (3)). The spouse or dependant's income must be KRW 1,000,000 or less, or employment income only with 총급여액 of KRW 5,000,000 or less. Age tests: ascendant 60 or over; descendant or adoptee 20 or under; sibling 20 or under or 60 or over; 기초생활 수급권자 and foster child (위탁아동) as art. 50 provides; a disabled person has no age limit | 2025, 2026 | 소득세법 art. 50, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| Additional, aged 70 or over | KRW 1,000,000 per person | 2025, 2026 | same: 소득세법 art. 51(1) |
| Additional, disabled | KRW 2,000,000 per person | 2025, 2026 | same |
| Additional, 부녀자 | KRW 500,000, where 종합소득금액 is KRW 30,000,000 or less and the resident is a woman who has a spouse, or a woman with no spouse who is a 세대주 with an art. 50(1)(3) dependant | 2025, 2026 | same |
| Additional, 한부모 | KRW 1,000,000, where the resident has no spouse and has a descendant or adoptee who is a basic deduction dependant. Where both apply, this one, not 부녀자 | 2025, 2026 | same |
| Personal deduction limit | Excess over 종합소득금액 is lost (art. 51(4)). Status under arts 50, 51 and 59의2 is tested at the end of the year, or on the day before death or recovery from a disability (art. 53(4)). An age in art. 50(1)(3) or art. 59의2 is met if reached on any day in the year (art. 53(5)). Without the art. 70(4)(1) papers, only the self basic deduction and the standard credit apply (art. 54(2)) | 2025, 2026 | same |
| National pension (연금보험료공제) | Contributions paid, for a person with comprehensive income, deducted from 종합소득금액 within the art. 51의3(3) limit | 2025, 2026 | same: 소득세법 art. 51의3 |
| Insurance premiums (보험료공제) | Health, long-term care and employment insurance borne by an employee. Only for a resident with employment income, on application (art. 52(1), (8)). Claiming it ends the KRW 130,000 standard credit | 2025, 2026 | same: 소득세법 art. 52 |
| 노란우산공제 (소기업·소상공인 공제부금) | Amount paid, up to KRW 6,000,000 where 사업소득금액 is KRW 40,000,000 or less; KRW 5,000,000 where it is KRW 60,000,000 or less; KRW 4,000,000 where it is KRW 100,000,000 or less; KRW 2,000,000 above that. That amount is scaled by (사업소득금액 − rental income) ÷ 사업소득금액, and the deduction cannot exceed 사업소득금액 − rental income; R-KR-4 stops rental cases. A 법인 대표 with 총급여액 of KRW 80,000,000 or less uses 근로소득금액 in place of 사업소득금액 | 2025, 2026 | 조세특례제한법 art. 86의3, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279739&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251111&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=284389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 |
| Overall limit | KRW 25,000,000 on the deductions listed in 조세특례제한법 art. 132의2. Its list was not read in full, and item 7의2 is new in the 2026 text: Needs Input where the limit could bind | 2025, 2026 | same: 조세특례제한법 art. 132의2 |

The prior version listed health and employment insurance as deductions for the self-employed. That was wrong: see Expenses.

### Tax credits (세액공제)

Credits reduce tax and are not paid out: excess credits are treated as nil, with the pension account credit treated as unclaimed first (소득세법 art. 61). Order: reliefs, credits with no carry-forward, then credits with carry-forward (art. 60(1)).

| Credit | Amount and conditions | Tax year | Official source |
| --- | --- | --- | --- |
| Standard credit, employment income | KRW 130,000, for a resident with employment income who claims none of art. 59의4 special credits, art. 52 deductions or 조세특례제한법 art. 95의2 | 2025, 2026 | 소득세법 art. 59의4(9)(1), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| Standard credit, 성실사업자 | KRW 120,000, for a resident without employment income who meets all limbs of 시행령 art. 118의8 and makes no 조세특례제한법 art. 122의3 claim | 2025, 2026 | same: 소득세법 art. 59의4(9)(2)가; 시행령 art. 118의8, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279961&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290841&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261001&vSct=&ancYnChk=0 |
| Standard credit, others | KRW 70,000, for a resident without employment income and with no art. 122의3 claim | 2025, 2026 | same: 소득세법 art. 59의4(9)(2)나 |
| Child credit | 1 child KRW 250,000; 2 children KRW 550,000; 3 or more KRW 550,000 + KRW 400,000 for each child after the second. Child or grandchild who is a basic deduction dependant, including an adoptee or foster child | 2025, 2026 | 소득세법 art. 59의2(1), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| Child credit, age test | 2025: 8 or over. 2026: 9 or over. The article now says 13 or over, reached in steps: 2027 10, 2028 11, 2029 12 (법률 제21548호 부칙 art. 2) | 2025, 2026 | same. Children and grandchildren born in 2017 are excluded from the stepped ages by 부칙 art. 2(3). Read literally the 13 or over test applies to them; the intended result is held |
| Birth or adoption credit | KRW 300,000 for a first child, KRW 500,000 for a second and KRW 700,000 for a third or later | 2025, 2026 | same: 소득세법 art. 59의2 |
| Pension account credit | 12% of the contribution, or 15% where 종합소득금액 is KRW 45,000,000 or less (employment income only: 총급여액 KRW 55,000,000 or less). 연금저축 limit KRW 6,000,000; with 퇴직연금 KRW 9,000,000. ISA transfers: art. 59의3(3), (4) | 2025, 2026 | same: 소득세법 art. 59의3 |
| Bookkeeping credit (기장세액공제) | 20% × computed tax × (사업소득금액 per books ÷ 종합소득금액), limit KRW 1,000,000, for a 간편장부대상자 who keeps double entry and files the art. 70(4)(3) papers. Excluded where income is understated by 20% or more, or papers are not kept for 5 years from the end of the filing period, subject to the force majeure exception | 2025, 2026 | same: 소득세법 art. 56의2 |
| Employment credit (근로소득세액공제) | Tax on employment income up to KRW 1,300,000: 55%. Above: KRW 715,000 + 30% of the excess. Limit by 총급여액: up to 33,000,000, 740,000; up to 70,000,000, 740,000 − (pay − 33,000,000) × 8/1000, floor 660,000; up to 120,000,000, 660,000 − (pay − 70,000,000) × 1/2, floor 500,000; above, 500,000 − (pay − 120,000,000) × 1/2, floor 200,000 | 2025, 2026 | same: 소득세법 art. 59 |
| E-filing credit, national | KRW 10,000 for a return the taxpayer files directly after 대통령령 제36127호 of 27 February 2026 (KRW 20,000 in the earlier text), or the smaller of KRW 5,000 and 결정세액 in art. 73 cases. Applies to the May and June 2026 filing | 2025, 2026 | 조세특례제한법 art. 104의8, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279739&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251111&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=284389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0; 시행령 art. 104의5(2), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279959&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=288915&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 |
| Medical, education and monthly rent credits for business owners | 성실사업자 (조세특례제한법 art. 122의3 conditions) or a 성실신고확인 filer: medical and education credits and the monthly rent credit, against tax on business income only, to the year including 31 December 2026. Rate, limit and clawback: see Reviewer attention thresholds | 2025, 2026 | 조세특례제한법 art. 122의3, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279739&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251111&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=284389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 |
| Certification cost credit (성실신고 확인비용) | 60% of the cost directly spent on the certification, limit KRW 1,200,000, against tax on business income, for a 성실신고확인 filer who files the 성실신고확인서 and the claim form. Clawed back where income is understated by 10% or more of the corrected income, with no credit for the next 3 years | 2025, 2026 | same: 조세특례제한법 art. 126의6; 시행령 art. 121의6, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279959&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=288915&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 |

The prior version's child credit, 'KRW 150,000 per child (age ≤ 7: KRW 200,000)', matches no version read and was replaced. Art. 59의4 medical, education and insurance credits are for employment income, with the art. 122의3 route above for business owners; donation credits in art. 59의4(4) exclude a person with business income only, subject to the exceptions there.

### Expense rates, 2025 year (경비율)

Rates are set by the NTS Commissioner and must be fixed at least 1 month before the filing period starts (소득세법 시행령 art. 145(3)). 국세청고시 제2026-14호 (30 March 2026) applies to the 2025 year (art. 2). Rates are percentages by 업종코드. For a personal service provider (인적용역, codes 940***), the base simple rate applies to revenue up to KRW 40,000,000 and the excess rate to revenue above that (art. 4). The rows below are selected; read any other code from the notice. Only the 2025 year is covered. The prior version's approximate rates ('~72%' and so on) matched no row and were all replaced.

| Prior version's type | Code and name | 단순경비율 base | 단순경비율 excess | 기준경비율 | Tax year | Official source |
| --- | --- | --- | --- | --- | --- | --- |
| IT, software | 722005 컴퓨터 프로그래밍 | 75.2 | none | 26.0 | 2025 | 국세청고시 제2026-14호: https://nts.go.kr/nts/na/ntt/selectNttInfo.do?nttSn=1350024 |
| IT, software | 722000 응용 소프트웨어 | 75.2 | none | 24.7 | 2025 | same |
| IT, software | 721000 컴퓨터시스템통합자문 및 구축 | 75.0 | none | 23.4 | 2025 | same |
| IT, software | 940909 컴퓨터프로그래머 | 64.1 | 49.7 | 17.4 | 2025 | same |
| IT, software | 940926 소프트웨어프리랜서 | 64.4 | 50.2 | 20.9 | 2025 | same |
| Design, creative | 749910 시각디자인 | 78.8 | none | 19.1 | 2025 | same |
| Design, creative | 940200 화가 | 68.0 | 55.2 | 16.6 | 2025 | same |
| Design, creative | 940100 작가 | 58.7 | 42.2 | 7.2 | 2025 | same |
| Design, creative | 940306 1인미디어콘텐츠창작자 | 64.1 | 49.7 | 12.1 | 2025 | same |
| Consulting | 741400 경영컨설팅 | 77.3 | none | 23.1 | 2025 | same |
| Consulting | 741401 경영지도사 | 73.2 | none | 26.3 | 2025 | same |
| Consulting | 940600 자문, 감독, 지도료, 고문료 | 58.4 | 41.8 | 7.6 | 2025 | same |
| Retail | 525101 전자상거래업 | 86.0 | none | 11.4 | 2025 | same |
| Retail | 525102 기타 통신판매 | 87.6 | none | 13.8 | 2025 | same |
| Restaurant | 552101 한식일반 | 89.7 | none | 9.7 | 2025 | same |
| Restaurant | 552303 커피숍 | 87.5 | none | 15.1 | 2025 | same |
| Doctor (standard rate only) | 851219 기타 의원 | 67.1 | none | 15.0 | 2025 | same |
| Doctor (standard rate only) | 851211 치과의원 | 61.7 | none | 17.2 | 2025 | same |
| Doctor (standard rate only) | 851212 한의원 | 56.6 | none | 18.9 | 2025 | same |
| Lawyer (standard rate only) | 741101 변호사 | 44.6 | none | 15.9 | 2025 | same |
| Tax adviser (standard rate only) | 741201 세무사 (세무조정, 고문료) | 58.2 | none | 23.0 | 2025 | same |
| Education | 809017 외국어학원 | 83.2 | none | 23.7 | 2025 | same |
| Education | 940903 재단사 및 학원강사 | 61.7 | 46.4 | 15.4 | 2025 | same |
| Education | 940920 학습지 방문강사 | 75.0 | 65.0 | 31.5 | 2025 | same |

Doctors, lawyers and the other art. 143(7) groups cannot use 단순경비율 whatever the table shows, so only 기준경비율 is relevant to them.

### Bookkeeping and estimate thresholds

The prior version's table (KRW 48,000,000 for most services, KRW 75,000,000 for services, KRW 150,000,000 for manufacturing) mixed 3 different tests and left out the KRW 300,000,000 group. These are the tests read. Each uses revenue from the year before, not the current year, except where a row says so. Revenue excludes disposals of business tangible assets for the 간편장부 and 성실신고 tests.

| Group (시행령 art. 208(5), art. 143(4)) | 간편장부대상자: prior year revenue under | 단순경비율: prior year revenue under | 성실신고확인: current year revenue at or above | Tax year | Official source |
| --- | --- | --- | --- | --- | --- |
| 가: agriculture, forestry, fishing, mining, wholesale and retail (not commodity brokerage), real estate sale, and anything not in 나 or 다 | 300,000,000 | 60,000,000 | 1,500,000,000 | 2025, 2026 | 소득세법 시행령 arts 133, 143(4), 208(5), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279961&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290841&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261001&vSct=&ancYnChk=0 |
| 나: manufacturing, accommodation and food, electricity and gas, water and waste, construction (not non-residential building), residential development and supply, transport and storage, information and communications, finance and insurance, commodity brokerage | 150,000,000 | 36,000,000 | 750,000,000 | 2025, 2026 | same |
| 다: real estate rental and other real estate (not sale), professional, scientific and technical services, facility management and business support, rental services, education, health and social work, arts and sport, associations, repair and other personal services, household employment | 75,000,000 | 24,000,000 | 500,000,000 | 2025, 2026 | same |

Limbs on these groups:

- **New business, bookkeeping.** A person who starts in the year is a 간편장부대상자 whatever the revenue (art. 208(5)(1)), unless the art. 208(5) proviso excludes them: see Never 간편장부대상자 below.
- **New business, expense rates.** That person is a 단순경비율 filer only if current year revenue is under the 간편장부 column for the group (art. 143(4)(1) and opening words), and they are outside Never 단순경비율 below. Above the column the estimate route is 기준경비율, at the 간편장부대상자 multiple.
- **단순경비율 for a continuing business needs both tests.** Prior year revenue under the column, and current year revenue under the 간편장부 column (art. 143(4), opening words).
- **Personal services.** 인적용역 under 부가가치세법 시행령 art. 42(1) sits in group 나 for 단순경비율 and group 다 for 간편장부 (NTS page: https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2230&cntntsId=7669). Bath houses sit in 나 for bookkeeping (시행규칙 art. 95의2) and 다 for expense rates.
- **Several businesses.** Main business revenue + other revenue × (main business threshold ÷ other business threshold) (art. 208(7), applied to expense rates by art. 143(6)).
- **Never 간편장부대상자.** Medical, veterinary and pharmacy businesses (art. 147의2) and the listed professions in 부가가치세법 시행령 art. 109(2)(7): 변호사, 심판변론인, 변리사, 법무사, 공인회계사, 세무사, 경영지도사, 기술지도사, 감정평가사, 손해사정인, 통관업, 기술사, 건축사, 도선사, 측량사, 공인노무사, 의사, 치과의사, 한의사, 수의사, 약사, 한약사 (list as printed on NTS https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2231&cntntsId=7670; the decree limb itself was not read beyond the reference).
- **Never 단순경비율 (art. 143(7)).** Those same two groups, a person who had to join as a cash receipt merchant and did not (that year only), and a person notified 3 or more times totalling KRW 1,000,000 or more, or 5 or more times, for card or cash receipt breaches (that year only).
- **Everyone else with a business** must keep double entry (복식부기의무자, 소득세법 art. 160).
- **성실신고 service list.** The KRW 500,000,000 column also takes the service businesses in 별표 3의3 (시행령 art. 133).

| Multiple on the 기준경비율 result | Figure | Tax year | Official source |
| --- | --- | --- | --- |
| 간편장부대상자 | 2.8 | 2025, 2026 | 소득세법 시행규칙 art. 67, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=272661&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20250701&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=286379&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| 복식부기의무자 | 3.4 | 2025, 2026 | same |

### Withholding rates

| Payment | Rate | Tax year | Official source |
| --- | --- | --- | --- |
| Business income within 소득세법 art. 127(1)(3) and 시행령 art. 184 | 3% national | 2025, 2026 | 소득세법 art. 129(1)(3), 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |
| Foreign professional athlete | 20% national | 2025, 2026 | same |
| Local special collection (특별징수) | 10% of the income tax withheld, so 0.3% of a 3% payment | 2025, 2026 | 지방세법 art. 103의13, 2025: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276349&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0; 2026: https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 |

### Enactment position

- **Law for 2025.** 소득세법 and related Acts as they stood at 31 December 2025.
- **2025 revision, enacted.** 소득세법 법률 제21221호 (23 December 2025) and 국세기본법 법률 제21212호 (23 December 2025) are law. Band rates did not change. Changes that touch this file are the art. 59의4 education credit, which concerns employment income, and the late payment rule in 국세기본법 art. 47의4 from 1 July 2026 (see Penalties and interest).
- **April 2026 law.** 소득세법 법률 제21548호 (21 April 2026), in force on promulgation and applying to the year containing that date, changed the child credit age.
- **Decree rename.** 기획재정부령 became 재정경제부령 after the ministry's reorganisation. The substance of the art. 67 multiple did not change.
- **2027 text.** The version dated 1 January 2027 differs on virtual asset income (arts 14, 21, 70(2), 84 and 127 among the differences seen). A full comparison of that version and of later versions dated 9 September 2027 and 1 January 2028 was not made. R-KR-7 stops any 2027 computation.
- **2026 revision, not law as read.** The government announced proposals on 3 August 2026 and sent 11 amending bills to the National Assembly on 3 September 2026. As summarised by the National Assembly Budget Office (NABO), October 2026, they include a 1 point cut in the personal service withholding rate, a higher dependant income test (KRW 3,000,000 and KRW 7,500,000), a monthly rent credit limit of KRW 12,000,000, the end of the birth and adoption credit and the marriage credit, and a 3 year extension for 성실사업자 medical and related credits. The bill text and its passage status were not read. None of these is applied here.

The marriage credit (혼인세액공제) in 조세특례제한법 was not otherwise read. It is Needs Input if claimed.

## The base

### Income

Comprehensive income under 소득세법 art. 4 aggregates interest, dividend, business, employment, pension and other income. Art. 14(3) keeps these outside the aggregate: non-taxable income, daily workers' pay, interest and dividends at the art. 129(2) rate, income of the listed non-distributing bodies, income separately taxed under 조세특례제한법, art. 14(3)(6) interest and dividends, small housing rental income, and separately taxed other income and pensions. Business income is in art. 19, and is total receipts (총수입금액, art. 24) less necessary expenses (필요경비, art. 27).

Receipts belong to the year in which they become fixed (art. 39(1)), not the year of the bank credit. Decree rules on specific timing were not read: a receipt straddling year end is Needs Input.

Not in 총수입금액 (art. 26): income tax and local income tax refunds and amounts applied to other tax; assets received free as limited by art. 26(2); income carried from earlier years; own produce used in the listed businesses; refund interest; and VAT output tax (art. 26(9)). A VAT-registered general operator's receipts therefore include VAT that is not revenue.

**Methods.** There are 4 routes, and the prior version's table described the last as 'revenue minus major expenses, then multiplied by standard rate', which was wrong:

| Route | Who | Business income |
| --- | --- | --- |
| Double entry (복식부기) | Required for 복식부기의무자; open to all | 총수입금액 − 필요경비 on the books |
| Simplified books (간편장부) | 간편장부대상자 | 총수입금액 − 필요경비 on the books |
| 단순경비율 | 단순경비율 적용대상자 without books | max(revenue − revenue × 단순경비율, 0), with revenue excluding the employment retention amount in 시행규칙 art. 67의2. For 940*** in 2025: max(min(revenue, 40,000,000) × (1 − 기본율) + max(revenue − 40,000,000, 0) × (1 − 초과율), 0), under Notice art. 4 |
| 기준경비율 | Others without books | The lower of (A) and (B) below, while the multiple applies |

The 기준경비율 formula (시행령 art. 143(3)(1)):

(A) = max(revenue − min(매입비용 + 임차료 + 급여·임금·퇴직급여 + revenue × 기준경비율, revenue), 0)

(B) = 단순경비율 income × the multiple (2.8 or 3.4). For 940***, this file reads that income as including the split above. That is a reading of 시행령 art. 143(3)(1) and Notice art. 4, neither of which says so in terms, and a reviewer should confirm it.

- 매입비용 excludes purchases of business tangible and intangible assets. 임차료 is rent of those assets. Both, and pay, must rest on evidence.
- For a 복식부기의무자 the rate is half the 기준경비율.
- The multiple applies up to the year including 31 December 2027, and the decree says the income 'may' be set at it.
- Evidence that cannot be supplied needs a 주요경비지출명세서 (art. 143(9)).
- Where no rate has been set, art. 143(3)(2) falls back to the income of a comparable business. That is another reason a 2026 estimate is Needs Input here.

Income on an estimate is not free of penalty: see Example 1. Carried losses are also lost on most estimates: see Losses.

### Expenses

Necessary expenses are costs generally accepted in the business and corresponding to the revenue (소득세법 art. 27). Not allowed (art. 33(1)): income tax and local income tax; fines and penalties; 가산금 and enforcement costs; failure to collect; household costs (가사 경비); depreciation over the limit; revaluation losses; unpaid individual consumption or liquor tax on goods taken out but not sold, unless added to the product value; VAT input tax, except where exempt, as the decree lists, or VAT a 간이과세자 paid; construction interest; interest to unidentified creditors; discretionary public charges; costs unrelated to the business; prepaid expenses; and damages for intentional or grossly negligent harm to others' rights.

**Social contributions.** `kr-social-insurance` computes them; this file supplies only the treatment:

| Item | Treatment | Basis |
| --- | --- | --- |
| Employer share of staff health, employment and long-term care insurance | 필요경비 | 소득세법 시행령 art. 55(1)(11) |
| Owner's own premium as 직장가입자 (사용자 본인) | 필요경비 | art. 55(1)(11의2) |
| Owner's own premium as 지역가입자 | 필요경비 | art. 55(1)(11의3) |
| Employment insurance for artists, platform workers and the self-employed | 필요경비 | art. 55(1)(11의4) |
| Industrial accident insurance for platform workers and small business owners | 필요경비 | art. 55(1)(11의5) |
| Employee's own health, care and employment premium | 소득공제 (art. 52), only with employment income | 소득세법 art. 52(1) |
| National pension (own) | 소득공제, not 필요경비 | 소득세법 art. 51의3 |

The prior version treated health premiums as a 소득공제 for everyone. That was wrong for the owner's own premium. On a books route it reduces income as an expense. On an estimate route the treatment is Needs Input: the rate may replace expenses, so the premium may give no separate deduction, but no text read says so in terms.

**Mixed use and home office.** Household costs are not allowed (art. 33(1)(5); 시행령 art. 61). The prior version said 'floor area ratio' is an accepted basis and that proportionate rent and utilities are deductible at the business percentage. No primary text read fixes a basis. Treat it as conditioned: a business share needs a record that shows business use. With no record or split, the amount is not deducted and is Needs Input.

**기업업무추진비 (entertainment, formerly 접대비).** The prior version used the old name and said the cap 'depends on the type of business'. The text reads:

- **Evidence.** One item over KRW 30,000 (경조금 over KRW 200,000) is not deductible unless paid by 신용카드 등 or supported by a listed document. Listed: credit, debit and foreign credit cards, named prepaid cards and the other 시행령 art. 83(4) instruments; 현금영수증; 계산서 or 세금계산서; 매입자발행세금계산서 or 계산서; and 원천징수영수증 where the supplier is an unregistered service provider. Exceptions: cash abroad where only cash is accepted, and payment through a financial company to a farmer or fisher with a remittance statement (소득세법 art. 35(2); 시행령 art. 83).
- **Annual cap.** 12,000,000 (중소기업 36,000,000) × months ÷ 12, plus revenue × 30/10,000 up to KRW 10,000,000,000; 30,000,000 + 20/10,000 of the excess up to KRW 50,000,000,000; 110,000,000 + 3/10,000 of the excess above. Revenue from related parties counts at 10% of the rate (art. 35(3); 시행령 arts 83(9), 98(1)).
- **Names and purpose.** Keep them as support. The statutory test is the evidence above, not the attendee list.

**Business cars (업무용승용차).** Art. 33의2 applies only to 복식부기의무자, and a 운행기록부 is one route, not a blanket duty. 시행령 art. 78의3 sets straight-line depreciation over 5 years, a business-only insurance route, and limits: with no log, costs up to KRW 15,000,000 count in full (pro rata for part years) and above that the share is 15,000,000 ÷ costs; depreciation over KRW 8,000,000 and disposal losses carry forward; a statement goes with the return, with a 1% penalty under 소득세법 art. 81의14. The rule on a second car without insurance changed in the December 2025 and February 2026 decree amendments: Needs Input. Other taxpayers' vehicle costs follow art. 27 and the household limit, with the business share shown by record.

**Assets.** Capital cost goes through depreciation (art. 33(1)(6); 시행령 arts 62 to 67). Depreciation rates are not reproduced: Needs Input. An asset of KRW 1,000,000 or less per trading unit is expensed in the year it enters use, except assets held in quantity by the nature of the business and assets acquired to start or expand the business (시행령 art. 67(4)). Whatever the cost, these are deductible only if charged as an expense in the year they enter use: 어구; 영화필름, 공구, 가구, 전기기구, 가스기기, household items and fittings, 시계, 시험기기, 측정기기 and 간판; rental videotapes and music CDs under KRW 300,000 each; and phones, including mobile phones, and personal computers with peripherals (art. 67(7)). The prior version's KRW 500,000 flag is a review flag only.

**Evidence.** A business with an expense over the 시행령 art. 208의2 limits must hold a 계산서, 세금계산서, card slip or 현금영수증 (소득세법 art. 160의2). Art. 208의2(1) has 9 limbs of exception, including KRW 30,000 or less and a trade with a non-resident or foreign corporation with no place of business in Korea. The others are not reproduced: check them before charging the penalty.

### Allowances, ladder and ordering

Walk the ladder in this order. It replaces the prior version's flow, which applied national due × 1.10.

1. Total revenue, gross of withholding and platform fees, excluding VAT output tax and art. 26 items.
2. Less 필요경비, or the estimate route, for 사업소득금액.
3. Add employment income (총급여액 − 근로소득공제). Current year business losses come off in the art. 45 order. Carried losses come next.
4. 종합소득금액.
5. Less personal deductions, art. 51의3 pension, art. 52 premiums for employees, and 노란우산공제, for 과세표준. Where 과세표준 would be negative it is nil: max(종합소득금액 − deductions, 0).
6. Tax on 과세표준 from the national table: 산출세액.
7. Less reliefs and credits, in the art. 60 order: 결정세액. Add penalties (가산세).
8. Less 중간예납, 토지등 매매차익예정신고 tax, 수시부과세액, withholding, 납세조합 징수세액 and 납세조합공제 (소득세법 art. 76(3)): national balance, payable or refundable. Two union amounts are held. First, arts 150(3), 151 and 152(2) have the union collect the tax after the monthly credit, but art. 76(3)(5) does not define 납세조합 징수세액. This file reads it as that net amount collected, and a reviewer should confirm that reading. Second, art. 76(3)(5) deducts 그 공제액 without saying which amount that is on a return. This file reads it as the art. 150(3) proviso amount, 3% of the computed tax on the employment income the union withheld, and a reviewer should confirm that reading too. Until then both amounts are held: take the balance before them, and show any balance after them as conditional on both readings. Where no union collected tax, both are nil and the balance before them stands. Art. 150(4) limits the credit to KRW 1,000,000 a year, or KRW 1,000,000 × the months in the tax period or of employment ÷ 12 where that period is under 1 year. The art. 150(2) business limb ended with collections to 31 December 2024. Count the credit once, here and not in step 7. That is an inference, and a reviewer should confirm it: art. 76 takes 세액공제액 in (1) and this credit in (3)(5), and art. 152(1) names 세액공제 and 납세조합공제 apart, but 법률 제20615호 부칙 art. 14 calls it a 세액공제, and no text says so in terms. Its place on the return forms is unverified: the forms were not read.
9. Separately: local tax on the same 과세표준 from the art. 92(1) table, less local credits, plus local penalties, less local 토지등 매매차익예정신고 tax, 수시부과세액, 특별징수세액 and 납세조합 징수세액 (지방세법 art. 95(3)): local balance. The local 납세조합 징수세액 is the amount actually collected under art. 103의17(1), 10% of the income tax the union collects and pays under 소득세법 arts 150 and 151. Art. 95(3)(5) has no 공제액 limb, so this amount does not turn on the step 8 readings. Whether art. 167의2(1) of 지방세특례제한법 gives a local credit of 10% of 납세조합공제 is held: it covers tax credited under 소득세법 and does not name this credit, so take the balance before any such share and show any balance after it as conditional.

**Rounding.** The prior version said round taxable income down to KRW 10,000. No text read supports that. 국고금 관리법 art. 47 drops amounts under KRW 10 on receipts and amounts under KRW 1 on a national tax base; local governments may apply the same rule. This file does not round 과세표준 to KRW 10,000. Show the rounding on the payment line only.

### Losses

A business loss on the books comes off, in the year, against employment, pension, other, interest and dividend income in that order (소득세법 art. 45(1)). A loss on real estate rental is ring-fenced, except residential rental (art. 45(2)). The remainder carries forward 15 years from the end of the loss year, earliest first, against business, employment, pension, other, interest and dividend income in that order (art. 45(3)). Older losses may be under transitional rules not read: Needs Input. Where income is estimated, carried losses do not come off, except where books were destroyed by force majeure (art. 45; NTS https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2224&cntntsId=7664). A small or medium business may carry a loss back one year by application by the filing deadline, with both years filed on time (art. 85의2).

### Withholding

Only these payments carry the 3%: supplies exempt from VAT under 부가가치세법 art. 26(1)(5) (medical and health services) and art. 26(1)(15) (personal services), other than the medicine share of dispensing and the entertainers in 부가가치세법 시행령 art. 42(1)바 (소득세법 art. 127(1)(3); 시행령 art. 184). The payer must be a business, a corporation or other person within the article, or a national or local government.

The prior version said 'most' self-employed Koreans have 3.3% withheld and told the reader to 'always gross up'. That is conditioned. Sales of goods and VAT-taxable services do not carry this withholding. A person who sells design services through a VAT-registered business, for example, has no withholding unless a document shows it. Gross up only where a 원천징수영수증, a 지급명세서 entry shown on Hometax or an invoice shows the gross and the tax.

The worked figure in the prior version was wrong. On KRW 1,000,000, tax is 30,000 + 3,000 = 33,000 and the net is 967,000, not 966,700 and 33,300.

Reconcile bank inflows against withholding receipts, so that all income is reported gross and all withholding is claimed as credits.

Business income in art. 144의2 (insurance agents, door-to-door sales and contract delivery) has year-end settlement and may not need a May return (art. 73(1)(4)). Those cases need the NTS list and are Needs Input here.

### Defaults

A default stands only where the law read fixes the result of the missing fact. Everything else is Needs Input.

| Situation | Treatment | Basis |
| --- | --- | --- |
| Business type unknown | Stop computing. Needs Input: rates and thresholds turn on it | Notice; 시행령 arts 143, 208 |
| Bookkeeping method unknown | Needs Input. Prior year revenue and group settle the legal status, not whether books exist. The prior version's default of 간편장부 is withdrawn | 시행령 art. 208(5) |
| Route unclear | Needs Input. Show each available route as Example 1 does. The prior version's default of 기준경비율 'as more conservative' is withdrawn: it is a legal category, not a choice | 시행령 art. 143(4) |
| No books, 단순경비율 tests unproved | Needs Input | 시행령 art. 143(4), (7) |
| 2026 estimate route | Needs Input: no rate read | Notice art. 2 |
| Estimated tax unknown | Needs Input, leave out of the credits. The prior version's 'will result in penalty calculation' is withdrawn | 소득세법 art. 65 |
| Family papers missing | Default stands: self basic deduction and the standard credit only, until the art. 70(4)(1) papers exist. Flag as Needs Input | 소득세법 art. 54(2) |
| Family fact unclear (age, income, disability) | Needs Input | Arts 50, 51 |
| Withholding not evidenced | Needs Input. Leave the credit out | Withholding above |
| Mixed-use cost with no record | Default stands: not deducted. Flag as Needs Input | Art. 33(1)(5) |
| Entertainment item over KRW 30,000 with no listed evidence | Default stands: not deducted | Art. 35(2) |
| Business or personal character unclear | Needs Input, in a suspense line | Arts 27, 33 |
| 성실사업자 limbs unproved | Default stands at KRW 70,000, with the KRW 120,000 effect disclosed | Art. 59의4(9) |
| Local rate other than standard | Needs Input | 지방세법 art. 92(2) |
| Asset cost, life or date unknown | Needs Input | 시행령 arts 62 to 67 |

### Reviewer attention thresholds

Each row is a flag, not a rule of law, unless a source is shown.

| Flag | Threshold | Action |
| --- | --- | --- |
| Double entry required | Prior year revenue at or above the 간편장부 column, for a business not started in the year, or a listed profession | 시행령 art. 208(5); check records and the 7/10,000 penalty test |
| Estimated tax | Instalment of KRW 500,000 or more (소득세법 art. 86(4)) | Check the notice |
| VAT registration | Any business: register within 20 days of starting, with no revenue threshold in 부가가치세법 art. 8. The prior version's 'Revenue > KRW 48,000,000' is not a registration test | Route to `south-korea-vat` |
| KRW 48,000,000 | Prior year business revenue under this is one 소규모사업자 limb. The others are a new starter in the year and a person within art. 73(1)(4) (시행령 art. 132(4)) | Check the record, receipt and evidence penalties |
| Tax accountant recommended | Revenue over KRW 100,000,000, carried from the prior version as a review habit, not law | Recommend a 세무사 |
| 성실신고확인 | Current year revenue at or above the table column | Check the 30 June date and certificate |
| Large purchase | Over KRW 500,000, carried from the prior version; the statutory figure is KRW 1,000,000 per trading unit, with the art. 67(7) items in Assets | Check for a capital asset |
| 조세특례제한법 art. 7 relief | Any small or medium business in a listed industry | Not computed; the article runs to years ending by 31 December 2028 |
| 최저한세, 농어촌특별세 | Any relief claimed | Not computed |
| 성실사업자 credit clawback | Income understated by 10% or more of the corrected income (성실사업자 20%): 조세특례제한법 art. 122의3(5) | Read the Act: the NTS page differs, see Source conflicts |
| Art. 122의3 rates | Medical and education 15%, or 20% for 미숙아 and 선천성이상아 medical costs and 30% for 난임시술 (art. 122의3(1)). Monthly rent 15%, or 17% where 종합소득금액 is KRW 45,000,000 or less, only where it is KRW 70,000,000 or less; rent over KRW 10,000,000 does not count (art. 122의3(3)). Both come off tax on business income only (art. 122의3(1) and (3)), and credit above that tax is lost (art. 122의3(4)). After a clawback, no art. 122의3 credit for the next 3 periods (art. 122의3(6)) | Check the conditions for the 성실사업자 route: revenue over 50% of the 3 year average, 2 years or more in business, and the decree |

### Classifying a bank line

This is a deterministic pre-classifier. It is a prompt, not law: where a line does not match, or a condition cannot be shown, it is Needs Input. Account names (소모품비, 지급수수료 and so on) are bookkeeping labels, not statutory categories.

**Income (입금):**

| Pattern | Head | Treatment | Notes |
| --- | --- | --- | --- |
| 타행입금 [client name] / 이체입금 | 사업소득 | Gross revenue | Wire transfer from a business client |
| 자동이체 입금 [client] | 사업소득 | Revenue | Auto-transfer standing order from a client |
| 카카오페이 입금 / KAKAOPAY | 사업소득 | Revenue, gross of fees | KakaoTalk Pay settlement |
| 네이버페이 정산 / NAVERPAY | 사업소득 | Revenue, gross of fees | Naver Pay e-commerce settlement |
| 쿠팡페이 정산 / COUPANG | 사업소득 | Revenue, gross of fees | Coupang marketplace settlement |
| 토스 입금 / TOSS CREDIT | 사업소득 | Revenue | Toss digital payment receipt |
| 원천징수 후 입금 | 사업소득 | Revenue, gross up only with a document | 3% national + 0.3% local |
| 급여이체 [employer] | 근로소득 | Not business income | Employment salary |
| 이자입금 / 이자수익 [bank] | 이자소득 | Not business income | Check R-KR-3 |
| 배당금 입금 | 배당소득 | Not business income | Check R-KR-3 |
| 세금환급 국세청 | Exclude | Not income | Art. 26(1) |
| 대출금 입금 | Exclude | Not income | Loan proceeds |

**Expenses (출금):**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| 사무실임대료 / 임차료 [landlord] | 임차료 | Deductible for business premises | Evidence |
| 공과금 / 전기요금 [KEPCO/한국전력] | 수도광열비 | Business share, with a record | Household share out |
| 도시가스 / 가스요금 | 수도광열비 | Business share, with a record | Household share out |
| 인터넷 요금 [KT/SK브로드밴드/LG유플러스] | 통신비 | Business share, with a record | Mixed use |
| 휴대폰 요금 [SK텔레콤/KT/LG유플러스] | 통신비 | Business share, with a record | Mixed use |
| 교통비 [대중교통/버스/지하철] | 여비교통비 | Deductible if business | T-money and Cashbee transit charges |
| KTX / SRT [train] | 여비교통비 | Deductible if business | Keep the boarding pass |
| 대한항공 / 아시아나 / 저비용항공사 | 여비교통비 | Deductible if business | |
| 접대비 / 식사 [restaurant] | 기업업무추진비 | Art. 35 evidence and cap | A personal meal is out |
| 도서비 [Kyobo/Aladin] | 소모품비 | Deductible if professional | |
| 교육훈련비 [Fastcampus/패스트캠퍼스/학원] | 교육훈련비 | Deductible if business related | |
| Adobe / Microsoft / Google Workspace | 소모품비 / 임차료 | Deductible if business | Foreign supplier: check evidence |
| Figma / Notion / Slack | 소모품비 | Deductible if business | Foreign supplier: check evidence |
| 세무사 수수료 | 지급수수료 | Deductible for the business part | Personal return fees: Needs Input |
| 법무사 / 변호사 수수료 | 지급수수료 | Deductible if business related | |
| 국민건강보험 / 건보 | 필요경비 for the owner's own premium | Books route: expense. Estimate route: Needs Input, held | Replaces the prior 'exclude' row |
| 국민연금 / 연금보험료 | 소득공제 | Not 필요경비 | Art. 51의3 |
| 종합소득세 납부 / 소득세 | Exclude | Tax payment | Art. 33(1)(1) |
| 지방소득세 납부 | Exclude | Local tax payment | Art. 33(1)(1) |
| 중간예납 국세청 | Exclude | Credit against national tax | Art. 33(1)(1) |
| 부가가치세 납부 | Exclude for a general operator | A 간이과세자's VAT paid is outside the input tax bar | Art. 33(1)(9) |
| 개인인출 / 본인출금 | Exclude | Drawings | Art. 33(1)(5) |

**Platform lines:**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| 카카오뱅크 이체 / KakaoBank Transfer | Possible business income | Confirm client versus personal transfer |
| 토스뱅크 입금 / TossBank Credit | Possible business income | Digital bank receipt |
| 케이뱅크 이체 / K bank | Possible business income | Digital bank |
| 네이버파이낸셜 / 네이버페이 | Business income | Naver Pay settlement |
| 원천징수 3.3% | Gross up with a document | National 3% + local 0.3% |

### Bank formats

| Bank | Format | Key fields |
| --- | --- | --- |
| KB국민은행 (Kookmin) | CSV / PDF | 거래일, 거래내용, 출금금액, 입금금액, 잔액 |
| 신한은행 (Shinhan) | CSV | 거래일자, 적요, 출금액, 입금액, 잔액 |
| 우리은행 (Woori) | CSV | 날짜, 내용, 출금, 입금, 잔액 |
| KEB하나은행 (Hana) | CSV | 거래일, 거래내용, 출금(원), 입금(원), 잔액(원) |
| 카카오뱅크 (KakaoBank) | CSV | 거래일시, 거래내용, 출금금액, 입금금액, 잔액 |
| 토스뱅크 (TossBank) | CSV / App | 날짜, 내용, 금액, 잔액 |
| 케이뱅크 (K bank) | CSV | 거래일, 내용, 출금, 입금, 잔액 |

| Korean term | English | Hint |
| --- | --- | --- |
| 타행이체 입금 | Transfer from another bank | Potential business income |
| 자동이체 입금 | Auto-transfer credit | Regular income from a client |
| 카드결제 | Card payment | Expense |
| ATM출금 / 자동화기기 | ATM withdrawal | Personal: investigate |
| 세금이체 / 국세청 | Tax payment | Exclude |
| 공과금 자동이체 | Utility auto-debit | Business or personal |
| 이자입금 | Interest credit | Other income |
| 중간예납 | Estimated tax prepayment | Tax credit |
| 원천징수 후 수령 | Received after withholding | Gross up with a document |

### Excel working paper

```
종합소득세 WORKING PAPER -- Tax Year ____ -- estimated, not reviewed
납세자 (Taxpayer): _______________  사업자번호: ___________
업종 코드 (Business type code): ___________
경로 (Route): 복식부기 / 간편장부 / 단순경비율 / 기준경비율 [circle one]

A. 총수입금액 (GROSS REVENUE)
  A1. Total business revenue (gross, before withholding, excluding VAT output tax) ___________

B. 필요경비 (NECESSARY EXPENSES)
  B1. 임차료 (rent)                           ___________
  B2. 수도광열비 (utilities -- business share) ___________
  B3. 통신비 (communications -- business share) ___________
  B4. 여비교통비 (travel)                     ___________
  B5. 기업업무추진비 (capped, evidence tested) ___________
  B6. 광고선전비 (advertising)                ___________
  B7. 소모품비 (consumables / SaaS)           ___________
  B8. 감가상각비 (depreciation)               ___________
  B9. 외주비 (subcontracting)                 ___________
  B10. 지급수수료 (professional fees)         ___________
  B11. 건강보험료 등 (owner's own premiums, 시행령 art. 55) ___________
  B12. 기타경비 (other expenses)              ___________
  B13. Total 필요경비                         ___________

C. 사업소득금액 (A1 - B13, or the estimate route) ___________
C2. 근로소득금액 (mixed cases)                ___________
C3. 이월결손금 (carried loss, books route)    ___________
C4. 종합소득금액 (C + C2 - C3)                ___________

D. 소득공제 (INCOME DEDUCTIONS)
  D1. 기본공제 and 추가공제                   ___________
  D2. 연금보험료공제 (pension)                ___________
  D3. 보험료공제 (employee premiums only)     ___________
  D4. 기타 공제 (노란우산공제 etc.)           ___________
  D5. Total 소득공제                          ___________

E. 과세표준 max(C4 - D5, 0)                   ___________

F. 산출세액 (national table)                  ___________

G. 세액공제 (TAX CREDITS)
  G1. 표준세액공제 / other credits            ___________

H. 결정세액 (F - G1)                          ___________
H2. 가산세 (penalties)                        ___________

I. 기납부세액 (national)
  I1. 원천징수 (3%)                           ___________
  I2. 중간예납                                ___________
  I3. 매매차익예정, 수시부과 (art. 76(3)) ___________
  I4. 납세조합공제 (art. 76(3)(5); amount held, see ladder step 8; kept out of G1 by inference, see ladder step 8; form mapping unverified) ___________
  I5. 납세조합 징수세액 (art. 76(3)(5); amount held, see ladder step 8) ___________

J. NATIONAL BALANCE before I4 and I5 (H + H2 - I1 - I2 - I3) ___________
J2. J - I4 - I5, conditional on both readings in ladder step 8 ___________

K. 개인지방소득세 (local table on E)          ___________
K2. Local credits (2025: 10% of national credits except e-filing; 2026: show with and without, art. 167의2 held; no share of I4, see K6) ___________
K3. Local penalties                           ___________
K4. 특별징수 (0.3%)                           ___________
K5. 매매차익예정, 수시부과, 납세조합 (art. 95(3)) ___________
K6. 10% of I4, if art. 167의2(1) reaches 납세조합공제 (held, see ladder step 9) ___________

L. LOCAL BALANCE before K6 (K - K2 + K3 - K4 - K5), filed through Wetax ___________
L2. L - K6, conditional on the readings in ladder steps 8 and 9 ___________

REVIEWER FLAGS:
  [ ] Business type code confirmed?
  [ ] All withholding receipts (원천징수영수증) collected?
  [ ] Estimated tax (중간예납) credited?
  [ ] Pension in 소득공제; owner's health premium in 필요경비 (books route)?
  [ ] Entertainment evidence and cap applied?
  [ ] Double-entry threshold checked for this business?
```

## Deadlines and filing

Where a date falls on a Saturday, Sunday, public holiday, substitute holiday or Labour Day (노동절), it moves to the next day (국세기본법 art. 5(1), as amended on 11 November 2025). A system failure also moves the date (art. 5(3)). Dates for 2026 are computed from the statute: no NTS page for that year was read.

| Item | 2025 year | 2026 year | Basis |
| --- | --- | --- | --- |
| 사업장현황신고 (VAT-exempt business) | 10 February 2026 | 10 February 2027 | 소득세법 art. 78; NTS https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2283&cntntsId=7699 |
| Final return and payment (종합소득세) | 1 June 2026, because 31 May 2026 is a Sunday | 31 May 2027 | Arts 70, 76 |
| 성실신고확인 filers | 30 June 2026 | 30 June 2027 | Art. 70의2 |
| Local income tax | Same dates, to the local government | Same dates | 지방세법 art. 95(1); 지방세기본법 art. 24(1) |
| Instalment of national tax | Within 2 months after the due date. Computed, not read on a page: 3 August 2026, as 1 August is a Saturday; 성실신고 filers 31 August 2026, as 30 August is a Sunday | Computed, not read on a page: 2 August 2027, as 31 July is a Saturday; 성실신고 filers 30 August 2027 | 소득세법 art. 77 |
| Estimated tax (중간예납), paid in the year itself | 1 December 2025, as 30 November was a Sunday | 30 November 2026 | 소득세법 art. 65 |
| VAT | Route to `south-korea-vat`. The prior version's '25 January and 25 July' is the final return date for a general operator's 2 periods (부가가치세법 art. 49), beside the interim step in art. 48. A 간이과세자 has one period, the year (art. 67) | Same | 부가가치세법 |

**Payment in instalments.** The prior version said 'with NTS approval'. The article needs no approval. Tax payable over KRW 10,000,000 may be split: up to KRW 20,000,000, the excess over KRW 10,000,000; above KRW 20,000,000, up to 50% (소득세법 art. 77; 시행령 art. 140). Local income tax over KRW 1,000,000 may be split within 2 months: up to KRW 2,000,000, the excess over KRW 1,000,000; above that, up to 50% (지방세법 art. 95(4); 시행령 art. 92(3)).

**The 2025 year extension (date-limited).** NTS 7664 records an administrative extension of the payment date from 1 June 2026 to 31 August 2026, with instalments to 2 November 2026. It covered (1) businesses within the January 2026 VAT payment extension: general operators with 2024 revenue of KRW 1,000,000,000 or less and first half 2025 sales down 30% or more on the prior year, in manufacturing, construction, wholesale, retail, food, accommodation, transport or services; and all 간이과세자; excluding real estate rental and professional services; (2) businesses in the oil-sensitive VAT extension; and (3) operators hurt by unpaid platform settlements (티몬, 위메프). It needed a return by 1 June 2026, and excluded people with financial income over KRW 20,000,000 and 성실신고 filers. Others could apply on Hometax: 로그인 > 증명·등록·신청·사업자현황 > 세금관련 신청·신고 공통분야 > 신고·납부 기한연장 신청/내역조회 > 신고분 납부기한 연장신청. This is administrative practice, not statute. It extended payment, not filing, and those dates have passed. Whether local tax had the same extension was not read: held. No such measure is assumed for 2026.

**Estimated tax (중간예납).** It is half (the prior version's 'approximately 50%') of the prior year's 중간예납기준액, with notices issued 1 to 15 November and payment by 30 November (art. 65). It is not collected where the instalment is under KRW 500,000 (art. 86(4)). The rest of the list comes from 시행령 art. 123 and NTS 7673 for 2026. Outside it: a person who started in 2026 and was not in business at 31 December 2025; a person who suspended or closed by 30 June 2026, or closed later with 수시 payment or assessment; a 납세조합 member whose union withheld monthly from January to June; a real estate seller whose preliminary payment exceeds 50% of the base; and a person with only these: interest, dividend, employment, pension or other income; 사무지원 서비스 income; income assessed under art. 82; self-employed artists (저술가, 화가, 배우, 가수, 영화감독, 연출가, 촬영사, as the page lists them); athletes, coaches and referees; independent insurance and securities solicitors; door-to-door sales commissions where the 2025 year-end settlement was made; separately taxed small housing rental income; and joint business income of 전환정비사업조합 members. A person whose half-year tax is under 30% of the base may file an estimate (art. 65(3)): half of the computed tax, less reliefs, interim payments, 수시부과 and withholding. A 복식부기의무자 with no base must file (art. 65(5)). Local income tax has no such instalment in the articles read.

**Filing forms.** Hometax, or paper, 별지 제40호서식(1); 제40호서식(4) for 단순경비율. NTS 7665 attachments: the return and payment statement; deduction and credit statements with proofs; for 복식부기의무자 the balance sheet, income statement, trial balance and adjustment statement (art. 70(4); failure to attach is treated as no return); 간편장부 소득금액계산서; 추계소득금액계산서; 성실신고확인서; 영수증수취명세서 (별지 제40호의5); 결손금소급공제세액환급신청서.

**성실신고확인.** Certifier: 세무사, 공인회계사, 세무법인 or 회계법인; a 세무사 cannot certify their own return (시행령 art. 133).

**Local return.** After the Hometax return, follow 개인지방소득세 신고 이동 to Wetax, or 신고내역조회 > 지방소득세 신고이동 (NTS 7664). Wetax itself was not read. Filing with the wrong authority remains valid (지방세법 art. 95(1)). Paying a provisional 납부서 by the deadline counts as filing, where NTS sent one (art. 95(5), (6); 시행령 art. 92(4)). Amendments and refund claims go to the local government (art. 96; 지방세기본법 arts 49, 50).

**No return needed (소득세법 art. 73; NTS 7664).** Employment income alone, settled at year end, unless the person has pay, public pension, retirement or settled business income from 2 or more payers not combined at year end, has pay or retirement income with no withholding duty, or was not settled. Prior year revenue under KRW 75,000,000 and no other income, as an insurance agent, door-to-door seller or contract delivery seller settled by the company. Retirement income and settled business income only. Non-taxed or separately taxed income only. Other income of KRW 3,000,000 or less where separate taxation is chosen. The NTS list ends with 등 (and so on), so a case outside these limbs is Needs Input. 사업소득 of any other kind needs a return, including a nil or loss result (art. 70(1)).

**Amended and late returns.** 수정신고 (국세기본법 art. 45), 경정청구 within 5 years, or 3 months after a decision that increases tax (art. 45의2), and 기한 후 신고 (art. 45의3).

## Penalties and interest

| Offence | Penalty | Basis |
| --- | --- | --- |
| No return (무신고) | 20% of tax; fraud 40%, offshore fraud 60%. 복식부기의무자: larger of that and revenue × 7/10,000 (fraud 14/10,000). A 복식부기의무자 who files an estimate without the art. 70(4) statements is treated as filing no return (NTS 7665, NTS 7669) | 국세기본법 art. 47의2; 소득세법 art. 70(4) |
| Under-reporting (과소신고) | 10% of the additional tax; fraud 40% (offshore 60%) + 10% on the rest. 복식부기의무자 fraud: larger of the 40% (60%) amount and under-reported revenue × 14/10,000, plus the 10% on the rest | Art. 47의3 |
| Late payment (납부지연), text to 30 June 2026 | Tax × days × 22/100,000 (the prior version's 0.022%, about 8.03% a year), to the date of payment, leaving out the days from the notice date to the notice due date; 3% of tax unpaid at a notice due date. Days after the notice due date count for 5 years at most. The days limb does not apply where the tax on a notice is under KRW 1,500,000 | Art. 47의4(1), (7), (8); 시행령 art. 27의4(1) |
| Late payment, text from 1 July 2026 | Daily 22/100,000 from the day after the legal due date to the day before the notice date or the payment date. After the notice due date: 3%, then 67/10,000 per month to the day before payment, 5 years at most, plus the collection notice cost by registered post. Where the tax on a notice is under KRW 1,500,000, the monthly limb and that cost do not apply, and the 3% still does | Art. 47의4(1), (7), (8); 시행령 art. 27의4(2). 법률 제21212호 부칙 art. 3: a notice due date passed by 30 June 2026 stays on the old text |
| Records not kept (무기장) | Computed tax × (unrecorded income ÷ 종합소득금액, taken as 1 if above 1 and 0 if below 0) × 20%. Not for 소규모사업자. The prior version's 'KRW 200,000 to 2,000,000' has no primary support and was replaced | 소득세법 art. 81의5; 시행령 arts 132(4), 147(1) |
| Art. 81의5 with no-return penalty | Only the larger (equal: 국세기본법) | 국세기본법 art. 47의2(6) |
| No 성실신고확인서 | Larger of computed tax × (business income ÷ 종합소득금액, taken as 1 if above 1 and 0 if below 0) × 5%, and business revenue × 2/10,000. Applies with no computed tax | 소득세법 art. 81의2 |
| 영수증수취명세서 | 1% of the amount not filed or not clear. Not 소규모사업자 or 단순경비율 filers; a 기준경비율 filer is exempt only on costs other than 매입비용, 임차료 and pay | Art. 81; 시행령 art. 147(1), (2) |
| 증명서류 (evidence) | 2% of amounts without proper evidence. Same carve-outs as the row above | Art. 81의6; 시행령 art. 147(1), (2) |
| 사업장현황 report | 0.5%, for medical, veterinary and pharmacy only | Art. 81의3; 시행령 art. 147의2 |
| 사업용계좌, card and cash receipts | Art. 81의8 0.2%; art. 81의9 5%, and cash receipts 1%, 5% or 20% as listed | Arts 81의8, 81의9 |
| 계산서 | 1% and the listed summary penalties | Art. 81의10 |
| 지급명세서 | 1% (0.5% if filed within 3 months); daily workers 0.25% (0.125% if filed within 1 month); 간이지급명세서 0.25% (0.125% if filed within 1 month, or within 3 months for 근로소득 of workers other than daily workers paid before 1 January 2027) | Art. 81의11(1)(1); 법률 제19196호 부칙 art. 6(4), which keeps the earlier art. 81의11(1)(1)나 for that income |

These penalties sit in different Acts and each reaches only its own duty. The art. 47의2 to 47의4 rules apply to national tax. Local tax has its own rules (지방세기본법 arts 53 to 55) and is not penalised by the national Act. Art. 81의5 penalty is charged within 소득세법 on the duties in arts 160 and 161. 지방세법 art. 99(1) sets the local share of those 소득세법 penalties at 10%, with the larger-only rule where 지방세기본법 arts 53 or 54 also apply.

**Reductions (국세기본법 art. 48).** Reasonable cause and the extension grounds remove a penalty (art. 48(1)). Amended return, of the art. 47의3 penalty: 90% within 1 month, 75% within 3, 50% within 6, 30% within 12, 20% within 18 and 10% within 24. Late return, of the art. 47의2 penalty: 50% within 1 month, 30% within 3, 20% within 6. Not available where the person knew a correction was coming. These do not reduce the late payment penalty.

**Local tax.** 지방세기본법 art. 53: 20%, fraud 40%. Art. 54: 10%, fraud 40% + 10%. Art. 55: 22/100,000 per day to payment or notice (시행령 art. 34(1)), capped at 75% of the tax (art. 55(1)); 3% at a notice due date; monthly 66/10,000 (art. 34(2)), for 60 months at most (art. 55(1)), not under KRW 450,000 (art. 55(4)). Art. 57(2): the same reductions. Where 소득세법 art. 70(4) treats a person as filing no return, the local return is treated as not filed too (지방세법 art. 99(2)).

## Cross-border points

R-KR-1 (non-residents), R-KR-5 (foreign income, foreign tax and treaties) and R-KR-6 (the 5 year foreign resident rule) stop the workflow. Other points:

- **Foreign suppliers.** A foreign software line (Adobe, Figma and so on) is an expense if for the business. The art. 160의2(2) documents are not needed where the supplier is a non-resident or foreign corporation with no place of business in Korea (시행령 art. 208의2(1)(4)), so confirm that fact; proof of the cost is still kept under art. 160의2(1). Any VAT on imported services needs checking.
- **Foreign currency.** Currency is KRW. Art. 97 of the decree covers exchange differences on foreign currency assets and debts. A rate for converting a receipt was not read: a foreign currency receipt is Needs Input and may trigger R-KR-5.
- **Foreign entertainment.** Cash abroad is an art. 35(2) exception only where the decree limb is met.
- **Treaties.** No treaty was read, and none is applied.

## Two worked examples that recompute

This section is in the child skill `kr-income-tax-reference`, moved there word for word so this file stays under the size limit. Load it with this skill.

## Ask the client first

Questions come first. Do not produce a figure or working paper before asking, and treat any answer still missing as Needs Input.

1. **Status.** Are you resident for the whole year? Any death, departure, joint business, foreign income, rental income, capital gain, crypto, pension or other income? Do interest and dividends exceed KRW 20,000,000?
2. **Business.** What is your main business type (업종), and do you have an 업종코드? Total gross revenue for the year and for the year before (before 3.3% withholding)? VAT status: general, 간이 or exempt?
3. **Records.** Did you keep simplified (간편장부) or double-entry (복식부기) books? What evidence do you hold for purchases, rent and pay? Any loss carried forward, with the loss year's return?
4. **Withholding and prepayment.** Did any clients withhold 3.3%, and do you have 원천징수영수증 from each? Did you pay estimated tax (중간예납) in November, and how much?
5. **Family and deductions.** Marital status and number of dependants, with ages and income? National pension (국민연금) and national health insurance (국민건강보험) total paid in the year, and your membership type? Any 노란우산공제 or pension account?
6. **Mixed use.** Do you use a vehicle for business, and do you keep a driving log (운행기록부)? Did you work from a home office, what share is used for business, and what record supports it?

**If the client has only a bank statement.** This is intake only. Sort the lines using Classifying a bank line so the questions are specific: wire credits as potential 사업소득, and 국민연금 and 국민건강보험 debits as items to confirm. Do not assume every receipt is net of withholding. Do not apply a default route. Flag purchases over KRW 500,000 for review. Then ask the questions above, before any output. Whatever stays unanswered is Needs Input.

### Completion checks

- [ ] No refusal fired, and residence confirmed?
- [ ] Business type (업종) confirmed, and the expense rate read for that code and year?
- [ ] Client payments grossed up only with a document?
- [ ] Bank inflows reconciled against withholding receipts, with income gross and withholding credited?
- [ ] Local income tax computed on the art. 92 table, with its own credits and filing?
- [ ] Pension in 소득공제; owner's health premium in 필요경비 (books route); employee premiums in art. 52?
- [ ] Estimated tax (중간예납) credited against national tax only?
- [ ] Double-entry threshold checked against the prior year revenue and group, not a single figure, with a new starter a 간편장부대상자 at any revenue unless art. 208(5) excludes them?
- [ ] Standard credit matched to employment income, 성실사업자 limbs and art. 52 claims?
- [ ] Deadline moved for a weekend or holiday?
- [ ] Figures labelled estimated and open items listed?

## Sources

Read on 5 November 2026. law.go.kr text was fetched at the version dates shown. Tables in the statutes are images: arts 55(1) and 35(3) were checked by viewing the image, others from the image's alternative text. Translations of statutory terms are the author's, not official.

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| 소득세법, in force 31 December 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276127&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251001&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared with the 2026 text on the rate, deduction, credit, withholding and penalty articles listed in the next row |
| 소득세법, in force 5 November 2026 (법률 제21221호 with 제21548호) | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 1의2, 3, 4, 5, 6, 14, 19, 24, 26, 27, 33, 33의2, 35, 39, 43, 45, 47, 50 to 54, 55, 56의2, 59 to 59의4, 60, 61, 65, 70, 70의2, 73, 74, 76, 77, 78, 80, 81 to 81의14 (headings and operative sentences), 85, 85의2, 86, 127, 129, 144의2, 149, 150, 152, 160, 160의2, 160의5 and the 법률 제21548호 부칙, with 법률 제20615호 부칙 art. 14 |
| 소득세법, version in force 1 July 2022 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=237497&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20220701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 81의11, 164의3, for the earlier rule kept by 법률 제19196호 부칙 art. 6(4) |
| 소득세법, version dated 1 January 2026 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260101&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 59의2 |
| 소득세법, version dated 21 April 2026 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=285523&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260421&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 59의2 |
| 소득세법, version dated 1 January 2027 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=280405&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20270101&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared on rates and selected articles, no full comparison |
| 소득세법 시행령, in force 28 November 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279961&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared on arts 67, 83, 118의8, 132, 133, 143, 147, 208, 208의2(1) |
| 소득세법 시행령, in force 1 October 2026 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290841&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261001&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 55, 61, 67, 78, 78의3, 83, 97, 118의8, 119의3, 123, 132, 133, 140, 143, 145, 147, 147의2, 184, 208, 208의2(1) |
| 소득세법 시행규칙 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=286379&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 67, 67의2, 95의2 at 1 July 2025 and 1 July 2026, which differ only in the ministry name; the forms list at 1 July 2026 |
| 국세기본법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=289999&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261002&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 5, 45, 45의2, 45의3, 47의2 to 47의5, 48 and 법률 제21212호 부칙 at 2 October 2026. The 11 November 2025 text was machine compared on those articles; arts 47의4, 47의5 and 48 differ, and those spans were read |
| 국세기본법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=283623&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 27의4 at 15 September 2025 and 1 July 2026 |
| 지방세법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=282559&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260701&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 91, 92, 94 to 97, 99, 103의13; no difference between the 2025 and 2026 versions on them; art. 103의17 at the 2026 version |
| 지방세법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290815&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261001&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 92 |
| 지방세기본법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290139&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261002&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 24, 49, 50, 53 to 55, 57, with no difference from the 11 November 2025 text on them |
| 지방세기본법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=290497&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20261002&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 34 |
| 지방세특례제한법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=286607&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260602&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 167의2, 167의3 and 법률 제12955호 부칙 art. 2 |
| 지방세특례제한법, version dated 9 September 2027 (법률 제21901호, 8 September 2026) | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=289389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20270909&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 167의2, 167의3 and 법률 제12955호 부칙 art. 2 match the row above, with the end date unchanged |
| 조세특례제한법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=284389&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 7 (industry list), 86의3, 104의8, 122의3, 126의6, 132의2 (limit only) |
| 조세특례제한법 시행령 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=288915&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260918&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 104의5, 121의6 and the 104의5 부칙 |
| 조세특례제한법, dated 11 November 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279739&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251111&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: compared with the current text on arts 7, 86의3, 104의8, 122의3, 126의6, 132의2 |
| 조세특례제한법 시행령, in force 28 November 2025 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=279959&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20251128&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 104의5; compared on art. 121의6 |
| 부가가치세법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276117&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260102&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: arts 8, 26, 48, 49, 67 |
| 국고금 관리법 | https://www.law.go.kr/LSW/lsInfoR.do?lsiSeq=276079&chrClsCd=010202&urlMode=lsInfoP&viewCls=lsInfoP&efYd=20260102&vSct=&ancYnChk=0 | 2026-11-05 | Read in part: art. 47 |
| 국세청고시 제2026-14호, 2025년 귀속 경비율 고시 | https://nts.go.kr/nts/na/ntt/selectNttInfo.do?nttSn=1350024 | 2026-11-05 | Read in part: arts 2 and 4 and the rate rows in the table above; 1,542 rows parsed, others not individually checked |
| NTS 종합소득세 개요 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2224&cntntsId=7664 | 2026-11-05 | Read in full: dates, extension, no return cases, Wetax link |
| NTS 신고납부기한 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2225&cntntsId=7665 | 2026-11-05 | Read in full: dates and attachments |
| NTS 세액계산 흐름도 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2226&cntntsId=7666 | 2026-11-05 | Read in full |
| NTS 세율 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&cntntsId=7667 | 2026-11-05 | Read in full: table labelled 2023 to 2025 |
| NTS 가산세 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2228&cntntsId=7668 | 2026-11-05 | Read in full |
| NTS 기장의무 판단 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2230&cntntsId=7669 | 2026-11-05 | Read in full |
| NTS 간편장부 안내 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2231&cntntsId=7670 | 2026-11-05 | Read in full |
| NTS 성실신고확인제도 안내 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2234&cntntsId=7672 | 2026-11-05 | Read in full |
| NTS 중간예납 안내 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2236&cntntsId=7673 | 2026-11-05 | Read in full |
| NTS 사업장현황신고 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2283&cntntsId=7699 | 2026-11-05 | Read in full |
| NTS 사업소득 | https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6464&cntntsId=7900 | 2026-11-05 | Read in full: withholding lists |
| NABO 2026년 세법개정안 분석 | https://www.nabo.go.kr/board/file/down.do?fid=33319646 | 2026-11-05 | Digest of bills, read in part: pp. 1 to 6 and 54 to 58, and term searches over the 294 pages |

### Source conflicts

- **Health premiums.** The prior version treated them as a 소득공제. 시행령 art. 55(1) makes the owner's own premium 필요경비. Corrected.
- **NTS 7672 and 조세특례제한법 art. 122의3(5).** The page states a clawback test on revenue and expenses of 20% and a monthly rent date of 31 December 2025. The Act read says 사업소득금액, 10% (성실사업자 20%), and 31 December 2026. The Act is used here; the page may be dated.
- **NTS 7664 on holidays.** The page lists 공휴일 and 토요일. 국세기본법 art. 5(1) as amended adds 일요일, 대체공휴일 and 노동절. The Act is used.
- **NTS 7668 caption year.** The penalty table's year label differs from its heading. Only rates matching the statute are used.
- **`south-korea-vat`.** That sibling guide states the simplified VAT figures its own way, and this file's prior version used KRW 48,000,000 as a registration test. This file defers to that guide on VAT, which was not changed.

### Other legacy topics

- **Contributor.** The prior version's table named the Open Accountants Community as contributor and its skill version as 2.1.
- **Key legislation.** The prior table's references were corrected: business income is art. 19 (art. 27 is necessary expenses); income deductions are arts 50 to 54; tax credits are arts 56 to 59의4 and art. 65 is estimated tax; local income tax is 지방세법 arts 91 to 103의13.
- **Known gaps.** Non-resident Korean-source income; financial income above the test (금융소득 종합과세); real estate capital gains (양도소득세); corporate income tax (법인세); international income and treaties.
- **Disclaimer.** This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional, such as a 세무사 or 공인회계사, before filing or acting on them.

Not yet confirmed: the 2026 expense rate notice; whether 지방세특례제한법 art. 167의2 reaches a 2026 return filed in 2027; the local e-filing credit amount under art. 167의3; local government rate variations under 지방세법 art. 92(2); the text and passage of the 2026 revision bills, including the withholding rate, dependant income test, monthly rent, birth and marriage credits; the result for children born in 2017 under 법률 제21548호 부칙 art. 2(3); the 2026 NTS pages for dates, including any extension for that year; whether local tax had the 2025 payment extension; the pension deduction on an estimate route (시행령 art. 143(2)); the absence of a separate health premium deduction on an estimate route; the split of tax to employment income for art. 59(1); the amount of 납세조합공제 on a return under 소득세법 art. 76(3)(5); whether 납세조합 징수세액 in art. 76(3)(5) is the net amount collected; the mapping of 납세조합공제 to the return forms; the inference that 납세조합공제 stays outside the credits in step 7; whether 지방세특례제한법 art. 167의2(1) gives a local credit for 납세조합공제; the basis for a home office share; the second car rule in 시행령 art. 78의3; transitional limits on older carried losses; depreciation rates; the art. 132의2 list; the marriage credit; 조세특례제한법 art. 7 relief, 최저한세 and 농어촌특별세 computations; currency conversion of receipts; the 시행령 별표 3의3 service list; and the art. 144의2 year-end settlement list.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the upstream template with Tier 2 metadata; rates and thresholds tested against primary text; local income tax, expense rates, bookkeeping tests, health premiums, child credit, instalments and penalties corrected; refusal messages and question threshold added; onboarding fallback changed to intake only |
| 2.1 | November 2026 | Estimated tax: KRW 500,000 instalment floor replaces the KRW 300,000 prior year test |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Korean bank formats; local platform patterns (KakaoTalk Pay, Naver Pay, Toss); worked examples |
| 1.0 | 2025 | Initial version |
