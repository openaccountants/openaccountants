---
name: kr-income-tax-reference
description: Reference sections for kr-income-tax (Two worked examples that recompute), moved from the parent skill word for word so each file stays under the size limit. MUST load alongside kr-income-tax.
version: 2.2
jurisdiction: KR
tax_year: 2025
tax_year_notes: "Coverage starts with the 2025 year (2025년 귀속, filed in 2026) and includes the 2026 year (2026년 귀속, filed in 2027). The law was read at 5 November 2026. Expense rates are those of 국세청고시 제2026-14호, which applies to 2025 only; no rate notice for 2026 was read, so a 2026 computation on 단순경비율 or 기준경비율 is Needs Input. The 2026 revision bills before the National Assembly are not treated as law. The local credit rule in 지방세특례제한법 art. 167의2 has a stated end date of 31 December 2026, and its effect on a 2026 return filed in 2027 is held."
last_updated: 2026-11-05
depends_on:
  - kr-income-tax
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# kr-income-tax: reference sections

Moved word for word from `kr-income-tax`. Load that skill first.

## Two worked examples that recompute

All figures are estimated, not reviewed. Each block recomputes with the repository checker. Examples 1 to 3 walk the ladder to the balance due.

### Example 1: self-employed, 2025, on 3 routes

A resident sells online (525101, group 가). 2025 revenue KRW 80,000,000, no employment income. Actual costs on simplified books KRW 62,000,000, including the owner's 지역가입자 health premium. Pension KRW 2,400,000. Basic deduction for self only. No withholding, no estimated tax, no e-filing credit, not a 성실사업자, so KRW 70,000 standard credit.

**Leg A: books.** Status is 간편장부대상자 on any prior year revenue used here. Leg A applies whichever 2024 revenue is taken.

```oa-check
name: KR 2025 self-employed on simplified books
inputs:
  revenue: 80000000
  expenses: 62000000
  basic: 1500000
  pension: 2400000
  standard_credit: 70000
steps:
  - income: max(revenue - expenses, 0)
  - taxable: max(income - basic - pension, 0)
  - tax: 840000 + (taxable - 14000000) * 0.15
  - national_due: tax - standard_credit
  - local_tax: 84000 + (taxable - 14000000) * 0.015
  - local_due: local_tax - standard_credit * 0.10
  - total: national_due + local_due
expected:
  income: 18000000
  taxable: 14100000
  tax: 855000
  national_due: 785000
  local_due: 78500
  total: 863500
```

**Leg B: no books, 2024 revenue KRW 50,000,000.** Under KRW 60,000,000, so 단순경비율 applies, and it is at or above KRW 48,000,000, so this is not a 소규모사업자 and the art. 81의5 penalty applies. The pension deduction is carried here as a claim; 시행령 art. 143(2) names arts 50 to 52 for a government estimate and does not name art. 51의3, so the reviewer should confirm it. This leg, like Leg C, assumes no separate deduction for the owner's health premium. That assumption is held.

```oa-check
name: KR 2025 no books, simple rate
inputs:
  revenue: 80000000
  simple_rate: 0.86
  basic: 1500000
  pension: 2400000
  standard_credit: 70000
steps:
  - income: max(revenue - revenue * simple_rate, 0)
  - taxable: max(income - basic - pension, 0)
  - tax: taxable * 0.06
  - record_penalty: tax * 0.20
  - national_due: tax - standard_credit + record_penalty
  - local_due: taxable * 0.006 - standard_credit * 0.10 + record_penalty * 0.10
  - total: national_due + local_due
expected:
  income: 11200000
  taxable: 7300000
  tax: 438000
  record_penalty: 87600
  national_due: 455600
  local_due: 45560
  total: 501160
```

**Leg C: no books, 2024 revenue KRW 70,000,000.** At or above KRW 60,000,000, so 단순경비율 is shut and 기준경비율 applies. Purchases, rent and pay with evidence total KRW 45,000,000. The rate is 11.4%, and 2.8 is the multiple.

```oa-check
name: KR 2025 no books, standard rate
inputs:
  revenue: 80000000
  main_costs: 45000000
  standard_rate: 0.114
  simple_rate: 0.86
  multiple: 2.8
  basic: 1500000
  pension: 2400000
  standard_credit: 70000
steps:
  - route_a: max(revenue - min(main_costs + revenue * standard_rate, revenue), 0)
  - route_b: (revenue - revenue * simple_rate) * multiple
  - income: min(route_a, route_b)
  - taxable: max(income - basic - pension, 0)
  - tax: 840000 + (taxable - 14000000) * 0.15
  - record_penalty: tax * 0.20
  - national_due: tax - standard_credit + record_penalty
  - local_due: 84000 + (taxable - 14000000) * 0.015 - standard_credit * 0.10 + record_penalty * 0.10
  - total: national_due + local_due
expected:
  route_a: 25880000
  route_b: 31360000
  income: 25880000
  taxable: 21980000
  tax: 2037000
  record_penalty: 407400
  national_due: 2374400
  local_due: 237440
  total: 2611840
```

| Route | National and local due (KRW) |
| --- | --- |
| A, books | 863,500 |
| B, 단순경비율, 2024 revenue 50,000,000 | 501,160 |
| C, 기준경비율, 2024 revenue 70,000,000 | 2,611,840 |

**Decision.** Which route wins depends on prior year revenue. At 2024 revenue of KRW 50,000,000, the simple rate beats these books, even with the penalty, because its 86% exceeds actual costs of 77.5% of revenue. At KRW 70,000,000, the books win by KRW 1,748,340. Both results rest on the assumptions held in Legs B and C. The prior version's claim that books yield lower income for most service businesses was withdrawn as a generalisation: compute each available route. An estimate also gives up any carried loss.

### Example 2: mixed income, 2026

A resident has 총급여액 KRW 40,000,000 with national tax of KRW 1,000,000 and local tax of KRW 100,000 withheld. A software freelance side business (940926) has gross fees of KRW 20,000,000 with 3.3% withheld on documents, and KRW 6,000,000 of costs on books. Books are used because no 2026 rate was read. Deductions: self KRW 1,500,000, pension KRW 1,800,000, art. 52 premiums KRW 1,500,000. Claiming art. 52 ends the KRW 130,000 standard credit (it saves more than the credit here: KRW 225,000 of tax at 15%).

The employment credit limit is 740,000 − (40,000,000 − 33,000,000) × 8/1000 = 684,000. The split of tax to employment income for art. 59(1) is held: 시행령 art. 119의3(1) sets an income share split, but only for 소득세법 art. 61(1). This example assumes the limit binds, which needs tax on employment income of KRW 1,243,637 or more. An income share split gives about KRW 2,980,000. If the applicable split gave less, the credit would be 55% of that tax, and every balance below would need rerunning.

```oa-check
name: KR 2026 mixed employment and business income
inputs:
  pay: 40000000
  gross_fees: 20000000
  costs: 6000000
  basic: 1500000
  pension: 1800000
  premiums: 1500000
  employer_tax: 1000000
  employer_local: 100000
steps:
  - employment_deduction: 7500000 + (pay - 15000000) * 0.15
  - employment_income: pay - employment_deduction
  - business_income: max(gross_fees - costs, 0)
  - total_income: employment_income + business_income
  - taxable: max(total_income - basic - pension - premiums, 0)
  - tax: 840000 + (taxable - 14000000) * 0.15
  - credit: max(740000 - (pay - 33000000) * 0.008, 660000)
  - national_after: tax - credit
  - fee_tax: gross_fees * 0.03
  - national_balance: national_after - employer_tax - fee_tax
  - local_tax: 84000 + (taxable - 14000000) * 0.015
  - local_paid: employer_local + fee_tax * 0.10
  - local_balance_with_credit: local_tax - credit * 0.10 - local_paid
  - local_balance_without_credit: local_tax - local_paid
expected:
  employment_income: 28750000
  total_income: 42750000
  taxable: 37950000
  tax: 4432500
  credit: 684000
  national_after: 3748500
  national_balance: 2148500
  local_tax: 443250
  local_balance_with_credit: 214850
  local_balance_without_credit: 283250
```

**Decision.** If the employment credit limit binds, the national balance is KRW 2,148,500, and the local balance is KRW 214,850 if art. 167의2 reaches a 2026 return filed in 2027 and KRW 283,250 if it does not. Show both local results until the reviewer settles art. 167의2, and rerun all of them if the art. 59(1) split gives less than KRW 1,243,637.

### Example 3: employee, 2025

An employee with 총급여액 KRW 50,000,000 files a return. Self, spouse and 2 children aged 9 and 6 in 2025, all qualifying: basic KRW 6,000,000. Pension KRW 2,250,000, art. 52 premiums KRW 1,900,000. Withheld: national KRW 1,500,000, local KRW 150,000. Only the 9 year old meets the 8 or over test for 2025, so the child credit is for 1 child: KRW 250,000.

```oa-check
name: KR 2025 employee
inputs:
  pay: 50000000
  basic: 6000000
  pension: 2250000
  premiums: 1900000
  child_credit: 250000
  withheld: 1500000
  local_withheld: 150000
steps:
  - employment_deduction: 12000000 + (pay - 45000000) * 0.05
  - employment_income: pay - employment_deduction
  - taxable: max(employment_income - basic - pension - premiums, 0)
  - tax: 840000 + (taxable - 14000000) * 0.15
  - credit_raw: 715000 + (tax - 1300000) * 0.30
  - limit: max(740000 - (pay - 33000000) * 0.008, 660000)
  - credit: min(credit_raw, limit)
  - national_after: tax - credit - child_credit
  - national_balance: national_after - withheld
  - local_after: 84000 + (taxable - 14000000) * 0.015 - credit * 0.10 - child_credit * 0.10
  - local_balance: local_after - local_withheld
expected:
  taxable: 27600000
  tax: 2880000
  credit_raw: 1189000
  limit: 660000
  national_after: 1970000
  national_balance: 470000
  local_after: 197000
  local_balance: 47000
```

### Example 4: late return and payment, 2025 year

Tax of KRW 1,000,000 and local tax of KRW 100,000 were due on 1 June 2026. Both the return and payment were made on 20 June 2026, a late return within 1 month, so the art. 47의2 penalty halves. There are 19 days from 2 June to 20 June, on the text before 1 July 2026. Not a 복식부기의무자, and no art. 81의5 penalty is assumed.

```oa-check
name: KR 2025 late return and payment
inputs:
  tax: 1000000
  local: 100000
  days: 19
steps:
  - return_penalty: tax * 0.20 * 0.50
  - payment_penalty: tax * days * 0.00022
  - national_total: tax + return_penalty + payment_penalty
  - local_return_penalty: local * 0.20 * 0.50
  - local_payment_penalty: local * days * 0.00022
  - local_total: local + local_return_penalty + local_payment_penalty
expected:
  return_penalty: 100000
  payment_penalty: 4180
  national_total: 1104180
  local_return_penalty: 10000
  local_payment_penalty: 418
  local_total: 110418
```

### Bank line fixtures

```oa-check
name: KR withholding on a documented KRW 1,000,000 fee
inputs:
  gross: 1000000
steps:
  - national: gross * 0.03
  - local: national * 0.10
  - net: gross - national - local
expected:
  national: 30000
  local: 3000
  net: 967000
```

| Line | Treatment |
| --- | --- |
| KB국민은행 `2025.03.15 / 타행이체 ABC디자인컴퍼니 / 입금 970,100 / 잔액 4,521,300` | Needs Input. 970,100 is not 967,000 (3.3%) or 970,000 (3%), and the prior version reached KRW 1,000,000 gross by assumption. Ask for the 원천징수영수증 or invoice. Design services may not be within the withholding limbs |
| 카카오뱅크 `2025-05-10 / 카카오페이 정산 / +350,000 / 잔고 2,840,000` | 사업소득. Take gross sales and fees from the KakaoPay dashboard; KRW 350,000 is the net settlement if fees were netted |
| 신한은행 `2025-04-30 / 국민연금보험료 자동이체 / -268,500 / 잔액 1,450,200` | Not 필요경비. Record as 연금보험료공제 if the contribution is the person's own |
| 우리은행 `2025-11-30 / 국세청 중간예납 / -650,000 / 잔액 3,210,000` | Exclude. Credit KRW 650,000 against national tax. 30 November 2025 was a Sunday, so the due date was 1 December; the date on the line stays as given |
| 하나은행 `2025-07-22 / 음식점 강남ABC식당 / -88,000 / 잔액 2,125,000` | 기업업무추진비 only if it entertained a business contact, and only with art. 35(2) evidence, as the item is over KRW 30,000. A bank line alone is not that evidence. A personal meal is out |
| KEB하나은행 `2025-09-01 / ADOBE SYSTEMS / -80,000 / 잔액 3,870,000` | 소모품비 if used for the business. Deductible only for the business share. The art. 160의2(2) documents are not needed only if the supplier has no place of business in Korea (시행령 art. 208의2(1)(4)); keep proof of the cost |

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
